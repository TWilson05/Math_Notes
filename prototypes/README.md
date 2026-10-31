# Local publishing prototypes

Two small builds of the same Probability excerpt. Nothing here deploys a website. Start with [the audit](../MIGRATION_AUDIT.md), [figure inventory](../FIGURE_INVENTORY.md), and [recommendation](../MIGRATION_PLAN.md).

## Build and view

Tested on Windows with Python 3.10.11 and TeX Live 2026 (`make4ht` 0.4e). Install a TeX distribution containing latexmk, pdflatex, latex, make4ht, dvisvgm, standalone, venndiagram, and the original style's dependencies. Poppler-compatible `pdfinfo`, `pdftotext` and `pdftoppm` are used for validation/inspection; this machine's TeX installation supplies them. No Node, Pandoc, custom Sphinx extension, or global Python install is required.

From the repository root, in PowerShell:

```powershell
python -m venv prototypes/.venv
prototypes/.venv/Scripts/python -m pip install -r prototypes/requirements-lock.txt
prototypes/.venv/Scripts/python prototypes/build.py
prototypes/.venv/Scripts/python prototypes/validate.py
python -m http.server 8765 --bind 127.0.0.1 --directory prototypes/_build
```

On Linux/macOS, replace `prototypes/.venv/Scripts/python` with `prototypes/.venv/bin/python`. Linux builds are proposed, not yet tested. [requirements.txt](requirements.txt) records the four direct dependencies; [requirements-lock.txt](requirements-lock.txt) records the tested resolved Python environment. Do not upgrade dependencies implicitly during migration.

Open these local URLs while the server is running:

- Sphinx: <http://127.0.0.1:8765/sphinx/html/index.html>
- TeX4ht: <http://127.0.0.1:8765/tex4ht/book.html>

PDFs: [Sphinx PDF](_build/sphinx/latex/mathematics-prototype.pdf) and [native LaTeX PDF](_build/native-pdf/book.pdf). Both home pages also provide a working download. Outputs, generated figures, downloadable PDFs and the virtual environment are ignored by Git and rebuilt locally. MathJax is pinned to 3.2.2 on jsDelivr; HTML mathematics currently needs network access. Search runs locally without a service. The TeX4ht prototype does not implement site-wide search.

For HTML-only work after the first full build:

```powershell
prototypes/.venv/Scripts/python prototypes/build.py sphinx-html
prototypes/.venv/Scripts/python prototypes/build.py tex4ht-html
```

Sphinx retains its doctree cache. Figure preparation avoids rewriting unchanged source files. A full build also checks PDFs and figures. PDF files are snapshots: HTML-only builds do not refresh the downloads. Logs, timing JSON and validation JSON are under [_build](_build/). To measure a fresh/no-op/one-page Sphinx build and fresh/no-op TeX4ht build, run `prototypes/.venv/Scripts/python prototypes/benchmark.py` once; it refuses to overwrite an existing benchmark directory.

## Scope and source mapping

| Original material | Selection | Adaptation |
|---|---|---|
| [Probability/Foundations](../Sections/Probability/Foundations.tex) | Lines 4–14 | Probability notation/axioms wrapped as a named definition; nested list becomes MyST list. |
| Same source | Lines 17–20 | Intersection formula and existing Venn source, compiled to SVG/PDF. No raster assets included. |
| Same source | Lines 34, 36–41 | Disjoint-union explanation, uniform distribution, one-die example. The redundant plain-text heading at line 35 becomes a heading. |
| Same source | Lines 58–69 | Named theorem, numbered equation and proof. All five aligned lines, including the repeated line, retained exactly. |
| [notation.tex](shared/notation.tex) | New fixtures | Exercises 12 mapped macros, including matrices and optional derivative arguments; explicitly not new textbook content. |

The sample does **not** reproduce the entire Foundations section. It skips the two-dice example and later material deliberately. New captions, semantic wrappers, labels, links, navigation and one PDF page break are presentation additions. MyST normalizes paragraph breaks and changes “We denoted” to “We denote”; mathematical expressions are retained. The source's terminology “event omega” in the uniform paragraph is retained for editorial review.

[prepare.py](prepare.py) is a deliberately small extraction/template script for this experiment, **not a general LaTeX converter**. It produces [sample.tex](shared/sample.tex), [foundations.md](sphinx/probability/foundations.md), the notation page and the TeX4ht MathJax loader. Edit the script/templates for this prototype; regeneration overwrites those generated files. The explicit extraction assertions catch some source movement, but are not a parser. Production authoring should use ordinary MyST files or ordinary TeX files, not expand this script into a conversion framework.

[fizztex.sty](../fizztex.sty) is copied unchanged into isolated PDF build directories. The shared [MathJax macro map](shared/mathjax-macros.json) supplies browser equivalents for the sample. `matrixx` and `augmatrix` omit TeX-only grouping/arraystretch controls but retain entries and delimiters. Optional numerator defaults are preserved. The other 53 top-level style definitions are **not certified** by this prototype; in particular indicator, color-box, contour-integral and special-font handling still need the compatibility gates in the plan.

## Validation and known limits

[validate.py](validate.py) checks all original TeX/style hashes against [audit-data.json](audit-data.json), local HTML links/assets/anchors, PDF text and unresolved-reference/error/overflow logs, and exact inclusion–exclusion expression-body parity. Do not regenerate the audit baseline to excuse an unexpected original-source change; inspect the Git diff first. The original tracked source and images also had an empty Git diff at completion.

Browser validation additionally checked 28 rendered math items on each Foundations page and two display groups on each notation page, with no MathJax error nodes or stray dollar signs. Both SVG images loaded; the Sphinx nested navigation, theorem/figure/equation links, full-book download and search were checked. A 390-pixel viewport check found no body-width overflow in Sphinx. PDF pages containing figures, derivations and notation were rendered to PNG and inspected. These checks are sample-level, not a complete accessibility audit or mathematical proofreading of the collection.

TeX4ht's generated parent/tail links initially pointed to absent anchors in this installed toolchain. The prototype uses standard crosslink configuration for next/previous links and an explicit book-home navigation link; final local-link checks pass. Its image alt text remains `[Picture]`, and its split-page headings begin at h4/h5. Correct these through documented per-figure/heading configuration before public use. Sphinx uses descriptive figure alt text and semantic headings. Both generated PDFs are untagged; neither has been validated for accessible PDF conformance.

No all-course conversion, complete-book PDF, per-section PDF feature, public Pages workflow, figure-rights clearance or deployment is included in this first-stage prototype.
