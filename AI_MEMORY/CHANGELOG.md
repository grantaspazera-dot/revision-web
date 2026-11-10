# Pakeitimų žurnalas

Naujesni įrašai viršuje. Istoriniai punktai iki 2026-11-10 perrašyti iš `git log` žinučių. Tų commitų `site.zip` vidaus diff eilutė po eilutės neperžiūrėtas, išskyrus dabartinį `main` archyvą, kuris atidarytas techninei atminčiai.

## 2026-11-10 – techninė atmintis

- Šaka `cursor/ai-memory-rollout-e2ef`. Į `main` nestumta ir nederinta.
- Sukurti `AGENTS.md` ir `AI_MEMORY/` pagal REVISION OS standartą v1.0, 12 skyrių.
- Funkcinio kodo, `site.zip`, workflow ir svetainės turinio pakeitimų nėra.
- `DATABASE_SCHEMA.md` nekurtas: duomenų bazės šioje repo nėra, išorinė schema `NOT VERIFIED`.

## 2026-10-31 – `14ef47e` REVISION P8.3 – gyva versija

- Dabartinis `main`. Archyvo datos 2026-10-31. GitHub Pages diegimas sėkmingas (paleidimas `41200037879`).
- Kas pasikeitė archyvo viduje nuo ankstesnio commit, eilutės tikslumu – `NOT VERIFIED`.

## 2026-10-25 – `9d9e8b5` Klaidų taisymai, Kodėl REVISION, Skambinti mygtukas, 404, og image

- Diegimas sėkmingas (`40230588051`). Turinio diff – `NOT VERIFIED`. Dabartiniame archyve yra `404.html`, `assets/og-image.png` ir skambinimo nuorodos.

## 2026-10-24 – `f7148b0` Form sends via forma.revision.lt

- Diegimas sėkmingas (`40074560261`).
- Dabartinis `assets/form.js` pirmiausia siunčia į `https://forma.revision.lt/send.php`, o `mailto:info@revision.lt` naudoja, kai serveris nepasiekiamas.

## 2026-10-24 – `c340453` Switch site to revision.lt

- Diegimas sėkmingas (`40070533812`).
- Dabartiniame archyve `CNAME` yra `revision.lt`, canonical ir sitemap naudoja `https://revision.lt/`.

## 2026-10-24 – `1c3e031` Update site: remove DEMO, LinkedIn, privacy policy

- Diegimas sėkmingas (`40066351231`).
- Dabartiniame archyve yra `privatumas.html`, LinkedIn ir YouTube nuorodos. Commit žinutės „remove DEMO, LinkedIn“ ir dabartinio turinio santykis – `NOT VERIFIED` (vėlesni commitai galėjo nuorodas grąžinti). `README.md` DEMO frazę vis dar turi.

## 2026-10-24 – `e40088b` Add deploy workflow

- Atsirado `.github/workflows/deploy.yml`. Pirmas diegimas sėkmingas (`40065996256`).

## 2026-10-24 – `b3b08a0` Add site

- Atsirado `site.zip`. To meto archyvo turinys – `NOT VERIFIED`.

## 2026-10-24 – `282e961` Initial commit

- Pradinis commit. Tiksli failų sudėtis – `NOT VERIFIED`.
