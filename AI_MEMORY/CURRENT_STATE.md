# Dabartinė būklė

Patikrinimo data: 2026-11-10. Būsena aprašo `main` commit `14ef47e` ir tuo metu gyvą svetainę. Ši dokumentacijos šaka gyvos svetainės nekeičia.

## Versijos

| Kas | Reikšmė |
| --- | --- |
| Gyvas commit | `14ef47ef78a71045f49bc34ac943a0a9525a2520` |
| Žinutė | „REVISION P8.3 – gyva versija“ |
| Data | 2026-10-31 14:12 +0200 |
| Autorius | GitHub paskyra `grantaspazera-dot` |
| `site.zip` | 9 171 756 B, 197 failai, archyvo datos 2026-10-31 |
| Svetainės `lastmod` | `sitemap.xml` – 2026-10-31 |
| Privatumo tekstas | „Atnaujinta 2026-10-24“ |
| Pages sertifikatas | galioja iki 2027-01-22 (`revision.lt`, `www.revision.lt`) |

CSS komentarai archyve žymi sluoksnius iki P7.2. Atskiras programos versijos numeris, nesusijęs su commit žinute P8.3, – `UNKNOWN`.

## Kas veikia

- https://revision.lt/ HTTP 200. `index.html` baitai sutampa su archyvu (SHA-256 `3e1d0951bbae49d41f76583512852ca6ab7b93a9618cc16f0168ec0d7aac06da`, 31 109 B).
- Neegzistuojantis kelias grąžina HTTP 404, kūnas sutampa su `404.html` (SHA-256 `75508b2619695b41c200c6f3f9867d5f80e6c8231c127875a101df27f051734a`, 10 362 B).
- `www.revision.lt` grąžina 301 į `https://revision.lt/`.
- Pages nustatymas: workflow, šaka `main`, `cname: revision.lt`, `https_enforced: true`. API laukas `custom_404` yra `false`, nors `404.html` gyvai pateikiamas (kūnas sutapo). Ką API laukas reiškia šiam workflow – `NOT VERIFIED`.
- Šeši diegimo paleidimai nuo workflow atsiradimo iki P8.3 baigėsi sėkmingai. Visi buvo `push` į `main`.
- `https://forma.revision.lt/send.php` atsako. GET be naršyklės 2026-11-10 grąžino HTTP 403 ir `{"ok":false,"error":"origin"}`. Laiškas nesiųstas.
- Peržiūra https://grantaspazera-dot.github.io/revision-web-preview/ atsako 200, `noindex,nofollow`.
- Demo https://demo.revision.lt/ atsako 200.

## Apribojimai

- Šaltinio, iš kurio surenkamas `site.zip`, repo neturi.
- Duomenų bazės nėra. `DATABASE_SCHEMA.md` nekurtas. Formos serverio schema – `NOT VERIFIED`.
- `DEVELOPMENT_RULES.md` ir `SECURITY_RULES.md` nekartojami; taisyklės yra `AGENTS.md`.
- Testų, lint ir vietinio serverio konfigūracijos nėra.
- `README.md` ir GitHub aprašas vis dar sako „DEMO (peržiūra)“.
- Diegimas neturi `paths` filtro: bet koks `push` į `main`, įskaitant vien dokumentus, paleidžia gyvą publikavimą. Žr. `MODULES/PUBLIKAVIMAS.md`.
- Įmonės kodas svetainėje nenurodytas – `UNKNOWN`.

## Šaltiniai, kuriais remtasi

- Repozitorijos failų sąrašas ir `git log`.
- `.github/workflows/deploy.yml` visas tekstas.
- `site.zip` turinys: sąrašas, `CNAME`, `robots.txt`, `sitemap.xml`, puslapių antraštės, `assets/main.js`, `assets/p4.js`, `assets/form.js`, CSS pirmos eilutės, privatumo ir kontaktų tekstas.
- GitHub API: Pages, workflow paleidimai, peržiūros repo failų sąrašas ir jos `deploy.yml`.
- HTTP patikra 2026-11-10: gyvas `index.html` ir `404.html` palyginti su archyvu, `www`, formos GET, peržiūros ir demo antraštės bei titulai.

Nepalygini visi 197 archyvo failai su gyvu domenu. Be `index.html` ir `404.html` atitikimas gyvai svetainei – `NOT VERIFIED`, nors diegimo istorija rodo, kad P8.3 artefaktas buvo įkeltas 2026-10-31 12:12 UTC.

## Sąmoningai neliešta

`site.zip`, workflow, `README.md`, gyva svetainė, DNS ir `main` šaka.
