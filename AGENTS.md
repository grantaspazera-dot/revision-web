# AGENTS.md – REVISION svetainės repozitorija

Šis failas yra darbo sutartis agentams repozitorijoje `grantaspazera-dot/revision-web`. Techninė atmintis yra `AI_MEMORY/`. Prieš užduotį skaityk tik ją ir su užduotimi susijusius failus. Visos projekto dokumentacijos kalba – lietuvių. Nepatikrintus faktus žymėk `UNKNOWN` arba `NOT VERIFIED`. Slaptažodžių, raktų ir privačių prisijungimų į dokumentus nerašyk.

`README.md` eilutė „DEMO (peržiūra)“ yra pasenusi. Ja nesivadovauk. Patikrinta būklė aprašyta `AI_MEMORY/CURRENT_STATE.md`.

## Kas čia yra

Čia yra UAB REVISION LT viešos svetainės **publikavimo** repozitorija. Šaknyje yra `site.zip`, `README.md` ir `.github/workflows/deploy.yml`. Svetainės HTML, CSS ir JS šaltinio šiame repozitorijoje nėra: viešas rinkinys pagaminamas už repozitorijos ribų ir įdedamas į `site.zip`. Kur jis gaminamas – `UNKNOWN`.

Numatytoji šaka `main` per GitHub Pages Actions išpakuoja `site.zip` ir aptarnauja gyvą svetainę **https://revision.lt** (www nukreipia į šią pačią svetainę). Tai ne demonstracinė kopija.

## Savininko taisyklės

Šaltinis: savininko nurodymas 2026-11-10 techninės atminties užduotyje. Repozitorijoje atskiros rašytinės politikos iki tol nebuvo.

1. Pirmiausia atsarginė kopija (Git istorija, atskira šaka; svetainės pakeitimams – peržiūros repozitorija).
2. Svetainės pakeitimai pirmiausia peržiūroje: `grantaspazera-dot/revision-web-preview` (https://grantaspazera-dot.github.io/revision-web-preview/).
3. Gyvos svetainės, `main` šakos, DNS ir domeno nekeisk be atskiro, aiškaus savininko patvirtinimo. Patvirtinimas dokumentacijai ar peržiūrai nėra patvirtinimas gyvai svetainei.
4. Nejunk ir nederink šios dokumentacijos šakos į `main`, kol savininkas atskirai nepatvirtina.

## Draudžiama be atskiro patvirtinimo

- Keisti, perpakavoti ar pakeisti `site.zip`.
- Keisti svetainės turinį, įskaitant `CNAME` archyvo viduje (dabar jame yra `revision.lt`).
- Keisti `.github/workflows/`.
- Stumti į `main`, derinti PR į `main` arba ranka paleisti „Deploy site to GitHub Pages“.
- Keisti DNS, GitHub Pages domeną ar sertifikatą.

Dokumentacijos šakos įkėlimas ir PR diegimo nepaleidžia. **Sujungimas į `main` paleistų.** Paaiškinimas: `AI_MEMORY/MODULES/PUBLIKAVIMAS.md`.

## Darbo režimas

Laikykis REVISION OS AI Development & Technical Memory Standard v1.0 (2026-11-08) proceso: suprask užduotį, skaityk atmintį, ribok apimtį, patikrink realų kodą ir Git, keisk tik tai, kas būtina, patikrink rezultatą, atnaujink tik paveiktus atminties failus, palik `AI_MEMORY/TASK_HISTORY/` įrašą ir pabaigoje pateik standarto 10 skyriaus ataskaitą.

Režimai: FAST (mažas izoliuotas pakeitimas), STANDARD (modulio elgsena), ARCHITECT (architektūra, diegimas, domenas, keli moduliai). Diegimas į gyvą svetainę visada yra ARCHITECT ir reikalauja atskiro patvirtinimo.

Jei dokumentacija ir failai nesutampa, tikėk patikrintu failu, pataisyk atmintį ir tęsk. Veikiančio kodo vien buvimas dar nereiškia, kad jis teisingas: galimą klaidą užrašyk `AI_MEMORY/KNOWN_ISSUES.md`, jei ji neįeina į užduotį.

Duomenų bazės schemos failo nėra, nes šioje repozitorijoje duomenų bazės nėra. Išorinio `forma.revision.lt` saugyklos schema – `NOT VERIFIED`. Atskiri `DEVELOPMENT_RULES.md` ir `SECURITY_RULES.md` nekartojami: kūrimo ir saugumo taisyklės yra šiame faile.

## Patikra

Automatinės testų komandos repozitorijoje nėra. Dokumentacijos užduočiai pakanka struktūros, nuorodų ir, jei keičiama svetainė, tikslinio turinio palyginimo. Neteigk, kad testas praėjo, jei jis nepaleistas. Svetainės pakeitimo nevadink baigtu, kol nepatikrinta peržiūra ir savininkas atskirai nepatvirtino gyvos publikacijos.
