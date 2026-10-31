# Repository conventions for coding agents

- Read [MIGRATION_PLAN.md](MIGRATION_PLAN.md), [STYLE_GUIDE.md](STYLE_GUIDE.md), and [MIGRATION_CHECKLIST.md](MIGRATION_CHECKLIST.md) before editing migrated textbook content.
- Preserve every original file in `Sections/`, `Images/`, `MathNotes.tex`, and `fizztex.sty`. Do not silently correct, omit, or rewrite mathematics during structural migration.
- Treat `book/` as the active Sphinx/MyST publishing tree. Keep generated files under `book/_build/` or `book/figures/generated/`; do not commit build products.
- Use standard Sphinx/MyST and `sphinx-proof` features before proposing a custom extension. Keep browser macros centralized in `book/_static/mathjax-macros.json` and compare them with the native PDF.
- Every migrated page must include a traceability comment pointing to its original TeX source. Every public figure requires a manifest record, provenance, alt text and review status.
- Run HTML and PDF builds with warnings as errors and run the validation checks before reporting completion. Investigate warnings rather than adding broad suppressions.
- Do not publish or modify GitHub Pages deployment configuration without explicit review of the existing workflow and content clearance.
