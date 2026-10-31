# Arguments

<!-- Source: [Sections/Introductory_Logic/Arguments.tex](../../Sections/Introductory_Logic/Arguments.tex) -->

## Introduction to Arguments, Fallacies, and Logic

Familiar types of logic:

- Quarrels
- Legislative debates
- Labour negotiations
- Diplomatic discussions
- Legal arguments
- Mathematical proofs
- Scientific demonstrations

Arguments in the broad sense:

- attempt to build a case in favour of some claim
- involve the presentation of reasons or evidence (premises) in support of a conclusion
- are social exchanges often involving a series of speech acts uttered by two or more parties
- are governed by a set of rules or standards (sometimes implicit)
- attempt to advance knowledge by justifying or undermining a conclusion

Arguments in the narrow sense are sets of propositions composed of an argument's *premises* and *conclusion*.
Logic, understood broadly, studies arguments in the broad sense.
Logic, understood narrowly, studies arguments in the narrow sense.

**Placing Arguments in Standard Form**
Ex: Archimedes must be either a hero or a martyr. After all, anyone who dies in battle is one or the other. And, as we know, Archimedes perished during the capture of Syracuse.


```latex
\begin{tabular}{p{16cm}}
**Premise 1:** Anyone who dies in battle is either a hero or a martyr
**Premise 2:** Archimedes perished during the capture of Syracuse
\hline
**Conclusion:** Therefore, Archimedes must be either a hero or a martyr
\end{tabular}\\
```

How to place an argument in standard form:

- Identify the premises and conclusion
- Eliminate any unnecessary or redundant words or phrases
- Clarify any ambiguities
- Separate the premises from the conclusion with a horizontal line

How to Handle Sub-Arguments
You could display as one argument or display as separate arguments with the conclusion of the sub-argument becoming a premise of the main argument
Ex2: If Bill wants to live in Auckland, then he has to learn to sail. If Bill has to learn to sail, then he will have to learn navigation. It turns out that Bill does want to live in Auckland. So Bill will have to learn navigation.

Displayed as one argument:

```latex
\begin{tabular}{p{16cm}}
    **Premise: **If Bill wants to live in Auckland, then he has to learn to sail
    **Premise: **If Bill has to learn to sail, then he has to learn navigation
    **Premise: **Bill wants to live in Auckland
    \hline
    **Conclusion: **Therefore, Bill has to learn navigation.
\end{tabular}\\
```

Displayed as two arguments:

```latex
\begin{tabular}{p{16cm}}
    **Premise: **If Bill wants to live in Auckland, then he has to learn to sail
    **Premise: **Bill wants to live in Auckland
    \hline
    **Intermediate Conclusion: **Bill has to learn to sail.
\end{tabular}\\
```


```latex
\begin{tabular}{p{16cm}}
    **Premise: **If Bill has to learn to sail, then he has to learn navigation
    **Premise: **Bill has to learn to sail.
    \hline
    **Conclusion: **Therefore, Bill has to learn navigation.
\end{tabular}\\
```

Ex3: Geometry should not include lines that are strings, in that they are sometimes straight and sometimes curved, since the ratios between straight and curved lines are not known, and I believe cannot be discovered by human minds, and therefore no conclusion based upon such ratios can be accepted as rigorous and exact. [Rene Descartes]


```latex
\begin{tabular}{p{16cm}}
    The strings are sometimes straight and sometimes curved
    The ratios between straight and curved lines are not known and cannot be discovered by human minds
    \hline
    No conclusion based upon the ratios between straight and curved lines can be accepted as rigorous and exact
\end{tabular}\\
```


```latex
\begin{tabular}{p{16cm}}
    No conclusion based upon the ratios between straight and curved lines can be accepted as rigorous and exact
    \hline
    Geometry should not include lines that are strings
\end{tabular}\\
```

**Identifying Propositions**
Propositions are

- bearers of truth (either true/false)
- distinct from questions (interrogatives), commands (imperatives), prayers, etc.
- usually expressed by statements (declarations), but sometimes also by other means, e.g. rhetorical questions

Ex: Sue is visiting Hong Kong.
is a proposition
Ex2: When is Bill's birthday?
not a proposition
Ex3: Who doesn't know London is a great city?
This is a rhetorical question stating that London is a great city
so it is a proposition

**Indicator Words or Phrases for Conclusions**

- thus
- hence
- therefore
- consequently
- which implies that
- so
- it follows that
- for this reason
- we may conclude that
- which proves that

**Indicator Words or Phrases for Premises**

- because
- as
- since
- moreover
- given that
- provided that
- assuming that
- on the grounds that

**Evaluating Arguments**
The quality of an argument depends on

- the truth of the argument's premises
- the strength of the consequence relation that holds between the arguments premises and conclusion

Two main ways to criticize an argument are

- to show that the premises are (likely) not true
- to show that the consequence relation is (likely) not strong

**Consequence Relations**

- If the premises of an argument, when assumed to be true, provide good evidence in favour of that argument's conclusion, the argument has a strong consequence relation
- If the premises of an argument, when assumed to be true, provide poor evidence in favour of that argument's conclusion, the argument has a weak consequence relation
- A consequence relation that is neither strong nor weak is moderate

Ex: Strong

```latex
\begin{tabular}{p{16cm}}
    Socrates is a father
    \hline
    Therefore Socrates is male
\end{tabular}\\
```

Ex2: Moderate

```latex
\begin{tabular}{p{16cm}}
Plato lives in Athens
\hline
Therefore Plato is Greek
\end{tabular}\\
```

Ex3: Weak

```latex
\begin{tabular}{p{16cm}}
Aristotle is male
\hline
Therefore Aristotle is a father
\end{tabular}\\
```

**Deductive Arguments**
A *deductive argument* is one presented with the intention of being judged by *deductive standards*.
An argument meets the standard of deductive adequacy only when it is impossible for its conclusion to be false, assuming that its premises are all true.
The consequence relation is as strong as it can get.

**Inductive Arguments**
An *inductive argument* is one presented with the intention of being judged by *inductive standards*.
An argument meets the standard of inductive adequacy only when it is not deductively adequate and its premises, if true, increase the likelihood of its conclusion also being true.
Ex: Deductive vs. inductive
Deductive:

```latex
\begin{tabular}{p{16cm}}
Russell had a brother
\hline
Russel had a sibling
\end{tabular}\\
```

Inductive:

```latex
\begin{tabular}{p{16cm}}
Russell had a sibling
\hline
Russell had a brother
\end{tabular}\\
```

**Logic vs. Rhetoric**
Rhetoric:

- studies arguments that are *in fact* persuasive
- is defined as the science of persuasion

Logic:

- studies arguments that *ought to be* persuasive or that would be persuasive to an ideally rational agent.
- is defined as the science of reasoned (or rational) persuasion.

## Types of Arguments

**The Quarrel**
**The ``Yes, you did," "No, I didn't" Quarrel**
Sue: I thought you told me that you were going to be at the library last Friday.
Bill: No. Don't you remember? I said I would be at the beach.
Sue: No. You said you would be at the library. Otherwise I would have wanted to go with you.
Bill: You're not remembering things correctly—that was the day I said I would be at the beach!

Bill and Sue disagree about what the facts are. They disagree what premises they share. They have *promissory instability*.

**The``You don't love me anymore" Quarrel**
Bill: You don't love me.
Sue: But I do! How could I call you a "mindless bore" without caring for you enough to risk giving offense, perhaps even losing you?
Bill: Sure, sure. How do I know that this isn't just what you have in mind—losing me, as you call it, or breaking up, as I would say?
Sue: Bill, you just don't understand. Be reasonable.

Bill and Sue agree about the facts but they disagree about what the facts imply. Bill and Sue disagree about what conclusions they should draw. They have *conclusional instability*.

**Definition**:
A *quarrel* is any argument in which:

- the disputants suffer from premissory or conclusional instability (or both)
- lack of a shared method for conflict resolution
- refure to agree to disagree

**Fallacies**
A *fallacy* is:

- a bad argument or inference that has a propensity to appear good
- a common or seductive error in reasoning

Ex: The press should print all news that is in the public interest. The public interest in this murder case is intense. Therefore, the press should print news about this case.

Note that the argument involves an ambiguous phrase "public interest" (meaning "of benefit to the public" versus "of interest to the public"). This is called an *equivocation*.

**The Ad Baculum**
An *ad baculum* argument occurs whenever a conclusion is drawn on the basis of an appeal to force, intimidation, or threat of bad consequences.
If the appeal is relevant, it is non-fallacious
If the appeal is irrelevant, it is fallacious

Ex: Our paper certainly deserves the support of every German. We shall continue to forward copies of it to you, and hope that you will not want to expose yourself to unfortunate consequences in the case of cancellation.

This does not recommend any explicit belief so it is not fallacious.

- If an argument is about what is sensible or prudent to *do*, the argument is not fallacious
- If an argument is about what is sensible or rational to *believe*, the argument is fallacious.

Ex:2 ``Toyota Motor said will build a new plant in Baja, Mexico, to build Corolla cars for U.S. NO WAY! Build a plant in U.S. or pay big border tax." [Donald Trump, 2017]
Not fallacious.

Ex3: Zach: ``My father owns the department store that gives your newspaper forty percent of your advertising revenue, and my understanding is that you don't want to publish any story of my arrest for spray painting the college."
Newspaper editor: ``Yes, Zach, I see your point. The story doesn't seem to be newsworthy.

Whether or not the story deserves the attention of the public needs to be judged by some other criteria, not the ones given by Zach, thus the argument is fallacious.

Ex4: Zach: ``My father owns the department store that gives your newspaper forty percent of your advertising revenue, and my understanding is that you don't want to publish any story of my arrest for spray painting the college."
Newspaper editor: ``Yes, Zach, I see your point. Looks like we shouldn't do it lest we all lose our jobs, indeed.

As a consideration of what the newspaper should do in order to avoid the bad consequences, the appeal is highly relevant, this non-fallacious argument.

**The Ad Hominem**
An ad hominem argument occurs whenever a conclusion is drawn on the basis of an appeal to some fact or alleged fact about one's opponent.
If the appeal is relevant, the argument is non-fallacious
If the appeal is irrelevant, the argument is fallacious

There are two main types of ad hominem

- the *abusive ad hominem*, in which an insulting or unwelcome allegation is advanced about one's opponent
- the *circumstantial ad hominem*, in which a non-abusive allegation is advanced about one's opponent, or about his or her circumstances

Ex: Abusive
No one should trust Sue's argument about hospital funding. After all, I heard that she was fired from her job in the acute care unit.

Ex2: Circumstantial ad hominem
No one should trust Bill's argument about school funding. After all. his sister is a teacher.

Ex3: Critic: ``How can you derive pleasure from gunning down a helpless animal? Surely the killing of deer or trout for amusement is barbarous."
Sportsman: ``If you're so concerned, why do you feed on the flesh of animals? Aren't you being inconsistent?"

**What's so special about logic?**

- Logic is Public. Unlike "feelings" or "intuitions"—which also motivate beliefs but which are essentially private—reasoned arguments provide us with a public mechanism for the resolution of disagreements
- Logic is Safe. Unlike physical means of conflict resolution—which range from personal intimidation to warfare—logic gives us a safe, non-harmful mechanism for the resolution of disagreements
- Logic is Effective. Careful, logical reasoning from acceptable premises to reliable conclusions is the method most likely to lead to accurate beliefs and, hence, the method most likely to help us improve our lives

## Debates

Debates occur in parliaments, congress, diets, bunds, and other government houses, as well as in other contexts. They are well-governed contests of words between two or more sides, presented over by a speaker, referee, or chairperson. They are won and lost depending upon who wins the approval of "the house" or some other jury

The goal of a debate is not explicitly to discover the truth but, rather, to win the approval of the house. It is only through open debate, the public offering of conjecture and criticism, that large scale advances in human knowledge are possible. Because of their structure, debates allow for the type of public conjecture and criticism necessary for advances in human knowledge. Debates remain an effective and objective *route* to the truth.

Social institutions in which knowledge advances through debate includes:

- opposition parties in government
- trial by judge or jury in an adversarial legal system
- peer-reviewed scientific and scholarly journals
- the free press

Advantages:
Because a debate is rule-governed and presided over by a neutral speaker or chairperson, there are clear winners and losers.
Because a debate is resolved by vote of the house, or by some other similar mechanism, total premissory or conclusional agreement among the contending parties is not required.
As long as a debate opens each debater's views to a wide variety of criticism, it is likely to be an effective and objective method for advancing truth.

Disadvantages:
Because the ultimate goal is to win, factors such as *sophistry, insincerity,* and *ambiguity* may be invoked by the participants
Because of *ad populum* arguments and the *bandwagon effect*, group decision-making can be unstable and non-objective
Because many debates are highly regulated, they cease to be free markets for ideas.
Because even eyewitness reports and expert testimony can be unreliable, evidence offered during debates can sometimes be misleading
Because expert testimony can be non-objective, the fallacy of ad verecundiam may be involved
**The Ad Populum**
An ad populum argument occurs whenever a conclusion is drawn, or invited to be drawn, on the basis of an appeal to popular belief.
If the appeal is relevant, the argument is non-fallacious
If the appeal is irrelevant, the argument is fallacious.
There are two main types of ad populum:

- **boosterism** arguments, in which appeal is made to the sentiments or prejudices of one's audience
- **popularity** arguments, in which appeal is made to ``common knowledge" or popular belief more generally

Ex1: Boosterism:
``Your right to bear arms is as Canadian as maple syrup" [John Robson]
In this case, the author merely advances a view that appeals to his intended local audience, namely that being ``free", or ``having a right", to possess a firearm must be taken as an indispensable part of being a ``true" Canadian.

Ex2:
Bill: If your position is that physicians should not be allowed to opt out of medicare, and must be bound entirely by standards and rates set by government, how can you defend the declining standard of health care that is resulting from the current emigration of the best qualified physicians from our community?
Sue: I was born and raised not far from here, and what's clear to me is that the people of this fine community have a right to medical care when family members are in desperate need. I know that, because people support this fundamental right, they also support medicare, regardless of the whims of a lot of fancy, overpaid specialists.

In this case, Sue merely advances a view that appeals to her local audience, namely that medicare is a good thing for their town.

Ex3: popularity:
``Those who say that astrology is not reliable are mistaken. The wisest men of history have all been interested in astrology; kings and queens of all ages have guided the affairs of nations by it."

An appeal to how many people throughout history held this belief
``Those who say ... are mistaken" makes it a fallacious argument

Ex4: popularity:
``The wisest men of history have all been interested in astrology; kings and queens of all ages have guided the affairs of nations by it. So, it probably makes sense to pay attention to what it says and spend some time trying to figure out whether it's really reliable."

As a claim that the position in question (Astrology is reliable), based on the given information, deserves more attention/further investigation, it is totally legitimate, thus a non-fallacious argument

**Enthymemes**
An enthymeme is an argument in which one or more core propositions (a premise or conclusion) is not stated explicitly, but is merely assumed implicitly to be part of the argument.

Ex: Sue will make an excellent kindergarten teacher; everyone who loves children always does, you know.
Premise: Everyone who loves children will make an excellent kindergarten teacher
Premise (implied): [Sue loves children]
Conclusion: Sue will make an excellent kindergarten teacher

Ad populum arguments as enthymemes:

```latex
\begin{tabular}{p{5cm}}
    Everyone believes p
    \hline
    Therefore, p is true
\end{tabular}\\
```

Ex:

```latex
\begin{tabular}{p{6cm}}
    Everyone believes that water is wet
    \hline
    Therefore, water is wet
\end{tabular}\\
```

We can add the implied premise [Water's being wet is the best explanation of the fact that everyone believes that water is wet]

Evaluating arguments as enthymemes:
Before judging an argument to be fallacious, we must determine whether the argument is an enthymeme.
If it is an enthymeme, we must reconstruct the argument showing all unstated propositions
We should apply the *principle of clarity* when reconstructing enthymemes. (i.e. we should give people the benefit of the doubt, though not be so charitable that we add what was not intended)

**The Ad Verecundiam**
An ad verecundiam argument occurs whenever a conclusion is drawn, or invited to be drawn, on the basis of an appeal to the expert opinion of an authority.
If the appeal is relevant, the argument is non-fallacious
If the appeal is irrelevant, the argument is fallacious

Ex: My favourite basketball player recommends using this brand of toothpaste; he's obviously successful, so I think I'll try it

This is fallacious because he's not an expert in the field of dentistry.

Ex2: My doctor tells me that I have pneumonia and that I need to take my medicine and stay in bed, so I think I better do what I'm told

This is non-fallacious as the expertise is relevant

Conditions for arguments from authority

- The authority must have special competence in an area, and not simply glamour, prestige, or popularity
- The judgment of the authority must be within his or her special field of competence
- The authority must be interpreted correctly
- Direct evidence must always be available, at least in principle
- The authority must not be hand-picked from among competing experts because of his or her opinion
- A consensus technique is required for adjusting disagreements among equally qualified authorities

Locke's ad verecundiam argument

```latex
\begin{tabular}{p{16cm}}
    Proposition p is endorsed by people who are experts on this matter
    \hline
    Therefore, it is immodest of you, indeed it is a kind of insolence, to persist in your opposition to p.
\end{tabular}\\
```

The Port Royal ad verecundiam fallacy

```latex
\begin{tabular}{p{12cm}}
    Proposition p is endorsed by people who are superior social rank
    \hline
    Therefore, it is appropriate to agree to p
\end{tabular}\\
```

De Facto vs. De Jure Authorities
A de facto authority is someone who is an expert in a given field
A de jure authority is someone who has particular abilities as a result of his or her title or office

Ex:
An expert forensic accountant who tells you that you are entitled to a payment of \$10,000 from your employer
vs. a trial judge who tells you that you are entitled to a payment of \$10,000 from your employer

**The Ad Misericordiam**
Ad ad misericordiam argument occurs whenever a conclusion is drawn, or invited to be drawn, on the basis of an appeal to mercy or pity
If the appeal is relevant, the argument is non-fallacious
If the appeal is irrelevant, the argument is fallacious

Ex: Although the accused was rightly convicted of a serious crime, and although the sentence proposed by the prosecution would be just, the court is asked to show the accused mercy, owing to his bad health and advanced age.

Emotive fallacies
These occur whenever emotion interferes inappropriately with the ultimate goals of argument
Examples: ad hominem (abusive), ad populum (boosterism), ad misericordiam

## Dialectic

**Aristotle's Basic Rules of Dialectic**
A dialogue or dialogical argument involves a discussion or dialogue between two or more parties.
A dialectical argument is a specific type of dialogical argument. It involves questions and answers between two or more parties.

- *Examination arguments* are used to discover what prepositions two parties jointly hold, and what follows from these or other propositions.
- *Instruction (or Socratic) arguments* are used whenever a teacher directs a student to the right answer by asking a series of questions.
- *Refutation arguments* are arguments used to show that a respondent accepts contradictory propositions and to show that a respondent cannot consistently defend a thesis

Ex: Examination
Child: Why do I have to do what I'm told?
Parent: Because I want you to be safe. You want to be safe, too, don't you?
Child: Yes
Parent: Well, doing what you're told will help keep you safe
Child: Why?
Parent: Because I know what’s safe and what isn’t.
Child: So when I know what’s safe and what isn’t, then I won’t have to do what I’m told.
Parent: Yes. By then you’ll be able to choose what to do yourself.
Child: Okay.

Ex2: Instruction
Student: Why are there infinitely many prime numbers?
Teacher: Think about it this way: assume that there are only finitely many prime numbers. Now multiply them all together and then add one. Would this new number be prime?
Student: No, because it would be bigger than every prime number.
Teacher: And would it be composite (i.e. evenly divisible by some prime)?
Student: No, since it would always have one as a remainder.
Teacher: And must every number be either prime or composite?
Student: Yes.
Teacher: So it follows that ...
Student: ... that there can be no such number and the assumption that there are only finitely many primes must be false.

Ex3: Refutation
Lawyer: Where were you on the evening of November 15th?
Witness: At home watching television with my brother.
Lawyer: And why do you remember this so clearly?
Witness: Because we always watch Monday night football together.
Lawyer: So you’d remember if you weren’t at home that night?
Witness: Yes.
Lawyer: But it turns out that you signed several credit card receipts for dinner and the movies on the evening of the 15th.
Witness: I guess I did.
Lawyer: So it’s not true that you remember watching football with your brother that night?
Witness: I guess not.

Possible results of a refutation argument:
Refutation in the *strong sense* is when a thesis or proposition is refuted in the strong sense when it is shown to be false
Refutation in the *weak sense* is when a thesis or proposition is refuted in the weak sense when it is shown that a respondent has insufficient grounds for holding it.
A *stalemate* occurs when all participants concede that the questioner is not going to succeed in refuting the respondent's thesis in either the strong or the weak sense.

Eight rules of dialectic:

- **Selecting Participants:** are the participants equally matched?
- **Defining a Goal:** is this a refutation? An instruction argument? An examination argument?
- **Questioning the Respondent:** does the questioner ask clear and straightforward questions?
- **Responding to the Questioner:** does the respondent reply truthfully and consistently?
- **Dealing with Ignorance:** how does the respondent deal with ignorance?
- **Postponing Answers:** are answers only postponed only by mutual consent?
- **Terminating the Exchange:** how is the dialogue terminated?
- **Changing Dialectic Roles:** are changes in dialectic roles made only by mutual consent?

**The Ad Ignorantiam**
An ad ignorantiam argument occurs whenever a conclusion is drawn, or invited to be drawn, on the basis of an appeal to ignorance.
If the appeal is relevant, the argument is non-fallacious
If the appeal is irrelevant, the argument is fallacious

Ex:

```latex
\begin{tabular}{p{8cm}}
    A cure for cancer hasn't been found
    \hline
    Therefore, no cure for cancer can be found
\end{tabular}\\
```

This is fallacious
Ex2:

```latex
\begin{tabular}{p{8cm}}
    The existence of ghosts has not yet been proved
    \hline
    Therefore, ghosts do not exist
\end{tabular}\\
```

This is also fallacious

Ad ignoranciam fallacies confuse refutations in the strong sense with refutations in the weak sense

```latex
\begin{tabular}{p{8cm}}
    You are unable to provide proof of your thesis
    \hline
    Therefore, your thesis must be false
\end{tabular}\\
```

Autoepistemic Reasoning:
In contrast, some ad ignorantiam arguments are valid

```latex
\begin{tabular}{p{8cm}}
    If $p$ were the case, I would know that $p$
    But I don't know that $p$
    \hline
    Therefore, it is not the case that $p$
\end{tabular}\\
```

Ex:

```latex
\begin{tabular}{p{16cm}}
    If I am in the middle of a blizzard, then I would know that I am in the middle of a blizzard
    But I do not know that I am in the middle of a blizzard
    \hline
    Therefore, it is not the case that I am in the middle of a blizzard
\end{tabular}\\
```

Another non-fallacious ad ignorantiam
Sometimes ignorance of the consequences of actions or policies also justifies caution in decision-making
Ex:

```latex
\begin{tabular}{p{16cm}}
    We are currently ignorant of the biological and social consequences of human cloning
    \hline
    Therefore, human cloning ought not to be permitted at the present time
\end{tabular}\\
```

Logical Necessities
A proposition is *logically necessary* (or a logical truth) if it is true regardless of how the world might be
Ex: Socrates was born in Athens or it's not the case that Socrates was born in Athens

Logical impossibilities:
A proposition is logically impossible (or a logical falsehood) if it is false regardless of how the world might be
Ex: Socrates was born in Athens and it's not the case that Socrates was born in Athens

Logical Contingency:
A proposition is logically contingent if it is neither logically necessary nor logically impossible
Ex: Socrates was born in Athens
Ex: If Socrates was born in Athens then his father was Greek

**The Fallacy of Complex Questions**
The fallacy of complex question occurs whenever

- a question contains a hidden, illicit, or unsupported assumption
- it involves two or more questions rolled into one assumption
- it is misleading because it makes it difficult for a respondent to counter false or unjustified presuppositions

Ex: have you stopped beating your dog?

Safe and risky questions:
Questions ask respondents to select between a series of alternative propositions. These alternative propositions are the question's *direct answers*. Any proposition implied by all of a question's direct answers is a *presupposition* of that question. A question is *safe* if all its presuppositions are logically necessary. A question is risky if it is not safe.
Safe questions cannot mislead us since none of their presuppositions can be false. A question is *moderately safe* if all of its presuppositions are true. Moderately safe questions will not normally mislead us since none of their presuppositions are false.

Ex: Is the ambassador to Australia or is she the ambassador to New Zealand?
Direct answers:

- She is the ambassador to Australia
- She is the ambassador to New Zealand

Sample presupposition: She is the ambassador to Australia or she is the ambassador to New Zealand
Evaluation: This question is risky since some of its presuppositions are not necessarily true.

Ex2: Is she the ambassador to Australia or not?
Direct answers:

- She is the ambassador to Australia
- It is not the case that she is the ambassador to Australia

Sample presupposition: She is the ambassador to Australia or it is not the case that she is the ambassador to Australia.
Evaluation: This question is safe since all its presuppositions are necessarily true

Ex3: Is the king of the U.S.A. is coming to UBC next week?
Direct answers:

- Yes, the king of the US is coming to UBC next week
- No, the king of the US is not coming to UBC next week

A presupposition: At least, the king of the US exists now
Evaluation: question is not safe

Ex4: Is the queen of England coming to UBC next week?
Direct answers:

- Yes, the queen of England is coming to UBC next week
- No, the queen of England is not coming to UBC next week

A presupposition: Queen of England exists, but it is not necessarily true. (England may not have a queen at that time)
Evaluation: It is risky, not safe, yet it is moderately safe
