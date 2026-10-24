#!/usr/bin/env python3
"""eBible USFM (Šarić) -> data/saric/NN-ID.json, jedna datoteka po knjizi.

Pokretanje: python3 -I scripts/build_saric.py
Prije toga: scripts/fetch_saric.sh
"""
import datetime
import glob
import hashlib
import json
import os
import re
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, ".cache", "saric")
OUT = os.path.join(ROOT, "data", "saric")

# eBible koristi ESG (Estera s grčkim dodacima); u katalogu je to jedna knjiga EST.
SOURCE_IDS = {"ESG": "EST"}

# Redoslijed slova za dodatke Esteri (latinska tradicija, bez j i v).
PART_LETTERS = "abcdefghiklmnopqrstuwxyz"

errata = []


def clean(text):
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"\s+", " ", text).strip()
    # Izvor mjestimice ima razmak ispred interpunkcije („ove : devu”).
    return re.sub(r" ([,.:;!?])", r"\1", text)


def parse_usfm(path):
    raw = open(path, encoding="utf-8").read()
    # \vp X\vp* je objavljeni broj (dodatak, npr. „a”, „1a”) unutar stiha.
    raw = re.sub(r"\\vp ([^\\]*?)\\vp\*", lambda m: f"\x00VP {m.group(1).strip()}\x00", raw)

    meta, intro, chapters = {}, [], []
    chapter = None
    verse = None
    pending_p = False

    def add_text(s):
        nonlocal verse
        if verse is None:
            return
        verse["text"] += " " + s

    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(r"\\(id|h|toc1|toc2|toc3|mt1)\s+(.*)", line)
        if m:
            meta[m.group(1)] = clean(m.group(2))
            continue
        if line.startswith("\\ip "):
            intro.append(clean(line[4:]))
            continue
        m = re.match(r"\\c\s+(\d+)", line)
        if m:
            chapter = {"chapter": int(m.group(1)), "verses": []}
            chapters.append(chapter)
            verse = None
            continue
        if line == "\\p":
            pending_p = True
            continue
        m = re.match(r"\\v\s+(\d+)\s*(.*)", line)
        if not m:
            raise ValueError(f"{path}: nepoznat redak: {line[:80]}")
        num, rest = int(m.group(1)), m.group(2)
        verse = {"v": num, "text": ""}
        if pending_p:
            verse["p"] = True
            pending_p = False
        chapter["verses"].append(verse)
        # Razdvoji dodatke označene s \vp u zasebne dijelove istog stiha.
        parts_seen = []
        for seg in rest.split("\x00"):
            if seg.startswith("VP "):
                label = seg[3:].replace(" ", "")
                part = label[len(str(num)):] if label.startswith(str(num)) else label
                if part and part in parts_seen:
                    # Izvor ponavlja slovo (npr. Est 1,1 „a” iza „q”): uzmi sljedeće slovo niza.
                    fixed = PART_LETTERS[PART_LETTERS.index(parts_seen[-1]) + 1]
                    errata.append({"book": meta.get("id"), "chapter": chapter["chapter"], "v": num,
                                   "source_part": part, "part": fixed,
                                   "reason": "ponovljena oznaka dodatka u izvoru"})
                    part = fixed
                if part:
                    parts_seen.append(part)
                if not verse["text"].strip():
                    if part:
                        verse["part"] = part
                else:
                    verse = {"v": num, "text": ""}
                    if part:
                        verse["part"] = part
                    chapter["verses"].append(verse)
            else:
                add_text(seg)

    for ch in chapters:
        for v in ch["verses"]:
            v["text"] = clean(v["text"])
            # „part” ide odmah iza „v” radi čitljivosti.
            if "part" in v:
                v_ordered = {"v": v["v"], "part": v["part"], "text": v["text"]}
                if v.get("p"):
                    v_ordered["p"] = True
                v.clear()
                v.update(v_ordered)
    return meta, intro, chapters


def main():
    catalog = json.load(open(os.path.join(ROOT, "data", "books.json"), encoding="utf-8"))
    by_id = {b["id"]: b for b in catalog["books"]}
    os.makedirs(OUT, exist_ok=True)

    stats = {"books": 0, "chapters": 0, "verses": 0}
    for path in sorted(glob.glob(os.path.join(SRC, "usfm", "*.usfm"))):
        meta, intro, chapters = parse_usfm(path)
        bid = SOURCE_IDS.get(meta["id"], meta["id"])
        book = by_id[bid]
        doc = {
            "translation": "saric",
            "book": bid,
            "order": book["order"],
            "testament": book["testament"],
            "deuterocanonical": book["deuterocanonical"],
            "name": meta.get("toc1") or book["name"],
            "abbr": book["abbr"],
        }
        if intro:
            doc["intro"] = intro
        doc["chapters"] = chapters
        name = f"{book['order']:02d}-{bid}.json"
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write("\n")
        stats["books"] += 1
        stats["chapters"] += len(chapters)
        stats["verses"] += sum(len(c["verses"]) for c in chapters)

    zip_path = os.path.join(SRC, "hrv_usfm.zip")
    translations_path = os.path.join(ROOT, "data", "translations.json")
    translations = {}
    if os.path.exists(translations_path):
        translations = json.load(open(translations_path, encoding="utf-8"))
    translations["saric"] = {
        "name": "Sveta Biblija, prijevod Ivana Ev. Šarića",
        "first_published": "1941–1942, Sarajevo",
        "confession": "katolički",
        "canon": 73,
        "source": "https://ebible.org/Scriptures/hrv_usfm.zip",
        "source_details": "https://ebible.org/find/details.php?id=hrv",
        "source_sha256": hashlib.sha256(open(zip_path, "rb").read()).hexdigest(),
        "built": datetime.date.today().isoformat(),
        "rights": "eBible i CrossWire ga označavaju kao Public Domain; Šarić je umro 1960., "
                  "pa po hrvatskom i EU pravu (život + 70) tekst postaje javno dobro 1. 1. 2031. "
                  "Koje je izdanje digitalizirano nije utvrđeno.",
        "notes": [
            "Estera: izvor ESG, grčki dodaci su dijelovi stiha s poljem 'part'.",
            "Sirah: proslov je u polju 'intro'.",
            "'p': true označava početak odlomka.",
        ],
        "stats": stats,
    }
    with open(translations_path, "w", encoding="utf-8") as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(os.path.join(ROOT, "data", "saric-errata.json"), "w", encoding="utf-8") as f:
        json.dump(errata, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(stats, f"errata: {len(errata)}")


if __name__ == "__main__":
    main()
