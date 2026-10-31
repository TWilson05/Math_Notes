"""Extract only the documented sample; generate adapters without editing originals."""
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    # Do not invalidate incremental builds when content is unchanged.
    if not path.exists() or path.read_text(encoding='utf-8') != text:
        path.write_text(text, encoding='utf-8')


def main():
    src = (ROOT / 'Sections/Probability/Foundations.tex').read_text(encoding='utf-8')
    lines = src.splitlines()
    def excerpt(start, end):
        return '\n'.join(lines[start - 1:end]) + '\n'
    venn = excerpt(18, 20)
    assert r'\begin{venndiagram2sets}' in venn and r'\fillACapB' in venn
    proof = excerpt(61, 68).strip()
    assert proof.startswith('Observe that') and proof.endswith(r'\end{align*}')
    equation = excerpt(59, 59).strip().removeprefix(r'\[').removesuffix(r'\]')
    assert equation == r'\prob(A\cup B)=\prob(A)+\prob(B)-\prob(A\cap B)'
    write(BASE / 'shared/intersection.tex', venn)
    write(BASE / 'shared/inclusion-proof.tex', proof + '\n')
    write(BASE / 'shared/inclusion-equation.tex', equation + '\n')
    figure = '\\documentclass[border=4pt]{standalone}\n\\usepackage{venndiagram}\n\\begin{document}\n' + venn + '\\end{document}\n'
    write(BASE / 'shared/figure.tex', figure)
    # Native TeX for PDF and TeX4ht; ordinary amsthm structure added explicitly.
    body = r'''\section{Probability}
\subsection{Foundations}\label{sec:foundations}
\subsubsection{Events and probability}
\begin{definition}[Probability measure]\label{def:probability}
''' + excerpt(4, 14) + r'''\end{definition}
Intersection: $A\cap B=\brcurly{\omega\in\Omega:\ \omega\in A\text{ and }\omega\in B}$.
\begin{figure}[htbp]
\centering
\input{intersection.tex}
\caption{Intersection of two events. Existing Venn source; local review only.}\label{fig:intersection}
\end{figure}
\subsubsection{Discrete uniform distribution}
''' + (excerpt(34, 34) + excerpt(36, 40)).replace('\\\\\n', '\n\n') + r'''
\begin{example}[One die]
For a die, we have $\Omega=\{1,2,3,4,5,6\}$ and $\prob(\{\omega\})=\frac{1}{6}$.
\end{example}
\subsubsection{Inclusion--exclusion}
\begin{theorem}[Two events]\label{thm:inclusion}
Let $A$ and $B$ be two events. Then
\begin{equation}\label{eq:inclusion}
''' + equation + r'''
\end{equation}
\end{theorem}
\begin{proof}
''' + proof + r'''
\end{proof}
See Definition~\ref{def:probability}, Theorem~\ref{thm:inclusion},
equation~\eqref{eq:inclusion}, Figure~\ref{fig:intersection},
and Section~\ref{sec:foundations}.
'''
    write(BASE / 'shared/sample.tex', body)
    # MyST uses the same original math strings, with explicit semantic markup.
    proof_md = proof.replace(r'\begin{align*}', '\n$$\n\\begin{aligned}').replace(r'\end{align*}', '\\end{aligned}\n$$\n')
    md = r'''# Foundations

## Events and probability

```{prf:definition} Probability measure
:label: def-probability

We can define the following notation for probability:

- We denote the *state space* or *universal set* as $\Omega$ or $S$.
- An *event* is a "nice" subset of the state space, i.e. an event $A$ fulfils $A\subseteq\Omega$. The set of all events is often denoted by $\mathcal{A},\ \mathcal{E},$ or $\mathcal{F}$.
- A *probability measure* $\prob$ is a map taking events as argument with
  - $\prob:\ \mathcal{A}\to[0,1]$
  - $\prob(\Omega)=1$
  - For a countable index set $I$ with $(A_i)_{i\in I}$ being disjoint events, we have $\prob\brround{\bigsqcup\limits_{i\in I}A_i}=\sum\limits_{i\in I}\prob(A_i)$.
```

Intersection: $A\cap B=\brcurly{\omega\in\Omega:\ \omega\in A\text{ and }\omega\in B}$.

```{figure} ../assets/intersection.*
:name: fig-intersection
:alt: Two overlapping circles labelled A and B; only their shared lens is shaded.
:width: 65%

Intersection of two events. Existing Venn source; local review only.
```

## Discrete uniform distribution

We use the square cups $\sqcup$ to denote the disjoint union of sets. This means that $A_1\sqcup A_2$ implies that the two sets have no overlap and they are disjoint: $A_1\cap A_2=\emptyset$.

We require that $\Omega$ is non empty and finite. If every event $\omega$ is equally likely, we have a discrete uniform distribution. This means that

$$\prob(\{\omega\})=\frac{1}{|\Omega|}\ \forall\omega\in\Omega$$

Then the probability of an event $A$ is

$$\prob(A)=\frac{|A|}{|\Omega|}$$

We call this setting a discrete uniform distribution or uniformly random.

```{prf:example} One die
For a die, we have $\Omega=\{1,2,3,4,5,6\}$ and $\prob(\{\omega\})=\frac{1}{6}$.
```

```{raw} latex
\clearpage
```

## Inclusion–exclusion

````{prf:theorem} Two events
:label: thm-inclusion

Let $A$ and $B$ be two events. Then

```{math}
:label: eq-inclusion
''' + equation + r'''
```
````

```{prf:proof}
''' + proof_md + r'''
```

See {prf:ref}`def-probability`, {prf:ref}`thm-inclusion`,
equation {eq}`eq-inclusion`, {numref}`fig-intersection`,
and the [notation checks](notation.md).
'''
    write(BASE / 'sphinx/probability/foundations.md', md)
    gallery = (BASE / 'shared/notation.tex').read_text(encoding='utf-8')
    gallery = '\n'.join(line for line in gallery.splitlines() if not line.startswith('%'))
    write(BASE / 'sphinx/probability/notation.md', '# Notation checks\n\nAdded compatibility fixtures, not additional textbook content.\n\n' + gallery.replace(r'\[', '$$').replace(r'\]', '$$') + '\n\nReturn to [Foundations](foundations.md).\n')
    macros = json.loads((BASE / 'shared/mathjax-macros.json').read_text())
    config = {'tex': {'macros': macros, 'tags': 'ams'}}
    write(BASE / 'tex4ht/mathjax-config.js', 'window.MathJax = ' + json.dumps(config) + ';\n' +
          'const mathjaxScript = document.createElement("script");\n' +
          'mathjaxScript.src = "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js";\n' +
          'document.head.appendChild(mathjaxScript);\n')
    print('Prepared the Probability sample and notation fixtures; originals unchanged.')


if __name__ == '__main__':
    main()
