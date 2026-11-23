# Modulis: Publikavimas

## 1. Paskirtis

Iš `main` šakos paimti `site.zip`, išpakuoti ir publikuoti GitHub Pages aplinkoje, kuri aptarnauja https://revision.lt.

## 2. Pagrindinės funkcijos

Workflow failas `.github/workflows/deploy.yml`, pavadinimas „Deploy site to GitHub Pages“.

Paleidimas:

- `push` į šaką `main`;
- `workflow_dispatch`.

`pull_request` trigerio nėra. `paths` ir `paths-ignore` nėra.

Leidimai: `contents: read`, `pages: write`, `id-token: write`. Viena grupė `pages`, `cancel-in-progress: true`. Aplinka `github-pages`.

Žingsniai: `actions/checkout@v4`, `mkdir _site && unzip -q site.zip -d _site`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3` su keliu `_site`, `actions/deploy-pages@v4`.

Domeną nuneša archyvo `CNAME` (`revision.lt`), ne atskiras failas repo šaknyje.

## 3. Darbo eiga

1. Commit patenka į `main` (sujungimas irgi yra `push`).
2. Veiksmas išpakuoja visą archyvą, įskaitant `CNAME` ir `.nojekyll`.
3. Pages pakeičia gyvą svetainę tuo rinkiniu.

Peržiūros repo `grantaspazera-dot/revision-web-preview` turi tokį patį workflow tekstą. Jos Pages adresas yra `https://grantaspazera-dot.github.io/revision-web-preview/`, be savojo domeno. Ji gyvo `revision.lt` nepakeičia.

## 4. Įvestis ir išvestis

Įvestis: `site.zip` toje šakoje, kurią veiksmas išsiskaito. Išvestis: Pages artefaktas ir viešas svetainės turinys. Dokumentų failai (`AGENTS.md`, `AI_MEMORY/`) į `_site` nepatenka, nes jų nėra archyve. Jie vis tiek keliauja kartu su commit, jei commit yra `main`.

## 5. Failai

- `.github/workflows/deploy.yml`
- `site.zip`
- archyvo viduje: `CNAME`, `.nojekyll`, svetainės failai

## 6. API

GitHub Actions ir Pages. Kito diegimo API nėra.

## 7. Duomenų bazė

Nėra.

## 8. Priklausomybės

Priklauso nuo `site.zip` vientisumo ir nuo GitHub Pages aplinkos. Svetainės ir užklausos moduliai lankytoją pasiekia tik po šio diegimo.

## 9. Teisės ir saugumas

Workflow paslapčių nenaudoja ir į žurnalą jų nerašo. `pages: write` leidžia pakeisti gyvą svetainę. Todėl:

- nekelk svetainės pakeitimų tiesiai į `main`;
- nederink net dokumentacijos PR, kol savininkas atskirai nepatvirtina;
- nespausk „Run workflow“;
- nekeisk šio failo, `site.zip` ir `CNAME` be atskiro patvirtinimo.

Prieš svetainės keitimą: atsarginė kopija (šaka ir esamas commit), pakeitimas peržiūros repo, savininko patvirtinimas, tik tada gyvas diegimas.

## 10. Klaidos ir ribos

Jei `site.zip` sugadintas, `unzip` žingsnis nutrūksta ir senas Pages artefaktas lieka, kol naujas diegimas nepavyksta. Tai įprasta Actions elgsena; šiam repo atskirai nesugadintu archyvu nepatikrinta.

`cancel-in-progress` gali nutraukti ankstesnį dar vykstantį diegimą, jei į `main` ateina antras push. Ar tai nutiko – istorijoje nematyta.

## 11. Testavimas

2026-11-10 workflow **nepaleistas**. Išvada apie dokumentus padaryta iš YAML ir iš istorijos:

| Situacija | Ar veiksmas paleidžiamas |
| --- | --- |
| Nauja šaka, ne `main` | Ne. Trigeris yra tik `main`. |
| Atidarytas PR | Ne. `pull_request` trigerio nėra. |
| Sujungimas į `main`, net jei keitėsi tik Markdown | Taip. Filtro pagal kelius nėra. Veiksmas vėl išpakuotų `site.zip` ir publikuotų gyvą svetainę. |
| `workflow_dispatch` | Taip, rankiniu paleidimu. Nepaleista. |

Istorija: 6 sėkmingi `push` į `main` nuo 2026-10-24 iki 2026-10-31. Dokumentų-only `main` commit pavyzdžio nėra, todėl „būtų paleista“ yra išvada iš failo, ne iš įvykdyto dokumentų diegimo.

Gyva svetainė po P8.3 diegimo (`41200037879`, 2026-10-31 12:12 UTC) 2026-11-10 vis dar atidavė tą patį `index.html` kaip archyvas.

## 12. Apribojimai

Šis modulis yra gyva produkcija. Dokumentacijos šaka jo nekeičia ir į `main` nerašoma.
