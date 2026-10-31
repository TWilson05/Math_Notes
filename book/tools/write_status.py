"""Write the course migration inventory from the generated coverage data."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    coverage = json.loads((ROOT / "book/_build/migration-coverage.json").read_text(encoding="utf-8"))
    rows = ["# Migration status", "", "Generated from the source hierarchy and structural migration inventory. The original LaTeX under `Sections/` is retained unchanged.", "", "| Course | Original files | Migrated pages | Status | Unsupported/manual review |", "|---|---:|---:|---|---|"]
    for name, item in coverage.items():
        review = "; ".join(item["special_constructs"]) or "None detected by inventory"
        rows.append(f"| {item['title']} (`{name}`) | {len(item['original_files'])} | {len(item['new_files'])} | {item['status']} | {review} |")
    rows += ["", "## Explicit limitations and omissions", "", "- The migration is structural: source prose, equations, lists, images, and source hierarchy are retained, but many original theorem/proof labels did not exist and therefore cannot be reconstructed automatically.", "- TikZ, Venn diagram, and other native drawing environments are preserved as reviewed LaTeX source blocks rather than silently discarded. They need per-figure SVG/PDF conversion and accessibility text before publication.", "- `polylongdiv` is preserved and flagged for a dedicated rendering decision.", "- Tables using fixed-width `tabular` layout are preserved as LaTeX review blocks where a reliable responsive table conversion was not possible.", "- Figures copied under `book/figures/original/` retain uncertain provenance. They are local build assets only until the manifest records permission, attribution, and approval.", "- The native PDF builds, but its log contains overfull/underfull box warnings. These are typography review items, especially in Complex Analysis, Introductory Logic, ODEs, and figure-heavy chapters.", "- Original source files contain no comprehensive label/reference system. Existing references were not invented; future semantic labels should be added during editorial review.", "", "## Validation per course", "", "HTML and source-coverage checks are automated in `book/tools/validate_book.py` and `book/tools/migrate_remaining.py`. PDF validation is complete for the full generated edition; individual course typography still requires visual review of representative pages.", ""]
    (ROOT / "MIGRATION_STATUS.md").write_text("\n".join(rows), encoding="utf-8")


if __name__ == "__main__":
    main()
