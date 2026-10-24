#!/usr/bin/env bash
# Skida izvore Šarićeva prijevoda u .cache/ (nije u gitu).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .cache/saric
cd .cache/saric

curl -sSfL -o hrv_usfm.zip https://ebible.org/Scriptures/hrv_usfm.zip
rm -rf usfm && mkdir usfm && unzip -q hrv_usfm.zip -d usfm

# Drugi izvor, samo za unakrsnu provjeru.
curl -sSfL -o CroSaric.json \
  https://raw.githubusercontent.com/scrollmapper/bible_databases/master/sources/hr/CroSaric/CroSaric.json

shasum -a 256 hrv_usfm.zip CroSaric.json
