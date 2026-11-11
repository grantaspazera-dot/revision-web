#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patikra po site.zip pakeitimo: nuorodos, UTF-8, kainodara, CNAME.

Paleidimas iš repozitorijos šaknies:
  python3 scripts/check-site.py
"""
import json
import re
import sys
import tempfile
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
ZIP = ROOT / "site.zip"

OLD_PRICE = re.compile(
    r"(?<!\d)20(?:\s|&nbsp;|\u00a0)*€|100\s*€\s*/\s*40\s*€\s*/\s*20|100/40/20"
)
MOJIBAKE = re.compile(r"\uFFFD|Ã[\u0080-\u00BF]|Â[\u0080-\u00BF]")
TEXT_EXT = {".html", ".css", ".js", ".xml", ".txt", ".svg"}

REQUIRED = [
    "Inventorizacija PRO planai",
    "Populiariausias",
    "Tik skenavimas, be nomenklatūros",
    "Nomenklatūra prekių atpažinimui",
    "Lokacijų langas su būsenomis",
    "Likučių sulyginimas",
    "Skirtumų ataskaita",
    "Patikra ir pakartotinė patikra",
    "Darbų langas",
    "„Liko skaičiuoti“",
    "skenerių ir darbuotojų statistika",
    "aktai PDF",
    "patikrų istorija",
    "50&nbsp;€",
    "25&nbsp;€",
    "75&nbsp;€",
    "150&nbsp;€",
    "200&nbsp;€",
    "40&nbsp;€</data> už skenerį per inventorizaciją",
    "40&nbsp;€</data> už vienetą per darbo dieną",
    "150&nbsp;€/val.",
    "900&nbsp;€/d.",
    "be PVM",
    '"valueAddedTaxIncluded": false',
    'href="assets/kainos.css"',
    'id="kainos"',
    'id="plan-maxi"',
]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.refs = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if data.get("id"):
            self.ids.append(data["id"])
        for key in ("href", "src"):
            if data.get(key):
                self.refs.append(data[key])
        if data.get("srcset"):
            for part in data["srcset"].split(","):
                url = part.strip().split(" ")[0]
                if url:
                    self.refs.append(url)


def fail(errors, message):
    errors.append(message)


def local_target(raw):
    if not raw or raw.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    parsed = urlparse(raw)
    if parsed.scheme in ("http", "https"):
        return None
    if parsed.scheme:
        return None
    return unquote(parsed.path), unquote(parsed.fragment)


def main():
    errors = []
    if not ZIP.is_file():
        print("Nėra site.zip")
        return 1
    with tempfile.TemporaryDirectory() as tmp:
        site = Path(tmp)
        with zipfile.ZipFile(ZIP) as archive:
            cname = archive.read("CNAME")
            if cname != b"revision.lt":
                fail(errors, f"CNAME turi likti revision.lt, rasta {cname!r}")
            archive.extractall(site)
        pages = {}
        for path in site.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in TEXT_EXT:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError as exc:
                fail(errors, f"UTF-8 klaida {path.relative_to(site)}: {exc}")
                continue
            rel = str(path.relative_to(site))
            if OLD_PRICE.search(text):
                fail(errors, f"Sena 20 € / 100/40/20 kainodara: {rel}")
            if MOJIBAKE.search(text):
                fail(errors, f"Įtartina koduotė: {rel}")
            if path.suffix.lower() == ".html":
                parser = Collector()
                parser.feed(text)
                pages[rel] = (path, parser.ids, parser.refs, text)
        online = pages.get("revision-online.html")
        if not online:
            fail(errors, "Nėra revision-online.html")
        else:
            body = online[3]
            for needle in REQUIRED:
                if needle not in body:
                    fail(errors, f"Trūksta teksto revision-online.html: {needle}")
            start = body.find('<script type="application/ld+json">')
            end = body.find("</script>", start)
            if start < 0 or end < 0:
                fail(errors, "Nėra JSON-LD")
            else:
                raw = body[start + len('<script type="application/ld+json">') : end]
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError as exc:
                    fail(errors, f"JSON-LD negalioja: {exc}")
                else:
                    prices = []

                    def walk(node):
                        if isinstance(node, dict):
                            if "price" in node and "priceCurrency" in node:
                                prices.append((node.get("name"), node["price"], node["priceCurrency"]))
                            for value in node.values():
                                walk(value)
                        elif isinstance(node, list):
                            for value in node:
                                walk(value)

                    walk(data)
                    expected = {
                        ("Inventorizacija PRO MINI", "50.00", "EUR"),
                        ("Inventorizacija PRO VID", "100.00", "EUR"),
                        ("Inventorizacija PRO MAXI", "150.00", "EUR"),
                        ("Inventorizacija PRO PRO", "200.00", "EUR"),
                        ("Android programa", "40.00", "EUR"),
                        ("Skenerio nuoma", "40.00", "EUR"),
                        ("Mokymai ir konsultacijos", "150.00", "EUR"),
                        ("Inventorizacijos valdymas", "900.00", "EUR"),
                    }
                    if not expected.issubset(set(prices)):
                        fail(errors, f"JSON-LD kainos nesutampa: {sorted(prices)}")
        ids_by_file = {name: set(ids) for name, (_, ids, _, _) in pages.items()}
        for name, (_, ids, refs, _) in pages.items():
            if len(ids) != len(set(ids)):
                dup = [item for item in ids if ids.count(item) > 1]
                fail(errors, f"Pasikartojantis id {name}: {sorted(set(dup))}")
            base = (site / name).parent
            for ref in refs:
                target = local_target(ref)
                if target is None:
                    if ref.startswith("#") and ref[1:] not in ids_by_file[name]:
                        fail(errors, f"Nėra inkaro {name} {ref}")
                    continue
                path, fragment = target
                if path in ("",):
                    dest = name
                else:
                    if path.startswith("/"):
                        candidate = site / path.lstrip("/")
                    else:
                        candidate = (base / path).resolve()
                    try:
                        candidate.relative_to(site.resolve())
                    except ValueError:
                        fail(errors, f"Nuoroda išeina iš svetainės: {name} -> {ref}")
                        continue
                    if candidate.is_dir():
                        candidate = candidate / "index.html"
                    if not candidate.is_file():
                        fail(errors, f"404 {name} -> {ref}")
                        continue
                    dest = str(candidate.relative_to(site))
                if fragment and fragment not in ids_by_file.get(dest, ()):
                    fail(errors, f"Nėra inkaro {name} -> {ref}")
        for css in site.rglob("*.css"):
            text = css.read_text(encoding="utf-8")
            for match in re.finditer(r"url\(([^)]+)\)", text):
                raw = match.group(1).strip("'\" ")
                target = local_target(raw)
                if not target or not target[0]:
                    continue
                candidate = (css.parent / target[0]).resolve()
                if not candidate.is_file():
                    fail(errors, f"CSS 404 {css.relative_to(site)} -> {raw}")
    if errors:
        print(f"NEPRAEITA ({len(errors)})")
        for item in errors:
            print("-", item)
        return 1
    print("PRAEITA: nuorodos, UTF-8, kainodara, CNAME")
    return 0


if __name__ == "__main__":
    sys.exit(main())
