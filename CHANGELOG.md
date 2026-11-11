# Keitimų žurnalas

## 2026-11-10 – Inventorizacija PRO kainodara

Vieša programos nuoma aprašyta kaip **Inventorizacija PRO** (REVISION ONLINE). Keturi planai už vieną inventorizaciją, 7 dienų prieiga, kainos be PVM: MINI 50 €, VID 100 €, MAXI 150 € (ženklelis „Populiariausias“), PRO 200 €. Papildoma inventorizacija ir kiekviena papildoma diena po 7 dienų – 50 % plano kainos (25 / 50 / 75 / 100 €). Tai pakeičia 100 € / 40 € / 20 € schemą. Tos schemos tekstų P8.3 archyve nebuvo.

Priedai palikti: Android programa 40 € už skenerį per inventorizaciją, skenerio nuoma 40 € už vienetą per darbo dieną, mokymai ir konsultacijos 150 €/val. (paprastai 2 val.), inventorizacijos valdymas 900 €/d.

Pilnos kortelės yra `revision-online.html#kainos`. Pradžios puslapyje kainos neužima ekspertinių paslaugų vietos: ten yra nuoroda. Šaltinis: `docs/KAINODARA.md`.

Neliesta: `CNAME` (`revision.lt`), `.github/workflows/deploy.yml`, logotipai, programos ekranų nuotraukos, klientų logotipai.

Patikra: `python3 scripts/check-site.py`.

### Atšaukimas po sujungimo

Sujungimas į `main` paleidžia GitHub Pages ir iš naujo publikuoją https://revision.lt. Jei kainodarą reikia grąžinti, atšaukite sujungimo commit ir įkelkite į `main`:

```bash
git revert -m 1 <sujungimo-commit>
git push origin main
```

Tai vėl išpakuoja ankstesnį `site.zip`. DNS, `CNAME` ir Pages nustatymų nekeiskite.
