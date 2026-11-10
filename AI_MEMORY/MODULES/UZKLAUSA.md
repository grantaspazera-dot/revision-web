# Modulis: Užklausa

## 1. Paskirtis

Surinkti kliento poreikį ir perduoti jį REVISION LT. Vienintelis siuntimo kodas yra `site.zip` faile `assets/form.js`. Serveris `https://forma.revision.lt/send.php` šiai repozitorijai nepriklauso.

## 2. Pagrindinės funkcijos

- `assets/p4.js` modalas visuose turinio puslapiuose. Jis nieko nesiunčia. Pasirinkus kryptį atidaro `uzklausa.html?kryptis=...`.
- `form.js` veda klausimyną, patikrina laukus ir siunčia JSON.
- Pavykus rodo patvirtinimą. Nepavykus tinklui atidaro paruoštą `mailto:info@revision.lt` su tema „Užklausa iš svetainės“.

Kryptys kode: konsultacija, auditas, inventorizacija, mokymai, iranga, programa. Modalas turi ir „nežinau“ pasirinkimą. Klausimų medžio tekstas gyvena `form.js`; čia jo nekartojame.

## 3. Lankytojo eiga

1. Pasirenka kryptį modale arba puslapyje su `?kryptis=`.
2. Atsako į tos krypties klausimus, tada į bendrus projekto ir kontaktų klausimus.
3. Patikrina suvestinę ir spaudžia siųsti.
4. Sėkmės tekstas sako, kad susisieks per 24 val. Jei serveris nepasiekiamas, lankytojas turi pats išsiųsti atidarytą laišką.

Privalomi kontaktų laukai priklauso nuo pasirinkto bendravimo būdo (el. paštas arba telefonas). Įmonės pavadinimas ir vardas tikrinami kliente.

## 4. Įvestis ir išvestis

POST `https://forma.revision.lt/send.php`, `Content-Type: application/json`, `credentials: omit`, CORS. Kliento laukai: `direction`, `answers`, `company`, `name`, `email`, `phone`, `comment`, `marketing`, `website`, `elapsed`.

`website` yra paslėptas laukas, kurio lankytojas pildyti neturi. `elapsed` – sekundės nuo puslapio atidarymo. Tai apsauga nuo automatinio pildymo, matoma viešame scenarijuje. Serverio taisyklių čia neperkuriame.

Atsakas, kurio tikisi klientas: JSON su `ok: true` ir `confirmation` reikšmėmis `sent` arba `failed`. Kiti kliento kodu numatyti atvejai: HTTP 422 (taisyti kontaktus), 429 (per daug užklausų), 400 su `error: too_fast` (palaukti). Visa kita ir tinklo klaida veda į mailto. Laukimas nutraukiamas po 20 s.

Šie statusai perskaityti iš kliento. Vienintelis gyvas kreipinys 2026-11-10 buvo GET, ne POST: HTTP 403, kūnas `{"ok":false,"error":"origin"}`. Laiškas nesiųstas. Serverio elgsena – `NOT VERIFIED`.

## 5. Failai

- `uzklausa.html` – forma `#enquiry`, žingsniai `#step-host`, mygtukai `#btn-back` ir `#btn-next`.
- `assets/form.js` – klausimai ir siuntimas. Jungiamas tik šiame puslapyje.
- `assets/p4.js` – modalas `#p4-modal`.
- Poraštės ir kontaktų puslapio `mailto:info@revision.lt` bei `tel:+37061553311`.

## 6. API

Vienintelė sąsaja – aukščiau aprašytas POST. Serverio programos, autentifikacijos antraštės ir schemos repo neturi.

## 7. Duomenų bazė

Šiame modulyje jos nėra. Privatumo politika teigia, kad svetainė ir formos serveris užklausos turinio nesaugo, o iki 2 valandų laiko techninį skaitiklį pagal maišos funkcija užkoduotą IP. Tai svetainės tekstas (`privatumas.html`, data 2026-10-24). Įgyvendinimas – `NOT VERIFIED`.

## 8. Priklausomybės

Svetainės puslapiai atidaro formą. Siuntimas priklauso nuo `forma.revision.lt` ir nuo lankytojo pašto programos atsarginiame kelyje. Publikavimas turi pateikti tą patį `form.js`, kuris yra archyve.

## 9. Teisės ir saugumas

Forma vieša, be prisijungimo. Klientas nesiunčia slaptų raktų. Gautojas kode užfiksuotas kaip `info@revision.lt`. Rinkodaros sutikimas yra atskiras loginis laukas. Politika nurodo BDAR pagrindus ir 3 metų susirašinėjimo terminą, nebent sutartis ar įstatymas reikalauja ilgiau. Čia politikos teksto nekopijuojame.

Nesiųsk bandomųjų užklausų į gyvą endpointą be savininko patvirtinimo: jos gali išsiųsti tikrą laišką.

## 10. Klaidos ir ribos

- Serveris nepasiekiamas: mailto atsarga. Jei pašto programa neatsidaro, tekstas siūlo rašyti tiesiogiai.
- 422, 429 ir `too_fast` laiško neatidaro, palieka formą.
- Perkrovus puslapį neįsiųsti atsakymai dingsta (taip rašo ir privatumo tekstas; `form.js` saugyklos nenaudoja).
- Ilgas klausimų tekstas mailto nuorodoje gali viršyti naršyklės URL ribą. Ar tai įvyksta – `NOT VERIFIED`.

## 11. Testavimas

Perskaitytas `form.js` ir `p4.js`. POST, sėkmės laiškas ir mailto atsarga nepaleisti. GET į endpointą grąžino 403, kaip nurodyta aukščiau.

## 12. Apribojimai

Formos teksto ar adreso pakeitimas yra `site.zip` pakeitimas. Serverio taisymas yra ne šios repo darbas, kol neaiški jo saugykla (`UNKNOWN`).
