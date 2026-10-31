# Mathematics Notes migration plan

## Phase 2 status (2026-10-30)

The production Sphinx tree is now [book/](book/). The complete Differential Calculus course is migrated into six MyST pages under [book/differential-calculus/](book/differential-calculus/), with eight original figures copied into the reviewed publishing asset tree and one deterministic TikZ/PGFPlots workflow figure. The original TeX remains unchanged. HTML and PDF builds pass with warnings treated as errors; the PDF is 36 pages. The generated converter and parity check are [convert_differential.py](book/tools/convert_differential.py) and [validate_differential.py](book/tools/validate_differential.py).

The remaining chapters are intentionally not migrated. Figure provenance is still pending for the reused raster assets, and no deployment configuration or public publication was added. The full-course migration phases below remain the roadmap.

## Phase 3 status (2026-10-30)

All remaining source groups have now been structurally migrated into [book/](book/). [MIGRATION_STATUS.md](MIGRATION_STATUS.md) records the 15 remaining course groups, source-to-page mapping, and unsupported/manual-review constructs. The full HTML build and 546-page PDF build succeed locally. The edition remains unpublished because the PDF has layout diagnostics and the figure/provenance/accessibility review is incomplete.

## Recommendation

Use **Sphinx + MyST + Sphinx Book Theme + sphinx-proof**, with LaTeX mathematics retained inside MyST and LaTeX used for PDF generation. This is the best fit for the requested textbook navigation, search and incremental editing, based on the working samples and the repository audit. Keep the original TeX collection and style unchanged as the migration baseline. Migrate one reviewed section at a time; do not maintain two independently edited prose copies indefinitely.

This recommendation has a real authoring tradeoff: **MyST becomes the prose/structure source for migrated sections**. Sphinx is not a LaTeX-first publishing engine and does not directly ingest arbitrary original TeX chapters. Original math expressions, command names, vector source and the TeX PDF toolchain can be retained; the original prose wrappers cannot all remain the active website source. If “LaTeX-based source” means all future prose must remain in `.tex`, choose **TeX4ht + native LaTeX PDF** instead. Its working prototype demonstrates that this is viable, with a larger website/accessibility maintenance commitment. Do not adopt a custom TeX-to-MyST compiler just to disguise this distinction.

The 15 chapters need semantic restructuring under either choice: the original has no labels or references and no named theorem/definition environments, even though it has 34 proof environments. This reduces the advantage of preserving every existing formatting command. Conversely, 1,070 aligned displays and heavy custom notation make preserving math bodies essential.

## Repository-specific comparison

| Concern | Sphinx / MyST | TeX4ht / native LaTeX |
|---|---|---|
| Source conversion | Convert 84-file prose/import structure, nested lists and 105 tabular blocks selectively. Keep TeX expressions. No honest automatic-conversion percentage is available. | Most body TeX, imports, tables, proofs and style remain usable. Add semantic markup and adjust print layout for web. Full-package compatibility is not yet proven. |
| Mathematical notation | Explicit shared MathJax bridge; 12 macros exercised. PDF loads original style. | Same bridge needed for the selected MathJax mode; `.sty` alone does not define browser commands. Native PDF retains full style. Alternate TeX4ht MathML modes were not tested. |
| Theorems / references | Standard proof directives, stable labels, equation/figure roles. Sample links work; theorem and PDF styling need consistent conventions. | amsthm + hyperref work in the sample. Add new labels since originals have none. Default navigation required a small configuration fix. |
| Figures | Explicit SVG/PDF pair chosen by builder; existing Venn source works with no custom extension. | Existing Venn/TikZ runs through TeX4ht to SVG; native PDF embeds vector drawing directly. Generic alt text needs work. |
| Navigation / search | Nested chapter/page sidebar, in-page contents and static search supplied by the theme/Sphinx; exercised locally. | Split pages, contents and next/previous links work. A persistent nested sidebar and site search would require more integration, such as a reviewed static search tool (not added here). |
| PDF quality | Real LaTeX output with original macros. Sample required a page-break adjustment for the long boxed proof; PDF design is separate from the HTML theme. | Most direct control and closest to current print typography; sample uses amsthm and native figures. |
| Build behavior | Document dependency cache; no-op and one-page invalidation measured. Browser handles MathJax. | Standard make4ht reruns TeX passes even with unchanged input. Section-specific preview wrappers or documented draft mode can reduce iteration cost, but cross-book numbering requires full runs. |
| Future editing | VS Code edits MyST prose and familiar TeX math. Standard toctree/directives; no custom parser to maintain. | VS Code and existing TeX workflow remain familiar; more HTML configuration and search/navigation ownership. |
| Dependencies | Four direct Python packages plus existing TeX tools. A resolved lock file is included. | Existing TeX Live plus a small configuration and MathJax loader; search would add a tool. |
| Preservation | Original source remains intact; mathematical expressions retain their syntax wherever supported. Layout syntax changes substantially. | Highest preservation of ongoing `.tex` authoring and PDF behavior. More print-specific markup may survive into imperfect HTML unless reviewed. |

## Prototype evidence and limits

Rebuild and view both samples using [prototypes/README.md](prototypes/README.md). Both contain Probability → Foundations → three topics, a definition, example, theorem, numbered equation, full aligned proof, figure and cross-references. The notation fixture exercises optional-argument derivatives, matrix/augmented-matrix delimiters, number sets, expectation, variance and script-L. The source equation and proof expression bodies match exactly between formats.

Final checks: 85 original TeX/style hashes unchanged; original tracked source/images/PDF have no Git diff; seven Sphinx HTML pages and five TeX4ht HTML pages pass local link/resource checks. The native LaTeX PDF is two pages; Sphinx's PDF is seven pages including its front matter. Both pass text/reference/log checks without missing characters or overfull boxes. Browser math renders without errors on both content pages and both notation pages. SVG figures load; Sphinx search returns the sample. Representative PDF pages were visually inspected.

The small samples establish feasibility, not complete compatibility. They do not certify all 65 style definitions, every table, `\polylongdiv`, `\ind`, color boxes, esint symbols or font variants. No raster rights were assumed. Linux/Pages builds and full-book PDF layout remain untested. TeX4ht's generic figure alt text and h4/h5 split-page heading levels remain known accessibility limitations. The PDF outputs are untagged. These are explicit follow-up gates, not silently omitted content.

### Build measurements

One local run on Windows / Python 3.10.11 / TeX Live 2026 / make4ht 0.4e, excluding dependency installation and browser MathJax loading:

| HTML build | Seconds |
|---|---:|
| Sphinx, fresh output and doctrees | 4.939 |
| Sphinx, unchanged rebuild | 2.508 |
| Sphinx, one document timestamp changed | 5.142 |
| TeX4ht, fresh output | 26.656 |
| TeX4ht, unchanged rebuild | 13.544 |

The one-page measurement touches the notation page without altering its bytes; the log confirms one changed source is read. Theme/index writes and process startup dominate this tiny sample, so it is not faster than the fresh build in this run. Do not extrapolate these numbers linearly to 500 pages. Recent PDF rebuilds after source/config changes took roughly five seconds for native LaTeX and twelve seconds for Sphinx's LaTeX compilation, plus about three seconds to generate its TeX. These were not controlled cold-PDF benchmarks. Reproduction is in [benchmark.py](prototypes/benchmark.py); logs and JSON are local build outputs.

## Proposed layout and website structure

Keep the original root, Sections and Images locations during migration to preserve includes. New directories below are a proposal, not a bulk move:

```text
MathNotes.tex, fizztex.sty, Sections/, Images/   original migration baseline
MIGRATION_AUDIT.md, FIGURE_INVENTORY.md, MIGRATION_PLAN.md
prototypes/                                    this review experiment
book/
  conf.py, index.md
  foundations/index.md, numbers.md, ...
  introductory-logic/...
  pre-calculus/...             # one directory per original main section
  probability/index.md, foundations.md, counting.md, ...
  bibliography.md
  _static/textbook.css
  downloads/                  # generated complete book and section PDFs
figures/
  sources/                    # reviewed TikZ or Python source
  manifest.json               # source, license, attribution, alt text, approval
  generated/                  # cached SVG + PDF, never edited by hand
publishing/
  mathjax-macros.json
  requirements.txt, requirements-lock.txt
  latex/                      # print-specific wrappers/settings
.vscode/tasks.json            # preview HTML, PDF, figure rebuild, validation
.github/workflows/            # validation first; deployment only after review
```

The home page offers chapter overview, search and the full PDF download. Each of the 15 original main sections is a top-level chapter, in the root order recorded in the audit. Nested sidebar levels are chapter/course → section page → in-page topic. Preserve course identifiers as chapter metadata where the bibliography establishes them; do not invent a one-to-one course mapping. Split especially long section files into topic pages when helpful. Bibliography, notation index and figure attribution are back matter. Explicitly include the currently unimported Power Laws material in the coverage ledger.

## Formatting and notation conventions

Use one H1 per page, H2/H3 for topics, sentence-case prose headings and semantic paragraphs instead of forced line breaks. Use proof directives for definitions, theorems, propositions, lemmas, corollaries, examples and proofs; assign durable labels such as `probability-inclusion-exclusion`, independent of numbering. Use native math/figure roles for references, with chapter-aware numbering. Avoid links to page numbers in HTML.

Retain TeX math expressions, including custom macro names. Use inline dollar math and labelled math directives for displayed statements; use `aligned` inside a display for derivations. Preserve the number and order of derivation lines. Distinguish actual data tables from arrays and prose laid out with tabular. Tables need headers and responsive overflow; rewrite presentation only after comparing meaning. Keep the original duplicate proof line until a separately reviewed mathematical edit removes it.

Use a restrained theme: readable line length, high contrast, gentle theorem accents, consistent spacing, keyboard navigation, descriptive figure text and horizontal scrolling for genuinely wide equations. PDF needs its own title page, table of contents, running heads, chapter breaks, theorem numbering, bibliography and overflow review. Browser “Print to PDF” is not the complete textbook PDF pipeline. Proof boxes currently use sphinx-proof's standard admonition rendering; review that print treatment before committing to a full book style.

### Macro compatibility strategy

Treat [fizztex.sty](fizztex.sty) as the original definition source and [audit-data.json](prototypes/audit-data.json) as the usage inventory. The audit finds 65 top-level definitions (including an internal helper), 54 used in the corpus. The sample maps 12 explicitly; unsupported or untested definitions must not be guessed away.

1. Classify all used macros as standard MathJax, exact configurable equivalent, package-extension candidate, or vector fallback. Inventory local `\argument` and `\bigO` too.
2. Maintain one small reviewed browser macro map shared by web prototypes; load the original style for PDF. Do not ship all TeX package internals to MathJax.
3. Test optional arguments, matrix grouping, prescripts, `\mathscr`, esint symbols and `\colourboxed` independently against native PDF. Retain argument signatures and delimiters.
4. For `\ind=\mathds{1}`, preserve the glyph through a vetted font strategy or vector expression with accessible text; do not replace it with a visually different blackboard or bold 1 silently. Calligra and polynom need separate decisions. A local approved vector fallback is preferable to an incorrect symbol.
5. Fail the publishing check on unknown commands, MathJax error nodes, missing characters, missing targets or required figures. Record unresolved cases and block affected sections. Expand the sample gallery before migrating each course's new macro families.

## Figure modernization

[FIGURE_INVENTORY.md](FIGURE_INVENTORY.md) covers 122 raster files, 127 inclusions and 15 embedded figures. All raster provenance is uncertain; one JPEG duplicate is unreferenced. Do not presume a course screenshot is original because it is in the repository.

Preserve every original. Record author/source/license/permission/attribution and approval per asset. Use TikZ for set/geometry/circuit diagrams, Python for analytic plots and data, and SVG for suitable illustrations. Compile approved source once into vector SVG for HTML and PDF for print. Cache by source, inputs and toolchain; do not rebuild all figures on each HTML edit. Check axes, scale, domains, shading, labels and mathematical correctness against the original. Provide captions, alt text and source attribution. Unapproved or mathematically uncertain figures block publication of their sections; never silently drop them. A redraw does not by itself resolve attribution or content-rights questions.

## Build and editing workflow

For Sphinx development, keep its doctree cache and use `sphinx-build -b html -W --keep-going` on the same output directory. Rebuild figures only when their sources change. Use the standard MyST extension in VS Code if desired; add simple tasks that call the pinned Python environment and latexmk. A local HTTP server is sufficient for preview; an auto-reload dependency is optional, not required.

Use Sphinx's LaTeX builder followed by latexmk for the reviewed migrated book. latexmk avoids unnecessary passes, but changing one chapter can still repaginate the full PDF. Refresh downloadable PDFs in release builds and when testing print changes, not on every prose edit. Until all chapters migrate, preserve the original PDF workflow and clearly label each generated edition's coverage. A future separate full-original-source wrapper can enable all 15 imports without editing the current root; that full build must be repaired and validated before it is advertised as a complete textbook. Do not stitch independently numbered course PDFs together and call that the final polished book.

For optional individual-section PDFs, use documented Sphinx `latex_documents` entries rooted at selected sections, or small native-TeX wrappers in the LaTeX-first path. Give them local numbering and explicit references to the complete edition; cross-section references may not resolve in isolated documents. Implement and validate this after the complete-book structure is approved. It is not implemented in the prototype.

If TeX4ht is chosen, maintain standard amsthm/hyperref semantic source and wrappers; split at subsection boundaries, add a shared navigation design and evaluate a static search index. Use per-section preview builds for development and a complete root build for coherent numbering at release. Benchmark actual courses before adding caching infrastructure. Preserve native PDF generation with latexmk.

## GitHub Pages strategy — after review

No deployment workflow or public site has been created. First add a validation-only workflow for pull requests: pinned Python install, cached dependencies/approved figures, warning-as-error HTML build, internal links, browser MathJax checks and PDF generation with log inspection. Confirm filename case and all packages on Linux. Upload private/repository CI review artifacts according to repository visibility; do not publish uncleared content through a public preview.

After prototype approval and content/figure clearance, use one GitHub Pages site and the standard `configure-pages`, `upload-pages-artifact` and `deploy-pages` actions with `pages: write` and `id-token: write` limited to the deployment job. Publish only the generated HTML directory plus approved PDF downloads. Include `.nojekyll` so underscore asset directories survive, use relative project-site URLs, and test at `/repository-name/`, not only the domain root. Deploy from the chosen branch or a reviewed manual release workflow with the Pages environment gate. Pin action revisions when implementing. No paid search/backend service is needed.

Vendor the pinned MathJax runtime/fonts before release if offline operation and independence from the CDN are desired; keep its license and version recorded. Caches must not decide which content is approved to publish. Full PDFs and section downloads must match the deployed source revision.

## Phased migration

| Phase | Courses / work | Exit criteria |
|---|---|---|
| 0 — review this experiment | Choose the active authoring format; review both samples, typography and source tradeoff. | Framework decision, sample math/figure review, no deployment. |
| 1 — establish conventions | Complete macro gallery, figure manifest, stable labels, coverage ledger, bibliography and CI-only builds. | No silent command fallbacks; Linux validation; standard edit/preview tasks. |
| 2 — first full chapters | Probability and Mathematical Proof. | Named theorem/proof structure, tables reviewed, all original content accounted for, HTML/PDF parity. Probability's indicator/color boxes must pass first. |
| 3 — foundational material | Foundations (including Power Laws), Pre-Calculus, Differential Calculus, Integral Calculus. | Geometry/graph figures cleared or redrawn; long division and all calculus notation validated. |
| 4 — algebra and higher calculus | Linear Algebra, Multivariable Calculus, Vector Calculus. | Matrix/augmented-matrix equivalence, multivariable diagrams and integral glyphs validated. |
| 5 — analytic methods | Series and Transforms, ODEs, PDEs. | Script operators, long derivations, Fourier/phase portraits and boundary-condition tables reviewed. |
| 6 — remaining specialist material | Complex Analysis, Variational Calculus, Introductory Logic. | Complex-map geometry, contours, variational TikZ, logic symbols and argument-layout tables validated. |
| 7 — complete edition | All 15 chapters and back matter; optional section PDFs. | Coverage ledger has no unexplained omissions; full PDF layout checked; links/search/accessibility and figure clearance pass; user reviews release before Pages publication. |

At each phase compare original versus migrated equations, assumptions, proofs, examples, tables and figures. Keep a separate editorial issue list for suspected original mathematical errors. Do not fold corrections into conversion without recording and reviewing them. Archive original TeX as provenance once a section's active authoring source changes; record that choice so future edits do not diverge between formats.
