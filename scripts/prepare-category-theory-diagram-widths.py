"""Precompute website crop widths from reviewed physical sizes, never PNG density.

The source PDF is used only here to verify the normal body font. The website
renderer reads the committed JSON and has no dependency on the user's PDF.
"""
import collections
import hashlib
import json
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
FONT_PT = 9.9626  # Source cambridge7A.cls normalsize: 10 TeX pt, measured PDF bp.
PREFIX = "/library/volume-87/diagrams/"


def main():
    manifest = json.loads((ROOT / "scripts/category-theory-source-manifest.json").read_text(encoding="utf-8-sig"))
    source = Path(manifest["sourcePath"])
    if hashlib.sha256(source.read_bytes()).hexdigest() != manifest["sourceSha256"]:
        raise ValueError("Source PDF hash differs from the reviewed manifest")
    diagrams = {}
    crop_pages = set()
    with pymupdf.open(source) as pdf:
        for record in sorted((ROOT / "source/category-theory/review").glob("pdf-*.json")):
            review = json.loads(record.read_text(encoding="utf-8-sig"))
            page_number = review["pdfPage"]
            for diagram in review.get("diagrams", []):
                url, width = diagram["path"], diagram["widthPt"]
                clip = diagram["clipPt"]
                if not url.startswith(PREFIX) or url in diagrams:
                    raise ValueError(f"Unexpected or duplicate crop URL: {url}")
                if width <= 0 or abs(width - (clip[2] - clip[0])) > 0.02:
                    raise ValueError(f"Physical crop width mismatch: {url}")
                asset = ROOT / "docs/public" / url.lstrip("/")
                if hashlib.sha256(asset.read_bytes()).hexdigest() != diagram["sha256"]:
                    raise ValueError(f"Reviewed crop hash mismatch: {url}")
                diagrams[url] = {
                    "widthPt": width,
                    "bodyFontPt": FONT_PT,
                    "widthEm": round(width / FONT_PT, 6),
                    "sourcePdfPage": page_number,
                    "clipPt": clip,
                    "sha256": diagram["sha256"],
                }
                crop_pages.add(page_number)
        for page_number in sorted(crop_pages):
            counts = collections.Counter()
            for block in pdf[page_number - 1].get_text("dict")["blocks"]:
                for line in block.get("lines", []):
                    for span in line["spans"]:
                        if span["font"] == "NimbusRomNo9L-Regu" and len(span["text"].strip()) >= 25:
                            counts[round(span["size"], 6)] += len(span["text"])
            if not counts or counts.most_common(1)[0][0] != FONT_PT:
                raise ValueError(f"Normal body font changed on source PDF page {page_number}: {counts}")
    payload = {
        "sourceSha256": manifest["sourceSha256"],
        "bodyFontPt": FONT_PT,
        "bodyFontEvidence": "PDF text spans on every crop page: NimbusRomNo9L-Regu 9.9626 PDF pt; matching cambridge7A.cls normalsize is 10 TeX pt.",
        "diagramCount": len(diagrams),
        "diagrams": diagrams,
    }
    destination = ROOT / "scripts/category-theory-diagram-widths.json"
    destination.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Prepared {len(diagrams)} crop widths from {len(crop_pages)} verified body-font pages: {destination}")


if __name__ == "__main__":
    main()
