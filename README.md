# ⚠️ ARHIVIRANO — Projekt je preseljen na [`stepanic/biblija`](https://github.com/stepanic/biblija)

> [!IMPORTANT]
> **Ovaj repozitorij (`domovinatv/biblija`) je arhiviran kako bi se izbjeglo dupliciranje.**
> Sav daljnji razvoj, kompletan deterministički JSON katalog (73 knjige, 1.329 poglavlja, 35.410 redaka s USFM kodovima i ispravljenim `errata.json`), **SQLite (FTS5)** baza podataka, cjeloviti **[Audit & Diff izvještaj](https://github.com/stepanic/biblija/blob/main/AUDIT.md)** te **Astro 5 + Cloudflare Workers/D1 web aplikacija (*Biblija kroz 365 dana*)** nalaze se u glavnom repozitoriju:
>
> ### 👉 **[https://github.com/stepanic/biblija](https://github.com/stepanic/biblija)**
>
> **Važna napomena o atribuciji izvora u ovom repozitoriju:** Unakrsnom stih-po-stih usporedbom u [`stepanic/biblija`](https://github.com/stepanic/biblija/blob/main/AUDIT.md) dokazano je da izvori `eBible.org (hrv_usfm)` i `CrossWire (CroSaric)` — koji su u međunarodnim bazama desetljećima označeni kao *„prijevod Ivana Ev. Šarića"* — zapravo sadrže stariju digitalizaciju **Zagrebačke Biblije (Kršćanska sadašnjost, 1968.)**, a ne Šarićev prijevod. Svi oštećeni stihovi iz oba izvora su unakrsno popravljeni i objedinjeni u **[`stepanic/biblija`](https://github.com/stepanic/biblija)**.

---

# Biblija: hrvatska katolička Biblija u JSON-u (Arhiva)

Strukturirana, offline baza hrvatskog katoličkog prijevoda Svetoga pisma: knjiga, poglavlje i
stih u običnim JSON datotekama, bez API-ja i bez baze podataka. Jedna datoteka po knjizi,
73 knjige katoličkog kanona, uključujući deuterokanonske knjige i grčke dodatke Esteri i Danielu.

Zasad sadrži prijevod **Ivana Ev. Šarića** (1941./42.), jedini katolički prijevod na hrvatski
koji je dostupan u otvorenom strukturiranom obliku. Projekt je dio [DOMOVINA.ai](https://domovina.ai).

## Brzi početak

```bash
git clone https://github.com/domovinatv/biblija.git
```

```python
import json

ivan = json.load(open("biblija/data/saric/50-JHN.json", encoding="utf-8"))
print(ivan["name"])                                # Evanđelje po Ivanu
print(ivan["chapters"][2]["verses"][15]["text"])   # Iv 3,16
```

```bash
# Psalam 23 u terminalu
jq -r '.chapters[22].verses[] | "\(.v) \(.text)"' data/saric/23-PSA.json
```

## Što je u repou

| Putanja | Sadržaj |
|---|---|
| [`data/books.json`](data/books.json) | katalog 73 knjige: USFM kod, katolički redoslijed, kratica (Post, Izl… Otk), naziv, deuterokanonske oznake |
| [`data/saric/`](data/saric) | Šarićev prijevod, `NN-ID.json` za svaku knjigu (`01-GEN.json` … `73-REV.json`) |
| [`data/translations.json`](data/translations.json) | podaci o prijevodu: izvor, sha256 izvora, prava, statistika |
| [`data/saric-errata.json`](data/saric-errata.json) | svaka ispravka u odnosu na izvor, s obrazloženjem |
| [`data/saric-compare.json`](data/saric-compare.json) | usporedba s drugim neovisnim izvorom, stih po stih |
| [`scripts/`](scripts) | preuzimanje izvora, izgradnja JSON-a, validacija |
| [`docs/PLAN.md`](docs/PLAN.md) | istraživanje: hrvatski prijevodi, prava, izvori i plan |

Brojke: 73 knjige, 1.328 poglavlja i 35.539 zapisa (stihova i dijelova stihova). Ukupno oko 6 MB.

### Oblik datoteke

```json
{
  "translation": "saric",
  "book": "JHN",
  "order": 50,
  "testament": "NT",
  "deuterocanonical": false,
  "name": "Evanđelje po Ivanu",
  "abbr": "Iv",
  "chapters": [
    { "chapter": 1, "verses": [ { "v": 1, "text": "U početku bijaše Riječ…", "p": true } ] }
  ]
}
```

| Polje stiha | Značenje |
|---|---|
| `v` | broj stiha |
| `part` | slovo dodatka unutar stiha. Postoji samo kod grčkih dodataka Esteri (npr. Est 4,17a–z). |
| `text` | tekst stiha, Unicode NFC, normalizirani razmaci |
| `p` | `true` ako stih počinje novi odlomak |

Knjige se identificiraju [USFM kodovima](https://ubsicap.github.io/usfm/identification/books.html)
(`GEN`, `TOB`, `SIR`, `MAT`…), pa se lako spajaju s drugim prijevodima i alatima.

### Napomene o tekstu

- **Redoslijed stihova** je redoslijed tiskanog izdanja. Na 7 mjesta stihovi su premješteni
  kao u Jeruzalemskoj Bibliji: 1 Sam 9, Job 36, Iz 33, Jr 29, Jr 36, Nah 2 i Hab 2.
  Primjer: Jr 29,8–9 dolazi iza 15. stiha. Ako trebaš numerički redoslijed, sortiraj po `v`.
- **Dodaci Esteri** su zasebni zapisi s istim `v` i različitim `part`.
- **Sirah** ima proslov u polju `intro`.
- **Daniel 3** u izvoru završava stihom 99.

## Izgradnja i provjera

Tekst se gradi iz [eBible.org `hrv`](https://ebible.org/find/details.php?id=hrv) (USFM).
Provjerava se stih po stih prema neovisnom izvoru,
[scrollmapper/bible_databases](https://github.com/scrollmapper/bible_databases) (CrossWire `CroSaric`).

```bash
scripts/fetch_saric.sh             # izvori u .cache/ (nije u gitu)
python3 -I scripts/build_saric.py  # data/saric/*.json, translations.json, errata
python3 -I scripts/validate.py     # struktura i usporedba izvora
```

Potreban je samo Python 3 bez dodatnih paketa. Rezultat zadnje provjere:

- struktura: 0 problema;
- tekst se poklapa s drugim izvorom u svakom stihu. Jedina razlika je 9 stihova u Esteri,
  gdje drugi izvor upisuje oznake dodataka u sam tekst;
- dvije ispravke oznaka u izvoru (Est 1,1 i 3,13), zapisane u `saric-errata.json`.

## Zašto samo Šarić?

U bazu ulaze samo prijevodi koje je odobrila Katolička Crkva. Ostali katolički prijevodi nisu
slobodno dostupni:

| Prijevod | Stanje |
|---|---|
| **Zagrebačka Biblija** (Kršćanska sadašnjost; online kao [biblija.ks.hr](https://biblija.ks.hr), izdanje 2015.) | zaštićena autorskim pravom; [uvjeti korištenja](https://biblija.ks.hr/uvjeti-koristenja/) izričito zabranjuju preuzimanje i uključivanje u baze podataka bez pisanog odobrenja KS-a |
| **Jeruzalemska Biblija** (KS, 1994.) | zaštićena |
| **Novi prijevod 2025.** (HBD, Verbum, Naša ognjišta) | zaštićen; status crkvenog odobrenja je osporavan (vidi [docs/PLAN.md](docs/PLAN.md)) |

Ako nositelji prava odobre uporabu, prijevod se dodaje u isti oblik, kao `data/<prijevod>/`.

## Prava i licenca

- **Kod** (`scripts/`) i struktura podataka (`data/books.json`, sheme) objavljeni su pod
  [MIT licencom](LICENSE).
- **Biblijski tekst** nije obuhvaćen tom licencom. eBible.org i CrossWire Šarićev prijevod
  označavaju kao *Public Domain*. Šarić je umro 1960., pa po hrvatskom i EU pravu (život + 70)
  izvorni tekst nedvojbeno prelazi u javno dobro 1. 1. 2031. Nije utvrđeno koje je izdanje
  digitalizirano.
- Ako si nositelj prava na neko izdanje i smatraš da je objava sporna, otvori
  [issue](https://github.com/domovinatv/biblija/issues).

## Doprinos

Greške u tekstu prijavi kroz [issue](https://github.com/domovinatv/biblija/issues). Navedi
referencu (npr. „Jr 36,5”) i izvor ispravka, idealno tiskano izdanje sa stranicom. Ispravke se
ne unose ručno u `data/saric/*.json`, nego u build kao errata, kako bi ostale vidljive i ponovljive.
