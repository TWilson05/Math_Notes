from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
project = "Mathematics Notes"
author = "Tyler Wilson"
copyright = "Local review build; publication rights are tracked per figure"
extensions = ["myst_parser", "sphinx.ext.mathjax", "sphinx.ext.todo", "sphinx_proof"]
myst_enable_extensions = ["dollarmath", "amsmath", "colon_fence"]
html_theme = "sphinx_book_theme"
html_theme_options = {"show_navbar_depth": 3, "show_toc_level": 2, "navigation_with_keys": True}
html_title = "Mathematics Notes"
html_static_path = ["_static"]
html_css_files = ["textbook.css"]
exclude_patterns = ["_build", "generated"]
numfig = True
math_numfig = True
numfig_secnum_depth = 1
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js"
mathjax3_config = {"tex": {"macros": json.loads((HERE / "_static/mathjax-macros.json").read_text(encoding="utf-8"))}}
latex_engine = "pdflatex"
latex_documents = [("index", "mathematics-notes.tex", "Mathematics Notes", author, "manual")]
latex_additional_files = [str(HERE.parent / "fizztex.sty")]
latex_elements = {
    "papersize": "letterpaper",
    "pointsize": "11pt",
    "extraclassoptions": "oneside,openany",
    "preamble": r"\usepackage{dsfont,tcolorbox}\usepackage{fizztex}\newcommand{\bigO}{\mathcal{O}}\newcommand{\argument}[2]{#2}\setlength{\headheight}{14pt}",
}
