"""Verify reviewed scan crops and calibrate their widths against actual print.

OCR's synthetic Times-Roman font sizes are deliberately not used. The matching
author PDF provides the native CMR10 size. The physical horizontal scale of
each scanned crop page is measured from the same printed running-head rule;
matching prose-line geometry is a fallback for chapter-opening pages.
Only this preparation command needs the two PDFs. The website uses the saved
mapping and has no dependency on an original file on the user's computer.
"""
import argparse
import collections
import hashlib
import json
import unicodedata
from pathlib import Path

import numpy as np
from PIL import Image
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
PREFIX = "/library/volume-88/diagrams/"
OFFICIAL_URL = "https://math.mit.edu/~etingof/representationtheorybook.pdf"
OFFICIAL_SHA = "6ecd809a32ec277a72785868ad1adc9e4cd2ee7d361a9a84fa40af34f56464cf"
DEFAULT_OFFICIAL = ROOT / "tmp/pdfs/representation-theory/diagram-scaling/official-representationtheorybook.pdf"
DPI = 300


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def longest_ink_rule(page, clip):
    """Measure a long continuous black rule in a narrow running-head strip."""
    # Render in the same RGB colour space as the canonical crops.
    pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csRGB, alpha=False, clip=clip)
    rgb = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
    ink = rgb.min(axis=2) < 100
    best = (0, 0, 0)
    for y, row in enumerate(ink):
        jumps = np.diff(np.r_[False, row, False].astype(np.int8))
        starts, ends = np.flatnonzero(jumps == 1), np.flatnonzero(jumps == -1)
        if len(starts):
            i = np.argmax(ends - starts)
            if ends[i] - starts[i] > best[0]:
                best = (int(ends[i] - starts[i]), int(starts[i]), int(y))
    return {
        "widthPx": best[0], "widthPt": best[0] * 72 / DPI,
        "leftPt": (pix.x + best[1]) * 72 / DPI,
        "topPt": (pix.y + best[2]) * 72 / DPI,
        "dpi": DPI, "blackThreshold": 100,
    }


def prose_lines(page):
    result = {}
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            text = "".join(span["text"] for span in line["spans"])
            normalized = "".join(c for c in unicodedata.normalize("NFKD", text).lower() if c.isalnum())
            if len(normalized) >= 40 and normalized not in result:
                result[normalized] = (line["bbox"], text)
    return result


def matched_prose_geometry(scan, official):
    left, right = prose_lines(scan), prose_lines(official)
    matches = [(left[key], right[key]) for key in left if key in right]
    if len(matches) < 3:
        return None
    x = np.array([(o[0][edge], s[0][edge]) for s, o in matches for edge in [0, 2]])
    y = np.array([((o[0][1] + o[0][3]) / 2, (s[0][1] + s[0][3]) / 2) for s, o in matches])
    sx, tx = np.polyfit(x[:, 0], x[:, 1], 1)
    sy, ty = np.polyfit(y[:, 0], y[:, 1], 1)
    return {
        "matchedLineCount": len(matches), "scaleX": round(float(sx), 9),
        "scaleY": round(float(sy), 9),
        "horizontalResidualRmsePt": round(float(np.sqrt(np.mean((x[:, 1] - sx * x[:, 0] - tx) ** 2))), 6),
        "verticalResidualRmsePt": round(float(np.sqrt(np.mean((y[:, 1] - sy * y[:, 0] - ty) ** 2))), 6),
        "exampleMatchedLines": [s[1] for s, _ in matches[:3]],
    }


def body_font(official):
    counts = collections.Counter()
    for page in official:
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    if span["font"] == "CMR10" and span["text"].strip():
                        counts[round(span["size"], 9)] += len(span["text"])
    if not counts:
        raise ValueError("Official PDF has no native CMR10 body-font evidence")
    measured, count = counts.most_common(1)[0]
    if abs(measured - 10 * 72 / 72.27) > 0.00001:
        raise ValueError(f"Unexpected official CMR10 body-font size: {measured}")
    return measured, count


def calibrate_page(number, scan, official, font_pt):
    if not 9 <= number <= 236:
        raise ValueError(f"Source page {number} is outside the matching official body-page range")
    s, o = scan[number - 1], official[number - 1]
    sr = longest_ink_rule(s, pymupdf.Rect(0, 0, s.rect.width, 45))
    rr = longest_ink_rule(o, pymupdf.Rect(0, 130, o.rect.width, 168))
    geometry = matched_prose_geometry(s, o)
    if sr["widthPt"] >= 260 and rr["widthPt"] >= 260:
        scale = sr["widthPt"] / rr["widthPt"]
        method = "same printed running-head rule, actual raster ink at 300 dpi"
        # An exact prose match also checks that the scan and clear pages align.
        # Sparse all-diagram pages still have a page-number/running-head rule.
        if geometry and abs(scale - geometry["scaleX"]) > 0.015:
            raise ValueError(f"Rule and matching-prose scale disagree on source page {number}")
    elif geometry and geometry["horizontalResidualRmsePt"] <= 1.5 and geometry["matchedLineCount"] >= 3:
        scale = geometry["scaleX"]
        method = "horizontal regression of exact matching long prose-line coordinates; no OCR font size"
    else:
        raise ValueError(f"Cannot reliably calibrate source crop page {number}: rule={sr}, matches={geometry}")
    if not 0.97 <= scale <= 1.06:
        raise ValueError(f"Unexpected scan horizontal scale on page {number}: {scale}")
    return {
        "sourcePdfPage": number, "officialPdfPage": number, "printedPage": str(number - 8),
        "method": method, "scanScaleX": round(scale, 9),
        "effectiveHorizontalBodyFontPt": round(font_pt * scale, 9),
        "sourceRunningHeadRule": sr, "officialRunningHeadRule": rr,
        "matchingProseGeometry": geometry,
    }


def verify_crop(page, clip, asset, diagram):
    with Image.open(asset) as image:
        actual = np.array(image.convert("RGB"))
        inferred_dpi = image.width / (clip[2] - clip[0]) * 72
    specified = diagram.get("dpi", diagram.get("renderDpi"))
    candidates = [int(specified)] if specified else []
    candidates += sorted({250, 288, 300, 360, 400, 600, round(inferred_dpi)}, key=lambda value: abs(value - inferred_dpi))
    for dpi in dict.fromkeys(candidates):
        if dpi < 250:
            continue
        # PDFBeads masked scans can cache a resampled image after the narrow
        # header calibration clip. A fresh document reproduces the canonical
        # translator's direct-from-PDF crop, without accepting an error bound.
        with pymupdf.open(page.parent.name) as original:
            pix = original[page.number].get_pixmap(dpi=dpi, colorspace=pymupdf.csRGB, alpha=False, clip=pymupdf.Rect(clip))
            expected = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
        if expected.shape == actual.shape and np.array_equal(expected, actual):
            return {"dpi": dpi, "widthPx": pix.width, "heightPx": pix.height, "sourcePixelMatch": True}
    raise ValueError(f"Crop pixels do not equal a >=250 dpi render of the recorded original clip: {asset}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--official-pdf", type=Path, default=DEFAULT_OFFICIAL)
    parser.add_argument("--allow-pending", action="store_true", help="Generate only verified existing reviews and list missing reviews explicitly")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "scripts/representation-theory-source-manifest.json").read_text("utf-8-sig"))
    original = Path(manifest["sourcePath"])
    if sha256(original) != manifest["sourceSha256"]:
        raise ValueError("Source PDF hash differs from the reviewed manifest")
    if sha256(args.official_pdf) != OFFICIAL_SHA:
        raise ValueError("Official calibration PDF changed; inspect and update evidence explicitly")
    reviews_dir = ROOT / "source/representation-theory/review"
    available = {int(p.stem.split("-")[1]): p for p in reviews_dir.glob("pdf-*.json")}
    pending = sorted(set(range(1, manifest["pdfPageCount"] + 1)) - available.keys())
    if pending and not args.allow_pending:
        raise ValueError(f"{len(pending)} primary review records are still missing; use --allow-pending during preparation")
    diagrams, calibrations = {}, {}
    with pymupdf.open(original) as scan, pymupdf.open(args.official_pdf) as official:
        if len(scan) != 238 or len(official) != 236:
            raise ValueError("The reviewed scan/official page pairing changed")
        font_pt, font_characters = body_font(official)
        # This viewed pair fixes the native body font and demonstrates scan
        # geometry even while no crop reviews have been delivered yet.
        calibrations["10"] = calibrate_page(10, scan, official, font_pt)
        for number, review_path in sorted(available.items()):
            review = json.loads(review_path.read_text("utf-8-sig"))
            if review["pdfPage"] != number:
                raise ValueError(f"Review filename/page mismatch: {review_path}")
            for diagram in review.get("diagrams", []):
                url, width, clip = diagram["path"], diagram["widthPt"], diagram["clipPt"]
                if not url.startswith(PREFIX) or url in diagrams or ".." in Path(url).parts:
                    raise ValueError(f"Unexpected or duplicate crop URL: {url}")
                if len(clip) != 4 or width <= 0 or abs(width - (clip[2] - clip[0])) > 0.02:
                    raise ValueError(f"Physical crop width mismatch: {url}")
                if clip[1] >= clip[3] or not scan[number - 1].rect.contains(pymupdf.Rect(clip)):
                    raise ValueError(f"Crop lies outside the original page: {url}")
                asset = ROOT / "docs/public" / url.lstrip("/")
                if sha256(asset) != diagram["sha256"]:
                    raise ValueError(f"Reviewed crop hash mismatch: {url}")
                if str(number) not in calibrations:
                    calibrations[str(number)] = calibrate_page(number, scan, official, font_pt)
                calibration = calibrations[str(number)]
                body_pt = calibration["effectiveHorizontalBodyFontPt"]
                diagrams[url] = {
                    "widthPt": width, "bodyFontPt": body_pt,
                    "widthEm": round(width / body_pt, 6), "scanScaleX": calibration["scanScaleX"],
                    "sourcePdfPage": number, "clipPt": clip, "sha256": diagram["sha256"],
                    "pixelVerification": verify_crop(scan[number - 1], clip, asset, diagram),
                }
    payload = {
        "sourceSha256": manifest["sourceSha256"], "sourcePdfPageCount": manifest["pdfPageCount"],
        "reviewRecordCount": len(available), "pendingReviewPages": pending,
        "completeReviewInventory": not pending,
        "bodyFontPt": font_pt,
        "bodyFontEvidence": {
            "officialUrl": OFFICIAL_URL, "officialSha256": OFFICIAL_SHA, "officialPdfPageCount": 236,
            "nativeFont": "CMR10", "nativeFontPdfPt": font_pt, "nativeFontTexPt": 10,
            "matchingSizeCharacterCount": font_characters,
            "sourcePagePairing": "Scan PDF 9–236 and author PDF 9–236 both carry printed pages 1–228; front matter differs.",
            "calibration": "Each crop width is divided by native CMR10 PDF pt multiplied by that scan page's measured horizontal scale. Synthetic OCR font sizes are never used.",
            "referencePairVisuallyViewed": ["source PDF page 10", "author PDF page 10"],
            "note": "Scan horizontal and vertical scales can differ; the horizontal scale controls image width in em.",
        },
        "pageCalibrations": calibrations, "diagramCount": len(diagrams), "diagrams": diagrams,
    }
    destination = ROOT / "scripts/representation-theory-diagram-widths.json"
    destination.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Prepared {len(diagrams)} verified crop widths; {len(calibrations)} measured scan pages; {len(pending)} missing reviews: {destination}")


if __name__ == "__main__":
    main()
