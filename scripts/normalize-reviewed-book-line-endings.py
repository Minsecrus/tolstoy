#!/usr/bin/env python3
"""Normalize reviewed manuscripts to LF without changing their logical UTF-8 text.

Dry run is the default. --apply requires current primary AND independent review
bindings for every page before any write. This is a byte migration, not a new
claim of mathematical or visual review. Historical before-hashes are preserved
in line-ending-normalization.json. Output PDFs and reading bodies are untouched.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
BOOKS = ("category-theory", "representation-theory")
DIRECT_HASHES = {"en": ("enSha256", "englishSha256"),
                 "zh": ("zhSha256", "chineseSha256")}
NESTED_HASHES = ("markdownSha256", "sourceSha256", "sourceHashes", "sha256", "snapshots")
INCOMPLETE = ("unresolved", "unresolvedFindings", "unreviewed", "unreviewedPages",
              "doubtfulReadings", "pendingVisibleNotes")
VERIFIED = {"verified", "complete", "verified_with_source_correction_note",
            "verified-after-correction"}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encode_json(data: object) -> bytes:
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def logical_text(data: bytes) -> str:
    """Only CRLF is normalized; lone CR is not accepted or silently changed."""
    text = data.decode("utf-8", errors="strict")
    if "\r" in text.replace("\r\n", ""):
        raise ValueError("lone CR found; only a CRLF-to-LF migration is supported")
    return text.replace("\r\n", "\n")


def objects(value: object, pointer: str = ""):
    if isinstance(value, dict):
        yield pointer, value
        for key, child in value.items():
            yield from objects(child, pointer + "/" + str(key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from objects(child, pointer + "/" + str(index))


def hash_slots(record: dict):
    """Yield only explicitly typed manuscript-language hash fields."""
    for language, names in DIRECT_HASHES.items():
        for name in names:
            if name in record:
                yield language, record, name, name
    for name in NESTED_HASHES:
        nested = record.get(name)
        if isinstance(nested, dict):
            for language in ("en", "zh"):
                if language in nested:
                    yield language, nested, language, name + "/" + language


class MigrationError(ValueError):
    pass


class Plan:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.original: dict[Path, bytes] = {}
        self.json_docs: dict[Path, object] = {}
        self.writes: dict[Path, bytes] = {}
        self.books: list[dict] = []
        self.hash_updates: list[dict] = []
        self.blockers: list[str] = []

    def relative(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def read(self, path: Path) -> bytes:
        if path not in self.original:
            self.original[path] = path.read_bytes()
        return self.original[path]

    def document(self, path: Path):
        if path not in self.json_docs:
            self.json_docs[path] = json.loads(self.read(path).decode("utf-8-sig"))
        return self.json_docs[path]

    def prospective(self, path: Path) -> bytes:
        if path in self.writes:
            return self.writes[path]
        if path in self.json_docs:
            value = self.json_docs[path]
            # Avoid serializing untouched JSON just to alter its newline style.
            if value != json.loads(self.read(path).decode("utf-8-sig")):
                return encode_json(value)
        return self.read(path)


def preflight_checker(plan: Plan, book: str) -> dict:
    checker = plan.root / "scripts" / f"check-{book}-audits.py"
    result = subprocess.run([sys.executable, str(checker), "--require-complete", "--json"],
                            cwd=plan.root, capture_output=True, encoding="utf-8",
                            env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    try:
        report = json.loads(result.stdout)
    except ValueError:
        raise MigrationError(f"{book}: audit checker returned no valid JSON: {result.stderr[:500]}")
    if result.returncode or not report.get("complete"):
        plan.blockers.append(f"{book}: independent review is incomplete or stale; "
                             f"current={report.get('currentSnapshotReviewedPages')}/"
                             f"{report.get('pdfPageCount')}; "
                             f"missing={report.get('currentSnapshotMissing')}; "
                             f"stale={report.get('staleSnapshots')}; "
                             f"invalid={report.get('invalidRecords')}")
    return report


def prepare_book(plan: Plan, book: str) -> None:
    directory = plan.root / "source" / book
    manifest = plan.document(plan.root / "scripts" / f"{book}-source-manifest.json")
    count = manifest["pdfPageCount"]
    # Freeze the same JSON evidence that the checker will inspect. If any
    # reviewer updates it during the preflight, apply's concurrency check fails.
    for path in sorted(directory.rglob("*.json")):
        if path.name != "line-ending-normalization.json":
            plan.document(path)
    checker = preflight_checker(plan, book)
    bodies, changes = {}, []
    for page in range(1, count + 1):
        for language in ("en", "zh"):
            path = directory / language / f"pdf-{page:04d}.md"
            before = plan.read(path)
            normalized = before.replace(b"\r\n", b"\n")
            text_before, text_after = logical_text(before), logical_text(normalized)
            if text_before != text_after or text_after.encode("utf-8") != normalized:
                raise MigrationError(f"{plan.relative(path)}: logical UTF-8 text changed")
            bodies[(page, language)] = (path, before, normalized)
            if normalized != before:
                changes.append({"pdfPage": page, "language": language,
                                "path": plan.relative(path), "beforeSha256": sha(before),
                                "afterSha256": sha(normalized),
                                "crlfPairsRemoved": before.count(b"\r\n"),
                                "beforeByteCount": len(before), "afterByteCount": len(normalized),
                                "logicalUtf8CharacterCount": len(text_after),
                                "actualTextCharactersUnchanged": True,
                                "logicalUtf8TextUnchanged": True})
                plan.writes[path] = normalized

    # Preflight every primary, including pages that already use LF. Some legacy
    # audit checkers validate primary flags without checking primary hashes.
    for page in range(1, count + 1):
        path = directory / "review" / f"pdf-{page:04d}.json"
        record = plan.document(path)
        if (record.get("pdfPage", record.get("page")) != page or
                any(record.get(key) for key in INCOMPLETE) or
                ("complete" in record and record["complete"] is not True) or
                any(key in record and record[key] not in VERIFIED
                    for key in ("status", "reviewStatus")) or
                any(record.get(key) is not True for key in
                    ("visualReviewed", "englishTranscribed", "chineseTranslated", "formulaChecked"))):
            plan.blockers.append(f"{plan.relative(path)}: primary review is incomplete")
        slots = list(hash_slots(record))
        if {language for language, _, _, _ in slots} != {"en", "zh"}:
            plan.blockers.append(f"{plan.relative(path)}: primary lacks both manuscript hashes")
        for language, holder, key, _ in slots:
            if holder[key] != sha(bodies[(page, language)][1]):
                plan.blockers.append(f"{plan.relative(path)}: stale primary {language} SHA256")

    # Read all book JSON, including optional progress/publication records. Only
    # the migration history is excluded: its before-hashes are immutable history.
    export_path = plan.root / "tmp" / "pdfs" / f"{book}-export" / "export-source-check.json"
    snapshot = plan.document(export_path) if export_path.exists() else None
    if snapshot is not None:
        saved_bodies = copy.deepcopy(snapshot.get("readingBodies"))
        for number, bound in snapshot.get("sourceHashes", {}).items():
            page = int(number)
            if (page, "zh") not in bodies or bound != sha(bodies[(page, "zh")][1]):
                plan.blockers.append(f"{plan.relative(export_path)}: stale exported source page {page}")
                continue
            after = sha(bodies[(page, "zh")][2])
            if bound != after:
                snapshot["sourceHashes"][number] = after
                plan.hash_updates.append({"path": plan.relative(export_path),
                                          "pointer": f"/sourceHashes/{number}",
                                          "pdfPage": page, "language": "zh",
                                          "beforeSha256": bound, "afterSha256": after})
        if snapshot.get("readingBodies") != saved_bodies:
            raise MigrationError("export readingBodies must be preserved exactly")

    changed_old = {row["beforeSha256"] for row in changes}
    for path, document in list(plan.json_docs.items()):
        if path.parent != directory and directory not in path.parents:
            continue
        for pointer, record in objects(document):
            slots = list(hash_slots(record))
            if not slots:
                continue
            page = record.get("pdfPage", record.get("page"))
            if type(page) is not int or not 1 <= page <= count:
                raise MigrationError(f"{plan.relative(path)}{pointer}: manuscript hash without valid page")
            for language, holder, key, suffix in slots:
                _, before, after = bodies[(page, language)]
                if holder[key] != sha(before):
                    plan.blockers.append(f"{plan.relative(path)}{pointer}: stale {language} manuscript SHA256")
                    continue
                if before != after:
                    plan.hash_updates.append({"path": plan.relative(path), "pointer": pointer + "/" + suffix,
                                              "pdfPage": page, "language": language,
                                              "beforeSha256": holder[key], "afterSha256": sha(after)})
                    holder[key] = sha(after)

    pdf_name = {"category-theory": "Basic-Category-Theory-Zh.pdf",
                "representation-theory": "Introduction-to-Representation-Theory-Zh.pdf"}[book]
    pdf = plan.root / "output" / "pdf" / pdf_name
    pdf_hash = sha(plan.read(pdf)) if pdf.exists() else None
    plan.books.append({"book": book, "pageCount": count, "manuscriptCount": count * 2,
                       "crlfManuscripts": len(changes), "changes": changes,
                       "primaryBindingsPreflighted": count,
                       "independentCurrentPages": checker.get("currentSnapshotReviewedPages"),
                       "existingOutputPdfSha256": pdf_hash, "outputPdfRewritten": False,
                       "exportSnapshotPresent": snapshot is not None,
                       "exportReadingBodiesUnchanged": True,
                       "inspectedBookJsonFiles": sum(directory in p.parents for p in plan.json_docs),
                       "changedOldHashes": changed_old})


def refresh_file_bindings(plan: Plan) -> None:
    """Refresh explicitly path-bound whole-file hashes, never global SHA strings."""
    bindings = []
    for path, document in plan.json_docs.items():
        for pointer, record in objects(document):
            if not isinstance(record.get("path"), str) or not isinstance(record.get("sha256"), str):
                continue
            relative = record["path"].replace("\\", "/")
            target = (plan.root / relative).resolve()
            if not target.is_relative_to(plan.root):
                continue
            if target in plan.writes or target in plan.json_docs:
                original = plan.read(target)
                if record["sha256"] != sha(original):
                    plan.blockers.append(f"{plan.relative(path)}{pointer}: stale path-bound file SHA256 for {relative}")
                    continue
                bindings.append((path, pointer, record, target, record["sha256"]))
    # Whole-file bindings may refer to other modified JSON. Resolve this graph
    # until stable; cyclic self-digests are rejected instead of silently forged.
    for _ in range(len(bindings) + 2):
        changed = False
        for _, _, record, target, _ in bindings:
            current = sha(plan.prospective(target))
            if record["sha256"] != current:
                record["sha256"] = current
                changed = True
        if not changed:
            break
    else:
        raise MigrationError("whole-file SHA256 dependency cycle; cannot normalize safely")
    for path, pointer, record, target, original_hash in bindings:
        if record["sha256"] != original_hash:
            plan.hash_updates.append({"path": plan.relative(path), "pointer": pointer + "/sha256",
                                      "boundFile": plan.relative(target),
                                      "beforeSha256": original_hash, "afterSha256": record["sha256"]})


def finalize_plan(plan: Plan) -> None:
    refresh_file_bindings(plan)
    for path, document in plan.json_docs.items():
        if document != json.loads(plan.read(path).decode("utf-8-sig")):
            plan.writes[path] = encode_json(document)
    # If a changed body hash survives in an unrecognized schema, stop and report
    # its exact location. History is excluded; no unrelated image/PDF hashes are
    # searched-and-replaced merely because a hexadecimal string looks alike.
    for book in plan.books:
        directory = plan.root / "source" / book["book"]
        for path, document in plan.json_docs.items():
            if directory not in path.parents:
                continue
            def inspect(value, pointer=""):
                if isinstance(value, dict):
                    for key, child in value.items():
                        inspect(child, pointer + "/" + str(key))
                elif isinstance(value, list):
                    for index, child in enumerate(value):
                        inspect(child, pointer + "/" + str(index))
                elif isinstance(value, str) and any(
                        digest in book["changedOldHashes"]
                        for digest in re.findall(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", value)):
                    plan.blockers.append(f"{plan.relative(path)}{pointer}: unrecognized stale body-hash reference")
            inspect(document)
        if not book["changes"]:
            continue
        updates = [row for row in plan.hash_updates if row["path"].startswith(f"source/{book['book']}/")
                   or row["path"].startswith(f"tmp/pdfs/{book['book']}-export/")]
        event = {"operation": "CRLF_to_LF_only", "pageLanguageChanges": book["changes"],
                 "hashReferenceUpdates": updates, "actualTextCharactersUnchanged": True,
                 "textEqualityDefinition": "Strict UTF-8 strings are exactly equal after replacing only CRLF with LF; lone CR is rejected.",
                 "primaryAndIndependentBindingsCurrentBeforeMigration": not plan.blockers,
                 "allPagePrimaryBindingsChecked": book["pageCount"],
                 "allPageIndependentBindingsChecked": book["independentCurrentPages"],
                 "independentContentReviewRetained": True,
                 "reviewScope": "Existing recorded content reviews remain valid because only line-ending bytes change; this migration performs no new visual or mathematical review.",
                 "outputPdfSha256BeforeAndAfter": book["existingOutputPdfSha256"],
                 "outputPdfRewritten": False, "exportReadingBodiesUnchanged": True}
        event["migrationId"] = sha(json.dumps(event, ensure_ascii=False, sort_keys=True,
                                             separators=(",", ":")).encode("utf-8"))
        path = directory / "line-ending-normalization.json"
        history = json.loads(plan.read(path).decode("utf-8-sig")) if path.exists() else {"version": 1, "book": book["book"], "events": []}
        if history.get("version") != 1 or history.get("book") != book["book"] or not isinstance(history.get("events"), list):
            raise MigrationError(f"{plan.relative(path)}: invalid migration history")
        if not any(row.get("migrationId") == event["migrationId"] for row in history["events"]):
            history["events"].append(event)
        plan.writes[path] = encode_json(history)


def apply(plan: Plan) -> None:
    if plan.blockers:
        raise MigrationError("preflight failed; --apply refuses all writes")
    lock = plan.root / "source" / ".reviewed-book-line-endings.lock"
    written, temporary_files = [], []
    with lock.open("xb") as stream:
        stream.write(b"normalize-reviewed-book-line-endings.py\n")
    try:
        # Optimistic concurrency check covers all preflight evidence, not only
        # the manuscripts that will change. Root must finish reviews first.
        for path, original in plan.original.items():
            if path.read_bytes() != original:
                raise MigrationError(f"{plan.relative(path)} changed after preflight; aborting")
        for path, data in sorted(plan.writes.items(), key=lambda item: str(item[0])):
            expected = plan.original.get(path)
            if (expected is None and path.exists()) or (expected is not None and path.read_bytes() != expected):
                raise MigrationError(f"{plan.relative(path)} changed concurrently; aborting")
            temporary = path.with_name(path.name + ".normalization-tmp")
            with temporary.open("xb") as stream:
                temporary_files.append(temporary)
                stream.write(data)
            os.replace(temporary, path)
            written.append(path)
        for path, expected in plan.writes.items():
            if path.read_bytes() != expected:
                raise MigrationError(f"{plan.relative(path)}: post-write byte verification failed")
        for book in plan.books:
            for change in book["changes"]:
                path = plan.root / change["path"]
                if logical_text(plan.original[path]) != logical_text(path.read_bytes()):
                    raise MigrationError(f"{change['path']}: post-write logical text verification failed")
            if book["existingOutputPdfSha256"]:
                pdf_paths = [path for path in plan.original if path.parent == plan.root / 'output' / 'pdf'
                             and sha(plan.original[path]) == book["existingOutputPdfSha256"]]
                if any(sha(path.read_bytes()) != book["existingOutputPdfSha256"] for path in pdf_paths):
                    raise MigrationError("protected output PDF changed concurrently")
    except BaseException:
        for path in reversed(written):
            if path in plan.original:
                path.write_bytes(plan.original[path])
            else:
                path.unlink()
        raise
    finally:
        for temporary in temporary_files:
            if temporary.exists():
                temporary.unlink()
        lock.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", action="append", choices=BOOKS,
                        help="Repeat to select books; defaults to both.")
    parser.add_argument("--apply", action="store_true", help="Apply only after all preflight checks pass.")
    parser.add_argument("--json", action="store_true", help="Print the complete deterministic migration plan.")
    args = parser.parse_args()
    plan = Plan(ROOT)
    try:
        for book in dict.fromkeys(args.book or BOOKS):
            prepare_book(plan, book)
        finalize_plan(plan)
        report = {"mode": "apply" if args.apply else "dry-run", "safeToApply": not plan.blockers,
                  "books": [{k: v for k, v in book.items() if k != "changedOldHashes"} for book in plan.books],
                  "plannedFileWrites": sorted(plan.relative(path) for path in plan.writes),
                  "hashReferenceUpdateCount": len(plan.hash_updates), "blockers": plan.blockers}
        if args.apply:
            apply(plan)
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            for book in plan.books:
                print(f"{book['book']}: {book['crlfManuscripts']}/{book['manuscriptCount']} manuscripts "
                      f"need CRLF -> LF; primary={book['primaryBindingsPreflighted']}/{book['pageCount']}; "
                      f"independent current={book['independentCurrentPages']}/{book['pageCount']}.")
            print(f"{report['mode']}: {len(plan.writes)} planned files, {len(plan.hash_updates)} explicit hash references; "
                  f"safeToApply={report['safeToApply']}; PDFs and readingBodies preserved.")
            for blocker in plan.blockers:
                print("BLOCKED: " + blocker)
        return 1 if plan.blockers else 0
    except (OSError, ValueError, KeyError) as error:
        print("Normalization refused: " + str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
