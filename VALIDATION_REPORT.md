# Full textbook validation report

Validation date: 2026-10-30. This report covers the complete local build after migrating all remaining course content into the established Sphinx/MyST tree. No deployment or merge was performed.

## Automated results

- **Courses:** 16 top-level chapters in the generated edition: the completed Differential Calculus chapter plus 15 remaining source groups, including Bibliography.
- **Source coverage:** 68 content TeX files mapped to 68 expected migrated content files. Root wrapper files are represented by chapter `index.md` files; original wrappers remain under `Sections/`.
- **HTML:** Sphinx 8.1.3 build completed with `-W --keep-going`; 88 generated HTML pages were produced.
- **Links/assets:** 11,854 local links and assets passed `book/tools/validate_book.py`.
- **PDF:** Sphinx LaTeX plus `latexmk` generated [mathematics-notes.pdf](book/_build/latex/mathematics-notes.pdf), 546 pages, 7.6 MB.
- **Fatal diagnostics:** No fatal TeX diagnostics, undefined-control-sequence errors, or missing-character errors remain in the final PDF log.
- **Figures:** All referenced raster figures were copied into the publishing asset tree with deterministic, space-free paths. The deterministic TikZ/PGFPlots workflow example builds to SVG and PDF.
- **Original preservation:** No files under `Sections/`, `Images/`, `MathNotes.tex`, or `fizztex.sty` were overwritten.

Re-run the checks from the repository root:

```powershell
python book/tools/convert_differential.py
python book/tools/migrate_remaining.py
prototypes/.venv/Scripts/python -m sphinx -W --keep-going -b html book book/_build/html
prototypes/.venv/Scripts/python book/tools/validate_book.py
prototypes/.venv/Scripts/python -m sphinx -W --keep-going -b latex book book/_build/latex
Push-Location book/_build/latex
latexmk -pdf -interaction=nonstopmode -halt-on-error mathematics-notes.tex
Pop-Location
prototypes/.venv/Scripts/python book/tools/validate_all.py
```

## Manual review still required

- The PDF log contains 27 overfull and 18 underfull box diagnostics. They are concentrated in Complex Analysis, ODEs, Introductory Logic, and dense figure/equation pages. The PDF is generated successfully, but these pages need visual typography review before publication.
- TikZ, Venn diagram, `tcolorbox`, matrix, and `polylongdiv` constructs are explicitly listed in [MIGRATION_STATUS.md](MIGRATION_STATUS.md). TikZ/Venn source is preserved and flagged rather than silently discarded; native vector conversion and accessibility descriptions remain course-level editorial work.
- Fixed-width logic tables and other `tabular` blocks are preserved as LaTeX review blocks where a responsive semantic table conversion was not reliable. They need visual and accessibility review in HTML and PDF.
- Raster figure provenance is uncertain for the existing collection. The copied assets are local build inputs only; each needs a manifest record with source, license/permission, attribution, alt text, reviewer and approval before publication.
- The source contains limited labels/references and no complete citation graph. Existing references were not invented. Semantic theorem labels, cross-course references, and bibliography integration remain editorial work.
- Browser MathJax checks and representative page screenshots should be repeated on the complete site before release. Automated HTML parsing confirms assets and links; it does not certify mathematical correctness, accessibility, or figure meaning.

The complete edition is buildable and structurally covered, but it is not publication-ready until the manual figure, typography, accessibility, and mathematical review items above are closed.
