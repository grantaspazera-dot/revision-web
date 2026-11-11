# Žinomos problemos ir atviri klausimai

Čia tik tai, kas patikrinta arba aiškiai nepatvirtinta. Tai nėra darbų sąrašas gyvai svetainei. Gyvos svetainės taisymai reikalauja atskiro savininko patvirtinimo.

## KI-1. README ir GitHub aprašas vadina svetainę demo

`README.md` ir repozitorijos aprašas: „REVISION LT svetainės DEMO (peržiūra)“. `main` per GitHub Pages aptarnauja https://revision.lt, o commit `1c3e031` žinutė mini DEMO nuėmimą iš svetainės. README šioje užduotyje nekeistas, kad dokumentacijos rinkinys liktų tik `AGENTS.md` ir `AI_MEMORY/`.

## KI-2. Dokumentų įrašymas į `main` paleidžia gyvą diegimą

`deploy.yml` klausosi visų `push` į `main` ir `workflow_dispatch`. `paths` filtro nėra. Istorijoje kiekvienas `push` į `main` paleido sėkmingą diegimą. Vien dokumentacijos sujungimas į `main` išpakuotų tą patį `site.zip` ir vėl publikuotų https://revision.lt. Šaka ir PR diegimo nepaleidžia. Rankinis paleidimas kitoje šakoje irgi galėtų publikuoti tą šaką; tai nebuvo vykdyta – išvada iš workflow teksto.

## KI-3. Svetainės šaltinis nėra repozitorijoje

Keisti tekstą ar stilių galima tik per naują `site.zip`, o ne per atskirus HTML failus. Kur renkamas rinkinys – `UNKNOWN`. PR diff beveik neparodo svetainės turinio, nes jis suspaustas.

## KI-4. Užklausos formos elgsena nėra vien mailto

Savininko santrauka, kad forma atidaro `mailto:info@revision.lt`, atitinka tik atsarginį kelią ir poraštės nuorodas. Dabartinis `assets/form.js` pirmiausia daro POST į `https://forma.revision.lt/send.php`. Serverio kodas, laiško pristatymas ir saugojimas – `NOT VERIFIED`. GET 2026-11-10 grąžino HTTP 403.

## KI-5. Peržiūros repo nėra patvirtinta kaip naujesnis dizainas

`revision-web-preview` egzistuoja ir jos Pages svetainė yra `noindex`. Paskutinis commit 2026-10-30, gyvas P8.3 – 2026-10-31. Archyvų dydžiai skiriasi (peržiūra 9 172 622 B, ši repo 9 171 756 B). Pilnas diff – `NOT VERIFIED`. Teiginys „ten yra naujesnis dizainas“ 2026-11-10 datos atžvilgiu nepatvirtintas.

## KI-6. Nėra automatinių testų

Nėra testų, lint ar surinkimo komandos. Regresija matoma tik palyginus archyvą ir gyvą svetainę po savininko patvirtinto diegimo.

## KI-7. Nežinomi išoriniai šaltiniai

- Įmonės kodas ir PVM kodas svetainėje – `UNKNOWN`.
- `site.zip` generatorius – `UNKNOWN`.
- `forma.revision.lt` programa ir schema – `NOT VERIFIED`. Privatumo tekstas teigia, kad užklausų turinys ten nesaugomas.
- Ar serveris tikrai UAB Bacloud – `NOT VERIFIED` (svetainės tekstas taip sako; HTTP antraštė buvo LiteSpeed).
- `demo.revision.lt` šaltinio repo – `UNKNOWN`.
- REVISION ONLINE ir Android APP kodas – `UNKNOWN`. REVISION 2.0 svetainėje aprašyta kaip koncepcija, ne veikianti programa.
- Visi archyvo failai, išskyrus `index.html` ir `404.html`, su gyvu domenu baitais nepalyginti – `NOT VERIFIED`.

## KI-8. Įžvalgų puslapis be straipsnių

`izvalgos.html` pats rašo, kad straipsnių kol kas nepublikuoja ir rodo būsimas temas. Tai turinio būsena, ne diegimo klaida.

## KI-9. Actions versijos neprisegtos prie SHA

Workflow naudoja `actions/checkout@v4`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3`, `actions/deploy-pages@v4`. Tai stebėjimas, ne patvirtinta klaida. Keitimas būtų workflow keitimas ir reikalautų atskiro patvirtinimo.
