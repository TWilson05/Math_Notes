# Migration audit

Audit date: 2026-10-30. Scope: all original source, not just the currently enabled chapter. Original files are preserved. Reproduce the source inventory with `python prototypes/audit.py`; detailed counts, locations and SHA-256 baselines are in [audit-data.json](prototypes/audit-data.json).

## Repository and hierarchy

The repository contains 84 TeX files (including the root), 15 main sections, 75 subsection commands, 303 subsubsection commands, and approximately 15,327 uncommented source lines. The root uses `article`, not `book`; each main section imports smaller files with `import`/`subimport`. Main sections are natural future book chapters. Subsection files are natural web pages, except unusually long files that should be split at subsubsections.

[MathNotes.tex](MathNotes.tex) currently enables **only Probability**. Fourteen other chapters and the bibliography are commented out. The checked-in [MathNotes.pdf](MathNotes.pdf) has **42 pages**, not the complete approximately 500-page collection. Its metadata reports May 2024. This audit does not claim to have validated a complete all-course PDF.

| Chapter (root order) | Imported files |
|---|---:|
| Foundations | 12 |
| Introductory Logic | 4 |
| Pre-Calculus | 9 |
| Differential Calculus | 6 |
| Integral Calculus | 3 |
| Series and Transforms | 4 |
| Mathematical Proof | 2 |
| Probability | 2 |
| Linear Algebra | 6 |
| Multivariable Calculus | 3 |
| Vector Calculus | 3 |
| Ordinary Differential Equations | 4 |
| Partial Differential Equations | 3 |
| Variational Calculus | 1 |
| Complex Analysis | 4 |

[PowerLaws.tex](Sections/Foundations/PowerLaws.tex) exists but is not imported by [Foundations.tex](Sections/Foundations.tex). Do not lose it by crawling only the import graph. Preserve current filenames initially, including `First_Oder_ODEs.tex`, to avoid broken includes. No repository AGENTS.md was found. Build products are tracked, while the existing ignore file excludes only `.fls`; new prototype outputs are ignored separately.

## Mathematics, environments and structure

The collection uses 1,070 `align*`, two `flalign*`, 34 `proof`, 105 `tabular`, 107 `itemize`, 31 `enumerate`, two `multicols` and one direct `tcolorbox` environment. Many additional equations use `$$…$$` or `\[…\]`. Matrices often use custom commands rather than explicit environments. Tables include mathematical calculations, truth tables and layout, so a blind conversion to data tables would be wrong.

There are **no active `\label`, `\ref`, `\eqref`, or citation commands** in the scanned source, and no named theorem/definition environments. Theorems, definitions and examples generally appear as prose, bold headings or `Ex:`. `amsthm` supplies proofs. The bibliography has 13 course/lecture entries, without figure-level attribution. Migration must add semantic environments, stable labels and meaningful references under either framework; existing numbering cannot provide this automatically.

Forced `\\` paragraph breaks, `\centerline`, fixed image scales and widths, `\newpage`, tables used for layout, and manual spacing are print-specific. They should become paragraphs, semantic figures and responsive blocks. Preserve mathematical expressions during this structural work.

## Style and package compatibility

[fizztex.sty](fizztex.sty) contains bracket, matrix, derivative, number-set, operator, probability and display helpers. Most frequently used include `\brround` (1,049), `\Ra` (768), `\matrixx` (576), `\brcurly` (344), `\prob` (326), `\brangle` (283), and `\expect` (262). Full per-command usage is recorded in the machine-readable inventory. The style defines no custom theorem environments. Two additional local definitions are `\argument` in Introductory Logic (a fixed-width tabular wrapper) and `\bigO` in Complex Integration.

| Group | Existing dependency/commands | HTML implications |
|---|---|---|
| Core mathematics | amsmath, amssymb, amsfonts, array, mathtools | Standard MathJax math is suitable; preserve expression bodies and alignment. |
| Simple custom notation | brackets, sets, `\prob`, `\expect`, `\Var`, `\Res`, etc. | Explicit MathJax macro configuration; browsers do not load `.sty`. |
| Matrices | `\matrixx`, `\augmatrix`, `\detmatrix`, `\eqnsystem` | TeX grouping/`arraystretch` needs browser-safe definitions with equivalent delimiters and entries. |
| Optional arguments | `\ddx`, `\pdx` | Preserve optional numerators with three-element MathJax macro specifications; test empty and nonempty arguments. |
| Fonts | dsfont, mathrsfs, calligra; `\ind`, `\sr`, `\cursive` | `\mathds{1}` is not ordinary `\mathbb{1}`. Do not silently substitute glyphs. Calligra alphabet needs a fallback or explicit approval. `\sr` and `\cursive` are unused currently. |
| Integrals | esint (`\oiint` occurs) | Test actual contour/surface symbols; font and browser support is not established by the basic sample. |
| Combinatorics | `\perm`, `\comb` via mathtools `\prescript` | Requires MathJax mathtools or reviewed equivalent positioning. |
| Colored boxes | xcolor; 12 `\colourboxed` uses | The delimited `\def` and saved-color internals are not portable MathJax configuration; preserve text color and border separately. |
| Layout boxes | tcolorbox; `\formula`, `\formulabox` | Use semantic admonitions for web; wrapper macros currently unused. |
| Long division | polynom, two `\polylongdiv` uses | Dedicated vector fallback plus accessible description; not supported as ordinary browser mathematics. |
| Graphics | tikz, venndiagram | Compile existing vector source to SVG/PDF. No PGFPlots/axis use found. |
| Print layout | fullpage, multicol, inputenc | Keep for original PDF; replace with web layout. |
| Linking/imports | hyperref, import | TeX4ht understands TeX inclusion; Sphinx requires explicit toctrees and labels. |

The style is not self-contained: `\ind` needs dsfont and box helpers need tcolorbox, supplied by the root rather than required by the style. Graphics currently rely on transitive package loading rather than an explicit graphicx requirement. The style also globally redefines `\d`; that command has zero uses in the scanned content. Preserve the original style, but make dependencies explicit in new wrappers.

## Figures and editorial risks

See [FIGURE_INVENTORY.md](FIGURE_INVENTORY.md) for every raster and embedded drawing, including unreferenced assets and manual review status. Existing raster images cannot become high-quality vectors merely by exporting to SVG. Native figures comprise 11 TikZ pictures and four Venn diagrams. There is no evidence of a PGFPlots dependency. All referenced image paths exist with their current spelling; Linux case-sensitive builds still need verification.

Separate mathematical editing from conversion. For example, [Probability/Foundations.tex](Sections/Probability/Foundations.tex) describes two dice immediately before a one-die event calculation (lines 41–44), and the birthday derivation at lines 169–170 appears to omit a complement in an intermediate equality. [Complex_Functions.tex](Sections/Complex_Analysis/Complex_Functions.tex) contains inverse-map derivations and diagram coordinates that warrant review. Do not silently repair these during migration. The selected inclusion–exclusion proof contains a repeated line; the prototypes deliberately retain it.

## Prototype selection and comparison criteria

Use a small Probability → Foundations → Events/Properties hierarchy: probability-measure axioms, uniform probability, the existing intersection Venn diagram, and the two-event inclusion–exclusion statement and full aligned proof. Add theorem/definition wrappers and explicit cross-references, because the originals have none. These are documented structural additions, not claims about original semantics. Add a clearly marked notation smoke-test page for matrix and optional-argument compatibility.

Sphinx requires prose/structure conversion to MyST but can preserve TeX inside mathematics and use LaTeX for PDF generation. It cannot treat arbitrary original `.tex` sections as semantic MyST pages. TeX4ht can retain the original TeX body and style for PDF and much of HTML, but MathJax still requires a browser macro bridge and navigation/search need evaluation. Both need editorial markup and figure clearance. Build findings and the recommendation will be recorded in [MIGRATION_PLAN.md](MIGRATION_PLAN.md) after the prototypes run.
