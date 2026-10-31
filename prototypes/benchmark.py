"""Small local build measurements, never a full-book performance estimate."""
import json
import os
import sys
from build import BASE, BUILD, ROOT, TIMINGS, prepare_tex, run


def main():
    from prepare import main as prepare
    prepare()
    target = BUILD / 'benchmark-sphinx'
    if target.exists():
        raise SystemExit('Benchmark output already exists; keep the recorded run or choose a new directory.')
    args = [sys.executable, '-m', 'sphinx', '-W', '-b', 'html', BASE / 'sphinx', target]
    run('benchmark-sphinx-fresh', args, ROOT)
    run('benchmark-sphinx-noop', args, ROOT)
    page = BASE / 'sphinx/probability/notation.md'
    before = page.stat()
    try:
        # Same bytes, newer timestamp: exercises one-document invalidation.
        os.utime(page, None)
        run('benchmark-sphinx-one-page', args, ROOT)
    finally:
        os.utime(page, ns=(before.st_atime_ns, before.st_mtime_ns))
    tex = BUILD / 'benchmark-tex4ht'
    prepare_tex(tex)
    run('benchmark-tex4ht-fresh', ['make4ht', '-u', '-c', 'book.cfg', 'book.tex'], tex)
    run('benchmark-tex4ht-noop', ['make4ht', '-u', '-c', 'book.cfg', 'book.tex'], tex)
    (BUILD / 'benchmark.json').write_text(json.dumps(TIMINGS, indent=2) + '\n')


if __name__ == '__main__':
    main()
