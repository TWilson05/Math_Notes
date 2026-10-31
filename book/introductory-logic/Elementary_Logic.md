# Elementary Logic

<!-- Source: [Sections/Introductory_Logic/Elementary_Logic.tex](../../Sections/Introductory_Logic/Elementary_Logic.tex) -->

## Entailment

An argument is an *entailment* iff (if and only if) its conclusion conclusively follows from its premises
A set of premises *entails* a conclusion iff the conclusion conclusively follows from the premises.
Ex:

```latex
\begin{tabular}{p{8cm}}
    All beagles are dogs
    All dogs are mammals
    \hline
    Therefore, all beagles are mammals
\end{tabular}\\
```

Validity:
An argument or inference is valid iff it is not possible for the premises to be (jointly) true and, at the same times, the conclusion to be false.

Ex:

```latex
\begin{tabular}{p{8cm}}
    All horses are mammals
    All mammals are warm-blooded
    \hline
    Therefore, all horses are warm-blooded
\end{tabular}\\
```

Inference from the premises to the conclusion is good so the argument is valid.

Ex2:

```latex
\begin{tabular}{p{8cm}}
    All people are horses
    All horses have 3 heads
    \hline
    Therefore, all people have 3 heads
\end{tabular}\\
```

Despite the premises being false, the inference from the premises to the conclusion is good so the argument is valid.

Ex3:

```latex
\begin{tabular}{p{8cm}}
    If today is Monday then tomorrow is Tuesday
    Tomorrow is Tuesday
    \hline
    Therefore, today is Monday
\end{tabular}\\
```

The logical skeleton is displayed as the following:

```latex
\begin{tabular}{p{3cm}}
    If $p$ then $q$
    $q$
    \hline
    Therefore, $p$
\end{tabular}\\
```

An example of this is:

```latex
\begin{tabular}{p{10cm}}
    If you are Canadian, then you understand English or French
    You understand English or French
    \hline
    Therefore, you are Canadian
\end{tabular}\\
```

Validity is the matter of the argument's logical form only

Other invalid argument forms:

```latex
\begin{tabular}{p{3cm}}
    If $p$ then $q$
    Not $p$
    \hline
    Therefore, not $q$
\end{tabular}\\
```


```latex
\begin{tabular}{p{3cm}}
    Either $p$ or $q$
    Not $p$
    \hline
    Therefore, not $q$
\end{tabular}\\
```

Valid argument:

```latex
\begin{tabular}{p{3cm}}
    Either $p$ or $q$
    Not $p$
    \hline
    Therefore, $q$
\end{tabular}\\
```


```latex
\begin{tabular}{p{3cm}}
    If $p$ then not $q$
    Either $p$ or $q$
    \hline
    Therefore, either not $p$ or not $q$
\end{tabular}\\
```

Soundness:
An argument or inference is *sound* iff it is valid and it has true premises.

Impossibility vs. Improbability:
Recall that a proposition is *logically necessary* if it is true regardless of how the world might be and it is *logically impossible* if it is false regardless of how the world might be. It is *logically contingent* if it is neither one or the other.

A proposition is *logically impossible* if it is inconsistent with the laws of logic
A proposition is *physically impossible* if it is inconsistent with the laws of nature.
A proposition is *improbable* if it is (not impossible, but) unlikely to be true.

Propositional connectives are words or phrases which, together with one or more propositions, can be used to create new propositions

- ...and
- ...or
- if...then
- ...because

A proposition with no connectives is *atomic*
A proposition with one or more connectives is *molecular* or *compound*.

Propositional constants and variables
Propositional constants are expressed as $A,B,C,\ldots$ which stand for specific propositions which are either true or false.
Propositional variables are expressed as $a,b,c,\ldots$ and stand for arbitrary propositions which are neither true nor false.
(think constants vs. variables in math)
## Conjunction, Disjunction, and Negation

Truth-functional connectives
A *truth-functional connective* is any connective for which the truth values of its resulting molecular propositions are determined solely by the meaning of the connective together with the truth values of its component propositions
Examples:

- $\wedge$ which is used to abbreviate the word ``and"
- $\vee$ which is used to abbreviate one use of the word ``or"
- $\sim$ which is used to abbreviate the phrase ``it is not the case that"

Conjunction, Disjunction, and Negation

Conjunction:

$$
\begin{array}{c|c|c}
    p & q & p\wedge q\\
    \hline
    T & T & T\\
    T & F & F\\
    F & T & F\\
    F & F & F
\end{array}

$$

Disjunction

$$
\begin{array}{c|c|c}
    p & q & p\vee q\\
    \hline
    T & T & T\\
    T & F & T\\
    F & T & T\\
    F & F & F
\end{array}

$$

Negation

$$
\begin{array}{c|c}
    p & \sim p\\
    \hline
    T & F\\
    F & T
\end{array}

$$

Ex: $(p\&q)\vee r$ vs $p\&(q\vee r)$

$$
\begin{array}{c|c|c|c|c}
    p & q & r & (p\&q)\vee r & p\&(q\vee r)\\
    \hline
    T & T & T & T & T\\
    T & T & F & T & T\\
    T & F & T & T & T\\
    T & F & F & F & F\\
    F & T & T & T & F\\
    F & T & F & F & F\\
    F & F & T & T & F\\
    F & F & F & F & F
\end{array}

$$

## Conditionals and Biconditionals

Material conditional and biconditional
Material conditional: if $p$ then $q$

$$
\begin{array}{c|c|c}
    p & q & p\supset q\\
    \hline
    T & T & T\\
    T & F & F\\
    F & T & T\\
    F & F & T
\end{array}

$$

Material biconditional: checks if $p$ and $q$ have the same truth value (analogous to NXOR)

$$
\begin{array}{c|c|c}
    p & q & p\equiv q\\
    \hline
    T & T & T\\
    T & F & F\\
    F & T & F\\
    F & F & T
\end{array}

$$

When we combine multiple logical statements, the *major connective* is the logical statement which is applied last.
Ex: for $(p\&q)\vee(r\&s)$, $\vee$ is the major connective

$\veebar$ denotes the exclusive disjunction (exclusive or).

$$
\begin{array}{c|c|c}
    p & q & p\veebar q\\
    \hline
    T & T & F\\
    T & F & T\\
    F & T & T\\
    F & F & F
\end{array}

$$

Nor:

$$
\begin{array}{c|c|c}
    p & q & p\downarrow q\\
    \hline
    T & T & F\\
    T & F & F\\
    F & T & F\\
    F & F & T
\end{array}

$$

Nand:

$$
\begin{array}{c|c|c}
    p & q & p\uparrow q\\
    \hline
    T & T & F\\
    T & F & T\\
    F & T & T\\
    F & F & T
\end{array}

$$

## Testing Arguments for Validity

Tautology, Contingency, Contradictions
Ex: $p\supset(q\supset p)$

$$
\begin{array}{c|c|c}
    p & q & p\supset(q\supset p)\\
    \hline
    T & T & T\\
    T & F & T\\
    F & T & T\\
    F & F & T
\end{array}

$$

This is called a *tautology* (a logical truth)
More examples:
$p\vee(\sim p)$
$p\supset p$
$\sim(p\supset q)\equiv(p\&\sim q)$
$(p\equiv q)\equiv((p\&q)\vee(\sim p\&\sim q))$

Ex2: $(\sim p\equiv\sim q)\equiv(\sim p\equiv q)$

$$
\begin{array}{c|c|c}
    p & q & (\sim p\equiv\sim q)\equiv(\sim p\equiv q)\\
    \hline
    T & T & F\\
    T & F & F\\
    F & T & F\\
    F & F & F
\end{array}

$$

This is called a *self-contradictory claim* (a logical impossibility)
Some examples:
$p\&\sim p$
$\sim(p\vee \sim p)$
$(p\equiv q)\equiv\sim(p\equiv q)$

Ex3: $p\supset(p\supset q)$

$$
\begin{array}{c|c|c}
    p & q & p\supset(p\supset q)\\
    \hline
    T & T & T\\
    T & F & F\\
    F & T & T\\
    F & F & T
\end{array}

$$

This is called a *contingency*

Truth-table methods for testing validity

```latex
\begin{tabular}{p{2cm}}
    $p\supset q$
    $p$
    \hline
    $\therefore q$
\end{tabular}\\
```

For the argument to be valid, it requires that the conclusion cannot be false if premises are true
Joint truth-table for the whole argument:

$$
\begin{array}{c|c||c|c||c}
    p & q & p\supset q & p & q\\
    \hline
    T & T & T & T & T\\
    T & F & F & T & F\\
    F & T & T & F & T\\
    F & F & T & F & F
\end{array}

$$

There are no counterexamples so it is a valid argument (called Modus Ponens, M.P.)

Ex:

```latex
\begin{tabular}{p{8cm}}
    If Sue is busy, then she is doing well financially
    She is doing well financially
    \hline
    Therefore, Sue is busy
\end{tabular}\\
```

$P$= Sue is busy
$Q$= Sue is doing well financially

```latex
\begin{tabular}{p{2cm}}
    $P\supset Q$
    $Q$
    \hline
    $P$
\end{tabular}\\
```

Joint truth-table:

$$
\begin{array}{c|c||c|c||c}
    p & q & p\supset q & q & p\\
    \hline
    T & T & T & T & T\\
    T & F & F & F & T\\
    F & T & T & T & F\\
    F & F & T & F & F
\end{array}

$$

Row 3 is a counterexample so it is an invalid argument

Steps for testing for validity via truth tables

- Identify the premises and conclusion
- Identify all atomic propositions
- Identify all truth-functional connectives
- Formalize the argument
- Design a truth table
- Complete the truth table
- Test for truth-functional validity by looking for a counterexample

Ex2:

```latex
\begin{tabular}{p{11cm}}
    If Bill throws the fight, Sue will reject him
    If Bill doesn't throw the fight, the mob will take him for a ride
    Either Bill will throw the fight or he will not
    \hline
    Therefore, Sue will reject Bill or the mob will take him for a ride
\end{tabular}\\
```

$P$= Bill throws the fight
$Q$= Sue will reject Bill
$R$= The mob will take Bill for a ride

```latex
\begin{tabular}{p{2cm}}
    $P\supset Q$
    $\sim P\supset R$
    $P\vee \sim P$
    \hline
    $Q\vee R$
\end{tabular}\\
```

Joint truth-table:

$$
\begin{array}{c|c|c||c|c|c||c}
    p & q & r & p\supset q & \sim p\supset r & p\vee \sim p & q \vee r\\
    \hline
    T & T & T & T & T & T & T\\
    T & T & F & T & T & T & T\\
    T & F & T & F & T & T & T\\
    T & F & F & F & T & T & F\\
    F & T & T & T & T & T & T\\
    F & T & F & T & F & T & T\\
    F & F & T & T & T & T & T\\
    F & F & F & T & F & T & T
\end{array}

$$

No counterexample so the argument is valid

Three theories about the meaning of ``unless"

- Bill's dog will not come unless it's called
- Bill's dog will not come if it is not called
- If Bill's dog is not called, it will not come

``$p$ unless $q$" iff ``$p$ if not $q$"
$\to$ ``if not $q$ then $p$"
$\sim q \supset p$


- Mary will be fired unless she shapes up
- Either Mary will shape up or she will be fired

``$p$ unless $q$" iff ``$q$ or $p$"
$\to$ $p\vee q$


- Bill will be late unless Sue phones him
- If Sue doesn't phone him Bill will be late and if Sue does phone him Bill won't be late

``$p$ unless $q$" iff ``(if not $q$ then $p$) and (if $q$ then not $p$)"
$\to$ $(\sim q\supset p)\&(q\supset\sim p)$
$\sim q\equiv p$

Valid arguments with invalid forms:

```latex
\begin{tabular}{p{12cm}}
    If Sue has gone for a walk, then she has gone for a walk on the beach
    She has gone for a walk on the beach
    \hline
    Therefore, Sue has gone for a walk
\end{tabular}\\
```

Has argument form

```latex
\begin{tabular}{p{2cm}}
    $p\supset q$
    $q$
    \hline
    $p$
\end{tabular}
```

This is valid because the two claims are not independent (they are related)

Fallacies of relevance
Many arguments are invalid because they commit the fallacy of *ignoratio elenchi* (their premises are not related to their conclusions)
Ex:

```latex
\begin{tabular}{p{4cm}}
    Bill loves Sue
    \hline
    Therefore, 2+2=4
\end{tabular}
```

## Formal and Informal Logic

Grammatical vs Logical form
The *grammatical form* of a proposition (or of an argument) is the structure of the proposition (or argument) as indicated by the surface grammar of its natural language
The *logical form* of a proposition (or of an argument) is the logically effective structure of the proposition (or argument) as indicated by the meanings of the logical terms it contains
Ex: ``Tom, Dick and Harry lifted the box"
Grammatical form: (Tom, Dick, Harry) lifted the box
Potential logical forms:
(Tom, Dick, Harry) lifted the box
(Tom lifted the box) and (Dick lifted the box) and (Harry lifted the box)

Is validity always a function of an argument's logical form?
*Formalists* claim that all logical properties can be explained using logical form alone
*Anti-formalists* claim that not all logical properties can be explained using logical form alone
Ex: Socrates is a father, therefore, Socrates is male
vs. Socrates is a father [All fathers are male], therefore, Socrates is male

Uniform substitutions:
If you statement depends on a variable, such as $x$, the substitution must be uniform. i.e. if you have several occurrences of $x$ in the same instance, you must substitute the same value for all occurrences of that variable.

Arithmetic:
Numbers: 1,2,3,$\ldots$
Variables: $x,y,z,\ldots$
Logic:
Atomic Propositions: $P,Q,R$
Compound/Molecular Propositions: $(P\&Q),\sim R\supset\sim P,\ldots$
Propositional Variables: $p,q,r$
Propositional Forms: $(p\&q),\sim r\supset\sim p,\ldots$
Note: when doing substitutions, propositions must be well-formed (w.f.f.)
Ex: $P$ is wff
Ex2: $\sim(P\&Q)$ is wff
Ex3: $(P\&Q$ is not wff
Ex4: $\sim \&P$ is not wff
Ex5: $(R\sim P)\vee Q))$ is not wff

Ex: Start with a propositional form: $(p\& q)\vee \sim p$
Substitution 1: $p\to P$ and $q\to Q$
gives $(P\&Q)\vee \sim P$
Substitution 2: $p\to \sim P$ and $q\to\sim Q$
gives $(\sim P\&\sim Q)\vee \sim\sim P$
Note the result is not $(\sim P\&\sim Q)\vee P$. We don't simplify
For any given proposition, there exist infinitely many logically equivalent formulas which are not identical to the original one.

Ex: consider the case $P$ unless $Q$. It can be written as $P\vee Q$, $\sim Q\supset P$, or $\sim P\supset Q$

Formal logic studies the formal (or structural) attributes of propositions that affect validity and other logical properties and obtains a proposition's logical form by uniformly replacing its non-logical terms with variables
Informal logic studies the informal attributes of propositions that affect validity and other logical properties.

Begging the question:
This is a type of argument in the broad sense. It occurs whenever an arguer uses as a premise of his argument any proposition that his opponent presently rejects. (also called the fallacy of *petitio principii*
Moral: One does not defeat an opponent simply by mouthing propositions he already disagrees with

Ex: Student: You can't give me a C!
Prof: Oh, I thought your paper sort of suggested the opposite... Why do you think so?
Student: Why, I'm an A student

Arguing in a circle:
Circular arguments are a type of argument in the narrow sense. It occurs whenever an argument's conclusion simply repeats a premise, or asserts a proposition contained within or that is equivalent to, a premise.
Note: because an opponent is always likely to reject a premise that simply assumes (or presupposes) the very proposition that is supposed to be proved, arguing in a circle is one (main) way of begging the question.

Ex: Sue: Natural selection, roughly, is a theory that only the ``fittest survive"
Bill: Yes, that's what I often hear. But I don't really understand what the predicate ``fittest" mean. How do you define the individuals who are the ``fittest"?
Sue: Well, clearly, these are the ones that leave the most offspring.
Bill: Hold on a second! Doesn't that ``leave the most offspring" mean exactly the same thing as those who survive?
Sue's reply assumes that the fittest individuals leave the most offspring, but she defined the fittest individuals as those that leave the most offspring

Sextus' Puzzle:
Are all valid arguments circular?
Do they assume the very proposition that they are trying to prove? If not, how can they guarantee their conclusions?

The fallacy of equivocation:
The fallacy of equivocation occurs whenever an argument depends inappropriately on a semantic ambiguity or whenever a semantic ambiguity plays a significant but inappropriate role in an argument.

Ex: Criminal actions are illegal, and all murder trials are criminal actions, thus all murder trials are illegal.
Here the term ``criminal actions" is used with two different meanings.

Ex2: The end of a thing is its perfection. Death is the end of life. Therefore, death is the perfection of life
Here the equivocation on the word ``end" (i.e. goal versus termination) making four possible interpretations.

- The *goal* of a thing is its perfection (T)
    Death is the *goal* of life (F)
    Therefore, death is the perfection of life (F)
- The *termination* of a thing is its perfection (F)
    Death is the *termination* of life (T)
    Therefore, death is the perfection of life (F)
- The *goal* of a thing is its perfection (T)
    Death is the *termination* of life (T)
    Therefore, death is the perfection of life (F)
- The *termination* of a thing is its perfection (F)
    Death is the *goal* of life (F)
    Therefore, death is the perfection of life (F)

The fallacy of Amphiboly
The fallacy of ampliboly occurs whenever an argument depends inappropriately on a grammatical, rather than a purely semantic ambiguity or whenever a grammatical ambiguity plays a significant but inappropriate role in an argument

Ex: Thrifty people save old cardboard boxes and waste paper
Therefore, thrifty people waste paper
Waste can have two meanings so it can have the structures

```latex
\begin{tabular}{p{1cm}}
    $p\wedge q$
    \hline
    $q$
\end{tabular} or \begin{tabular}{p{1cm}}
```

    $p\wedge q$
    \hline
    $r$
\end{array}

$$
