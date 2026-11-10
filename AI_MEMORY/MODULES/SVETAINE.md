# Modulis: Svetainė

## 1. Paskirtis

Vieša UAB REVISION LT svetainė lietuvių kalba. Turinys supakuotas `site.zip` ir pateikiamas per modulį Publikavimas.

## 2. Pagrindinės funkcijos

- Paslaugų, įmonės ir kontaktų puslapiai.
- Bendras meniu, poraštė, skambinimo nuoroda `tel:+37061553311`.
- Krypties modalas (`assets/p4.js`) atidaro užklausą, pats duomenų nesiunčia.
- SEO: canonical, Open Graph, `robots.txt`, `sitemap.xml`, `assets/og-image.png` (1200×630 pagal meta).
- `404.html`. Nežinomame kelyje jis gyvai sutapo su archyvu (2026-11-10).

## 3. Lankytojo eiga

Meniu: Paslaugos, Konsultacijos ir auditas, Optimizavimas, Inventorizacija, Mokymai ir įranga, REVISION ONLINE, Kontaktai. Šalia – LinkedIn ir YouTube. „Aptarti poreikį“ atidaro modalą arba veda į `uzklausa.html`. Poraštėje yra `mailto:info@revision.lt`, demo nuoroda, apie mus, įžvalgos ir privatumas.

## 4. Įvestis ir išvestis

Įvestis – statiniai failai archyve. Išvestis – HTML dokumentai. Formos duomenų šis modulis nekaupia. `main.js` nenaudoja tinklo, slapukų ir saugyklos.

## 5. Failai

Archyve 197 failai. Puslapiai:

| Failas | `<title>` archyve |
| --- | --- |
| `index.html` | Sandėlio valdymas ir inventorizacija \| REVISION LT |
| `paslaugos.html` | Sandėlio valdymo ir inventorizacijos paslaugos \| REVISION LT |
| `konsultacijos-ir-auditas.html` | Sandėlio valdymo konsultacijos ir auditas \| REVISION LT |
| `procesu-optimizavimas.html` | Sandėlio procesų optimizavimas – lokacijos, ženklinimas, atsargos \| REVISION LT |
| `inventorizacija.html` | Prekių, atsargų ir turto inventorizacija \| REVISION LT |
| `mokymai-ir-iranga.html` | Inventorizacijos mokymai ir įrangos nuoma \| REVISION LT |
| `revision-online.html` | REVISION ONLINE – inventorizacijos programa \| REVISION LT |
| `uzklausa.html` | Užklausa – aptarkime jūsų sandėlio poreikį \| REVISION LT |
| `apie-mus.html` | Apie mus – inventorizacijos ekspertai \| REVISION LT |
| `kontaktai.html` | Kontaktai – susisiekime \| REVISION LT |
| `izvalgos.html` | Įžvalgos apie inventorizaciją ir sandėlį \| REVISION LT |
| `privatumas.html` | Privatumo politika \| REVISION LT |
| `privatumo-politika/index.html` | Privatumo politika \| REVISION LT; iškart nukreipia į `/privatumas.html` |
| `404.html` | Puslapis nerastas \| REVISION LT |

`procesu-optimizavimas.html` ir `revision-online.html` `<title>` šios kortelės rašymo metu nebuvo išrašyti atskira eilute. Jie yra archyve ir sitemap. Tikslūs title tekstai – `NOT VERIFIED` šiame faile, kol neperskaityta `<title>` eilutė. Nekartok spėjimo.

Scenarijai daugumoje puslapių: `assets/main.js`, `assets/p4.js`. `assets/form.js` – tik `uzklausa.html`. `404.html` naudoja absoliučius kelius `/assets/...`, kad veiktų ne šaknyje.

Stiliai: `assets/style.css`, `fonts.css`, `pack.css` ir sluoksniai `p0.css`–`p72.css`. Komentarai juose aprašo P0–P7.2 ir rollback kaip `<link>` pašalinimą. Ne visi puslapiai jungia visus sluoksnius (`privatumas.html` rinkinys trumpesnis).

Medija: `assets/img/`, `assets/brand/`, šriftai `assets/fonts/`. `assets/fonts/OFL.txt` – šrifto licencija.

`CNAME` archyvo šaknyje, turinys `revision.lt`. `.nojekyll` tuščias failas.

## 6. API

Savo HTTP API nėra. Išorinės nuorodos išvardytos `SYSTEM_ARCHITECTURE.md`.

## 7. Duomenų bazė

Nėra.

## 8. Priklausomybės

Publikavimas turi išpakuoti archyvą. Užklausos modulis reikalingas formos puslapiui. Demo ir peržiūra yra kitos svetainės.

## 9. Teisės ir saugumas

Turinys viešas. Autentifikacijos nėra. Peržiūrėtuose tekstiniuose failuose raktų ir slaptažodžių nerasta. Vieši kontaktai svetainėje: `info@revision.lt`, `grantas@revision.lt` (kontaktų puslapyje – direktorius Grantas Pažėra), telefonas `+370 615 53311`.

Privatumo politika nurodo valdytoją REVISION LT, UAB, prašymų kelią el. paštu ir VDAI nuorodą. Visas politikos tekstas čia nekopijuojamas.

## 10. Klaidos ir ribos

- Nežinomas URL: `404.html` (gyvai patikrinta vienu keliu).
- `izvalgos.html` straipsnių nerodo, tai parašyta pačiame puslapyje.
- `revision-online.html` skiria veikiančią REVISION ONLINE ir kuriamos REVISION 2.0 koncepciją. Programų kodas ne šiame modulyje.
- Dalis vaizdų poraštėje pažymėta „Dalis vaizdų – iliustracijos“.

## 11. Testavimas

2026-11-10 gyvo `index.html` ir vieno 404 atsako SHA-256 sutapo su archyvu. Kiti puslapiai gyvai neatsisiųsti. Naršyklėje paspaudimų scenarijus nepaleistas.

## 12. Apribojimai

Teksto pataisa neįmanoma be naujo `site.zip`. To daryti negalima be atsarginės kopijos, peržiūros ir atskiro savininko patvirtinimo.
