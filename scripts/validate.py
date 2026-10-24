#!/usr/bin/env python3
"""Provjera data/saric/*.json: struktura, praznine, i usporedba sa scrollmapper CroSaric.json.

Pokretanje: python3 -I scripts/validate.py
"""
import glob
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"[“”„\"’']", "", s)
    return re.sub(r"\s+", " ", s).strip()


ROMAN = {"I ": "1 ", "II ": "2 ", "III ": "3 "}


ALIASES = {"Revelation of John": "Revelation", "Song of Solomon": "Song of Songs"}


def ref_book_name(name):
    name = ALIASES.get(name, name)
    for roman, arabic in ROMAN.items():
        if name.startswith(roman):
            return arabic + name[len(roman):]
    return name


def main():
    catalog = json.load(open(os.path.join(ROOT, "data", "books.json"), encoding="utf-8"))["books"]
    files = sorted(glob.glob(os.path.join(ROOT, "data", "saric", "*.json")))
    errors = []
    reordered = []
    if len(files) != len(catalog):
        errors.append(f"očekivano {len(catalog)} knjiga, ima {len(files)}")

    ours = {}
    for path, book in zip(files, catalog):
        d = json.load(open(path, encoding="utf-8"))
        if d["book"] != book["id"]:
            errors.append(f"{os.path.basename(path)}: book {d['book']} != {book['id']}")
        prev_ch = 0
        for ch in d["chapters"]:
            if ch["chapter"] != prev_ch + 1:
                errors.append(f"{d['book']} {ch['chapter']}: poglavlje nije uzastopno")
            prev_ch = ch["chapter"]
            seen = set()
            for v in ch["verses"]:
                key = (v["v"], v.get("part", ""))
                if key in seen:
                    errors.append(f"{d['book']} {ch['chapter']},{v['v']}{v.get('part','')}: duplikat")
                seen.add(key)
                if not v["text"]:
                    errors.append(f"{d['book']} {ch['chapter']},{v['v']}: prazan stih")
                ours.setdefault((book["name_en"], ch["chapter"], v["v"]), []).append(v["text"])
            numbers = [v["v"] for v in ch["verses"]]
            missing = sorted(set(range(1, max(numbers) + 1)) - set(numbers))
            if missing:
                errors.append(f"{d['book']} {ch['chapter']}: nedostaju stihovi {missing}")
            main = [n for n, v in zip(numbers, ch["verses"]) if "part" not in v]
            if main != sorted(main):
                # Premještanja kao u Jeruzalemskoj Bibliji (npr. Jr 29,8–9 iza 15); nije greška.
                reordered.append(f"{d['book']} {ch['chapter']}")

    print(f"struktura: {len(errors)} problema")
    for e in errors[:50]:
        print("  ", e)
    print(f"premješteni stihovi (info): {', '.join(reordered) or 'nema'}")

    ref_path = os.path.join(ROOT, ".cache", "saric", "CroSaric.json")
    if not os.path.exists(ref_path):
        print("nema .cache/saric/CroSaric.json, preskačem usporedbu")
        return 1 if errors else 0
    ref = {}
    for b in json.load(open(ref_path, encoding="utf-8"))["books"]:
        for c in b["chapters"]:
            for v in c["verses"]:
                ref[(ref_book_name(b["name"]), c["chapter"], v["verse"])] = v["text"]

    only_ours = sorted(set(ours) - set(ref))
    only_ref = sorted(set(ref) - set(ours))
    differ = [k for k in set(ours) & set(ref) if norm(" ".join(ours[k])) != norm(ref[k])]
    print(f"usporedba sa scrollmapper: samo kod nas {len(only_ours)}, samo u scrollmapper {len(only_ref)}, "
          f"različit tekst {len(differ)}")
    report = {
        "only_ebible": [list(k) for k in only_ours],
        "only_scrollmapper": [list(k) for k in only_ref],
        "different_text": [
            {"ref": list(k), "ebible": " ".join(ours[k]), "scrollmapper": ref[k]} for k in sorted(differ)
        ],
    }
    out = os.path.join(ROOT, "data", "saric", "..", "saric-compare.json")
    with open(os.path.normpath(out), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print("izvještaj: data/saric-compare.json")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
