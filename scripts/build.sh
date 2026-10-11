#!/bin/sh
# Regenerate the whole corpus. Raw downloads are cached in ../_raw/au (LAWCODEX_RAW).
set -e
cd "$(dirname "$0")"
PY=${PYTHON:-python3}
RAW=${LAWCODEX_RAW:-../../_raw/au}
# version metadata must be refreshed; EPUBs are keyed by register id so unchanged ones are reused
rm -rf "$RAW/meta"
$PY fetch.py --refresh-lists --bulk C Constitution Act ContinuedLaw PrerogativeInstrument AdministrativeArrangementsOrder
$PY fetch.py --refresh-lists --bulk F LegislativeInstrument
# remove previously generated files so repealed titles disappear
cd .. && rm -rf constitution acts instruments continued-laws prerogative-instruments administrative-arrangements-orders && cd scripts
$PY convert.py Constitution Act ContinuedLaw PrerogativeInstrument AdministrativeArrangementsOrder LegislativeInstrument
$PY stats.py
