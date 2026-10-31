# Introduction to Proofs

<!-- Source: [Sections/Mathematical_Proof/Introduction_to_Proofs.tex](../../Sections/Mathematical_Proof/Introduction_to_Proofs.tex) -->

## A First Proof

The general method of writing a proof is to first write out some scratch work to solve the problem and then write a neat and structured proof which the reader will see.
Ex: Let $n$ be an integer. If $n$ is even then $n^2$ is even.
Scratch work:
We want to show that this implication is always true ($P\Ra Q)$
We assume the hypothesis, $n$ is even, is true (the false case doesn't tell us anything)
By the definition of even, $n=2k,\ k\in\Z$
$n^2=(2k)^2=4k^2=2(2k^2)$
Since $k\in\Z$ we know by an axiom that $2k^2\in\Z$ so, by the definition of even we know that $n^2$ is even.
We can rewrite this using modus ponens as

- $n$ is even $\Ra$ $n=2k$ for some integer $k$
- $n=2k$ for some integer $k$ $\Ra$ $n^2=4k^2$
- $n=4k^2$ $\Ra$ $n^2$ is two times an integer
- $n^2$ is two times and integer $\Ra$ $n^2$ is even

Then the final proof would be written as follows:

Proof:
Let $n$ be an integer. If $n$ is even then $n^2$ is even
Assume that $n$ is an even number.
Hence we know that $n=2k$ for some $k\in\Z$
If follows that $n^2=4k^2=2(2k^2)$
Since $2k^2$ is an integer, it follows that $n^2$ is even $\square$

Ex2: Let $a,b,c\in\Z$. If $a|b$ and $b|c$ then $a|c$
Proof:
By definition of divisibility, $b=ka$ and $c=lb$ for $k,l\in\Z$.
We want to show $a|c$. That is $c=na$ for $n\in\Z$
Since $c=lb$ and $b=ka$, we know $c=lka$
Since $k,l\in\Z$ we know $kl\in\Z$ so we are done $\square$

Let $a,b,c\in\Z$. If $a|b$ and $b|c$ then $a|c$
Proof:
We start by assuming the hypothesis to be true
Assume that $a|b$ and $b|c$, so that $b=ka$ and $c=lb$ for some $k,l\in\Z$
It follows that $c=kla$
Since $kl\in\Z$, we know that $a|c$ as required $\square$
