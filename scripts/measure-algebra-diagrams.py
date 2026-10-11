"""Recover original printed sizes of Algebra crops by matching source images.

PNG DPI metadata is not reliable: PyMuPDF Matrix renders can retain its 96 DPI
default regardless of their actual sampling density. This measurement manifest
uses source page pixels and the corresponding original PDF page geometry.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tmp/pdfs/algebra-export/deps"))
import cv2
import numpy as np
import pymupdf

cv2.setNumThreads(1)
SOURCE_PDF = Path("D:/Download/Algebra.pdf")
SOURCE_PAGES = ROOT / "tmp/pdfs/algebra/pages"
DEST = ROOT / "scripts/algebra-diagram-sizes.json"
SOURCE_DPI = 145.0
SAMPLING_CANDIDATES = [145.0, 288.0, 216.0, 432.0, 144.0, 300.0, 240.0, 200.0, 180.0, 192.0, 150.0, 96.0, 72.0]


def candidates():
    assets = {}
    for p in sorted((ROOT / "source/algebra/zh").glob("pdf-*.md")):
        for url in re.findall(r"!\[[^\]]*\]\((/library/volume-86/diagrams/[^)]+)\)", p.read_text(encoding="utf8")):
            asset = ROOT / "docs/public" / url.lstrip("/")
            assets[asset.name] = (int(p.stem.split("-")[1]), asset)
    assert len(assets) == 140, len(assets)
    return assets


def measure(job):
    name, source_page, path, page_width, page_height = job
    original = cv2.imread(str(SOURCE_PAGES / f"pdf-{source_page:04d}.png"), cv2.IMREAD_GRAYSCALE)
    crop = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    assert original is not None and crop is not None, name
    ch, cw = crop.shape
    oh, ow = original.shape
    assert float(np.std(crop)) > 1, f"Empty crop: {name}"
    scored = []
    dimensions_seen = set()

    def trial(dpi, broad):
        w = max(2, round(cw * SOURCE_DPI / dpi))
        h = max(2, round(ch * SOURCE_DPI / dpi))
        if w > ow or h > oh or (w, h) in dimensions_seen:
            return
        dimensions_seen.add((w, h))
        template = cv2.resize(crop, (w, h), interpolation=cv2.INTER_AREA if w < cw else cv2.INTER_LINEAR)
        response = cv2.matchTemplate(original, template, cv2.TM_CCOEFF_NORMED)
        _, score, _, location = cv2.minMaxLoc(response)
        scored.append({"dpi": dpi, "score": score, "x": location[0], "y": location[1], "w": w, "h": h, "broad": broad})

    for dpi in SAMPLING_CANDIDATES:
        trial(dpi, True)
    broad = sorted(scored, key=lambda r: r["score"], reverse=True)
    best_broad = broad[0]
    # Fine-search only uncertain matches; most crops were rendered at a small
    # set of fixed sampling densities. Pixel rounding can shift the optimum.
    if best_broad["score"] < .94:
        center = best_broad["dpi"]
        for fraction in [.98, .99, .995, 1.005, 1.01, 1.02]:
            trial(center * fraction, False)
    scored.sort(key=lambda r: r["score"], reverse=True)
    best = scored[0]
    physical_width = best["w"] / ow * page_width
    physical_height = best["h"] / oh * page_height
    result = {
        "sourcePdfPage": source_page,
        "widthPt": round(physical_width, 6),
        "heightPt": round(physical_height, 6),
        "dpi": round(best["dpi"], 6),
        "matchScore": round(best["score"], 6),
        "cropPixels": [cw, ch],
        "matchedSourcePixels": [best["x"], best["y"], best["w"], best["h"]],
        "sourcePagePixels": [ow, oh],
        "sourcePagePoints": [page_width, page_height],
        "runnerUpDensity": broad[1]["dpi"],
        "runnerUpScore": round(broad[1]["score"], 6),
        "assetSha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    return name, result


if __name__ == "__main__":
    pdf = pymupdf.open(SOURCE_PDF)
    assets = candidates()
    jobs = [(name, n, path, pdf[n - 1].rect.width, pdf[n - 1].rect.height) for name, (n, path) in assets.items()]
    output = {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for future in as_completed([pool.submit(measure, job) for job in jobs]):
            name, data = future.result()
            output[name] = data
            if len(output) % 10 == 0 or data["matchScore"] < .65:
                print(json.dumps({"done": len(output), "image": name, "dpi": data["dpi"], "score": data["matchScore"]}), flush=True)
    assert len(output) == 140
    assert all(v["matchScore"] >= .8 for v in output.values()), "Uncertain crop matches require visual investigation before saving sizes"
    manifest = {
        "method": "Multiscale normalized template correlation against the original 145 DPI page renders; physical dimensions derive from original PDF page geometry, not PNG metadata.",
        "sourceSha256": hashlib.sha256(SOURCE_PDF.read_bytes()).hexdigest(),
        "sourceRenderDpi": SOURCE_DPI,
        "opencvVersion": cv2.__version__,
        "images": dict(sorted(output.items())),
    }
    DEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    print(json.dumps({"saved": str(DEST), "images": len(output), "densities": dict(Counter(str(v["dpi"]) for v in output.values())), "lowestScores": sorted([(n, v["matchScore"], v["dpi"]) for n, v in output.items()], key=lambda r: r[1])[:15]}), flush=True)
