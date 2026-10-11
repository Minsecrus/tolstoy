"""Extract reference text and render requested pages; no review status is inferred."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--render", nargs=2, type=int, metavar=("FIRST", "LAST"))
    parser.add_argument("--dpi", type=int, default=145)
    args = parser.parse_args()
    source = args.pdf.resolve()
    work = ROOT / "tmp" / "pdfs" / "algebra"
    text_dir = work / "text"
    image_dir = work / "pages"
    text_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)
    pdf = pymupdf.open(source)
    manifest = {
        "sourceFileName": source.name,
        "sourceSha256": hashlib.file_digest(source.open("rb"), "sha256").hexdigest(),
        "pdfPageCount": len(pdf),
        "title": "Algebra",
        "author": "Serge Lang",
        "edition": "Revised Third Edition, corrected printing 2005",
        "extractionNotice": "Embedded OCR is an unverified reference. Extraction/rendering does not constitute visual review or translation.",
        "pages": [],
    }
    for number, page in enumerate(pdf, 1):
        text = page.get_text(sort=False)
        (text_dir / f"pdf-{number:04d}.txt").write_text(text, encoding="utf-8")
        manifest["pages"].append({
            "pdfPage": number,
            "widthPt": round(page.rect.width, 3),
            "heightPt": round(page.rect.height, 3),
            "embeddedTextCharacters": len(text),
            "embeddedTextSha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        })
    (ROOT / "scripts" / "algebra-source-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Extracted {len(pdf)} reference pages; SHA-256 {manifest['sourceSha256']}", flush=True)
    if args.render:
        first, last = args.render
        if not 1 <= first <= last <= len(pdf):
            raise ValueError("Render range is outside the PDF")
        for number in range(first, last + 1):
            target = image_dir / f"pdf-{number:04d}.png"
            if not target.exists():
                pdf[number - 1].get_pixmap(dpi=args.dpi, alpha=False).save(target)
            if number % 10 == 0 or number == last:
                print(f"Rendered PDF page {number}", flush=True)


if __name__ == "__main__":
    main()
