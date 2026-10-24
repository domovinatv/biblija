# Hrvatska Biblija u lokalnoj offline bazi: nalazi i plan

Stanje istraživanja: 2026-10-24.

## Zaključak

1. **biblija.ks.hr se ne smije preuzimati.** Uvjeti korištenja (ažurirani 14. 8. 2026.,
   <https://biblija.ks.hr/uvjeti-koristenja/>) izričito zabranjuju sustavno ili automatsko
   preuzimanje, scraping i crawling te uključivanje teksta u baze podataka i skupove podataka
   bez pisanog odobrenja Kršćanske sadašnjosti. Tekst je *Sveto pismo Staroga i Novoga zavjeta*,
   KS, Zagreb, 2015. (Zagrebačka Biblija). KS je nositelj isključivih prava. Stranica nema API ni
   izvoz; to je WordPress + Elementor. Jedini put je pismeni zahtjev na `urednistvo@ks.hr`.
2. **Jedini otvoreno dostupan potpuni katolički tekst je Šarić** (1941./42.), 73 knjige s
   deuterokanonskima, već strukturiran (JSON, USFM, OSIS, SWORD). Na tome gradimo prvu verziju.
3. **Tvrdnju da biblija.ks.hr ima puno grešaka nismo potvrdili.** Javnih prijava nismo našli,
   a sustavna usporedba bi zahtijevala upravo ono što uvjeti zabranjuju. Uvjeti (t. 8) priznaju
   moguće greške digitalne obrade i traže da se prijave KS-u.
4. **Nisu „4 službena prijevoda”.** Katolički cjeloviti prijevodi u uporabi su Zagrebačka
   Biblija (KS), Jeruzalemska Biblija (KS, isti prijevod s bilješkama), Šarić u više revizija
   te **novi katolički prijevod** iz prosinca 2025. (HBD, Verbum, Naša ognjišta; urednici
   Lujić i Zovkić). Uz njih postoje protestantski i Jehovini svjedoci (Novi svijet) te
   povijesni prijevodi (Kašić, Katančić).

## Fokus: samo prijevodi s odobrenjem Katoličke Crkve

U bazu ulaze samo prijevodi s crkvenim odobrenjem (kan. 825 ZKP: odobrenje Apostolske
Stolice ili biskupske konferencije). Protestantski (Biblica, Biblijska liga), adventistički i
Jehovinih svjedoka su isključeni.

- **biblija-govori.hr nije katolička.** Ne navodi izdavača ni prijevode, a „O nama” spominje
  „različite kršćanske denominacije”. Njezina „Dopisna škola” vodi na biblijskeistine.hr, čiji
  podnožje navodi *Kršćanska adventistička crkva u Republici Hrvatskoj*, Prilaz Gjure Deželića 77,
  Zagreb. Ne koristimo je.
- **Novi prijevod 2025. („Hrvatski standardni prijevod”, HBD, Verbum, Naša ognjišta) je sporan.**
  Izdavači tvrde da ima odobrenje HBK i BK BiH; predgovore su napisali predsjednici obiju
  konferencija. Kritičari (P. M. Radelj, vjeraidjela.com; Novi list 28. 5. 2026.) navode da je
  priopćenje HBK od 6. 6. 2024. dalo samo **suglasnost** da HBD izda *ekumenski studijski
  prijevod* kao vlastito izdanje, a ne formalno odobrenje. Na prijevodu su radili i adventisti.
  Status je *neutvrđen* dok se ne nađe sam tekst odobrenja HBK.

## Prijevodi

| Prijevod | Godina | Kanon | Prava | Strukturirano dostupno |
|---|---|---|---|---|
| Zagrebačka Biblija (Duda, Kaštelan; NZ Duda–Fućak) | 1968., izd. 2015. | 73 | KS, zaštićeno (Duda †2017.) | ne; samo biblija.ks.hr (zabrana) |
| Jeruzalemska Biblija | 1994. | 73 | KS | ne |
| Šarić (izvorni tekst) | 1941./42. | 73 | vidi napomenu niže | **da**: eBible, CrossWire, scrollmapper, getBible |
| Šarić, revizije (Martinjak; HBD 2006.) | 1988./1998., 2006. | 73 | HBD i suizdavači | ne |
| Novi katolički prijevod (HBD, Verbum, Naša ognjišta) | XII. 2025. | ? | izdavači | ne |
| Knjiga o Kristu (Biblica) | 1982.–2000. | samo NZ | Biblica | da (eBible `hrvbib`, thiagobodruk) |
| Novi svijet (JW) | rev. 2020. | 66 | Watch Tower | ne (samo čitanje online) |
| Kašić / Katančić | 1638. / 1831. | 73 | tekst slobodan | nije provjereno |

Nije provjereno:
- Koji je tekst temelj važećeg HBK lekcionara. Polazište je lekcionar Duda–Fućak iz 1969.
  Treba provjeriti na hbk.hr i hilp.hr.
- Je li novi prijevod iz 2025. odobren za liturgiju.

### Napomena o pravima na Šarićev tekst

eBible i CrossWire ga označavaju kao *Public Domain*. Šarić je umro 1960., a u Hrvatskoj i EU
autorsko pravo traje 70 godina od smrti, pa izvorni tekst prelazi u javno dobro **1. 1. 2031.**
Uz to se ne zna točno koje izdanje je digitalizirano. Izvor je unbound.biola.edu i
wwwyu.com/izrada, pa bi moglo biti i revidirano izdanje sa zasebnim pravima. Posljedica:
- lokalna, osobna, offline uporaba je u redu;
- **javna objava repoa ili aplikacije s tim tekstom prije 2031. nosi rizik.** Vlasnik je
  2026-10-24 odlučio repo ipak objaviti javno. README to navodi i nudi issue nositelju prava.

## Provjereni izvori (Šarić)

| Izvor | Format | Veličina | Napomena |
|---|---|---|---|
| eBible.org `hrv`: <https://ebible.org/Scriptures/hrv_usfm.zip> | USFM, 73 datoteke | 1,6 MB | ažurirano 20. 10. 2026.; ima naslove knjiga na hrvatskom (`\toc1`), odlomke (`\p`) |
| scrollmapper `CroSaric.json`: <https://raw.githubusercontent.com/scrollmapper/bible_databases/master/sources/hr/CroSaric/CroSaric.json> | JSON `books[].chapters[].verses[]` | 12 MB | engleski nazivi knjiga, bez odlomaka |
| CrossWire SWORD `CroSaric`: <https://crosswire.org/ftpmirror/pub/sword/packages/rawzip/CroSaric.zip> | SWORD/OSIS | 1,7 MB | v2.0 (2020.) dodala deuterokanonske knjige |
| getBible: <https://api.getbible.net/v2/croatia.json> | JSON | — | 66 knjiga, starija verzija (2003.), samo za usporedbu |

Brza provjera (2026-10-24, lokalno):
- scrollmapper ima 73 knjige i **35 502** stiha, eBible USFM 73 knjige i **35 448** stihova.
  *Razriješeno:* svih 54 su prazni stihovi u scrollmapper verzifikaciji.
- Daniel ima 14 poglavlja s dodacima (13 i 14, 3,24–90). U 3. poglavlju USFM završava na
  stihu 99; očekivano je 100.
- Estera (USFM `ESG`) ima 10 poglavlja i 167 `\v` oznaka, točno koliko i hebrejski tekst.
  *Razriješeno:* grčki dodaci **postoje**, ali su unutar stihova označeni s `\vp a\vp*`,
  `\vp 17i\vp*` itd. Build ih izdvaja u polje `part`. Izvor dvaput ponavlja slovo „a”
  (Est 1,1 iza „q”; 3,13 iza „f”), a `\vp 1\vp*` označava povratak na sam stih.
  Vidi `data/saric-errata.json`.

## Ciljna struktura u repou

```
data/
  books.json                    # katalog 73 knjige: id (USFM kod), red, hr nazivi, kratice, zavjet, deuterokanonska
  translations.json             # meta svakog prijevoda: izvor, izdanje, prava, datum preuzimanja, sha256
  saric/
    01-GEN.json … 73-REV.json   # jedna datoteka po knjizi (73 datoteke)
  <drugi-prijevod>/…            # isti oblik, npr. ks-2015 ako KS odobri
scripts/
  fetch_saric.py                # skida izvore u .cache/ (nije u gitu)
  build_saric.py                # USFM → data/saric/*.json
  validate.py                   # sheme, brojevi stihova, usporedba izvora
schema/
  book.schema.json
```

Oblik jedne knjige:

```json
{
  "translation": "saric",
  "book": "GEN",
  "order": 1,
  "name": "Knjiga Postanka",
  "short": "Post",
  "testament": "OT",
  "deuterocanonical": false,
  "chapters": [
    {
      "chapter": 1,
      "verses": [
        { "v": 1, "text": "U početku stvori Bog nebo i zemlju.", "p": true }
      ]
    }
  ]
}
```

Načela:
- **Kodovi knjiga su USFM** (`GEN`, `TOB`, `SIR`…). Tako se prijevodi i vanjski alati spajaju
  bez preslikavanja.
- **Red knjiga je katolički** (KKC 120): 46 + 27. Hrvatske nazive i kratice preuzimamo iz
  liturgijske prakse (Post, Izl, Lev, Br, Pnz… Mt, Mk, Lk, Iv).
- **`v` je string ako je potrebno.** Dodaci Esteri i Danielu, te stihovi poput „3a”, ne stanu
  uvijek u cijeli broj. Ključ verzifikacije ide u `translations.json`.
- **Tekst normaliziramo:** Unicode NFC, trim, jedan razmak, tipografski navodnici ostaju.
  Sirovi izvor se ne mijenja; sve korekcije idu u `data/saric/errata.json` s obrazloženjem.
- **Jedna knjiga po datoteci:** git diff ostaje čitljiv, a datoteke su male (0,05–1 MB).
  Iz istih JSON-a po potrebi generiramo SQLite (`biblija.sqlite`, FTS5 za pretragu).

## Plan rada

1. **Kostur:** `books.json` (73 knjige, hrvatski nazivi i kratice, deuterokanonske oznake;
   dodaci kao rasponi u Esteri i Danielu), JSON shema, `translations.json`.
2. **Šarić iz USFM-a (eBible):** parser za `\c \v \p \toc1 \toc3`, ispis 73 datoteke.
3. **Unakrsna provjera** scrollmapper JSON-a i getBible-a, stih po stih:
   - izvještaj o razlikama (onih 54 stiha, Dan 3,100, dodaci Esteri);
   - normalizacija i lista errata.
4. **Validacija u CI-ju:** shema, broj poglavlja i stihova po knjizi u odnosu na referentnu
   verzifikaciju, prazni stihovi, duplikati, čudni znakovi (` `, `–` naspram `-`).
5. **SQLite i FTS:** generirani artefakt, nije u gitu.
6. **Ostali prijevodi** (paralelno, ne-tehnički):
   - pismo KS-u (`urednistvo@ks.hr`): traži se dopuštenje za privatnu, nekomercijalnu offline
     bazu Zagrebačke Biblije 2015. Uz zahtjev ponuditi im natrag popis pronađenih grešaka; to je
     ujedno najlegitimniji način da se provjeri tvrdnja o greškama;
   - isto pitanje HBD-u i Verbumu za novi prijevod iz 2025.;
   - provjeriti tekst HBK lekcionara.
   Svaki odobreni prijevod ulazi u isti oblik `data/<prijevod>/`.

## Stanje (2026-10-24)

- Koraci 1–4 su gotovi za Šarića: `data/books.json`, `data/saric/*.json`, `scripts/validate.py`
  i CI (`.github/workflows/validate.yml`).
- Rezultat provjere: 0 strukturnih problema i potpuno podudaranje s CrossWire/scrollmapper
  tekstom. Razlike od 54 stiha bile su prazni stihovi u scrollmapper verzifikaciji. Grčki dodaci
  Esteri postoje (oznake `\vp` u USFM-u), a 7 „rupa” su premještanja stihova kao u
  Jeruzalemskoj Bibliji, ne nedostajući tekst.
- Repo je javan, uz napomenu o pravima u README-u.
- Otvoreno: SQLite i FTS (korak 5), upiti KS-u i HBD-u (korak 6), tekst HBK lekcionara.

## Dodatni nalazi (2026-10-24)

### Premještanja stihova
Validator je u 7 poglavlja javljao „preskočene” stihove: 1 Sam 9, Job 36, Iz 33, Jr 29, Jr 36,
Nah 2 i Hab 2. Ti stihovi zapravo postoje, ali stoje na drugom mjestu, kao u Jeruzalemskoj
Bibliji (npr. Jr 29,8–9 iza 15. stiha). Build čuva tiskani redoslijed, a validator ih
prijavljuje kao informaciju.

### biblija-govori.hr nije katolička
Stranica ne navodi izdavača. Njezina „Dopisna škola” vodi na biblijskeistine.hr, čiji
podnožje navodi Kršćansku adventističku crkvu u RH.

### KS aplikacije
U App Storeu postoje **HR Biblija** (6,99 $, offline, <https://apps.apple.com/us/app/id505828694>)
i **HR Biblija free** (samo iPhone, online, <https://apps.apple.com/us/app/id465471461>).
Kontakt je `ios@ks.hr`. Na Google Playu verziju nismo našli, ali nismo ni potvrdili da je nema.
Izvlačenje teksta iz aplikacije bilo bi isto kršenje prava kao scraping weba.

### Zašto ne strojni prijevod engleske Biblije
Razmatrali smo i odbacili LLM ili Google Translate prijevod katoličkog engleskog prijevoda:
- NABRE, RSV-2CE i NRSV-CE su zaštićeni, a prijevod prijevoda je prerada za koju treba
  dopuštenje. Slobodan je samo Douay-Rheims, a on je prijevod Vulgate.
- Kan. 825 traži odobrenje crkvene vlasti, a *Liturgiam authenticam* prijevod iz izvornih
  jezika. Takav tekst ne bi bio „službeni”.
- Interpretacije i greške se gomilaju kroz svaki prijevod, a teološko nazivlje ne bi
  odgovaralo lekcionaru.
Prihvatljiv je samo kao jasno označena pomoć za osobno proučavanje.

### Zašto je Zagrebačka Biblija potisnula Šarića (sažetak, nije potpuno provjereno)
- Šarić je 1945. emigrirao, pa se njegova Biblija desetljećima tiskala uglavnom u emigraciji.
- Drugi vatikanski koncil (*Dei Verbum* 22) potaknuo je nove prijevode iz izvornih jezika.
- Zagrebačka Biblija izašla je 1968., a lekcionar Duda–Fućak 1969.
Prije javne uporabe ove tvrdnje treba provjeriti na izvorima (HAZU, Hrčak).
