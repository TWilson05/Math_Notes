"""Validate local artifacts, cross-references and original-source preservation."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re
import subprocess

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
BUILD = BASE / '_build'


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.ids.update(attrs[a] for a in ('id', 'name') if a in attrs)
        self.links.extend(attrs[a] for a in ('href', 'src') if a in attrs)


def main():
    audit = json.loads((BASE / 'audit-data.json').read_text())
    for name, expected in audit['source_sha256'].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, f'Original changed: {name}'
    results = {'original_sources_unchanged': len(audit['source_sha256']), 'html': {}, 'pdf': {}}
    for folder in (BUILD / 'sphinx/html', BUILD / 'tex4ht'):
        pages = {p.resolve(): Page(p) for p in folder.glob('**/*.html') if '_static' not in p.relative_to(folder).parts}
        checked = 0
        for path, page in pages.items():
            for link in page.links:
                url = urlsplit(link)
                if url.scheme or url.netloc or link.startswith('javascript:'):
                    continue
                target = (path.parent / unquote(url.path)).resolve() if url.path else path
                assert target.exists(), f'Missing resource: {path.name} -> {link}'
                if url.fragment and target in pages:
                    assert unquote(url.fragment) in pages[target].ids, f'Missing anchor: {path.name} -> {link}'
                checked += 1
        results['html'][folder.relative_to(BUILD).as_posix()] = {'pages': len(pages), 'local_links_and_assets': checked}
    for pdf in (BUILD / 'native-pdf/book.pdf', BUILD / 'sphinx/latex/mathematics-prototype.pdf'):
        info = subprocess.check_output(['pdfinfo', str(pdf)], encoding='utf-8', errors='replace')
        extracted = subprocess.check_output(['pdftotext', '-layout', str(pdf), '-'], encoding='utf-8', errors='replace')
        for expected in ('Probability', 'Foundations', 'Definition', 'Theorem', 'Proof', 'Notation checks'):
            assert expected in extracted, f'{expected} missing from {pdf}'
        assert '??' not in extracted, f'Unresolved PDF reference: {pdf}'
        logfile = pdf.with_suffix('.log').read_text(encoding='utf-8', errors='replace')
        for error in ('Undefined control sequence', '\n!', 'undefined references', 'Overfull', 'Missing character:'):
            assert error not in logfile, f'{error} in {pdf.with_suffix(".log")}'
        results['pdf'][pdf.relative_to(BUILD).as_posix()] = {'pages': int(re.search(r'Pages:\s+(\d+)', info)[1]), 'text_and_log_checks': 'passed'}
    # Exact selected formula and proof body are shared; MyST changes only the outer math environment.
    md = (BASE / 'sphinx/probability/foundations.md').read_text(encoding='utf-8')
    equation = (BASE / 'shared/inclusion-equation.tex').read_text().strip()
    proof = (BASE / 'shared/inclusion-proof.tex').read_text().strip()
    aligned = re.search(r'\\begin\{align\*\}(.*?)\\end\{align\*\}', proof, re.S)[1]
    assert equation in md and aligned in md, 'Math changed between the two prototypes'
    results['selected_formula_and_proof_parity'] = 'exact expression-body match'
    (BUILD / 'validation.json').write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
