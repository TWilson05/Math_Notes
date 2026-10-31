# Migration status

Generated from the source hierarchy and structural migration inventory. The original LaTeX under `Sections/` is retained unchanged.

| Course | Original files | Migrated pages | Status | Unsupported/manual review |
|---|---:|---:|---|---|
| Bibliography (`Bibliography`) | 1 | 1 | migrated-structural-review | Bibliography.tex: environment thebibliography |
| Complex Analysis (`Complex_Analysis`) | 4 | 4 | migrated-structural-review | Complex_Algebra.tex: environment proof; Complex_Functions.tex: environment proof; Complex_Functions.tex: environment tikzpicture; Complex_Integration.tex: environment proof; Complex_Integration.tex: environment tikzpicture |
| Foundations (`Foundations`) | 13 | 13 | migrated-structural-review | Arithmetic.tex: environment array; NegativeNumbers.tex: environment matrix |
| Integral Calculus (`Integral_Calculus`) | 3 | 3 | migrated-structural-review | Integration_Techniques.tex: environment matrix; Integration_Techniques.tex: polylongdiv requires manual review |
| Introductory Logic (`Introductory_Logic`) | 4 | 4 | migrated-structural-review | None detected by inventory |
| Linear Algebra (`Linear_Algebra`) | 6 | 6 | migrated-structural-review | Eigen-Analysis.tex: environment matrix |
| Mathematical Proof (`Mathematical_Proof`) | 2 | 2 | migrated-structural-review | None detected by inventory |
| Multivariable Calculus (`Multivariable_Calculus`) | 3 | 3 | migrated-structural-review | Partial_Derivatives.tex: environment matrix |
| Ordinary Differential Equations (`ODEs`) | 4 | 4 | migrated-structural-review | None detected by inventory |
| Partial Differential Equations (`PDEs`) | 3 | 3 | migrated-structural-review | Heat_Equation.tex: environment scriptsize; Laplace_Equation.tex: environment tcolorbox |
| Pre-Calculus (`Pre-Calculus`) | 9 | 9 | migrated-structural-review | Linear_Functions.tex: environment matrix; Quadratic_Functions.tex: environment matrix; Transforming_Functions.tex: environment matrix; Polynomial_Functions.tex: polylongdiv requires manual review; Trig_Functions.tex: environment matrix |
| Probability (`Probability`) | 2 | 2 | migrated-structural-review | Counting.tex: environment matrix; Foundations.tex: environment proof; Foundations.tex: environment tikzpicture; Foundations.tex: environment venndiagram2sets |
| Series and Transforms (`Series_and_Transforms`) | 4 | 4 | migrated-structural-review | None detected by inventory |
| Variational Calculus (`Variational_Calculus`) | 1 | 1 | migrated-structural-review | Definition.tex: environment tikzpicture |
| Vector Calculus (`Vector_Calculus`) | 3 | 3 | migrated-structural-review | None detected by inventory |

## Explicit limitations and omissions

- The migration is structural: source prose, equations, lists, images, and source hierarchy are retained, but many original theorem/proof labels did not exist and therefore cannot be reconstructed automatically.
- TikZ, Venn diagram, and other native drawing environments are preserved as reviewed LaTeX source blocks rather than silently discarded. They need per-figure SVG/PDF conversion and accessibility text before publication.
- `polylongdiv` is preserved and flagged for a dedicated rendering decision.
- Tables using fixed-width `tabular` layout are preserved as LaTeX review blocks where a reliable responsive table conversion was not possible.
- Figures copied under `book/figures/original/` retain uncertain provenance. They are local build assets only until the manifest records permission, attribution, and approval.
- The native PDF builds, but its log contains overfull/underfull box warnings. These are typography review items, especially in Complex Analysis, Introductory Logic, ODEs, and figure-heavy chapters.
- Original source files contain no comprehensive label/reference system. Existing references were not invented; future semantic labels should be added during editorial review.

## Validation per course

HTML and source-coverage checks are automated in `book/tools/validate_book.py` and `book/tools/migrate_remaining.py`. PDF validation is complete for the full generated edition; individual course typography still requires visual review of representative pages.
