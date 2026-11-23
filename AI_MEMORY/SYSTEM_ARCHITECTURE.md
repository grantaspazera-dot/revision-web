# Sistemos architektūra

Patikrinimo data: 2026-11-10. Neįvykdyti teiginiai pažymėti `NOT VERIFIED` arba `UNKNOWN`.

## Technologijos

| Dalis | Kas patikrinta |
| --- | --- |
| Svetainė | Statinis HTML, CSS ir naršyklės JavaScript be karkaso. Šriftai – vietiniai Barlow Semi Condensed (`woff2`). |
| Pakavimas | Vienas `site.zip`. Failų datos archyve – 2026-10-31. `.nojekyll` išjungia Jekyll. |
| Pateikimas | GitHub Pages, `build_type: workflow`, šaka `main`. Veiksmas „Deploy site to GitHub Pages“. |
| Domenas | `CNAME` archyve: `revision.lt`. API: domenai `revision.lt` ir `www.revision.lt`, HTTPS priverstinis, sertifikatas galioja iki 2027-01-22. |
| Užklausų serveris | Naršyklė siunčia JSON į `https://forma.revision.lt/send.php`. Serverio kodo čia nėra. |
| Duomenų bazė | Šioje repozitorijoje jos nėra. `DATABASE_SCHEMA.md` nekurtas. |

Kūrimo mašina, kuri surenka HTML į `site.zip`, repozitorijoje nematyti. Jos vieta ir įrankiai – `UNKNOWN`. CSS komentarai archyve rodo sluoksnius P0–P7.2 su rollback pastabomis, bet generatoriaus nėra.

## Komponentai

```text
lankytojas
    │
    ▼
https://revision.lt          GitHub Pages (iš site.zip)
    │  statiniai puslapiai, main.js, p4.js
    │
    ├─ tel: ir mailto:info@revision.lt
    │
    ├─ uzklausa.html + form.js
    │       POST JSON ──► https://forma.revision.lt/send.php
    │                         (serverio kodas ne šioje repo; NOT VERIFIED)
    │       jei tinklas nepavyksta ──► mailto:info@revision.lt
    │
    └─ nuoroda ──► https://demo.revision.lt/     atskira GitHub Pages svetainė
                   programos interaktyvus demo, šaltinio repo UNKNOWN

peržiūra (kita repo, ne gyvas domenas)
https://grantaspazera-dot.github.io/revision-web-preview/
    noindex, canonical į https://revision.lt/
```

`www.revision.lt` 2026-11-10 grąžino HTTP 301 į `https://revision.lt/`.

## Duomenų srautai

Svetainė pati duomenų nerenka naršyklės saugykloje. `assets/main.js` komentaras ir kodas: meniu, atsiradimo animacijos ir skaitikliai, be tinklo užklausų ir be `localStorage`.

Užklausos srautas aprašytas `MODULES/UZKLAUSA.md`. Privatumo politika (atnaujinta 2026-10-24, tekstas archyve) teigia, kad užklausų turinys svetainėje ir formos serveryje nesaugomas, o iki 2 valandų laikomas tik techninis skaitiklis pagal maišos funkcija užkoduotą IP. Tai publikuotas tekstas. Serverio programa šioje repozitorijoje nepatikrinta – `NOT VERIFIED`.

Analitikos ar slapukų scenarijų peržiūrėtuose HTML ir JS failuose nėra. Privatumo tekstas teigia, kad svetainė slapukų ir sekimo nenaudoja.

## Integracijos

| Integracija | Ryšys | Būsena |
| --- | --- | --- |
| GitHub Pages | diegimas iš `main` | patikrinta, gyva svetainė sutampa su archyvo `index.html` ir `404.html` |
| `forma.revision.lt` | POST iš `form.js` | klientas patikrintas; serveris tik GET, be laiško siuntimo |
| `demo.revision.lt` | nuoroda iš svetainės | 2026-11-10 HTTP 200, GitHub.com, paskutinis keitimas 2026-10-29 |
| LinkedIn | `https://www.linkedin.com/in/grantaspazera/` | nuoroda svetainėje; profilio turinys `NOT VERIFIED` |
| YouTube | kanalas `UC1N-YpUS6yE2_qbl6lmYl1Q` | nuoroda svetainėje; turinys `NOT VERIFIED` |
| VDAI | `https://vdai.lrv.lt` privatumo puslapyje | nuoroda; turinys `NOT VERIFIED` |
| Peržiūros repo | `grantaspazera-dot/revision-web-preview` | atskira Pages svetainė, žr. žemiau |

`form.js` komentaras serverį vadina UAB Bacloud serveriu. 2026-11-10 atsakymo antraštė buvo `server: LiteSpeed`. Ar tai Bacloud – `NOT VERIFIED`.

## Peržiūra ir demonstracija

Tai skirtingi dalykai.

- **Peržiūros svetainė** – repo `revision-web-preview`. 2026-11-10 titulas sutapo su gamybiniu („Sandėlio valdymas ir inventorizacija | REVISION LT“), yra `<meta name="robots" content="noindex,nofollow">`, canonical – `https://revision.lt/`. Paskutinis commit 2026-10-30, „P8.3 preview (noindex)“. Archyvas ten 9 172 622 B, šioje repo – 9 171 756 B. Pilnas turinio skirtumas – `NOT VERIFIED`. Teiginys, kad ten šiuo metu gyvena naujesnis dizainas už 2026-10-31 gyvą P8.3, šiuo patikrinimu nepatvirtintas: peržiūros publikacija senesnė už gyvą `main`.
- **Programos demo** – https://demo.revision.lt/, titulas „Kaip veikia REVISION inventorizacija – interaktyvus demo | REVISION LT“. Šaltinio repozitorija – `UNKNOWN`.

## Duomenų bazė

Duomenų bazės, schemos, ORM ir migracijų šioje repozitorijoje nėra. `DATABASE_SCHEMA.md` nekurtas. Išorinio formos serverio lentelės – `NOT VERIFIED`. Jei paaiškėtų, kad `send.php` turi schemą, ją galima aprašyti tik turint tos schemos šaltinį, ne pagal spėjimą.

## Kas nepriklauso šiai architektūrai

REVISION ONLINE aprašyta `revision-online.html` kaip šiuo metu veikianti programa (ekranų nuotraukos su demonstraciniais duomenimis). REVISION 2.0 tame pačiame puslapyje pažymėta kaip kuriama koncepcija, ne veikianti programa. Abiejų programų kodas, API ir duomenų bazė šioje repo – `UNKNOWN` ir čia nedokumentuojami kaip esami moduliai.
