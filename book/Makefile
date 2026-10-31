.PHONY: html latex pdf figures check
PYTHON ?= ../prototypes/.venv/bin/python

html:
	$(PYTHON) -m sphinx -W --keep-going -b html . _build/html

latex:
	$(PYTHON) -m sphinx -W --keep-going -b latex . _build/latex

pdf: latex
	cd _build/latex && latexmk -pdf -interaction=nonstopmode -halt-on-error mathematics-notes.tex

figures:
	powershell -ExecutionPolicy Bypass -File tools/build_figures.ps1

check:
	$(PYTHON) tools/validate_differential.py
	$(MAKE) html
	$(PYTHON) tools/validate_book.py
	$(MAKE) latex
