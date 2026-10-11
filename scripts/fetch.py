#!/usr/bin/env python3
"""Fetch in-force titles from the Federal Register of Legislation (FRL) API.

Steps (each cached under RAW, so re-runs only fetch what is missing):
  1. list   : titles with isInForce=true for each collection -> RAW/lists/<Collection>.json
  2. meta   : latest version + its documents for each title    -> RAW/meta/<id>.json
  3. docs   : the EPUB rendition(s) of the latest version       -> RAW/epub/<id>/<registerId>-<vol>.epub
              (falls back to the Word .docx when no EPUB exists)

Usage: fetch.py [--refresh-lists] [--workers 4] Collection [Collection ...]
Collections: Constitution Act LegislativeInstrument ContinuedLaw PrerogativeInstrument
             AdministrativeArrangementsOrder
"""
import argparse
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from common import API, RAW, get, read_json, write_json

SELECT = ("id,name,makingDate,collection,subCollection,isPrincipal,isInForce,status,"
          "year,number,seriesType,optionalSeriesNumber,asMadeRegisteredAt,originatingBillUri")


def list_titles(collection, refresh=False):
    path = os.path.join(RAW, "lists", f"{collection}.json")
    if os.path.exists(path) and not refresh:
        return read_json(path)
    out, skip = [], 0
    while True:
        r = get(f"{API}/titles", params={
            "$filter": f"collection eq '{collection}' and isInForce eq true",
            "$select": SELECT, "$orderby": "id", "$top": "500", "$skip": str(skip),
            "$count": "true"})
        d = r.json()
        out.extend(d["value"])
        skip += 500
        print(f"  list {collection}: {len(out)}/{d['@odata.count']}", file=sys.stderr)
        if skip >= d["@odata.count"] or not d["value"]:
            break
    # de-duplicate (paging over a live dataset)
    seen, uniq = set(), []
    for t in out:
        if t["id"] not in seen:
            seen.add(t["id"])
            uniq.append(t)
    write_json(path, uniq)
    return uniq


def meta_path(tid):
    return os.path.join(RAW, "meta", f"{tid}.json")


def fetch_meta(tid):
    path = meta_path(tid)
    if os.path.exists(path):
        return read_json(path)
    r = get(f"{API}/versions/find(titleId='{tid}',asAtSpecification='Latest')",
            params={"$expand": "documents"})
    if r is None:
        return None
    d = r.json()
    write_json(path, d)
    return d


def pick_docs(meta):
    """Return the Primary documents to download: EPUB(s) if any, else Word, else PDF."""
    docs = [d for d in meta.get("documents") or [] if d["type"] == "Primary"]
    for fmt in ("Epub", "Word", "Pdf"):
        sel = sorted((d for d in docs if d["format"] == fmt and (fmt != "Word" or d.get("extension") == ".docx")),
                     key=lambda d: d["volumeNumber"])
        if sel:
            return sel
    return []


def doc_path(tid, d):
    return os.path.join(RAW, "epub", tid, f"{d['registerId']}-{d['volumeNumber']}{d['extension']}")


def fetch_docs(tid, meta):
    paths = []
    for d in pick_docs(meta):
        path = doc_path(tid, d)
        if not os.path.exists(path):
            # (the registerid parameter of documents/find does not select the document: use Latest)
            url = (f"{API}/documents/find(titleid='{tid}',asatspecification='Latest',"
                   f"type='Primary',format='{d['format']}',uniquetypenumber={d['uniqueTypeNumber']},"
                   f"volumenumber={d['volumeNumber']},"
                   f"rectificationversionnumber={d['rectificationVersionNumber']})")
            r = get(url)
            if r is None:
                if not d.get("synthetic"):
                    print(f"  ! 404 {tid} {d['format']} vol {d['volumeNumber']}", file=sys.stderr)
                continue
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path + ".tmp", "wb") as f:
                f.write(r.content)
            os.replace(path + ".tmp", path)
        paths.append(path)
    return paths


def bulk_versions(prefix, refresh=False):
    """Latest version of every title whose id starts with `prefix` (one request per 500 titles)."""
    path = os.path.join(RAW, "lists", f"versions-{prefix}.json")
    if os.path.exists(path) and not refresh:
        return read_json(path)
    out, skip = {}, 0
    while True:
        r = get(f"{API}/versions", params={
            "$filter": f"isLatest eq true and startswith(titleId,'{prefix}')",
            "$orderby": "titleId", "$top": "500", "$skip": str(skip), "$count": "true"})
        d = r.json()
        for v in d["value"]:
            out[v["titleId"]] = v
        skip += 500
        print(f"  versions {prefix}: {skip}/{d['@odata.count']}", file=sys.stderr)
        if skip >= d["@odata.count"] or not d["value"]:
            break
    write_json(path, out)
    return out


BULK = {}


def synthetic_meta(tid):
    """Meta from the bulk version list, assuming a single-volume EPUB (always the case so far)."""
    v = BULK.get(tid)
    if not v:
        return None
    m = dict(v)
    m["documents"] = [{"titleId": tid, "registerId": v["registerId"], "type": "Primary", "format": "Epub",
                       "volumeNumber": 0, "uniqueTypeNumber": 0, "rectificationVersionNumber": 0,
                       "extension": ".epub", "synthetic": True}]
    return m


def work(t):
    tid = t["id"]
    if not os.path.exists(meta_path(tid)) and tid in BULK:
        m = synthetic_meta(tid)
        if fetch_docs(tid, m):
            write_json(meta_path(tid), m)
            return tid, "ok"
    meta = fetch_meta(tid)
    if meta is None:
        return tid, "no-version"
    paths = fetch_docs(tid, meta)
    return tid, "ok" if paths else "no-docs"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("collections", nargs="+")
    ap.add_argument("--refresh-lists", action="store_true")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--bulk", default="", help="id prefix: use bulk version list instead of per-title meta")
    a = ap.parse_args()
    if a.bulk:
        BULK.update(bulk_versions(a.bulk, a.refresh_lists))
    for coll in a.collections:
        titles = list_titles(coll, a.refresh_lists)
        if a.limit:
            titles = titles[:a.limit]
        print(f"{coll}: {len(titles)} titles", file=sys.stderr)
        bad = []
        with ThreadPoolExecutor(min(a.workers, 4)) as ex:
            futs = [ex.submit(work, t) for t in titles]
            for i, f in enumerate(as_completed(futs), 1):
                try:
                    tid, st = f.result()
                except Exception as e:  # keep going; re-run to retry
                    print(f"  ! {e}", file=sys.stderr)
                    bad.append(str(e))
                    continue
                if st != "ok":
                    bad.append(f"{tid} {st}")
                if i % 200 == 0:
                    print(f"  {coll}: {i}/{len(titles)}", file=sys.stderr)
        print(f"{coll}: done, {len(bad)} problems", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)


if __name__ == "__main__":
    main()
