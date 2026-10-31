"""Local-only prototype build. Never deploys or modifies original source.

Usage: python prototypes/build.py [all|sphinx-html|tex4ht-html]
Run with prototypes/.venv/Scripts/python on Windows (.venv/bin/python on Unix).
"""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
BUILD = BASE / '_build'
TIMINGS = {}


def run(name, args, cwd):
    start = time.perf_counter()
    result = subprocess.run([str(a) for a in args], cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8', errors='replace')
    (BUILD / 'logs').mkdir(parents=True, exist_ok=True)
    (BUILD / 'logs' / (name + '.log')).write_text(result.stdout, encoding='utf-8')
    TIMINGS[name] = round(time.perf_counter() - start, 3)
    print(f'{name}: {TIMINGS[name]} s, exit {result.returncode}', flush=True)
    if result.returncode:
        print(result.stdout[-10000:])
        raise SystemExit(result.returncode)


def copy(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists() or source.read_bytes() != target.read_bytes():
        shutil.copy2(source, target)


def prepare_tex(target):
    target.mkdir(parents=True, exist_ok=True)
    for p in (BASE / 'shared').glob('*.tex'):
        copy(p, target / p.name)
    copy(ROOT / 'fizztex.sty', target / 'fizztex.sty')
    for name in ('book.tex', 'book.cfg', 'mathjax-config.js'):
        copy(BASE / 'tex4ht' / name, target / name)


def sphinx_html():
    run('sphinx-html', [sys.executable, '-m', 'sphinx', '-W', '--keep-going', '-b', 'html', BASE / 'sphinx', BUILD / 'sphinx/html'], ROOT)


def tex4ht_html():
    target = BUILD / 'tex4ht'
    prepare_tex(target)
    run('tex4ht-html', ['make4ht', '-u', '-c', 'book.cfg', 'book.tex'], target)
    # make4ht can return zero despite TeX errors; check its detailed outputs too.
    log = (target / 'book.log').read_text(encoding='utf-8', errors='replace')
    if '\n!' in log or 'Undefined control sequence' in log:
        raise RuntimeError('TeX4ht reported a TeX error; inspect book.log')


def main():
    from prepare import main as prepare
    prepare()
    BUILD.mkdir(parents=True, exist_ok=True)
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if mode == 'sphinx-html':
        sphinx_html()
    elif mode == 'tex4ht-html':
        tex4ht_html()
    elif mode == 'all':
        figures = BUILD / 'figures'
        figures.mkdir(parents=True, exist_ok=True)
        for name in ('figure.tex', 'intersection.tex'):
            copy(BASE / 'shared' / name, figures / name)
        run('figure-pdf', ['latexmk', '-pdf', '-interaction=nonstopmode', '-halt-on-error', 'figure.tex'], figures)
        # DVI → SVG needs no Ghostscript and preserves vector paths.
        run('figure-dvi', ['latex', '-interaction=nonstopmode', '-halt-on-error', 'figure.tex'], figures)
        run('figure-svg', ['dvisvgm', '--no-fonts', '-o', 'intersection.svg', 'figure.dvi'], figures)
        copy(figures / 'figure.pdf', BASE / 'sphinx/assets/intersection.pdf')
        copy(figures / 'intersection.svg', BASE / 'sphinx/assets/intersection.svg')
        native = BUILD / 'native-pdf'
        prepare_tex(native)
        run('native-pdf', ['latexmk', '-pdf', '-interaction=nonstopmode', '-halt-on-error', 'book.tex'], native)
        # Seed the download target so Sphinx can resolve it during its first PDF build.
        download = BASE / 'sphinx/downloads/mathematics-prototype.pdf'
        if not download.exists():
            copy(native / 'book.pdf', download)
        run('sphinx-latex', [sys.executable, '-m', 'sphinx', '-W', '--keep-going', '-b', 'latex', BASE / 'sphinx', BUILD / 'sphinx/latex'], ROOT)
        run('sphinx-pdf', ['latexmk', '-pdf', '-interaction=nonstopmode', '-halt-on-error', 'mathematics-prototype.tex'], BUILD / 'sphinx/latex')
        copy(BUILD / 'sphinx/latex/mathematics-prototype.pdf', download)
        sphinx_html()
        tex4ht_html()
        copy(native / 'book.pdf', BUILD / 'tex4ht/mathematics-prototype.pdf')
    else:
        raise SystemExit('Expected all, sphinx-html or tex4ht-html')
    (BUILD / ('timings-' + mode + '.json')).write_text(json.dumps(TIMINGS, indent=2) + '\n')


if __name__ == '__main__':
    main()
