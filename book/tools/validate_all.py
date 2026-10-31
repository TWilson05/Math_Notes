"""Validate source-to-page coverage and full-edition PDF diagnostics."""
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / "book"


def main() -> None:
    coverage = json.loads((BOOK / "_build/migration-coverage.json").read_text(encoding="utf-8"))
    migrated = sum(len(v["original_files"]) for v in coverage.values()) + 6
    source_files = 6
    for root in (ROOT / "Sections").glob("*.tex"):
        if root.stem == "Differential_Calculus":
            continue
        child = ROOT / "Sections" / root.stem
        source_files += len(list(child.glob("*.tex"))) if child.is_dir() else 1
    assert migrated == source_files, f"Coverage mismatch: {migrated} mapped vs {source_files} source files"
    for item in coverage.values():
        for target in item["new_files"]:
            assert (ROOT / target).exists(), target
    pdf = BOOK / "_build/latex/mathematics-notes.pdf"
    info = subprocess.check_output(["pdfinfo", str(pdf)], encoding="utf-8", errors="replace")
    pages = int(re.search(r"Pages:\s+(\d+)", info)[1])
    log = pdf.with_suffix(".log").read_text(encoding="utf-8", errors="replace")
    fatal = [line for line in log.splitlines() if line.startswith("!")]
    assert not fatal, "Fatal PDF diagnostics: " + "; ".join(fatal[:5])
    report = {"source_tex_files_mapped": migrated, "source_tex_files_expected": source_files, "coverage_passed": True, "pdf_pages": pages, "fatal_pdf_diagnostics": fatal, "pdf_overfull_diagnostics": len(re.findall(r"Overfull", log)), "pdf_underfull_diagnostics": len(re.findall(r"Underfull", log))}
    (BOOK / "_build/full-validation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
