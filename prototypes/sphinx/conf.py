from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
project = 'Mathematics Notes — Prototype'
author = 'Tyler Wilson'
copyright = 'Local review prototype; publication rights not cleared'
extensions = ['myst_parser', 'sphinx.ext.mathjax', 'sphinx_proof']
myst_enable_extensions = ['dollarmath', 'amsmath']
html_theme = 'sphinx_book_theme'
html_theme_options = {'show_navbar_depth': 3, 'show_toc_level': 2}
html_title = 'Mathematics Notes'
html_static_path = ['_static']
html_css_files = ['textbook.css']
exclude_patterns = ['_build']
numfig = True
math_numfig = True
numfig_secnum_depth = 1
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js'
mathjax3_config = {'tex': {'macros': json.loads((HERE.parent / 'shared/mathjax-macros.json').read_text())}}
latex_engine = 'pdflatex'
latex_domain_indices = False
latex_documents = [('index', 'mathematics-prototype.tex', 'Mathematics Notes', author, 'manual')]
latex_additional_files = [str(HERE.parents[1] / 'fizztex.sty')]
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'extraclassoptions': 'oneside,openany',
    'preamble': r'\usepackage{dsfont,tcolorbox}\usepackage{fizztex}\setlength{\headheight}{14pt}',
}
