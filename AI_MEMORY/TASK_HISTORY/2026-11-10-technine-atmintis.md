# TASK 2026-11-10-01 – Techninės atminties pirminis įdiegimas

- Data: 2026-11-10
- Būsena: atlikta dokumentacijos apimtyje, laukia savininko peržiūros; į `main` nederinta
- Režimas: ARCHITECT (gyva svetainė šalia, nors kodas nekeistas; diegimo poveikis įvertintas ir sustabdytas ties PR)

## Tikslas

Parengti REVISION OS AI Development & Technical Memory Standard v1.0 12 skyriaus techninę atmintį pagal realią `revision-web` būklę. Funkcinio kodo nekeisti.

## Pradinė problema

Repozitorijoje nebuvo `AGENTS.md` ir `AI_MEMORY/`. Vienintelis dokumentas `README.md` vadino gyvą svetainę demo. Nebuvo kur kitam agentui perskaityti diegimo, formos ir savininko ribų.

## Atlikti pakeitimai

Sukurta techninė atmintis ir agentų sutartis. `site.zip`, workflow, `README.md`, CNAME ir svetainės turinys nekeisti. `DATABASE_SCHEMA.md` nekurtas: duomenų bazės nėra, išorinė schema `NOT VERIFIED`.

## Pakeisti failai

- `AGENTS.md`
- `AI_MEMORY/PROJECT_OVERVIEW.md`
- `AI_MEMORY/SYSTEM_ARCHITECTURE.md`
- `AI_MEMORY/MODULE_REGISTRY.md`
- `AI_MEMORY/CURRENT_STATE.md`
- `AI_MEMORY/CHANGELOG.md`
- `AI_MEMORY/KNOWN_ISSUES.md`
- `AI_MEMORY/MODULES/SVETAINE.md`
- `AI_MEMORY/MODULES/UZKLAUSA.md`
- `AI_MEMORY/MODULES/PUBLIKAVIMAS.md`
- `AI_MEMORY/TASK_HISTORY/2026-11-10-technine-atmintis.md`

## Paveikti moduliai

Naujai aprašyti, kodo nekeisti: Svetainė, Užklausa, Publikavimas.

## API / duomenų bazės pakeitimai

Nėra.

## Atlikti testai ir rezultatai

- Struktūra, Git istorija ir workflow tekstas perskaityti.
- Archyvas atidarytas laikiname kataloge už repo ribų; repo failas nekeistas.
- Gyvas `index.html` ir vienas 404 atsakas sutapo su archyvu (SHA-256).
- `www.revision.lt` grąžino 301 į `https://revision.lt/`.
- Formos GET grąžino HTTP 403. POST ir mailto nepaleisti.
- Peržiūros svetainė ir `demo.revision.lt` grąžino HTTP 200; peržiūroje yra `noindex,nofollow`.
- Diegimo veiksmas šiai šakai nepaleistas. Iš YAML: PR ir ne-`main` šaka veiksmo nekelia; sujungimas į `main` pakeltų.

Nepaleista: automatiniai testai (jų nėra), naršyklės paspaudimai, visų 197 failų palyginimas su gyvu domenu, formos laiško siuntimas, `workflow_dispatch`, peržiūros ir gamybinio `site.zip` pilnas diff.

## Atnaujinta dokumentacija

Visa šios užduoties atmintis. `README.md` paliktas ir užregistruotas kaip KI-1.

## Likusios problemos

Žr. `KNOWN_ISSUES.md`. Svarbiausia: nederinti šio PR be atskiro savininko patvirtinimo, nes `main` neturi kelių filtro.

## Kitas rekomenduojamas žingsnis

Savininkas peržiūri PR. Jei atmintis teisinga ir jis atskirai leidžia sujungimą, sujungimas vis tiek paleis gyvą pakartotinį to paties `site.zip` diegimą. Jei to nenori, prieš sujungimą reikia atskiro, jo patvirtinto workflow pakeitimo (`paths` filtras) – tai jau ne šios užduoties darbas.
