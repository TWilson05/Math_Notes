# Logic

<!-- Source: [Sections/Mathematical_Proof/Logic.tex](../../Sections/Mathematical_Proof/Logic.tex) -->

## Statement Types and Definitions

A statement is a sentance that is either true or false and will have exactly one of those truth values. They are fact and lack subjectvity.
Types of Statements:

- Axiom: statements we accept as true without proof
    Ex: let $m,n\in\Z$ then $m+n$ is also an integer
- Fact: statements we accept as true without proof
    Ex: let $x\in\R$ then $x^2\geq0$
- Theorem: an important true statement
- Collary: a statement that follows from a previous theorem
- Lemma: a true statement that helps us prove a more important result
- Result/Proposition: true statements that we will prove are called results (or propositions if more important)

Even/odd numbers:

- An integer is even if it can be written as $n=2k$ for some $k\in\Z$
- An integer is odd if it can be written as $n=2l+1$ for some $l\in\Z$

Divisibility:

- Let $n,k\in\Z$. We say that $k$ divides $n$ if there is $l\in\Z$ so that $n=lk$. We write this as $k|n$ and say that $k$ is a divisor of $n$ and that $n$ is a multiple of $k$
- Let $n\in\N$. We say that $n$ is a prime when it has exactly two positive divisors ($1$ and itself).
    If $n$ has more than two positive divisors then we say it is composite
    Finally, the number 1 is neither prime nor composite
- The greatest common divisor of $a$ and $b$ is the largest positive integer that divides both $a$ and $b$.
    Ex: $\mathrm{GCD}(4,6)=2$
- The least common multiple of $a$ and $b$ is the smallest positive integer divisible by both $a$ and $b$.
    Ex: $\mathrm{LCM}(8,6)=24$
- Let $a,b\in\Z$ and $n\in\N$. We say that $a$ is congruent to $b$ modulo $n$ when $n|(a-b)$. The $n$ is referred to as the *modulus* and we write the congruence as $a\equiv b(\modu n)$
    When $n\nmid (a-b)$ we say that $a$ is not congruent to $b$ modulo $n$ and write $a\not\equiv b(\modu n)$
    Ex: $5\equiv 1(\modu4)$
    Ex2: $17\equiv1(\modu4)$
    Ex3: $3\not\equiv9(\modu4)$

## Set Notation

A set is defined as a collection of objects.
The objects are referred to as elements or members of the set.
Common notation uses capital letters for sets and lowercase numbers for elements.
The only question we can ask a set is ``is this object in the set"
If $a$ is an element of the set $A$, we write $a\in A$. If not, we write $a\notin A$.
The empty set is defined by $\varnothing=\{\}$
For small sets, we can define them by listing the elements. i.e. $B=\brcurly{1,2,3,4}$. However, for larger sets, we may make use of ellipses to represent skipped elements or using set builder notation.
Set builder notation is defined as:

$$
S=\brcurly{\text{expression }|\text{ rule}}

$$

Ex: $A=\brcurly{n^2|\text{\ensuremath{n} is a whole number}}=\brcurly{0,1,4,9,36,\ldots}$
Ex2: Rational Numbers: $\Q=\brcurly{\frac{a}{b}|a\in\Z,b\in\N}$
The number of elements in a set $S$ is called the cardinality of the set and is represented by $|S|$.
Ex: $|\varnothing|=0$
Ex2: $|\brcurly{1,2,3}|=3$
Ex3: $|\brcurly{\varnothing,\brcurly{1,2}}|=2$
## Logical Statements

A big part of math is proving that statements are true. We do this by starting from know facts (axioms, lemmas, theorems) and combining these facts using logic to build new facts.

An *open sentence* is a sentence whose truth value depends on the variable(s) that it contains (denoted by $P(x)$). i.e. the statement $x>3$ is open as its truth value is dependent on the value of $x$.

Negation:
Given $P$, we can form a new statement with the opposite truth value. This is typically denoted with either $\sim P$, $\neg P$, or $!P$
Ex: The negation of ``It is Tuesday" would be ``It is not Tuesday".
Truth table:

$$
\begin{array}{c|c}
P & \sim P\\
\hline
T & F\\
F & T
\end{array}

$$

It also follows that the negation of a negation is the original statement: $\sim(\sim P)=P$.

Conjunction and Disjunction:
This is analogous to ``and" and ``or".
The *conjunction* of $P$ and $Q$ is defined to be ``$P$ and $Q$", denoted by $P\wedge Q$
The *disjunction* of $P$ and $Q$ is defined to be ``$P$ or $Q$ inclusive", denoted by $P\vee Q$
This can be represented in the following truth table:

$$
\begin{array}{c|c|c|c}
    P & Q & P\wedge Q & P\vee Q\\
    \hline
    T & T & T & T\\
    T & F & F & T\\
    F & T & F & T\\
    F & F & F & F
\end{array}

$$

The conditional:
The *conditional* (or implication) is defined as ``If $P$ then $Q$", where the hypothesis is $P$ and the conclusion is $Q$. This is denoted by $P\Ra Q$
So, if $P$ is true, and $P\Ra Q$ is true then $Q$ must also be true. In the case where $P$ is false, this tells us nothing about $Q$. This can be summarized in the truth table:

$$
\begin{array}{c|c|c}
    P & Q & P\Ra Q\\
    \hline
    T & T & T\\
    T & F & F\\
    F & T & T\\
    F & F & T
\end{array}

$$

When formulating a proof, we want to prove that $P\Ra Q$ is always true and can then use *modus ponens* to prove the truth of $Q$.
Modus ponens is typically a proof with the following structure:

- Assume that hypothesis $P$ is true
- We see that $P$ implies $P_1$
- From this we know that $P_1$ implies $P_2$
    $\vdots$
- From $P_n$ we know that $Q$ must be true $\square$

With implications, we can also define the converse, contrapositive, and biconditional
Given $P\Ra Q$, the *converse* is defined to be $Q\Ra P$ and the *contrapositive* is defined to be $(\sim Q)\Ra (\sim P)$

$$
\begin{array}{c|c||c|c|c}
    P & Q & P\Ra Q & Q\Ra P & (\sim Q)\Ra (\sim P)\\
    \hline
    F & T & T & T & T\\
    T & F & F & T & F\\
    F & T & T & F & T\\
    F & F & T & T & T
\end{array}

$$

It is worth noting that the contrapositive is identical to the implication. This can be very useful in proofs because in some cases, the contrapositive may be easier to prove.
One more logical statement is the *biconditional* which is when $P\Ra Q$ and $Q\Ra P$ are both true. It is defined as ``$P$ if and only if $Q$", denoted by $P\Leftrightarrow Q$

$$
\begin{array}{c|c||c|c|c}
    P & Q & P\Ra Q & Q\Ra P & P\Leftrightarrow Q\\
    \hline
    F & T & T & T & T\\
    T & F & F & T & F\\
    F & T & T & F & F\\
    F & F & T & T & T
\end{array}

$$
