# Mathematics Notes style guide

This guide applies to migrated chapters in `book/`. Original TeX in `Sections/` remains the comparison source and is not reformatted by migration tools.

## Document structure

- `book/index.md` is the textbook home page.
- Each course is one top-level chapter directory with an `index.md` and one MyST page per substantial topic.
- Use one H1 per page, H2 for the topic headings that correspond to original `\subsubsection` headings, and H3 only for an internal subdivision.
- Every migrated page begins with an HTML comment linking its original TeX source.

## Mathematical content

Keep mathematical expressions and command names unchanged wherever the shared MathJax macro map supports them. Use `$$` with `aligned` for multi-line derivations; use a labelled `{math}` directive when a displayed equation is referenced. Do not alter a proof or intermediate equation during structural conversion. Suspected mathematical errors become editorial issues for review.

Use durable semantic labels such as `diff-mean-value-theorem`, not labels based on page numbers. Cross-reference equations, figures and theorem objects with MyST roles. Never rely on visible numbering alone.

## Environments

Use `sphinx-proof` directives for `{prf:definition}`, `{prf:theorem}`, `{prf:lemma}`, `{prf:proposition}`, `{prf:corollary}`, `{prf:example}`, `{prf:remark}`, and `{prf:proof}`. Keep proof text visually quiet: a light border, readable line length and no saturated color. Use ordinary paragraphs for explanations and exercises unless they need a numbered semantic object.

## Figures and tables

Use a `{figure}` directive with a descriptive `:alt:` and a sentence-case caption. Default width is 85%; use 55–95% only when the source aspect ratio or labels require it. Reference figures by label. Keep source files in `book/figures/sources/` and generated SVG/PDF files in `book/figures/generated/`; record provenance in `book/figures/manifest.json` before publication.

Use Markdown tables for actual data with a header row. Use a MathJax `array` only for mathematical layout or small sign charts. Wide tables must remain readable on a narrow viewport; do not turn equations into HTML tables.

## PDF and web presentation

Use restrained blue-gray accents, a readable 55–60rem text measure, and horizontal scrolling for genuinely wide mathematics. The Sphinx Book Theme supplies navigation and search. The PDF is generated through Sphinx's LaTeX builder and `latexmk`; its page breaks, theorem boxes, running heads and figure placement are reviewed separately from HTML.

Do not use forced `\\` for paragraph spacing, print-only `\centerline`, or arbitrary manual spacing in new MyST. Do not add code blocks unless the reader is meant to copy code; mathematical algorithms remain prose/math.
