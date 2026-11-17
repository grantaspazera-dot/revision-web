# Modulių registras

Registruojami tik šioje repozitorijoje realiai esantys moduliai. Inventorizacijos, sandėlio, naudotojų ar ataskaitų programų moduliai čia nekuriami: svetainė tas paslaugas aprašo, bet jų sistemų kodo repo neturi.

Duomenų bazės modulio nėra. `DATABASE_SCHEMA.md` nėra, nes schemos nėra ką tikrinti. Išorė – `NOT VERIFIED`.

| Modulis | Atsakomybė | Kur yra | Priklauso nuo | Sąsaja |
| --- | --- | --- | --- | --- |
| Svetainė | Vieši puslapiai, stiliai, medija, SEO, 404 | `site.zip` | Publikavimas, kad failai pasiektų domeną | Nuorodos į užklausą, telefoną, paštą, demo |
| Užklausa | Krypties modalas ir kelių žingsnių forma | `site.zip`: `uzklausa.html`, `assets/form.js`, `assets/p4.js` | Svetainės puslapiai; išorinis `forma.revision.lt` | JSON POST ir mailto atsarga |
| Publikavimas | `main` šakos išpakavimas į GitHub Pages | `.github/workflows/deploy.yml` | `site.zip` ir jame esantis `CNAME` | GitHub Pages aplinka `github-pages` |

Išsamiau: `MODULES/SVETAINE.md`, `MODULES/UZKLAUSA.md`, `MODULES/PUBLIKAVIMAS.md`.

## Sąmoningai neįtraukti pavyzdžiai

Standarto pavyzdiniai moduliai (atsargos, lokacijos, produktai, ataskaitos, naudotojai, sandėlis, auditas) šioje repo kaip kodas neegzistuoja. Jų failų `MODULES/` nekuriama.

REVISION ONLINE, Android APP, REVISION 2.0 ir `demo.revision.lt` yra išoriniai produktai arba atskiros svetainės. Jų šaltinis – `UNKNOWN`.
