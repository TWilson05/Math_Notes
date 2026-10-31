# Figure workflow example

This small deterministic example shows the intended workflow for new figures. The source is [tangent-line.tex](sources/tangent-line.tex); the generated SVG is produced by the local figure task and is never hand-edited.

````{only} html
```{figure} generated/tangent-line.svg
:name: fig-workflow-tangent
:alt: A parabola with a tangent line at a marked point.
:width: 70%

Workflow example: a simple mathematical diagram authored as TikZ and exported to SVG.
```
````

````{only} latex
```{figure} generated/tangent-line.pdf
:name: fig-workflow-tangent-pdf
:alt: A parabola with a tangent line at a marked point.
:width: 70%

Workflow example: the same TikZ source exported to PDF for print.
```
````

Record provenance, license, source, alt text, reviewer, and approval date in the figure manifest before using a figure in a public chapter.
