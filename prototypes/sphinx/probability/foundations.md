# Foundations

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
\prob(A\cup B)=\prob(A)+\prob(B)-\prob(A\cap B)
```
````

```{prf:proof}
Observe that $A\cup B=(A\setminus B)\sqcup(A\cap B)\sqcup(B\setminus A)$ which is a disjoint union. Hence,

$$
\begin{aligned}
    \prob(A\cup B)&=\prob(A\setminus B)+\prob(A\cap B)+\prob(B\setminus A)\\
    &=\prob(A\setminus B)+\prob(A\cap B)+\prob(B\setminus A)\\
    &=\prob(A)-\prob(A\cap B)+\prob(A\cap B)+\prob(B)-\prob(A\cap B)\\
    &=\prob((A\setminus B)\sqcup(A\cap B))+\prob((A\cap B)\sqcup(B\setminus A))-\prob(A\cap B)\\
    &=\prob(A)+\prob(B)-\prob(A\cap B)
\end{aligned}
$$

```

See {prf:ref}`def-probability`, {prf:ref}`thm-inclusion`,
equation {eq}`eq-inclusion`, {numref}`fig-intersection`,
and the [notation checks](notation.md).
