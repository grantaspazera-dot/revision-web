# Projekto apžvalga

Patikrinimo data: 2026-11-10. Šaltiniai išvardyti `CURRENT_STATE.md`.

## Paskirtis

`grantaspazera-dot/revision-web` publikuoja UAB REVISION LT viešą svetainę https://revision.lt. Įmonė svetainėje prisistato kaip sandėlio valdymo, inventorizacijos, audito, mokymų ir inventorizacijos technologijų tiekėja. Adresas svetainėje: R. Kalantos g. 119, Kaunas. Juridinio asmens kodas ir PVM kodas svetainės tekstuose nerasti – `UNKNOWN`.

Repozitorija nėra programos REVISION ONLINE, Android APP ar REVISION 2.0 šaltinis. Ji saugo jau surinktą svetainę ir jos diegimą.

## Kas naudojasi

- Lankytojai skaito paslaugų puslapius, skambina ar rašo el. paštu.
- Potencialūs klientai pildo užklausą `uzklausa.html`.
- Savininkas ir agentai keičia repozitoriją tik per šaką ir PR. Gyvą svetainę keičia tik atskiru patvirtinimu.

Vidinės paskyros, rolių ar administravimo šioje repozitorijoje nėra.

## Aukšto lygio sandara

```text
revision-web/
├── README.md                         pasenęs vienos eilutės aprašas
├── site.zip                          viešas svetainės rinkinys (197 failai)
├── .github/workflows/deploy.yml      GitHub Pages diegimas iš main
├── AGENTS.md                         agentų darbo sutartis
└── AI_MEMORY/                        techninė atmintis
```

Svetainės puslapiai, stiliai, paveikslai ir scenarijai yra tik `site.zip` viduje. Šaknyje atskiro `CNAME` nėra; domeno failas yra archyve ir jo turinys – `revision.lt`.

## Pagrindinės viešos funkcijos

- Paslaugų ir įmonės puslapiai lietuvių kalba.
- Užklausos vedlys su krypties pasirinkimu.
- Telefono ir el. pašto nuorodos.
- `robots.txt`, `sitemap.xml`, Open Graph paveikslas, `404.html`.
- Nuorodos į išorinę programos demonstraciją https://demo.revision.lt/ ir į peržiūros svetainę kitoje repozitorijoje.

## Ko šis projektas nedaro

- Nelaiko duomenų bazės ir migracijų.
- Neturi svetainės generatoriaus, paketų tvarkyklės ar testų.
- Netalpina REVISION ONLINE ar Android APP kodo. Jų saugykla – `UNKNOWN`.

## Jau buvusi dokumentacija

Iki šios atminties buvo tik `README.md`: „REVISION LT svetainės DEMO (peržiūra)“. Ta pati frazė yra GitHub repozitorijos apraše. Ji neatitinka patikrintos būklės: `main` aptarnauja https://revision.lt. README sąmoningai neperrašytas šioje užduotyje; prieštaravimas užregistruotas `KNOWN_ISSUES.md`. Nauja atmintis README turinio nekartoja kaip fakto.
