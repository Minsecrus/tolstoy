"""Typeset the checked Chinese book continuously, retaining source-page ranges.

Requires Pandoc and XeLaTeX. Intermediate files remain under tmp/pdfs/algebra-export.
No book source is edited. Formula AST nodes remain TeX, not raster images.
"""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "tmp/pdfs/algebra-export"
OUT = ROOT / "output/pdf/Algebra-Zh.pdf"

PREAMBLE = r"""\documentclass[UTF8,fontset=windows,11pt]{ctexart}
\usepackage[a4paper,top=22mm,bottom=22mm,left=22mm,right=22mm,headheight=14pt,headsep=7mm,footskip=10mm]{geometry}
\usepackage{amsmath,amssymb,amscd,mathtools,stmaryrd,mathrsfs}
\usepackage{graphicx,adjustbox,enumitem,fancyhdr,xcolor,hyperref,bookmark}
\setCJKmainfont{SimSun}[BoldFont=SimSun,BoldFeatures={FakeBold=1.5},ItalicFont=SimSun,ItalicFeatures={FakeSlant=0.15},BoldItalicFont=SimSun,BoldItalicFeatures={FakeBold=1.5,FakeSlant=0.15}]
\setCJKsansfont{SimSun}[BoldFont=SimSun,BoldFeatures={FakeBold=1.5}]
\setmainfont{Cambria}
\xeCJKsetup{PunctStyle=plain}
\hypersetup{unicode=true,hidelinks,linktoc=all,pdftitle={代数},pdfauthor={Serge Lang},pdfsubject={第三版修订版中文译本},bookmarksdepth=0}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt plus 1pt minus 1pt}
\linespread{1.13}
\setlength{\emergencystretch}{2em}
\sloppy
\setlist{nosep,leftmargin=1.8em,topsep=4pt,parsep=2pt}
\setcounter{secnumdepth}{-1}
\setcounter{tocdepth}{2}
\renewcommand{\contentsname}{目录}
\makeatletter
\renewcommand{\@pnumwidth}{2.5em}
\renewcommand{\@tocrmarg}{3.5em}
\makeatother
\ctexset{section={format=\Large\bfseries,beforeskip=9pt,afterskip=6pt},subsection={format=\large\bfseries,beforeskip=7pt,afterskip=5pt},subsubsection={format=\normalsize\bfseries,beforeskip=6pt,afterskip=4pt}}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\pandocbounded}[1]{#1}
\providecommand{\passthrough}[1]{#1}
\InputIfFileExists{algebra-page-headers.tex}{}{}
\newcommand{\pageoriginal}{\ifcsname AlgebraOriginal\thepage\endcsname\csname AlgebraOriginal\thepage\endcsname\fi}
\newcommand{\pagesection}{\ifcsname AlgebraSection\thepage\endcsname\csname AlgebraSection\thepage\endcsname\fi}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\scriptsize\color{gray}\pagesection}
\fancyhead[R]{\scriptsize\color{gray}\pageoriginal}
\fancyfoot[C]{\footnotesize\thepage}
\renewcommand{\headrulewidth}{0.2pt}
\renewcommand{\footrulewidth}{0pt}
\newwrite\sourcemap
\immediate\openout\sourcemap=algebra-page-map.tsv
\newif\ifAlgebraBody
\AlgebraBodyfalse
% These deferred writes travel with the line containing the source boundary.
% Original page boundaries neither start a paragraph nor force a new PDF page.
\DeclareRobustCommand{\sourcebegin}[1]{\ifAlgebraBody\write\sourcemap{S #1\space\thepage}\fi}
\DeclareRobustCommand{\sourceend}[1]{\ifAlgebraBody\write\sourcemap{E #1\space\thepage}\fi}
\newcommand{\booksection}[2]{\clearpage\pdfbookmark[0]{#2}{chapter-#1}}
\newcommand{\AlgebraDisplay}[2]{\begin{equation*}\adjustbox{max width=0.94\linewidth}{$\displaystyle #1$}#2\end{equation*}}
\DeclareRobustCommand{\AlgebraInline}[1]{\leavevmode\hskip0pt\adjustbox{max width=.96\linewidth}{$#1$}\hskip0pt}
\pdfstringdefDisableCommands{\def\AlgebraInline#1{#1}\def\sourcebegin#1{}\def\sourceend#1{}}
\begin{document}
\pdfbookmark[0]{目录}{contents}
\tableofcontents
\clearpage
\AlgebraBodytrue
"""


def escape_tex(s):
    chars = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(chars.get(c, c) for c in s)


def convert():
    WORK.mkdir(parents=True, exist_ok=True)
    reading = json.loads(subprocess.run(["node", "scripts/algebra-continuous-reading.mjs", "--json", "--language", "zh"], cwd=ROOT, text=True, encoding="utf8", stdout=subprocess.PIPE, check=True).stdout)
    sections = [s for s in reading["sections"] if s["key"] not in ["title-pages", "contents", "series-list"]]
    diagram_sizes = json.loads((ROOT / "scripts/algebra-diagram-sizes.json").read_text(encoding="utf8"))["images"]
    assert len(diagram_sizes) == 140, "All original diagram sizes must be measured"
    pieces = []
    source_hashes = {}
    reading_bodies = {}
    pages = {}
    for section in sections:
        for page in section["pages"]:
            n = page["pdfPage"]
            p = ROOT / f"source/algebra/zh/pdf-{n:04d}.md"
            source_hashes[str(n)] = hashlib.sha256(p.read_bytes()).hexdigest()
            review = json.loads((ROOT / f"source/algebra/review/pdf-{n:04d}.json").read_text(encoding="utf8"))
            assert all(review[k] for k in ["visualReviewed", "chineseTranslated", "formulaChecked"])
            pages[n] = page
            reading_bodies[str(n)] = page["body"]
            pieces.append(f"ALGEbrasource{n:04d}\n\n" + page["body"] + "\n\n")
    md = "".join(pieces)
    ast = json.loads(subprocess.run(["pandoc", "-f", "markdown-fancy_lists", "-t", "json"], input=md, text=True, encoding="utf8", stdout=subprocess.PIPE, check=True).stdout)
    chunks = {}
    current = None
    for block in ast["blocks"]:
        if block.get("t") == "Para" and len(block["c"]) == 1 and block["c"][0].get("t") == "Str" and re.fullmatch(r"ALGEbrasource\d{4}", block["c"][0]["c"]):
            current = int(block["c"][0]["c"][-4:])
            chunks[current] = []
        else:
            assert current is not None, block
            # Source heading levels differ between OCR batches. All numbered
            # mathematical sections belong to the same clickable TOC level.
            if block.get("t") == "Header" and block["c"][0] >= 2:
                heading = "".join(item.get("c", " ") for item in block["c"][2] if item.get("t") in ["Str", "Space"])
                if re.match(r"§\s*\d+", heading):
                    block["c"][0] = 2
            chunks[current].append(block)

    def marker(n, end=False):
        return {"t": "RawInline", "c": ["latex", (r"\sourceend{" if end else r"\sourcebegin{") + str(n) + "}"]}

    def attach_boundary(blocks, n, end=False):
        # Put bookkeeping inside the actual first/last typeset line. It has no
        # width, height, visible text, paragraph break, or formula semantics.
        # A heading is a moving argument: never copy source bookkeeping into
        # the generated contents, auxiliary files, or bookmark strings.
        edge = blocks[-1] if end else blocks[0]
        if edge.get("t") == "Header":
            command = marker(n, end)["c"][1]
            blocks.insert(len(blocks) if end else 1, {"t": "RawBlock", "c": ["latex", command]})
            return
        def attach(node):
            if isinstance(node, dict):
                kind = node.get("t")
                if kind == "Header":
                    return False
                if kind in ["Para", "Plain"]:
                    inlines = node["c"]
                    inlines.insert(len(inlines) if end else 0, marker(n, end))
                    return True
                if kind == "Figure":
                    node["sourceEnd" if end else "sourceBegin"] = n
                    return True
                children = list(node.values())
            elif isinstance(node, list):
                children = node
            else:
                return False
            return any(attach(child) for child in (reversed(children) if end else children))
        assert attach(blocks), (n, "no content line for source marker")

    joined = []
    joined_pages = []
    for section in sections:
        joined.append({"t": "RawBlock", "c": ["latex", r"\booksection{" + section["key"] + "}{" + escape_tex(section["title"]) + "}"]})
        joined.append({"t": "Header", "c": [1, ["section-" + section["key"], [], []], [{"t": "Str", "c": section["title"]}]]})
        for page in section["pages"]:
            n = page["pdfPage"]
            blocks = chunks[n]
            attach_boundary(blocks, n)
            attach_boundary(blocks, n, end=True)
            if page["joinsPrevious"]:
                assert joined[-1]["t"] == "Para" and blocks[0]["t"] == "Para", (n, "joining nonparagraph")
                if page.get("joinSeparator"):
                    joined[-1]["c"].append({"t": "Space"})
                joined[-1]["c"].extend(blocks[0]["c"])
                joined.extend(blocks[1:])
                joined_pages.append(n)
            else:
                joined.extend(blocks)
    ast["blocks"] = joined
    counters = {"inlineMath": 0, "displayMath": 0, "diagrams": 0, "mathPunctuation": 0}

    def walk(node):
        if isinstance(node, list):
            return [walk(v) for v in node]
        if not isinstance(node, dict):
            return node
        if node.get("t") == "Math":
            kind, tex = node["c"]
            # Two source formulas end in a Chinese sentence stop within $$.
            # Math fonts do not contain U+3002; retain it using the CJK text font.
            counters["mathPunctuation"] += tex.count("。")
            tex = tex.replace("。", r"\text{。}")
            if kind["t"] == "DisplayMath":
                counters["displayMath"] += 1
                tags = re.findall(r"\\tag\*?\{[^}]*\}", tex)
                tex = re.sub(r"\\tag\*?\{[^}]*\}", "", tex)
                return {"t": "RawInline", "c": ["latex", r"\AlgebraDisplay{" + tex + "}{" + "".join(tags) + "}"]}
            counters["inlineMath"] += 1
            # Keep the final sentence stop with this long congruence. Without
            # an explicit break XeCJK places its period alone on a new line.
            linebreak = r"\newline" if tex == r"\operatorname{grad}f(B)\equiv\operatorname{grad}f(A)\equiv0\pmod{\mathfrak p^{r-1}}" else ""
            return {"t": "RawInline", "c": ["latex", linebreak + r"\AlgebraInline{" + tex + "}"]}
        if node.get("t") == "Figure":
            images = []
            def find(v):
                if isinstance(v, dict):
                    if v.get("t") == "Image":
                        images.append(v["c"][2][0])
                    else:
                        for z in v.values(): find(z)
                elif isinstance(v, list):
                    for z in v: find(z)
            find(node["c"][2])
            assert images, node
            commands = []
            for url in images:
                assert url.startswith("/library/volume-86/diagrams/"), url
                asset = ROOT / "docs/public" / url.lstrip("/")
                assert asset.is_file(), asset
                size = diagram_sizes[asset.name]
                assert hashlib.sha256(asset.read_bytes()).hexdigest() == size["assetSha256"], f"Diagram size snapshot stale: {asset}"
                counters["diagrams"] += 1
                commands.append(r"\adjustbox{max width=\linewidth,max totalheight=.65\textheight}{\includegraphics[width=" + f"{size['widthPt']:.6f}bp" + "]{" + asset.as_posix() + "}}")
            before = r"\leavevmode\sourcebegin{" + str(node["sourceBegin"]) + "}" if "sourceBegin" in node else ""
            after = r"\sourceend{" + str(node["sourceEnd"]) + "}" if "sourceEnd" in node else ""
            return {"t": "RawBlock", "c": ["latex", "\\begin{center}\n" + before + "\n\n".join(commands) + after + "\n\\end{center}"]}
        return {k: walk(v) for k, v in node.items()}

    ast = walk(ast)
    body = subprocess.run(["pandoc", "-f", "json", "-t", "latex", "--wrap=none"], input=json.dumps(ast, ensure_ascii=False), text=True, encoding="utf8", stdout=subprocess.PIPE, check=True).stdout
    (WORK / "algebra.tex").write_text(PREAMBLE + body + "\n\\clearpage\n\\immediate\\closeout\\sourcemap\n\\end{document}\n", encoding="utf8")
    section_metadata = [{k: v for k, v in s.items() if k != "pages"} for s in sections]
    (WORK / "export-source-check.json").write_text(json.dumps({"pages": len(pages), "sections": section_metadata, "counts": counters, "sourceHashes": source_hashes, "readingBodies": reading_bodies, "joinedSourcePages": joined_pages, "generatedContents": True}, ensure_ascii=False, indent=2), encoding="utf8")
    print(json.dumps({"tex": str(WORK / "algebra.tex"), **counters}))


def build_page_mapping(page_count):
    snapshot = json.loads((WORK / "export-source-check.json").read_text(encoding="utf8"))
    events = [line.split() for line in (WORK / "algebra-page-map.tsv").read_text().splitlines()]
    starts = {int(n): int(physical) for kind, n, physical in events if kind == "S"}
    ends = {int(n): int(physical) for kind, n, physical in events if kind == "E"}
    retained = list(range(6, 12)) + list(range(17, 920))
    assert len(events) == 2 * len(retained)
    assert sorted(starts) == retained and sorted(ends) == retained
    assert all(1 <= starts[n] <= ends[n] <= page_count for n in retained)
    assert all(starts[a] <= starts[b] and ends[a] <= ends[b] for a, b in zip(retained, retained[1:])), "source boundaries must advance monotonically"
    mapping = []
    for n in retained:
        review = json.loads((ROOT / f"source/algebra/review/pdf-{n:04d}.json").read_text(encoding="utf8"))
        mapping.append({"sourcePdfPage": n, "printedPage": review["printedPage"], "firstExportPage": starts[n], "lastExportPage": ends[n]})
    by_source = {entry["sourcePdfPage"]: entry for entry in mapping}
    sections = {n: s for s in snapshot["sections"] for n in range(s["firstPdfPage"], s["lastPdfPage"] + 1)}
    physical_pages = []
    for physical in range(1, page_count + 1):
        sources = [n for n in retained if starts[n] <= physical <= ends[n]]
        if not sources:
            assert physical < starts[retained[0]], (physical, "content page without original source")
            physical_pages.append({"exportPage": physical, "sourcePdfPages": [], "originalLabel": "", "sectionTitle": "目录", "generated": True})
            continue
        printed = [str(by_source[n]["printedPage"]) for n in sources if by_source[n]["printedPage"] is not None]
        label = "原书 " + (printed[0] if printed[0] == printed[-1] else printed[0] + "–" + printed[-1]) if printed else ""
        physical_pages.append({"exportPage": physical, "sourcePdfPages": sources, "originalLabel": label, "sectionTitle": sections[sources[-1]]["title"]})
    return mapping, physical_pages


def write_page_headers(physical_pages):
    header_text = "\n".join(r"\expandafter\def\csname Algebra" + name + str(page["exportPage"]) + r"\endcsname{" + escape_tex(page[key]) + "}" for page in physical_pages for name, key in [("Original", "originalLabel"), ("Section", "sectionTitle")]) + "\n"
    path = WORK / "algebra-page-headers.tex"
    previous = path.read_text(encoding="utf8") if path.exists() else None
    path.write_text(header_text, encoding="utf8")
    return previous == header_text


def compile_pdf():
    from pypdf import PdfReader
    # The first pass measures source ranges; later passes print those ranges.
    # Header dimensions stay fixed, but verify the map stabilizes before export.
    for cache in ["algebra-page-headers.tex", "algebra.aux", "algebra.toc", "algebra.out"]:
        (WORK / cache).unlink(missing_ok=True)
    for run in range(4):
        log = WORK / f"xelatex-pass-{run + 1}.txt"
        with log.open("w", encoding="utf8") as output:
            result = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "algebra.tex"], cwd=WORK, stdout=output, stderr=subprocess.STDOUT, text=True, encoding="utf8", errors="replace")
        if result.returncode:
            print(log.read_text(encoding="utf8")[-6000:])
            raise RuntimeError(f"XeLaTeX failed; see {log}")
        print(f"XeLaTeX pass {run + 1} completed", flush=True)
        _, physical_pages = build_page_mapping(len(PdfReader(WORK / "algebra.pdf").pages))
        stable = write_page_headers(physical_pages)
        if run >= 1 and stable:
            return
    raise RuntimeError("Original-page header map did not stabilize after four passes")


def finalize():
    from pypdf import PdfReader, PdfWriter
    reader = PdfReader(WORK / "algebra.pdf")
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    mapping, physical_pages = build_page_mapping(len(reader.pages))
    for page in physical_pages:
        label = "目录 " + str(page["exportPage"]) if page.get("generated") else page["originalLabel"].removeprefix("原书 ")
        writer.set_page_label(page["exportPage"] - 1, page["exportPage"] - 1, prefix=label)
    writer.add_metadata({"/Title": "代数", "/Author": "Serge Lang", "/Subject": "第三版修订版中文译本", "/Language": "zh-CN"})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("wb") as output:
        writer.write(output)
    snapshot = json.loads((WORK / "export-source-check.json").read_text(encoding="utf8"))
    by_source = {page["sourcePdfPage"]: page for page in mapping}
    section_starts = [{"key": section["key"], "firstExportPage": by_source[section["firstPdfPage"]]["firstExportPage"], "lastExportPage": by_source[section["lastPdfPage"]]["lastExportPage"]} for section in snapshot["sections"]]
    report = {"pdf": str(OUT), "pageCount": len(reader.pages), "originalPageCount": len(mapping), "excludedSourcePages": [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 920, 921, 922, 923], "generatedContentsPages": sum(bool(page.get("generated")) for page in physical_pages), "bytes": OUT.stat().st_size, "pageMap": mapping, "physicalPages": physical_pages, "sectionStarts": section_starts}
    (WORK / "export-page-map.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf8")
    print(json.dumps({k: v for k, v in report.items() if k not in ["pageMap", "physicalPages", "sectionStarts"]}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--compile-only", action="store_true")
    args = parser.parse_args()
    if not args.compile_only:
        convert()
    if not args.prepare_only:
        compile_pdf()
        finalize()
