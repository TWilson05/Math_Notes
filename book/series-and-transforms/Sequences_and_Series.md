# Sequences and Series

<!-- Source: [Sections/Series_and_Transforms/Sequences_and_Series.tex](../../Sections/Series_and_Transforms/Sequences_and_Series.tex) -->

## Convergence of Sequences and Series

Recall, a sequence is a list of infinitely many numbers with a specified order

$$
\brcurly{a_n=f(n)}_{n=1}^\infty=\brcurly{a_1,\,a_2\,a_3,\ldots,\,a_n}

$$

A sequence converges if $a_n$ approaches $A$ as $n\to\infty$.

$$
\begin{aligned}
    \lim_{n\to\infty}a_n=A
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex: }\brcurly{a_n=\frac{1}{n}}_{n=1}^\infty=\lim_{n\to\infty}\frac{1}{n}=0
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex2: }\brcurly{a_n=(-1)^n}_{n=0}^\infty=\brcurly{1,-1,1,-1,\ldots}\therefore\text{ divergent}
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex3: }\brcurly{\frac{2x^2+3}{n^2+n}}_{n=1}^\infty=\lim_{n\to\infty}\frac{2n^2+3}{n^2+n}=2
\end{aligned}

$$

A series is when all the terms of a sequence are summed.
Geometric Series:

$$
\sum_{n=1}^\infty ar^n=\frac{a}{1-r}\text{ if $|r|<1$}

$$

where $a$ is the first term in the series and $r$ is the common ratio.
Proof:

$$
\begin{aligned}
    &S_N=\sum_{n=1}^\infty ar^n=a(1+r+r^2+\cdots+r^N)\\
    &rS_N=a(r+r^2+r^3+\cdots+r^N+r{N+1}\\
    &rS_N-S_N=a(r+r^2+r^3+\cdots+r^N+r{N+1}-S_N=a(r^{N+1}-1)\\
    &(1-r)S_N=a(1-r^{N+1})\\
    &S_N=\frac{a(1-r^{N+1})}{1-r}\\
    &S_\infty=\frac{a}{1-r}
\end{aligned}

$$

Ex: find the infinite sum of ${S=9-\frac{27}{5}+\frac{81}{25}-\frac{243}{125}+\cdots}$

$$
\begin{aligned}
    &S=9\brround{1-\frac{3}{5}+\brround{\frac{3}{5}}^2-\brround{\frac{3}{5}}^3+\cdots}\\
    &a=9,\,r=-\frac{3}{5}\\
    &|r|<1\,\therefore\,\text{convergent}\\
    &S_\infty=\frac{a}{1-r}=\frac{9}{1-3/5}=\frac{45}{8}
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex2: }&S=\sum_{n=1}^\infty\frac{4^n+5^n}{9^n}\\
    &S=\sum_{n=1}^\infty\brround{\frac{4}{9}}^n+\sum_{n=1}^\infty\brround{\frac{5}{9}}^n\\
    &S=\frac{4/9}{1-4/9}+\frac{5/9}{1-5/9}=\frac{41}{20}
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex3: }&\sum_{n=0}^\infty\frac{3^n}{8^{2n+1}}\\
    &S=\frac{1}{8}\sum_{n=0}^\infty\frac{3^n}{8^{2n}}=\frac{1}{8}\sum_{n=0}^\infty\brround{\frac{3}{8^2}}^n=\frac{1/8}{1-3/64}=\frac{8}{61}
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex4: }&\text{write the decimal \ensuremath{0.1\overline{23}} as a fraction}\\
    &0.1\overline{23}=\frac{1}{10}+\frac{23}{10^3}+\frac{23}{10^5}+\cdots=\frac{1}{10}+\frac{12}{10^3}\sum_{n=0}^\infty\brround{\frac{1}{100^n}}\\
    &S=\frac{1}{10}+\frac{23/1000}{1-1/100}=\frac{122}{990}
\end{aligned}

$$

Telescoping Series:
Telescoping series are typically in the form of

$$
S=\sum_{n=1}^\infty(a_n-a_{n+1})=(a_1-a_2)+(a_2-a_3)+\cdots+(a_{N-1}-a_N)=a_1-a_N

$$

$$
\begin{aligned}
    &S_\infty=\lim_{N\to\infty}(a_1-a_N)\\
    &\text{if }\lim_{N\to\infty}a_N=A\\
    &\text{then }S_\infty=a_1-A
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex: }&\sum_{n=1}^\infty\frac{1}{n(n+1)}\\
    &=\sum_{n=1}^\infty\brround{\frac{1}{n}-\frac{1}{n+1}}\\
    &\text{set }a_n=\frac{1}{n}\Ra \lim_{n\to\infty}a_n=0\\
    &S=a_1-A=1-0=1
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex2: }&\sum_{n=3}^\infty\brround{\cos\brround{\frac{\pi}{n}}-\cos\brround{\frac{\pi}{n+1}}}\\
    &=\cos\frac{\pi}{3}-\cos\frac{\pi}{4}+\cos\frac{\pi}{4}-\cos\frac{\pi}{5}+\cdots\\
    &S=\cos\brround{\pi}{3}-\lim_{N\to\infty}\cos\brround{\frac{\pi}{N+1}}=\frac{1}{2}-1=-\frac{1}{2}
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex3: }&\sum_{n=1}^\infty\ln\brround{1+\frac{1}{n}}\\
    &\sum_{n=1}^\infty\ln\brround{\frac{n+1}{n}}=\sum_{n=1}^\infty(\ln(n+1)-\ln(n))\\
    &S=\ln2-\ln1+\ln3-\ln2+\cdots+\ln(N+1)-\ln(N)\\
    &S=-\ln1+\ln(N+1)\to\infty\\
    &\therefore \text{ series diverges}
\end{aligned}

$$

## Convergence Tests

**Divergence Theorem:**
If $\{a_n\}_{n=1}^\infty$ does not converge to 0, then $\displaystyle{\sum_{n=1}^\infty a_n}$ diverges

$$
\begin{aligned}
    \text{Ex: }&\sum_{n=1}^\infty\frac{2n+1}{4n+4}\text{ diverges because }\lim_{n\to\infty}\frac{2n+1}{4n+4}\neq 0
\end{aligned}

$$

**Integral Test:**
The integral test allows us to compare the convergence of sums to those of integrals of the same function such that for $f(n)=a_n$, $f(x)>0$ and $f'(x)<0$, we get that

$$
\begin{aligned}
    &\text{if }\int_{N_0}^\infty f(x)dx\text{ converges, then }\sum_{n=N_0}^\infty a_n\text{ converges}\\
    &\text{if }\int_{N_0}^\infty f(x)dx\text{ diverges, then }\sum_{n=N_0}^\infty a_n\text{ diverges}
\end{aligned}

$$

The sums and integrals compare in the following way:

$$
\left|\sum_{n=a}^\infty f(n)-\int_a^\infty f(x)dx\right|<f(a)

$$

More simply put,

$$
\sum_{n=2}^\infty f(n)=\sum_{n=1}^\infty f(n)-a_1\leq\int_1^\infty f(x)dx\leq \sum_{n=1}^\infty f(n)

$$

Ex: For what values of $p\geq 0$ does $\displaystyle{\sum_{n=2}^\infty\frac{1}{n(\ln(n))^p}}$ converge?

$$
\begin{aligned}
    &f(x)=\frac{1}{x(\ln x)^p},\,N_0=2\\
    &I=\int_2^\infty\frac{dx}{x(\ln x)^p}\\
    &u=\ln x\Ra du=\frac{dx}{x}\\
    &I=\int_{\ln2}^{\ln\infty}\frac{du}{u^p}\\
    &\therefore\text{ by \ensuremath{p} test, converges only if }p>1
\end{aligned}

$$

We can also use the integral test to estimate remainders.
$R_N=S_\infty-S_N$. So $R_N$ is essentially the tail of the series: $R_N=a_{N+1}+a_{N+2}+\cdots$

$$
\int_{N+1}^\infty<R_N<\infty_N^\infty f(x)dx

$$

$$
\begin{aligned}
    \text{Ex: }&\text{Estimate \ensuremath{R_{100}} for }\sum_{n=1}^\infty\frac{1}{n^2}\\
    &\text{let }f(x)=\frac{1}{x^2}\\
    &\int_{101}^\infty\frac{dx}{x^2}<R_{100}<\int_{100}^\infty\frac{dx}{x^2}\\
    &\frac{1}{101}<R_{100}<\frac{1}{100}
\end{aligned}

$$

This means that the tail of the series in this example only impacts the 2nd decimal place
**Comparison Test:**
If $|a_n|\leq c_n$ and $\sum c_n$ converges, then $\sum a_n$ converges

$$
\begin{aligned}
    \text{Ex: }\sum_{n=1}^\infty\frac{1}{n^2}\text{ converges and }\frac{1}{n^2+1}<\frac{1}{n^2}\,\therefore\,\sum_{n=1}^\infty\frac{1}{n^2+1}\text{ converges}
\end{aligned}

$$

**Limit Comparison Test:**
If $\displaystyle{\lim_{n\to\infty}\frac{a_n}{b_n}=L}$ for $L\neq 0$ then the convergence of $a_n$ will math the convergence of $b_n$. i.e. if $b_n$ diverges then so must $a_n$.
We choose $b_n$ such that we know its convergence and it provides useful information

$$
\begin{aligned}
    \text{Ex: }&\sum_{n=1}^\infty\frac{n^2+\sin(n)}{n^4}\\
    &\text{set }b_n=\frac{1}{n^2}\\
    &\lim_{n\to\infty}\frac{a_n}{b_n}=\lim_{n\to\infty}\frac{\ds\brround{\frac{n^2+\sin(n)}{n^4}}}{\ds\brround{\frac{1}{n^2}}}=1\\
    &\text{limit exists and }L\neq 0\text{ so limit comparison test is valid}\\
    &b_n\text{ converges }\therefore\,a_n\text{ converges}
\end{aligned}

$$

**Alternating Series Test:**
For $a_n=(-1)^nb_n$ and $|a_n|\geq|a_{n+1}|$ then if $\displaystyle{\lim_{n\to\infty}|a_n|}=0$, $\sum a_n$ converges

$$
\begin{aligned}
    \text{Ex: }&\sum_{n=1}^\infty(-1)^{n-1}\frac{\sqrt{n}}{n+4}\\
    &b_n=\frac{\sqrt{n}}{n+4}\Ra b_n'=\frac{\ds\frac{n+4}{2\sqrt{n}}-\sqrt{n}}{\ds(n+4)^2}<0\text{ if }n>4\\
    &\lim_{n\to\infty}b_n=0\\
    &\therefore\text{ by the alternating series test, the series converges}
\end{aligned}

$$

We estimate the remainder of an alternating series using

$$
R_N=|S-S_N|\leq b_{n+1}

$$

Ex: How many terms are needed to get an error of $2.5\cdot 10^{-8}$ for $e^{-1}$

$$
\begin{aligned}
    &\text{recall }e^x=\sum_{n=0}^\infty\frac{x^n}{n!}\\
    &e^{-1}=\sum_{n=0}^\infty\frac{(-1)^n}{n!}\\
    &R_N=|S-S_N|\leq\frac{1}{(N+1)!}\Ra \brvertical{\frac{1}{e}\leq \frac{1}{(N+1)!}}\\
    &\text{guess }N=10\Ra \frac{1}{(10+1)!}\sim2.5\cdot10^{-8}
\end{aligned}

$$

**Absolute and Conditional Convergence:**
If $\sum|a_n|$ converges then $\sum a_n$ is said to converge absolutely
If $\sum a_n$ converges but $\sum|a_n|$ diverges then $\sum a_n$ is said to be conditionally convergent

$$
\begin{aligned}
    \text{Ex: }&\sum_{n=1}^\infty\frac{(-1)^n}{n}\\
    &|a_n|=\frac{1}{n}\\
    &\sum_{n=1}^\infty\frac{1}{n}\text{ diverges by the integral test}\\
    &\therefore\text{ the series is conditionally convergent}
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex2: }&\sum_{n=1}^\infty\frac{(-1)^n}{n^2}\\
    &|a_n|=\frac{1}{n^2}\\
    &\sum_{n=1}^\infty\frac{1}{n^2}\text{ converges by the integral test}\\
    &\therefore\text{ the series is absolutely convergent}
\end{aligned}

$$

**Ratio Test:**
The ratio test is set up in the form

$$
\lim_{n\to\infty}\brvertical{\frac{a_{n+1}}{a_n}}=L

$$

If $L>1$, $a_n$ diverges
If $L<1$, $a_n$ converges
If $L=1$, the test fails and does not tell us anything about the convergence

$$
\begin{aligned}
    \text{Ex: }&\sum_{n=1}^\infty(-1)\frac{n!}{5^n}\\
    &\lim_{n\to\infty}\brvertical{\frac{a_{n+1}}{a_n}}=\lim_{n\to\infty}\frac{\ds\brround{\frac{(n+1)!}{5^{n+1}}}}{\ds\brround{\frac{n!}{5^n}}}=\lim_{n\to\infty}\frac{5^n}{5^{n+1}}\cdot\frac{(n+1)!}{n!}=\lim_{n\to\infty}\frac{n+1}{5}=\infty\\
    &\therefore\text{ the series diverges}
\end{aligned}

$$

## Power Series

A power series is a particular series in the form of

$$
\sum_{n=0}^\infty A_n(x-c)^n=A_0+A_1(x-c)+A_2(x-c)^2+\cdots

$$

$\displaystyle{\sum_{n=0}^\infty A_n(x-c)^n}$ converges if $|x-c|<R$ and diverges if $|x-c|>R$ for where $R$ is the radius of convergence.

$$
\begin{aligned}
    \text{Ex: }&\sum_{n=0}^\infty\frac{x^n}{n!}\\
    &\lim_{n\to\infty}\brvertical{\frac{a_n}{a_{n+1}}}=|x|\lim_{n\to\infty}\brround{\frac{1}{n+1}}=0\\
    &\therefore\text{ series converges for all \ensuremath{x}}\\
    &\Ra R=\infty
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex2: }&\sum_{n=0}^\infty n!x^n\\
    &\lim_{n\to\infty}\brvertical{\frac{a_n}{a_{n+1}}}=|x|\lim_{n\to\infty}(n+1)=\eqnsystem{\infty\text{ if }x\neq 0\\0\text{ if }x=0}\\
    &\text{series converges only if }x=0\\
    &\therefore\,R=0
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex3: }&\sum_{n=1}^\infty(-1)^{n-1}\frac{x^n}{n}\\
    &\lim_{n\to\infty}\brvertical{\frac{a_n}{a_{n+1}}}=|x|\lim_{n\to\infty}\frac{n}{n+1}=|x|\\
    &\text{series is convergent if \ensuremath{|x|<1} and divergent if |x|>1}\\
    &\therefore\, R=1\\
    &\text{but what if \ensuremath{|x|=1}?}\\
    &\text{Endpoint \ensuremath{x=1}: }\sum_{n=1}^\infty(-1)^{n-1}\frac{1}{n}\to\text{convergent by alternating series test}\\
    &\text{Endpoint \ensuremath{x=-1}: }\sum_{n=1}^\infty(-1)^{2n-1}\frac{1}{n}=-\sum_{n=1}^\infty\frac{1}{n}\to\text{divergent by integral test}\\
    &\Ra x\in(-1,1]
\end{aligned}

$$

This range of $x$ values is called the interval of convergence

We can use power series to define functions as series. For example the geometric series is expressed as ${1+x+x^2+\cdots}$. The infinite sum works out to be $\dfrac{1}{1-x}$ using the formula $\dfrac{1}{1-r}$. From here (or by using Taylor expansion) we can express many functions as series.
Note that the Taylor series a special type of Power series that is defined as

$$
\sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(x-a)^n

$$

$$
\begin{aligned}
    \text{Ex: }&\text{show }\ln(1+x)=\sum_{n=0}^\infty(-1)^n\frac{x^{n+1}}{n+1}\text{ for }|x|<1\\
    &\frac{1}{1-x}=\sum_{n=0}^\infty x^n\\
    &\text{sub \ensuremath{x} for -x: }\frac{1}{1+x}=\sum_{n=0}^\infty(-1)^nx^n\\
    &\text{integrate: }\int\frac{dx}{1+x}=\sum_{n=0}^\infty(-1)^n\int x^ndx\\
    &\ln|1+x|=\sum_{n=0}^\infty(-1)^n\frac{x^{n+1}}{n+1}+C\\
    &x=0:\,\ln(1)=0=\sum_{n=0}^\infty(-1)^n\frac{x^{n+1}}{n+1}+C\Ra C=0\\
    &\therefore\,\ln|1+x|=\sum_{n=0}^\infty(-1)^n\frac{x^{n+1}}{n+1}
\end{aligned}

$$

Ex2: define the error function using power series.

$$
\begin{aligned}
    &\erf(x)=\frac{2}{\sqrt{\pi}}\int_0^xe^{-t^2}dt\\
    &e^x=\sum_{n=1}^\infty\frac{x^n}{n!}\\
    &e^{-t^2}=\sum_{n=1}^\infty\frac{(-t^2)^{n}}{n!}=\sum_{n=1}^\infty\frac{(-1)^nt^{2n}}{n!}\\
    &\int_0^x e^{-t^2}dt=\brsquare{\sum_{n=1}^\infty\frac{(-1)^nt^{2n+1}}{(2n+1)n!}}_0^x\\
    &\erf(x)=\frac{2}{\sqrt{\pi}}\sum_{n=1}^\infty\frac{(-1)^nx^{2n+1}}{(2n+1)n!}
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex3: }&\text{Which function is defined by the series }\sum_{n=0}^\infty n^2x^n\text{?}\\
    &\frac{1}{1-x}=\sum_{n=0}^\infty x^n\\
    &\frac{d}{dx}\brround{\frac{1}{1-x}}=\sum_{n=0}^\infty\frac{d}{dx}x^n\\
    &\frac{1}{(1-x)^2}=\sum_{n=0}^\infty nx^{n-1}\\
    &\frac{x}{(1-x)^2}=\sum_{n=0}^\infty nx^n\\
    &\frac{d}{dx}\frac{x}{(1-x)^2}=\sum_{n=0}^\infty\frac{d}{dx} nx^n\\
    &\frac{1-3x}{(1-x)^3}=\sum_{n=0}^\infty n^2x^{n-1}\\
    &\frac{x(1-3x)}{(1-x)^3}=\sum_{n=0}^\infty n^2x^n\\
\end{aligned}

$$

Some of the more common Power series you'll see are compiled in this list:

$$
\begin{aligned}
    &\frac{1}{1-x}=\sum_{n=0}^\infty x^n\text{ for \ensuremath{|x|<1}}\\
    &e^x=\sum_{n=0}^\infty\frac{x^n}{n!}\\
    &\ln(1+x)=\sum_{n=0}^\infty(-1)^n\frac{x^{n+1}}{n+1}\text{ for \ensuremath{|x|<1}}\\
    &\arctan x=\sum_{n=0}^\infty(-1)^n\frac{x^{2n+1}}{2n+1}\text{ for \ensuremath{|x|<1}}\\
    &\sin x=\sum_{n=0}^\infty(-1)^n\frac{x^{2n+1}}{(2n+1)!}\\
    &\cos x=\sum_{n=0}^\infty(-1)^n\frac{x^{2n}}{(2n)!}\\
    &(1+x)^p=\sum_{n=0}^\infty\frac{p!}{n!(p-n)!}x^n=1+px+\frac{p(p-1)}{2!}x^2+\frac{p(p-1)(p-2)}{3!}x^3+\cdots
\end{aligned}

$$

These Taylor series are useful in solving some otherwise difficult problems

$$
\begin{aligned}
    \text{Ex: }&\lim_{x\to0}\frac{\cos x^2-1+\frac{x^4}{2}}{x^8}\\
    &\cos u=1-\frac{u^2}{2!}+\frac{u^4}{4!}-\frac{u^6}{6!}+\cdots\\
    &\text{let }u=x^2\\
    &\cos x^2=1-\frac{x^4}{2!}+\frac{x^8}{4!}-\frac{x^12}{6!}+\cdots\\
    &\lim_{x\to0}\frac{\cos x^2-1+\frac{x^4}{2}}{x^8}=\lim_{x\to0}\frac{1-\frac{x^4}{2!}+\frac{x^8}{4!}-\frac{x^{12}}{6!}+\cdots-1+\frac{x^4}{2}}{x^8}=\lim_{x\to0}\frac{\frac{x^8}{4!}-\frac{x^{12}}{6!}+\cdots}{x^8}\\
    &=\lim_{x\to0}\brround{\frac{1}{4!}-\frac{x^4}{6!}+\cdots}=\frac{1}{4!}=\frac{1}{24}
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex2: }&\lim_{x\to\infty}\sqrt{x}\brround{\sqrt{x+4}-\sqrt{x+1}}\\
    &\sqrt{x+4}=\sqrt{x\brround{1+\frac{4}{x}}}=\sqrt{x}\sqrt{1+\frac{4}{x}}\\
    &\brround{1+\frac{4}{x}}^{1/2}=1+\frac{1}{2}\brround{\frac{4}{x}}+\frac{\frac{1}{2}\brround{\frac{1}{2}-1}}{2!}\brround{\frac{4}{x}}^2+\cdots=1+\frac{2}{x}-\frac{2}{x^2}+\cdots\\
    &\text{similarly, }\sqrt{x+1}=\sqrt{x}\sqrt{1+\frac{1}{x}}\\
    &\brround{1+\frac{1}{x}}^{1/2}=1+\frac{1}{2x}-\frac{1}{8x^2}+\cdots\\
    &\sqrt{x}\brround{\sqrt{x+4}-\sqrt{x+1}}=\sqrt{x}\brround{\sqrt{x}\brround{1+\frac{4}{x}}^{1/2}-\sqrt{x}\brround{1+\frac{1}{x}}^{1/2}}\\
    &=x\brround{\brround{1+\frac{4}{x}}^{1/2}-\brround{1+\frac{1}{x}}^{1/2}}=x\brround{\brround{1+\frac{2}{x}-\frac{2}{x^2}+\cdots}-\brround{1+\frac{1}{2x}-\frac{1}{8x^2}+\cdots}}\\&=\frac{3}{2}-\frac{15}{8x}+\cdots\\
    &\lim_{x\to\infty}\sqrt{x}\brround{\sqrt{x+4}-\sqrt{x+1}}=\frac{3}{2}
\end{aligned}

$$
