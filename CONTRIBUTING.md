# Contributing to Mathematics Notes

The active migrated source is under `book/`. Keep the original LaTeX under `Sections/` and `fizztex.sty` intact; it is the traceability baseline. Do not publish or delete an original figure while its provenance is uncertain.

## Local setup

From the repository root on Windows:

```powershell
python -m venv prototypes/.venv
prototypes/.venv/Scripts/python -m pip install -r prototypes/requirements-lock.txt
prototypes/.venv/Scripts/python -m sphinx -W --keep-going -b html book book/_build/html
prototypes/.venv/Scripts/python -m sphinx -W --keep-going -b latex book book/_build/latex
latexmk -pdf -interaction=nonstopmode -halt-on-error book/_build/latex/mathematics-notes.tex
python prototypes/validate.py
prototypes/.venv/Scripts/python book/tools/validate_differential.py
prototypes/.venv/Scripts/python book/tools/validate_book.py
```

Use `python -m http.server 8765 --bind 127.0.0.1 --directory book/_build/html` to inspect the site. Open the migrated chapter from the sidebar, resize to a narrow viewport, use search, and follow every new reference before submitting changes.

Regenerate the workflow figure with `make figures` or `powershell -ExecutionPolicy Bypass -File book/tools/build_figures.ps1`. The generated SVG/PDF files are ignored build assets; commit only their source and manifest record when the repository policy requires generated assets to be rebuilt in CI.

## Adding a chapter or section

Create a course directory under `book/`, add its `index.md`, add topic pages, and include the directory in `book/index.md`'s toctree. Preserve the original source path in each page's traceability comment. Add macros to `book/_static/mathjax-macros.json` only after comparing browser output with the native PDF. Add figure source, generated output and a manifest record together. Update the coverage ledger in `MIGRATION_CHECKLIST.md`.

Use the conventions in [STYLE_GUIDE.md](STYLE_GUIDE.md). Run the HTML build with warnings as errors, the PDF build, the source-preservation validator, and a browser review. Keep generated build outputs out of commits.
