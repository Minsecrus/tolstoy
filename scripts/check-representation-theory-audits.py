"""Check saved review coverage and bind it to current files; never infer visual review."""
import argparse
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BOOK = ROOT / "source" / "representation-theory"
COUNT = json.loads((ROOT / "scripts/representation-theory-source-manifest.json").read_text(encoding="utf8"))["pdfPageCount"]
VERIFIED_STATUSES = {"verified", "complete", "verified_with_source_correction_note",
                     "verified-after-correction"}
IMAGE_FLAGS = ("originalImageViewed", "originalViewed", "visualReviewed")
ENGLISH_FLAGS = ("englishCompared", "englishComparedInFull", "englishFullyRead")
CHINESE_FLAGS = ("chineseCompared", "chineseComparedInFull", "chineseFullyRead")
FORMULA_FLAGS = ("formulaAndHypothesesChecked", "allFormulasProofsAndExerciseConditionsChecked",
                 "formulaChecked", "formulasAndConditionsChecked")
INCOMPLETE_FIELDS = ("unresolved", "unresolvedFindings", "unreviewed", "unreviewedPages",
                     "doubtfulReadings", "pendingVisibleNotes")


def ranges(numbers):
    result = []
    for value in sorted(numbers):
        if result and result[-1][1] + 1 == value:
            result[-1][1] = value
        else:
            result.append([value, value])
    return [str(a) if a == b else f"{a}-{b}" for a, b in result]


def digest(page, language):
    path = BOOK / language / f"pdf-{page:04d}.md"
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def page_number(record):
    value = record.get("pdfPage", record.get("page"))
    return value if type(value) is int and 1 <= value <= COUNT else None


def hashes(record):
    result = {}
    for language, keys in {"en": ("enSha256", "englishSha256"),
                           "zh": ("zhSha256", "chineseSha256")}.items():
        for key in keys:
            if key in record:
                result.setdefault(language, []).append(record[key])
        nested = record.get("sourceSha256")
        if isinstance(nested, dict) and language in nested:
            result.setdefault(language, []).append(nested[language])
    return result


def unfinished(record):
    return (any(record.get(key) for key in INCOMPLETE_FIELDS)
            or ("complete" in record and record["complete"] is not True)
            or any(key in record and not verified_status(record[key])
                   for key in ("status", "reviewStatus")))


def verified_status(value):
    return isinstance(value, str) and value in VERIFIED_STATUSES


def negative_flags(record):
    return any(key in record and record[key] is not True
               for key in IMAGE_FLAGS + ENGLISH_FLAGS + CHINESE_FLAGS + FORMULA_FLAGS)


def nonempty_scope(value):
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return any(nonempty_scope(item) for item in value)
    if isinstance(value, dict):
        return any(nonempty_scope(item) for item in value.values())
    return False


def affirmative(record, keys):
    return any(record.get(key) is True for key in keys)


def reviewed(record):
    if unfinished(record):
        return False
    # Explicit negative or malformed flags override a completed status.
    if negative_flags(record):
        return False
    full_comparison = (affirmative(record, IMAGE_FLAGS) and affirmative(record, ENGLISH_FLAGS)
                       and affirmative(record, CHINESE_FLAGS))
    scope = any(nonempty_scope(record.get(key)) for key in
                ("scope", "actualReviewScope", "contentCompared"))
    # A status label alone cannot claim a person's full-page comparison.
    # Require explicit original-image, English, Chinese and math-condition
    # review, with a concrete record of what was actually checked.
    return scope and full_comparison and affirmative(record, FORMULA_FLAGS)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-complete", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    visual, bound, primary = set(), set(), set()
    stale, invalid, pending = [], [], []
    ledgers = []
    for path in sorted(BOOK.glob("math-audit*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, ValueError) as error:
            invalid.append(f"{path.name}: {error}")
            continue
        if not isinstance(data, dict):
            invalid.append(f"{path.name}: ledger must be an object")
            continue
        complete_status = (data.get("status") == "complete" if "status" in data
                           else data.get("complete") is True)
        if not complete_status or unfinished(data):
            pending.append(path.name)
            continue
        records = []
        for key in ("pages", "pageChecks", "auditedPages", "sourceSnapshots"):
            rows = data.get(key, [])
            if not isinstance(rows, list):
                invalid.append(f"{path.name}: {key} must be an array")
                continue
            for record in rows:
                # A list of audited page numbers is coverage metadata, not a
                # substitute for a pagewise personal review record.
                if key == "auditedPages" and type(record) is int:
                    continue
                if not isinstance(record, dict):
                    invalid.append(f"{path.name}: {key} entry must be an object")
                    continue
                records.append((key, record))
        page_checks, snapshots, blocked = {}, {}, set()
        for key, record in records:
            page = page_number(record)
            if page is None:
                invalid.append(f"{path.name}: invalid page number in record")
                continue
            if unfinished(record) or negative_flags(record):
                blocked.add(page)
                continue
            if reviewed(record):
                page_checks[page] = record
            # Separate sourceSnapshots records bind the same ledger's genuine
            # page checks. Other records without a review claim cannot supply
            # hashes for an unchecked revision.
            if reviewed(record) or key == "sourceSnapshots":
                saved = snapshots.setdefault(page, {})
                for language, values in hashes(record).items():
                    saved.setdefault(language, []).extend(values)
        valid, current = set(), set()
        for page in page_checks:
            if page in blocked:
                continue
            valid.add(page)
            saved = snapshots.get(page, {})
            matches = set(saved) == {"en", "zh"}
            for language, values in saved.items():
                if any(not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{64}", sha)
                       for sha in values):
                    invalid.append(f"{path.name} page {page} {language}: invalid SHA256")
                    matches = False
                elif len(set(values)) != 1:
                    invalid.append(f"{path.name} page {page} {language}: conflicting SHA256 values")
                    matches = False
                elif digest(page, language) != values[0]:
                    stale.append(f"{path.name} page {page} {language}")
                    matches = False
            if matches:
                current.add(page)
        visual.update(valid)
        bound.update(current)
        ledgers.append({"file": path.name, "reviewedPages": len(valid), "currentSnapshotPages": len(current)})
    for page in range(1, COUNT + 1):
        path = BOOK / "review" / f"pdf-{page:04d}.json"
        if not path.is_file():
            continue
        try:
            record = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, ValueError) as error:
            invalid.append(f"{path.name}: {error}")
            continue
        if not isinstance(record, dict):
            invalid.append(f"{path.name}: primary review must be an object")
            continue
        saved = hashes(record)
        current_hashes = (set(saved) == {"en", "zh"} and all(
            values and all(value == digest(page, language) for value in values)
            for language, values in saved.items()))
        if (page_number(record) == page and not unfinished(record) and current_hashes
                and all(record.get(k) is True for k in
                        ("visualReviewed", "englishTranscribed", "chineseTranslated", "formulaChecked"))
                and all(digest(page, language) for language in ("en", "zh"))):
            primary.add(page)
    complete = len(primary) == len(bound) == COUNT and not invalid
    report = {"pdfPageCount": COUNT, "primaryCompletePages": len(primary),
              "independentReviewedPages": len(visual), "currentSnapshotReviewedPages": len(bound),
              "primaryMissing": ranges(set(range(1, COUNT + 1)) - primary),
              "reviewMissing": ranges(set(range(1, COUNT + 1)) - visual),
              "currentSnapshotMissing": ranges(set(range(1, COUNT + 1)) - bound),
              "currentSnapshotPages": sorted(bound), "primaryCompletePageNumbers": sorted(primary),
              "staleSnapshots": stale, "invalidRecords": invalid, "pendingLedgers": pending,
              "ledgers": ledgers, "complete": complete,
              "limitation": "Validates recorded review coverage and file hashes; does not perform OCR or prove mathematical correctness."}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Primary complete: {len(primary)}/{COUNT}; recorded independent review: {len(visual)}/{COUNT}; current audited snapshots: {len(bound)}/{COUNT}.")
        print("Missing current audited snapshots: " + (", ".join(report["currentSnapshotMissing"]) or "none"))
        for issue in stale + invalid:
            print(issue)
        print(report["limitation"])
    if invalid or (args.require_complete and not complete):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
