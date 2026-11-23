# Keitimų žurnalas

## 2026-11-16 – DUK, įžvalgos ir mokymų kaina (revision.lt)

Trečias gyvas įkėlimas. Nauji puslapiai: `duk.html` (FAQPage JSON-LD), `kaip-pasiruosti-metinei-inventorizacijai.html`, `kodel-atsiranda-inventorizacijos-trukumai.html`, taip pat `llms.txt`. DUK nuoroda navigacijoje ir poraštėje. Mokymai – 2 val. – 300 € (be PVM); konsultacijos lieka 150 €/val. Peržiūros `noindex` pašalintas. `robots.txt` (`Allow: /` ir Sitemap) ir `CNAME` (`revision.lt`) grąžinti iš gyvo rinkinio. `sitemap.xml` paimtas iš peržiūros: 15 adresų, visi `https://revision.lt/`. Kanoniniai adresai lieka `https://revision.lt/`. Užklausos forma lieka `https://forma.revision.lt/send.php`.

Neliesta: `.github/workflows/deploy.yml`.

Atsarginė kopija prieš šį įkėlimą: šaka `backup/pre-pro3-2026-11-16` ir žyma `pre-pro3-2026-11-16` (commit `9553932`).

### Atšaukimas

```bash
git revert <šio-commit>
git push origin main
```

## 2026-11-16 – Inventorizacija PRO rezultatai ir etapai (revision.lt)

Antras gyvas įkėlimas tą pačią dieną. `inventorizacija.html` Rezultatų bloke trys veikiančios Inventorizacija PRO ekranų nuotraukos (likučiai, skirtumai, statistika). `revision-online.html` penki etapai aprašyti plačiau. Peržiūros `noindex` pašalintas; `robots.txt`, `sitemap.xml` ir `CNAME` (`revision.lt`) grąžinti iš ankstesnio gyvo rinkinio. Kanoniniai adresai lieka `https://revision.lt/`. Užklausos forma lieka `https://forma.revision.lt/send.php`.

Neliesta: `.github/workflows/deploy.yml`.

Atsarginė kopija prieš šį įkėlimą: šaka `backup/pre-pro2-2026-11-16` ir žyma `pre-pro2-2026-11-16` (commit `e883e8b`).

### Atšaukimas

```bash
git revert <šio-commit>
git push origin main
```

## 2026-11-16 – Inventorizacija PRO gyvai (revision.lt)

Į `main` įkeltas peržiūros `site.zip` iš `grantaspazera-dot/revision-web-preview` commit `2a38fef` (ekranų nuotraukos, mokymų žingsniai, Inventorizacija PRO pavadinimas). Peržiūros nustatymai paversti gyvais:

- pašalintas `<meta name="robots" content="noindex,nofollow">` iš visų HTML;
- grąžinti gyvi `robots.txt` (`Allow: /` ir `Sitemap`) ir `sitemap.xml` (naujų puslapių nebuvo);
- grąžintas `CNAME` (`revision.lt`);
- kanoniniai adresai lieka `https://revision.lt/`;
- užklausos forma lieka `https://forma.revision.lt/send.php`.

Neliesta: `.github/workflows/deploy.yml`.

Atsarginė kopija prieš publikavimą: šaka `backup/pre-pro-2026-11-16` ir žyma `pre-pro-2026-11-16` (commit `7e4a6ca`).

### Atšaukimas

```bash
git revert <šio-commit>
git push origin main
```

Tai vėl išpakuoja ankstesnį `site.zip`. DNS, `CNAME` ir Pages nustatymų nekeiskite.

## 2026-11-10 – Inventorizacija PRO kainodara

Vieša programos nuoma aprašyta kaip **Inventorizacija PRO** (REVISION ONLINE). Keturi planai už vieną inventorizaciją, 7 dienų prieiga, kainos be PVM: MINI 50 €, VID 100 €, MAXI 150 € (ženklelis „Populiariausias“), PRO 200 €. Papildoma inventorizacija ir kiekviena papildoma diena po 7 dienų – 50 % plano kainos (25 / 50 / 75 / 100 €). Tai pakeičia 100 € / 40 € / 20 € schemą. Tos schemos tekstų P8.3 archyve nebuvo.

Priedai palikti: Android programa 40 € už skenerį per inventorizaciją, skenerio nuoma 40 € už vienetą per darbo dieną, mokymai ir konsultacijos 150 €/val. (paprastai 2 val.), inventorizacijos valdymas 900 €/d.

Pilnos kortelės yra `revision-online.html#kainos`. Pradžios puslapyje kainos neužima ekspertinių paslaugų vietos: ten yra nuoroda. Šaltinis: `docs/KAINODARA.md`.

Neliesta: `CNAME` (`revision.lt`), `.github/workflows/deploy.yml`, logotipai, programos ekranų nuotraukos, klientų logotipai.

Patikra: `python3 scripts/check-site.py`.

### Atšaukimas po sujungimo

Sujungimas į `main` paleidžia GitHub Pages ir iš naujo publikuoją https://revision.lt. Jei kainodarą reikia grąžinti, atšaukite sujungimo commit ir įkelkite į `main`:

```bash
git revert -m 1 <sujungimo-commit>
git push origin main
```

Tai vėl išpakuoja ankstesnį `site.zip`. DNS, `CNAME` ir Pages nustatymų nekeiskite.

## 2026-11-23 – Individualios sistemos puslapis

Naujas `individualios-sistemos.html`: unikali valdymo sistema įmonei (prekės, turtas, procesai, žaliavos), 4 projektai (Inventorizacija PRO, Turto inventorizacija, Gamybos valdymas, REVISION OS) su tikrais programų ekranais ir darbo eiga. Be kainų, be kliento pavadinimo. Pradžios puslapyje nauja sekcija `#sistemos`, poraštėje nuoroda „Individualios sistemos“, `sitemap.xml` papildytas. Viršutinis meniu ir užklausos forma nekeisti. Patvirtinta: „PUBLIKUOK revision.lt“ (2026-11-23 09:35).

Atsarginė žyma: `pre-sistemos-2026-11-23` (b2fb6d5). Atšaukimas: `git revert 79db4cf && git push origin main` (arba atkurti `site.zip` iš žymos).
