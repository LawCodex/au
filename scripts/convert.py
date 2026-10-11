#!/usr/bin/env python3
"""Convert the cached FRL EPUB renditions into Markdown files with YAML front matter.

Usage: convert.py [--retrieved YYYY-MM-DD] Collection [Collection ...]
Reads RAW/lists/<Collection>.json, RAW/meta/<id>.json, RAW/epub/<id>/*.epub|*.docx
Writes ROOT/<dir>/<year>/<ID>-<slug>.md (constitution: ROOT/constitution/<slug>.md)
"""
import argparse
import datetime
import html
import os
import re
import sys
import unicodedata
import zipfile

import yaml
from lxml import etree

from common import COLLECTIONS, RAW, ROOT, SITE, read_json
from fetch import doc_path, pick_docs

XHTML = "{http://www.w3.org/1999/xhtml}"

# Paragraph class -> heading level (H1 is the title of the instrument).
HEADINGS = {
    # current OPC drafting templates (Acts and instruments)
    "ActHead1": 2,   # Chapter
    "ActHead2": 3,   # Part
    "ActHead3": 4,   # Division
    "ActHead4": 5,   # Subdivision
    "ActHead5": 6,   # section / regulation / rule
    "ActHead6": 2,   # Schedule
    "ActHead7": 3,   # Part of a Schedule
    "ActHead8": 4,   # Division of a Schedule
    "ActHead9": 5,   # Act/instrument amended by a Schedule
    "ENotesHeading1": 2,
    "ENotesHeading2": 3,
    "ENotesHeading3": 4,
    # older templates
    "HC": 2, "HP": 3, "HD": 4, "HS": 5, "HR": 6,
    "Scheduletitle": 2, "ScheduleTitle": 2, "ScheduleHeading": 2,
    "EndNotes": 2, "ENotesHeading": 2,
}
SKIP_CLASSES = re.compile(r"^(TOC\d*|Header|Footer|ContentsHead|ContentsSectionBreak|NotesSectionBreak|"
                          r"SchedSectionBreak|ContentsPage)$")
BLOCK = {"p", "table", "h1", "h2", "h3", "h4", "h5", "h6", "li", "img", "hr"}
SPACES = re.compile(r"[ \t\r\n     ​]+")


def slugify(s, maxlen=80):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rsplit("-", 1)[0]
    return s or "untitled"


def local(el):
    t = el.tag
    if not isinstance(t, str):
        return ""
    return t.split("}", 1)[-1].lower()


def style_of(el):
    return el.get("style") or ""


def is_tab_span(el):
    st = style_of(el)
    return "inline-block" in st and "width" in st


def inline(el, fmt=True):
    """Return Markdown inline text of an element (recursively)."""
    segs = []  # (text, italic, bold) ; text "\x00BR\x00" = line break

    def add(t, it, bd):
        if t:
            segs.append((t, it, bd))

    def walk(e, it=False, bd=False):
        name = local(e)
        if name in ("script", "style"):
            pass
        elif name == "br":
            add("\x00BR\x00", False, False)
        elif name == "img":
            alt = (e.get("alt") or "").strip()
            add(f"[image{': ' + alt if alt else ''}]", False, False)
        else:
            st = style_of(e).replace(" ", "")
            nit = it or name in ("i", "em") or "font-style:italic" in st
            nbd = bd or name in ("b", "strong") or "font-weight:bold" in st
            if name == "span" and is_tab_span(e):
                add(" ", nit, nbd)
            else:
                add(e.text, nit, nbd)
                for c in e:
                    if not isinstance(c.tag, str):
                        add(c.tail, nit, nbd)
                    else:
                        walk(c, nit, nbd)
        if e is not el:
            add(e.tail, it, bd)

    walk(el)
    # merge runs with identical formatting; whitespace-only runs join neighbours
    runs = []
    for t, it, bd in segs:
        if not fmt:
            it = bd = False
        if t == "\x00BR\x00":
            runs.append([t, False, False])
            continue
        if runs and runs[-1][0] != "\x00BR\x00" and (
                (runs[-1][1], runs[-1][2]) == (it, bd) or not SPACES.sub("", t)):
            runs[-1][0] += t
        else:
            runs.append([t, it, bd])
    out = []
    for t, it, bd in runs:
        t = SPACES.sub(" ", t)
        if t == "\x00BR\x00":
            out.append(t)
            continue
        e = esc(t)
        core = e.strip()
        if core and (it or bd):
            lead = " " if e[:1] == " " else ""
            trail = " " if e[-1:] == " " else ""
            if bd:
                core = f"**{core}**"
            if it:
                core = f"*{core}*"
            e = lead + core + trail
        out.append(e)
    s = SPACES.sub(" ", "".join(out))
    s = re.sub(r" ?\x00BR\x00 ?", "\x00BR\x00", s)
    s = re.sub(r"^(\x00BR\x00)+|(\x00BR\x00)+$", "", s.strip()).strip()
    return s


def esc(t):
    t = t.replace("\\", "\\\\").replace("*", "\\*").replace("`", "\\`")
    t = t.replace("<", "&lt;").replace(">", "&gt;") if ("<" in t or ">" in t) else t
    return t


LEADING = re.compile(r"^(#{1,6}\s|[-+]\s|>|\d+[.)](\s|$)|={3,}|-{3,}|_{3,})")


def para(text):
    if LEADING.match(text):
        if text[0].isdigit():
            m = re.match(r"^(\d+)([.)])", text)
            text = m.group(1) + "\\" + m.group(2) + text[m.end():]
        else:
            text = "\\" + text
    return text.replace("\x00BR\x00", "\\\n")


def plain(text):
    """Strip Markdown emphasis for headings."""
    t = text.replace("\x00BR\x00", " ")
    t = re.sub(r"(?<!\\)\*+", "", t)
    return SPACES.sub(" ", t).strip()


def cell_text(td):
    parts = []
    blocks = [c for c in td.iter() if local(c) in ("p", "li", "h1", "h2", "h3", "h4", "h5", "h6")]
    if blocks:
        for b in blocks:
            if any(local(a) in ("p", "li") for a in b.iterancestors() if a is not td and td in a.iterancestors()):
                continue
            t = inline(b)
            if t:
                parts.append(t)
    else:
        t = inline(td)
        if t:
            parts.append(t)
    return "<br>".join(p.replace("\x00BR\x00", "<br>") for p in parts)


def render_table(tbl):
    rows = []
    complex_ = False
    for tr in tbl.iter(XHTML + "tr", "tr"):
        # skip rows of nested tables (handled as complex)
        if next((a for a in tr.iterancestors() if local(a) == "table"), None) is not tbl:
            complex_ = True
            continue
        cells = []
        for td in tr:
            if local(td) not in ("td", "th"):
                continue
            cs, rs = int(td.get("colspan", "1") or 1), int(td.get("rowspan", "1") or 1)
            if cs > 1 or rs > 1:
                complex_ = True
            cells.append((cell_text(td), cs, rs, local(td) == "th"))
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    ncols = max(sum(c[1] for c in r) for r in rows)
    if ncols == 1 and not complex_:
        # single-column box: render as paragraphs
        return "\n\n".join(para(r[0][0].replace("<br>", "\x00BR\x00")) for r in rows if r[0][0])
    if not complex_:
        width = max(len(r) for r in rows)
        lines = []
        for i, r in enumerate(rows):
            vals = [c[0].replace("|", "\\|") for c in r] + [""] * (width - len(r))
            lines.append("| " + " | ".join(vals) + " |")
            if i == 0:
                lines.append("|" + "---|" * width)
        return "\n".join(lines)
    # complex table: minimal HTML
    out = ["<table>"]
    for r in rows:
        out.append("<tr>")
        for txt, cs, rs, th in r:
            tag = "th" if th else "td"
            attrs = (f' colspan="{cs}"' if cs > 1 else "") + (f' rowspan="{rs}"' if rs > 1 else "")
            out.append(f"<{tag}{attrs}>{md_inline_to_html(txt)}</{tag}>")
        out.append("</tr>")
    out.append("</table>")
    return "\n".join(out)


def md_inline_to_html(t):
    # cell text is Markdown-escaped; convert emphasis to HTML inside HTML blocks
    t = re.sub(r"(?<!\\)\*\*(.+?)(?<!\\)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\\)\*(.+?)(?<!\\)\*", r"<i>\1</i>", t)
    return t.replace("\\*", "*").replace("\\\\", "\\").replace("\\`", "`")


def iter_blocks(body):
    """Yield block-level elements in document order, not descending into tables."""
    stack = [iter(body)]
    while stack:
        try:
            e = next(stack[-1])
        except StopIteration:
            stack.pop()
            continue
        n = local(e)
        if not n:
            continue
        if n in BLOCK:
            yield e
            continue
        if n in ("ul", "ol", "div", "blockquote", "section", "tbody", "thead", "center", "a", "span", "font"):
            # inline-ish container holding text directly (rare): treat as paragraph
            if n in ("a", "span", "font"):
                yield e
                continue
            stack.append(iter(e))
            continue
        yield e


def html_files(z):
    """HTML files in spine order."""
    names = [n for n in z.namelist() if n.lower().endswith((".html", ".xhtml", ".htm"))]
    opf = next((n for n in z.namelist() if n.endswith(".opf")), None)
    if opf:
        try:
            root = etree.fromstring(z.read(opf))
            ns = {"o": "http://www.idpf.org/2007/opf"}
            items = {i.get("id"): i.get("href") for i in root.iterfind(".//o:manifest/o:item", ns)}
            base = os.path.dirname(opf)
            order = [os.path.normpath(os.path.join(base, items[r.get("idref")])).replace("\\", "/")
                     for r in root.iterfind(".//o:spine/o:itemref", ns) if r.get("idref") in items]
            order = [n for n in order if n in names]
            if order:
                return order
        except etree.XMLSyntaxError:
            pass
    return sorted(names)


def parse_html(data):
    parser = etree.HTMLParser(encoding="utf-8", remove_comments=True)
    try:
        root = etree.fromstring(data, etree.XMLParser(recover=True, huge_tree=True, remove_comments=True))
        if root is None or root.find(".//" + XHTML + "body") is None:
            raise etree.XMLSyntaxError("no body", None, 0, 0)
        return root.find(".//" + XHTML + "body")
    except etree.XMLSyntaxError:
        root = etree.fromstring(data, parser)
        return root.find(".//body")


def epub_to_md(paths, title):
    out = []
    first_img = True
    skipped_title = False
    for path in paths:
        if path.endswith(".docx"):
            out.extend(docx_to_md(path))
            continue
        if path.endswith(".pdf"):
            out.extend(pdf_to_md(path))
            continue
        with zipfile.ZipFile(path) as z:
            for name in html_files(z):
                body = parse_html(z.read(name))
                if body is None:
                    continue
                for e in iter_blocks(body):
                    n = local(e)
                    cls = (e.get("class") or "").strip()
                    if SKIP_CLASSES.match(cls):
                        continue
                    if n == "table":
                        t = render_table(e)
                        if t:
                            out.append(t)
                        continue
                    if n == "hr":
                        continue
                    if n == "img":
                        if first_img:
                            first_img = False
                            continue
                        alt = (e.get("alt") or "").strip()
                        out.append(f"[image{': ' + alt if alt else ''}]")
                        continue
                    # paragraph-like
                    imgs = e.findall(".//" + XHTML + "img") + e.findall(".//img")
                    if imgs and first_img and not "".join(e.itertext()).strip():
                        first_img = False
                        continue
                    if imgs:
                        first_img = False
                    t = inline(e)
                    if not t:
                        continue
                    if not skipped_title and cls in ("ShortT", "Title", "ShortTP1") and plain(t).lower() == title.lower():
                        skipped_title = True
                        continue
                    lvl = HEADINGS.get(cls)
                    if lvl is None and n[0] == "h" and n[1:].isdigit():
                        lvl = min(int(n[1:]) + 1, 6)
                    if lvl:
                        h = plain(t)
                        if h:
                            out.append("#" * lvl + " " + h)
                        continue
                    if cls in ("ItemHead", "ItemHeadNoNum"):
                        out.append("**" + plain(t).replace("*", "\\*") + "**")
                        continue
                    out.append(para(t))
    return out


def docx_to_md(path):
    """Fallback for titles without an EPUB rendition: paragraphs of a .docx (styles -> headings)."""
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    out = []
    with zipfile.ZipFile(path) as z:
        root = etree.fromstring(z.read("word/document.xml"), etree.XMLParser(huge_tree=True))
    body = root.find(W + "body")
    for el in body.iter(W + "p", W + "tbl"):
        if el.tag == W + "tbl":
            continue
        if any(a.tag == W + "tbl" for a in el.iterancestors()):
            # table cells: rendered row by row below
            continue
        st = el.find(f"{W}pPr/{W}pStyle")
        cls = st.get(W + "val") if st is not None else ""
        if SKIP_CLASSES.match(cls or ""):
            continue
        txt = "".join(t.text or "" for t in el.iter(W + "t", W + "tab"))
        txt = SPACES.sub(" ", txt).strip()
        if not txt:
            continue
        lvl = HEADINGS.get(cls)
        out.append(("#" * lvl + " " + txt) if lvl else para(esc(txt)))
    for tbl in body.iter(W + "tbl"):
        rows = []
        for tr in tbl.iter(W + "tr"):
            cells = [SPACES.sub(" ", "".join(t.text or "" for t in tc.iter(W + "t"))).strip().replace("|", "\\|")
                     for tc in tr.iter(W + "tc")]
            rows.append("| " + " | ".join(cells) + " |")
        if rows:
            out.append("\n".join(rows[:1] + ["|" + "---|" * rows[0].count(" | ") + "---|"] + rows[1:]))
    return out


def pdf_to_md(path):
    """Last-resort fallback for PDF-only titles: extracted text, one paragraph per blank-line block."""
    from pypdf import PdfReader
    out = []
    for page in PdfReader(path).pages:
        txt = page.extract_text() or ""
        for block in re.split(r"\n\s*\n", txt):
            lines = [SPACES.sub(" ", l).strip() for l in block.splitlines()]
            lines = [l for l in lines if l]
            if lines:
                out.append(para(esc("\x00BR\x00".join(lines))))
    return out


def date_only(s):
    return s[:10] if s else None


def out_path(t, coll):
    d, _ = COLLECTIONS[coll]
    name = t["name"]
    if coll == "Constitution":
        return os.path.join(ROOT, d, f"{slugify(name)}.md")
    year = t.get("year") or (t.get("makingDate") or "0000")[:4]
    fname = f"{t['id']}-{slugify(name, 70)}.md"
    if coll == "LegislativeInstrument" and LI_BIG_YEARS and str(year) in LI_BIG_YEARS:
        # GitHub lists at most 1,000 entries per directory: split crowded years by id block
        return os.path.join(ROOT, d, str(year), t["id"][:-3] + "xxx", fname)
    return os.path.join(ROOT, d, str(year), fname)


LI_BIG_YEARS = set()


def front_matter(t, meta, coll, retrieved):
    _, typ = COLLECTIONS[coll]
    fm = {
        "title": meta.get("name") or t["name"],
        "identifier": t["id"],
        "register_id": meta.get("registerId"),
        "type": typ,
    }
    if t.get("subCollection"):
        fm["subtype"] = t["subCollection"]
    if coll == "Act":
        fm["principal"] = bool(t.get("isPrincipal"))
    if t.get("seriesType") and t.get("number") and t.get("year"):
        st = {"Act": "Act No.", "SR": "Statutory Rules No.", "SLI": "Select Legislative Instrument No."}.get(
            t["seriesType"], t["seriesType"] + " No.")
        fm["number"] = f"{st} {t['number']}, {t['year']}"
    elif t.get("optionalSeriesNumber"):
        fm["number"] = t["optionalSeriesNumber"]
    fm["jurisdiction"] = "au"
    fm["language"] = "en"
    fm["date"] = date_only(t.get("makingDate"))
    comp = meta.get("compilationNumber")
    if comp and comp != "0":
        fm["compilation_number"] = int(comp) if comp.isdigit() else comp
        fm["last_amended"] = date_only(meta.get("start"))
    else:
        fm["last_amended"] = None
    fm["version_start"] = date_only(meta.get("start"))
    fm["status"] = {"InForce": "in_force", "Repealed": "repealed", "Ceased": "repealed"}.get(
        t.get("status"), "unknown")
    fm["source"] = f"{SITE}/{t['id']}/latest/text"
    fm["retrieved"] = retrieved
    return {k: v for k, v in fm.items() if v is not None}


class Dumper(yaml.SafeDumper):
    pass


def _str(d, s):
    quote = (":" in s or s != s.strip() or "#" in s or s[:1] in "'\"[]{}&*!|>%@`-?,"
             or s.lower() in ("yes", "no", "true", "false", "null", "on", "off", "~", "")
             or re.match(r"^[\d.\-+eE]+$", s) is not None)
    return d.represent_scalar("tag:yaml.org,2002:str", s, style='"' if quote else None)


Dumper.add_representer(str, _str)
Dumper.add_representer(datetime.date, lambda d, v: d.represent_scalar("tag:yaml.org,2002:timestamp", v.isoformat()))


def convert(t, coll, retrieved):
    tid = t["id"]
    mp = os.path.join(RAW, "meta", f"{tid}.json")
    if not os.path.exists(mp):
        return None, "no-meta"
    meta = read_json(mp)
    paths = [doc_path(tid, d) for d in pick_docs(meta)]
    paths = [p for p in paths if os.path.exists(p)]
    if not paths:
        return None, "no-docs"
    title = meta.get("name") or t["name"]
    blocks = epub_to_md(paths, title)
    fm = front_matter(t, meta, coll, retrieved)
    text = "---\n" + yaml.dump(fm, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=10000) + "---\n\n"
    text += f"# {title}\n\n" + "\n\n".join(blocks) + "\n"
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    path = out_path(t, coll)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return path, "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("collections", nargs="+")
    ap.add_argument("--retrieved", default=datetime.date.today().isoformat())
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    for coll in a.collections:
        titles = read_json(os.path.join(RAW, "lists", f"{coll}.json"))
        if coll == "LegislativeInstrument":
            import collections
            yc = collections.Counter(str(t.get("year") or (t.get("makingDate") or "0000")[:4]) for t in titles)
            LI_BIG_YEARS.update(y for y, n in yc.items() if n > 900)
        if a.only:
            titles = [t for t in titles if t["id"] in a.only.split(",")]
        ok, bad = 0, []
        for i, t in enumerate(titles, 1):
            try:
                p, st = convert(t, coll, a.retrieved)
            except Exception as e:
                p, st = None, f"error {type(e).__name__}: {e}"
            if st == "ok":
                ok += 1
            else:
                bad.append(f"{t['id']} {st}")
            if i % 500 == 0:
                print(f"  {coll}: {i}/{len(titles)}", file=sys.stderr)
        print(f"{coll}: {ok} written, {len(bad)} problems", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)


if __name__ == "__main__":
    main()
