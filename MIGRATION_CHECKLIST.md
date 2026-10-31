# Course migration checklist

Copy this checklist into the migration issue for each course.

- [ ] Confirm the course and every imported source file; include orphaned files in the coverage ledger.
- [ ] Record original file paths and source hashes before conversion.
- [ ] Inventory custom commands, packages, theorem/proof environments, labels, references, tables and figures.
- [ ] Choose page boundaries that preserve the original logical order.
- [ ] Convert headings, lists, displays and figures without changing equation bodies.
- [ ] Add semantic theorem/example/proof directives and durable labels where the original has none.
- [ ] Add all required browser macros to `book/_static/mathjax-macros.json` and test empty/optional arguments.
- [ ] Record every figure in `book/figures/manifest.json`; clear provenance, caption and alt text before publication.
- [ ] Generate deterministic SVG/PDF assets from source and keep source beside them.
- [ ] Compare source and migrated page-by-page for text, equations, proofs, exercises, tables and figure count.
- [ ] Build HTML with `-W --keep-going`; fix warnings instead of suppressing them.
- [ ] Build the Sphinx LaTeX output with `latexmk`; inspect log for undefined commands, missing characters and overfull boxes.
- [ ] Validate local links, anchors, assets, MathJax error nodes and source hashes.
- [ ] Review sidebar nesting, search results, mobile width, captions and keyboard navigation.
- [ ] Review rendered PDF pages containing long equations, tables, theorem boxes and figures.
- [ ] Update `MIGRATION_PLAN.md`, the coverage ledger and this checklist with known limitations.
- [ ] Obtain user review before enabling deployment for the migrated course.
