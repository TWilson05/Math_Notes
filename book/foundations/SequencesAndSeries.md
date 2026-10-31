# Sequences and Series

<!-- Source: [Sections/Foundations/SequencesAndSeries.tex](../../Sections/Foundations/SequencesAndSeries.tex) -->

## Summation Notation

Summation notation is a shorthand was to express the sum of a set of numbers. The bottom of the sigma tells you what index to start at and the top of the sigma tells you which number to end at.
Ex: $\sum \limits_{x=1}^5 x=1+2+3+4+5=15$
We can use similar notation for repeated multiplication as well. For this we use an upper case pi and use the same notation, using the starting point, stopping point, and index.
Ex: $\prod \limits_{x=2}^4=2\cdot 3\cdot 4=24$

## Arithmetic Sequence

A sequence is an ordered list of numbers. Each number in the list is referred to as an element or term. Each new term follows a pattern or rule to determine the next term in the sequence.
An arithmetic sequence is an ordered list of terms in which the difference between consecutive terms is constant. It is generally expressed as $\{a,a+d,a+2d,a+3d,\ldots\}$ The formula for the nth term of the sequence is given by,

$$
t_n=a+(n-1)d

$$

where $a$ is the first term, $d$ is the common difference between consecutive terms, and n is the term number.

## Arithmetic Series

An arithmetic series is the sum of all terms that form an arithmetic sequence. $S_n$ represents the sum of the first $n$ terms of a series.

$$
S_N=\frac{N}{2}(a+t_N)=\frac{N}{2}(2a+(N-1)d)=\sum \limits_{n=1}^N (a+(n-1)d)

$$

## Geometric Sequence

Geometric sequences are sequences in which the ratio of consecutive terms is constant. The common ratio, $r$, can be found by taking any term, except for the first, and dividing that term by the preceding term.
The general geometric sequence is $\{a,ar,ar^2,ar^3,\ldots\}$
The general term for a geometric sequence is,

$$
t_n=ar^{n-1}

$$

where $a$ is the first term and $r$ is the common ratio.

## Geometric Series

A geometric series is the expression for the sum of the first $N$ terms of a geometric sequence. It is expressed as,

$$
S_N=\frac{a(r^n-1)}{r-1}=\frac{rt_n-a}{r-1}=\sum \limits_{n=1}^N ar^{n-1}

$$

As the number of terms in the series gets increasingly large, it will either approach an infinite value or a fixed and finite value. The series comes to a fixed value for $|r|<1$. This infinite series can be computed as,
$S_\infty=\frac{a}{1-r}$\subsection{Sequences and Series}

## Summation Notation

Summation notation is a shorthand was to express the sum of a set of numbers. The bottom of the sigma tells you what index to start at and the top of the sigma tells you which number to end at.
Ex: $\sum \limits_{x=1}^5 x=1+2+3+4+5=15$
We can use similar notation for repeated multiplication as well. For this we use an upper case pi and use the same notation, using the starting point, stopping point, and index.
Ex: $\prod \limits_{x=2}^4=2\cdot 3\cdot 4=24$

## Arithmetic Sequence

A sequence is an ordered list of numbers. Each number in the list is referred to as an element or term. Each new term follows a pattern or rule to determine the next term in the sequence.
An arithmetic sequence is an ordered list of terms in which the difference between consecutive terms is constant. It is generally expressed as $\{a,a+d,a+2d,a+3d,\ldots\}$ The formula for the nth term of the sequence is given by,

$$
t_n=a+(n-1)d

$$

where $a$ is the first term, $d$ is the common difference between consecutive terms, and n is the term number.

## Arithmetic Series

An arithmetic series is the sum of all terms that form an arithmetic sequence. $S_n$ represents the sum of the first $n$ terms of a series.

$$
S_N=\frac{N}{2}(a+t_N)=\frac{N}{2}(2a+(N-1)d)=\sum \limits_{n=1}^N (a+(n-1)d)

$$

## Geometric Sequence

Geometric sequences are sequences in which the ratio of consecutive terms is constant. The common ratio, $r$, can be found by taking any term, except for the first, and dividing that term by the preceding term.
The general geometric sequence is $\{a,ar,ar^2,ar^3,\ldots\}$
The general term for a geometric sequence is,

$$
t_n=ar^{n-1}

$$

where $a$ is the first term and $r$ is the common ratio.

## Geometric Series

A geometric series is the expression for the sum of the first $N$ terms of a geometric sequence. It is expressed as,

$$
S_N=\frac{a(r^n-1)}{r-1}=\frac{rt_n-a}{r-1}=\sum \limits_{n=1}^N ar^{n-1}

$$

As the number of terms in the series gets increasingly large, it will either approach an infinite value or a fixed and finite value. The series comes to a fixed value for $|r|<1$. This infinite series can be computed as,

$$
S_\infty=\frac{a}{1-r}

$$
