# Formal Deductive Systems

<!-- Source: [Sections/Introductory_Logic/Formal_Deductive_Systems.tex](../../Sections/Introductory_Logic/Formal_Deductive_Systems.tex) -->

## Classification of Syetem P and Formal Logic

Idea of a proof:
Given $A$ and $A\supset(B\& C)$, can we prove $C$?

```latex
\begin{tabular}{p{3cm}}
    $A$
    $A\supset(B\& C)$
    \hline
    $C$
\end{tabular}\\
```

The first inference has this form:

```latex
\argument{1}{$q\supset q$\\ $p$\\ \hline $\therefore q$} with $p\to A$ and $q\to(B\&C)$\\
```

This form of reasoning is called *Modus Ponens* (MP)
MP has no counterexamples in its truth table so it is a valid inference

Formal Logical System
A natural language (e.g. English):
The alphabet is the set $\{a,A,b,B,\ldots,z,Z\}$
Words: \{apple, red,\ldots\}
An artificial language (Logical system P):
Vocabulary (alphabet) = \{A,B,C,\ldots,$\&,\vee,\sim,\supset,\equiv,(,)$\}
Well-Formed-Formulas (wff) (words) = \{$A,\sim B,(A\supset B),\ldots$\}

3 Formation rules of system P:

- $A,B,C,\ldots$ are wffs
- If $p,q$ are wffs then so are $\sim p,(p\& q),(p\vee q),(p\supset q),(p\equiv q)$
- Np other formulas are wffs

So the set of all wffs of System P, $\sum$, is
$\sum=\{A,B,C,\ldots,\sim A,\sim B,\sim C,\ldots,(A\& B),(B\vee D),(A\equiv Z),\ldots,\sim(B\vee D),\ldots\}$

The *primitive basis* for a formal system (or logic system)
 has two parts:
 An *object language*, defined by a vocabulary and a grammar (or formation rules)
 A *logic* defined by a (possibly empty) set of axioms and a set of transformation rules (or rules of inference)
 Propositions derived from the axioms by means of the rules of inference are called the theorems of the formal system.

 The primitive basis for System P:
 Vocabulary

- an infinite number of propositional constants: $A,B,C,\ldots$
- 5 propositional connectives: $\sim,\vee,\&,\supset,\equiv$
- 2 grouping indicators: $()$

 Grammar:

- three formation rules

 Axioms:

- none

 Transformation Rules:

- 10 conditional rules
- 10 biconditional rules
- 2 hypothetical rules
- truth-tables

 Conditional Transformation Rules

- MP: (modus ponens)

```latex
     \argument{1}{$p\supset q$\\ $p$\\ \hline $\therefore q$}
```

- MT:

```latex
     \argument{1}{$p\supset q$\\ $\sim q$\\ \hline $\therefore \sim p$}
```

- Conjunction

```latex
     \argument{1}{$p$\\$q$\\ \hline $\therefore p\& q$}
```

- Simplification

```latex
     \argument{1}{$p\& q$\\ \hline $\therefore p$} or \argument{1}{$p\& q$\\ \hline $\therefore q$}
```

- Addition

```latex
     \argument{1}{$p$\\ \hline $p\vee q$}
```

- Deductive Syllogism (DS)

```latex
     \argument{1}{$p\vee q$\\ $\sim p$\\ \hline $\therefore q$} or \argument{1}{$p\vee q$\\ $\sim q$\\ \hline $\therefore p$}
```

- Hypothetical Syllogism (HS)

```latex
     \argument{2}{$p\supset q$\\ $q\supset r$\\ \hline $\therefore p\supset r$}
```

- Repetition

```latex
     \argument{1}{$p$\\ \hline $\therefore p$}
```

- Constructive Dilemma (CD)

```latex
     \argument{2}{$p\supset r$\\ $q\supset s$\\ $p\vee q$\\ \hline $\therefore r\vee s$}
```

- Distructive Dilemma (DD)

```latex
     \argument{2}{$p\supset r$\\ $q\supset s$\\ $\sim r\vee \sim s$\\ \hline $\therefore \sim p\vee \sim q$}
```


 Ex: Prove that the following argument is valid:

```latex
 \argument{3}{$(A\&\sim B)\supset C$\\
```

 $A$
 $\sim B$
 \hline
 $A\& C$}
 step by step

$$
\begin{array}{cl}
    1. & (A\&\sim B)\supset C\\
    2. & A\\
    3. & \sim B\\
    \hline
    4. & A\& \sim B by conjunction of 2 and 3\\
    5. & C by MP of 1 and 4\\
    6. & A\& C by conjunction of 2 and 5
\end{array}

$$

Using a truth-table you can confirm that there are no counter examples, therefore, the inference is valid
Any argument can be proved to be valid in terms of truth tables iff there exists a proof of this argument in terms of rules of inference.


```latex
Ex2: Prove that \argument{2}{$A$\\ $A\supset B$\\ $B\supset C$\\ \hline $\therefore C\vee D$} is valid\\
```

We can prove that this is valid using truth tables but this is time consuming. It is much quicker using transformation rules.

$$
\begin{array}{cl}
    1. & A\\
    2. & A\supset B\\
    3. & B\supset C\\
    \hline
    4. & B from MP on 2,1\\
    5. & C from MP on 3,4\\
    6. & C\vee D from addition on 5
\end{array}

$$

For any valid argument there exist (no less than) infinitely many correct proofs using transformation rules
Ex3: prove $W\vee D$

$$
\begin{array}{cl}
    1. & A\\
    2. & (A\vee B)\supset \sim C\\
    3. & \sim C \supset D\\
    \hline
    4. & (A\vee B)\supset D by HS 2,3\\
    5. & A\vee B by addition 1\\
    6. & D by MP 4,5\\
    7. & W\vee D by addition 6
\end{array}

$$

Ex4: prove $D$

$$
\begin{array}{cl}
    1. & (A\vee B)\supset(C\& D)\\
    2. & C\supset E\\
    3. & A\&\sim E\\
    \hline
    4. & A by simp 3\\
    5. & \sim E by simp 3\\
    6. & \sim C by MT 2,5\\
    7. & A\vee B by add 4\\
    8. & C\vee D by MP 1,7\\
    9. & D by DS 8,6
\end{array}

$$

Ex5: prove $\sim D$

$$
\begin{array}{cl}
    1. & (\sim A\&\sim B)\supset(\sim C\vee \sim D)\\
    2. & (E\vee \sim F)\supset \sim A\\
    3. & \sim H\supset(B\supset J)\\
    4. & (\sim F\&\sim H)\supset(\sim\sim C\& \sim J)\\
    5. & \sim H\&(F\supset H)\\
    \hline
    6. & \sim H simp 5\\
    7. & F\supset H simp 5\\
    8. & \sim F MT 7.6\\
    9. & B\supset J MP 3,6\\
    10. & \sim F\&\sim H conj 8,6\\
    11. & \sim\sim C\&\sim J MP 4,10\\
    12. & \sim\sim C simp 11\\
    13. & \sim J simp 11\\
    14. & \sim B MT 9,13\\
    15. & E\vee \sim F add 8\\
    16. & \sim A MP 2,15\\
    17. & \sim A\&\sim B conj 16,14\\
    18. & \sim C\vee \sim D MP 1,17\\
    19. & \sim D DS 18,12
\end{array}

$$

Conditional Rules guidelines:

- Allows us to introduce a new line in a proof on the basis of one or more previous lines
- Indicate the logical form of both the line being introduced and the previous lines used as justification
- Can be applied to the whole formula in a line, not to its smaller subformulas

Biconditional Rules:

- Double Negation (DN)
    $p::\sim\sim p$
    This $::$ means that the left-hand-side is logically equivalent to the right-hand-side. This allows us to substitute one for the other in a proof
- Communication (Comm)
    $p\vee q::q\vee p$ or $p\& q:: q\& p$
- Distribution
    $p\&(q\vee r)::(p\& q)\vee(p\& r)$ or $p\vee(q\& r)::(p\vee q)\&(p\vee r)$
- Contraposition
    $p\supset q::\sim q\supset\sim p$
- Tautology
    $p::p\& p$ or $p::p\vee p$
- Implication
    $p\supset q::\sim p\vee q$
- Association
    $p\&(q\& r)::(p\& q)\& r$ or $p\vee(q\vee r)::(p\vee q)\vee r$
- DeMorgan's Laws
    $\sim(p\& q)::\sim p\vee\sim q$ or $\sim(p\vee q)::\sim p\&\sim q$
- Exportation
    $(p\& q)\supset r::p\supset(q\supset r)$
- Equivalence
    $p\equiv q::(p\supset q)\&(q\supset p)$ or $p\equiv q::(p\& q)\vee(\sim p\&\sim q)$

Ex: prove $\sim\sim C\vee A$

$$
\begin{array}{cl}
    1. & A\vee(B\& C)\\
    \hline
    2. & (A\vee B)\&(A\vee C)\\
    3. & A\vee B\\
    4. & A\vee C\\
    5. & C\vee A\\
    6. & \sim\sim C\vee A
\end{array}

$$

Ex2: Prove $\sim Q\supset P$

$$
\begin{array}{cl}
    1. & P\vee Q\\
    \hline
    2. & \sim\sim P\vee Q DN 1\\
    3. & \sim P\supset Q Impl 2\\
    4. & \sim P\supset \sim\sim Q DN 3\\
    5. & \sim Q\supset P Contra 4
\end{array}

$$


```latex
$\phi \vDash\Psi$ iff the argument \argument{0.7}{$\phi$\\ \hline $\therefore \Psi$} is truth-functionally valid. (called $\phi$ entails $\Psi$)\\
```

$\phi\vdash\Psi$ is $\phi$ implies $\Psi$ and is iff there exists a proof of the argument in terms of transformation rules.
$\phi\vDash\Psi$ iff $\phi\vdash\Psi$
Ex3: prove $Q$

$$
\begin{array}{cl}
    1. & P\equiv \sim Q\\
    2. & \sim(P\vee S)\\
    \hline
    3. & (P\supset\sim Q)\&(\sim Q\supset P) equiv 1\\
    4. & P\supset \sim Q simp 3\\
    5. & \sim Q\supset P simp 3\\
    6. & \sim P\&\sim S DeM 2\\
    7. & \sim P simp 6\\
    8. & \sim S simp 6\\
    9. & \sim \sim Q MT 5,7\\
    10. & Q DN 9
\end{array}

$$

Ex4: prove $U$

$$
\begin{array}{cl}
    1. & P\vee Q\\
    2. & Q\supset(R\& S)\\
    3. & P\supset(U\vee W)\\
    4. & \sim(S\vee W)\\
    \hline
    5. & \sim S\&\sim W DeM 4\\
    6. & \sim S simp 5\\
    7. & \sim W simp 6\\
    8. & \sim R\vee \sim S add 6\\
    9. & \sim(R\& S) DeM 8\\
    10. & \sim Q MT 2,9\\
    11. & P DS 1,10\\
    12. & U\vee W MP 3,11\\
    13. & U DS 12,7
\end{array}

$$

## Conditional Proof

Ex: prove $A\supset C$

$$
\begin{array}{cl}
    1. & (A\vee B)\supset(C\vee \sim D)\\
    2. & D\\
    \hline
    3. & \sim(A\vee B)\vee(C\vee \sim D) imp 1\\
    4. & (\sim A\&\sim B)\vee(C\vee \sim D) DeM 3\\
    5. & (C\vee \sim D)\vee(\sim A\&\sim B) Comm 4\\
    6. & ((C\vee \sim D)\vee \sim A)\&((C\vee \sim D)\vee \sim B) Dist 5\\
    7. & (C\vee \sim D)\vee \sim A simp 6\\
    8. & (C\vee \sim D)\vee \sim B simp 6\\
    9. & C\vee (\sim D\vee\sim A) assoc 7\\
    10. & (\sim D\vee\sim A)\vee C comm 9\\
    11. & \sim D\vee(\sim A\vee C) assoc 10\\
    12. & \sim D\vee(A\supset C) imp 11\\
    13. & \sim\sim D DN 2\\
    14. & A\supset C DS 12,13
\end{array}

$$

For arguments of $p\supset q$ we can assume $p$ and analyze the assumption in the scope of assumption.
Ex: prove $A\supset C$

$$
\begin{array}{cl}
    1. & (A\vee B)\supset(C\vee \sim D)\\
    2. & D\\
    \hline
    3. & A assp (CP)\\
    4. & A\vee B add 3\\
    5. & C\vee\sim D MP 1,4\\
    6. & \sim\sim D DN 2\\
    7. & C DS 5,6\\
    8. & A\supset C CP 3-7
\end{array}

$$

Ex2: prove $(A\& E)\supset \sim K$

$$
\begin{array}{cl}
    1. & (A\vee B)\supset\sim(C\vee D)\\
    2. & (\sim C\& E)\supset F\\
    3. & (F\vee H)\supset K\\
    \hline
    4. & A\& E assp (CP)\\
    5. & A simp 4\\
    6. & E simp 4\\
    7. & A\vee B add 5\\
    8. & \sim(C\vee D) MP 1,7\\
    9. & (\sim C\&\sim D) DeM 8\\
    10. & \sim C simp 9\\
    11. & \sim D simp 9\\
    12. & \sim C\& E conj 10,6\\
    13. & F MP 2,12\\
    14. & F\vee H add 13\\
    15. & \sim K MP 3,14
\end{array}

$$

Ex3: prove $(\sim B\supset\sim A)\supset(A\supset C)$

$$
\begin{array}{cl}
    1. & A\supset(B\supset C)\\
    \hline
    2. & \sim B\supset\sim A assp (CP)\\
    3. & A assp (CP)\\
    4. & A\supset B contra 2\\
    5. & B MP 4,3\\
    6. & B\supset C MP 1,3\\
    7. & C MP 6,5\\
    8. & A\supset C CP 3-7\\
    9. & (\sim B\supset\sim A)\supset(A\supset C) CP 2-8
\end{array}

$$

Indirect Proof
Assume the opposite of the proof and prove a contradiction (i.e. $\phi\&\sim\phi$)
Ex: prove $\sim P$

$$
\begin{array}{cl}
    1. & P\supset Q\\
    2. & (P\& Q)\supset R\\
    3. & R\supset \sim Q\\
    \hline
    4. & \sim\sim P Assp (IP)\\
    5. & P DN 4\\
    6. & Q MP 1,5\\
    7. & P\& Q conj 5,6\\
    8. & R MP 2,7\\
    9. & \sim Q MP 3.8\\
    10. & Q\&\sim Q Conj 6.9\\
    11. & \sim P IP 4-10
\end{array}

$$
