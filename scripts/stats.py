#!/usr/bin/env python3
"""Print file counts per top-level directory (and principal/amending split for Acts)."""
import collections
import os
import re

from common import ROOT

counts, acts = collections.Counter(), collections.Counter()
size = 0
for d, _, files in os.walk(ROOT):
    rel = os.path.relpath(d, ROOT)
    if rel.startswith((".git", "scripts")):
        continue
    for f in files:
        if not f.endswith(".md") or rel == ".":
            continue
        p = os.path.join(d, f)
        size += os.path.getsize(p)
        top = rel.split(os.sep)[0]
        if top == "instruments":
            top = "instruments/" + rel.split(os.sep)[1]
        counts[top] += 1
        if top == "acts":
            with open(p, encoding="utf-8") as fh:
                head = fh.read(800)
            m = re.search(r"^principal: (\w+)", head, re.M)
            acts["principal" if m and m.group(1) == "true" else "amending/other"] += 1
for k, v in sorted(counts.items()):
    print(f"{k}\t{v}")
print("total\t", sum(counts.values()))
print("acts split\t", dict(acts))
print(f"markdown size\t{size / 1e6:.1f} MB")
