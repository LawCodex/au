# LawCodex — Australia (`au`)

Australian **Commonwealth (federal)** legislation as plain Markdown: the Constitution, every
Commonwealth Act currently in force and every Commonwealth legislative instrument currently in force,
in their latest registered version (compilation), from the official
[Federal Register of Legislation](https://www.legislation.gov.au) (FRL).

Part of [LawCodex](https://github.com/LawCodex): the legislation of every country as Markdown in git.

Retrieved: **2026-10-11** (FRL API, `api.prod.legislation.gov.au/v1`).

## Contents

| Category | Directory | Files | Notes |
|---|---|---:|---|
| Constitution | `constitution/` | 1 | *Commonwealth of Australia Constitution Act* (Imperial Act 63 & 64 Vict. c. 12, incl. the Constitution), compilation No. 6 (amendments to 1977) |
| Acts | `acts/<year>/` | 4,773 | every Act the FRL marks as in force: 1,261 principal Acts + 3,512 amending/appropriation/other Acts still in force (`principal:` in front matter) |
| Legislative instruments | `instruments/<year>/` | 24,142 | every in-force legislative instrument (regulations, rules, determinations, airworthiness directives, …) — see below |
| Continued laws | `continued-laws/<year>/` | 213 | Norfolk Island laws continued in force as Commonwealth law |
| Prerogative instruments | `prerogative-instruments/<year>/` | 157 | Letters Patent, Royal Instructions, honours and awards regulations, … |
| Administrative Arrangements Order | `administrative-arrangements-orders/<year>/` | 1 | the current AAO |
| **Total** | | **29,287** | ~640 MB of Markdown |

Legislative instruments by FRL sub-collection (`subtype:` in front matter): Regulations 937, Rules 312,
By-laws 29, Court rules 16, and 22,848 without a sub-collection (determinations, orders, standards,
notices, instruments made by agencies, ~8,600 Civil Aviation Safety Authority airworthiness directives,
etc.).

## What is NOT covered

- **Repealed / ceased / never-commenced titles**: only titles with `isInForce = true` at retrieval time.
- **Historical versions**: only the latest registered version of each title. Note the FRL "latest"
  version can occasionally be a compilation whose start date is in the near future; the version start
  date is recorded as `version_start` in the front matter.
- **Notifiable instruments** (~3,500 in force; notices, appointments, etc. — not legislative in
  character), **Gazettes**, explanatory statements, bills and as-made versions of compiled titles.
- **State and territory legislation** (NSW, Vic, Qld, WA, SA, Tas, ACT, NT): each jurisdiction runs
  its own register (legislation.nsw.gov.au, legislation.vic.gov.au, legislation.qld.gov.au, …) and
  none offers a cheap official bulk download, so they are not included. (A non-official aggregate
  exists — the *Open Australian Legal Corpus* — but it is not an official source and was not used.)
- Images (formulas, diagrams, the coat of arms) are not reproduced; other images are marked
  `[image]` / `[image: alt text]`.

## Structure

```
constitution/commonwealth-of-australia-constitution-act.md
acts/<year>/<FRL id>-<slug>.md                         acts/2001/C2004A00818-corporations-act-2001.md
instruments/<year>/<FRL id>-<slug>.md                  instruments/2024/F2024L00349-fringe-benefits-tax-....md
instruments/<year>/<id block>xxx/<FRL id>-<slug>.md    (years with > 900 instruments, e.g. 2004/F2006B07xxx/)
continued-laws/<year>/…   prerogative-instruments/<year>/…   administrative-arrangements-orders/<year>/…
```

- `<FRL id>` is the official, permanent FRL title identifier (e.g. `C2004A00818` — the Corporations
  Act 2001; `F…` for instruments), kept in upper case as in the official URLs
  (`https://www.legislation.gov.au/C2004A00818/latest/text`).
- `<year>` is the year of the Act (from its number, e.g. *Act No. 50, 2001*) or, for other titles, the
  year it was made. Most pre-2005 instruments were back-captured into the register in 2004–2006 and are
  filed under their making date; the 2004–2009 directories are split into blocks of FRL ids so that no
  directory holds more than 1,000 files.
- Front matter: `title`, `identifier` (FRL title id), `register_id` (id of the registered version /
  compilation that was converted), `type` (`constitution`, `act`, `legislative_instrument`,
  `continued_law`, `prerogative_instrument`, `administrative_arrangements_order`), `subtype`
  (instruments), `principal` (Acts), `number` (e.g. `Act No. 62, 1958`, `Statutory Rules No. …`,
  `Select Legislative Instrument No. …`), `jurisdiction: au`, `language: en`, `date` (making / assent
  date), `compilation_number` and `last_amended` (compilation date) for compiled titles,
  `version_start`, `status`, `source`, `retrieved`.
- Text: the whole registered document, including the compilation cover page and the endnotes (legislation
  and amendment history); the table of contents is dropped. Headings follow the Office of
  Parliamentary Counsel styles: Chapter / Schedule `##`, Part `###`, Division `####`, Subdivision
  `#####`, section / regulation / rule `######`; endnote headings `##`–`####`. Subsections, paragraphs,
  definitions and notes are plain paragraphs (their numbering is part of the text). Italic and bold are
  kept (defined terms appear as `***term***`). Simple tables become Markdown tables, tables with merged
  cells are kept as minimal HTML.
- About 450 Acts (mostly amending Acts of 1975–2000 that were back-captured from print) have no
  structural styles in the source, so their sections are plain paragraphs without headings.
  39 titles without an EPUB rendition were converted from the Word file (fewer headings) and 5 from the
  PDF (text extraction).

## Source and licence

- Source: Federal Register of Legislation, Office of Parliamentary Counsel, Australian Government —
  <https://www.legislation.gov.au>, via its public OData API <https://api.prod.legislation.gov.au/v1/>
  (`titles`, `versions/find(…asAtSpecification='Latest')`, `documents/find(…format='Epub')`). The EPUB
  rendition of each registered version (an XHTML export of the authorised Word document) is converted.
- Licence: FRL content is published under the
  [Creative Commons Attribution 4.0 International licence (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
  — "© Commonwealth of Australia (Office of Parliamentary Counsel)"; see
  <https://www.legislation.gov.au/copyright>. This repository is a derivative (format conversion only)
  and is not an authorised version: for legal purposes consult the FRL.

## Regenerating

```sh
pip install -r scripts/requirements.txt
sh scripts/build.sh            # or step by step:
python3 scripts/fetch.py --bulk C Constitution Act ContinuedLaw PrerogativeInstrument AdministrativeArrangementsOrder
python3 scripts/fetch.py --bulk F LegislativeInstrument
python3 scripts/convert.py --retrieved YYYY-MM-DD Constitution Act ContinuedLaw PrerogativeInstrument AdministrativeArrangementsOrder LegislativeInstrument
python3 scripts/stats.py
```

- `scripts/fetch.py` — lists in-force titles per collection, gets the latest version metadata (per
  title, or in bulk with `--bulk <id prefix>`: one `versions` query per 500 titles) and downloads the
  EPUB (fallback: .docx, then PDF). Raw files are cached in `../_raw/au/` (`LAWCODEX_RAW`), ~1.6 GB
  for the full corpus; delete it afterwards. Polite client: `LawCodex/1.0` User-Agent, ≤ 4 workers,
  ≥ 0.3 s between requests, retries with backoff.
- `scripts/convert.py` — EPUB/DOCX/PDF → Markdown with YAML front matter.
- `scripts/stats.py` — counts per directory.

API notes: `$top` is capped at 500; filtering titles on `isPrincipal` fails server-side (filter
client-side instead); the `registerid` parameter of `documents/find` does not select a document (use
`asatspecification='Latest'`); the API occasionally drops connections or returns 503 for a few minutes.
