# Exponential and Logarithmic Functions

<!-- Source: [Sections/Pre-Calculus/Exponential_and_Logs.tex](../../Sections/Pre-Calculus/Exponential_and_Logs.tex) -->

## The Exponential Function

Exponential functions are those in the form of $y=c^x$ for where $c\neq0$ and $c\neq 1$
The general form is:

$$
f(x)=ac^{\frac{x-h}{b}}+k

$$

If $c>1$, the graph will model exponential growth and tend to infinity.
If $0<c<1$, the graph will model exponential decay and will tend to 0.

Solving same base equations:
Some exponential equations can be solved by setting the bases of both sides equal to another.

$$
\begin{aligned}
    \text{Ex: }&16^{x+3}=\left(\frac{1}{8}\right)^{x-10}\\
    &(2^4)^{x+3}=(2^{-3})^{x-10}\\
    &2^{4x+12}=2^{-3x+30}\\
    &4x+12=-3x+30\\
    &7x=18\\
    &x=\frac{18}{7}
\end{aligned}

$$

## Logarithms

Logarithms are the inverse of exponentials.

$$
\begin{aligned}
    y=c^x\to x&=c^y\\
    \log_cx&=\log_c(c^y)\\
    \log_cx&=y\log_cc\\
    y&=\log_cx
\end{aligned}

$$

They have the restrictions that $c>0$, $c\neq 1$ and $x>0$
Notation:
$\log_{10}x=\log x$ and is called the common logarithm.
$\log_ex=\ln x$ and is called the natural logarithm.

Log Rules:

$$
\begin{aligned}
    &\log_c1=0\\
    &\log_cc=1\\
    &c^{\log_cx}=x\\
    &\log_ca+\log_cb=\log(_c(ab)\\
    &\log_ca-\log_cb=\log\left(\frac{a}{b}\right)\\
    &\log_ca^n=n\log_ca\\
    &\log_cx=\frac{\log_nx}{\log_nc}\\
    &a^x=e^{x\ln a}
\end{aligned}

$$

## Solving Equations

We can solve logarithmic and exponential equations using the log rules mentioned.

$$
\begin{aligned}
    \text{Ex: }&2^x=3^{x+1}\\
    &\log_3(2^x)=\log_3(3^{x+1})\\
    &x\log_32=x+1\\
    &x(\log_32-1)=1\\
    &x=\frac{1}{\log_32}
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex2: }&\log(x+2)+\log(x-1)=1\\
    &\text{Restrictions: }x+2>0\Ra x>-2\text{ and }x-1>0\Ra x>1\\
    &\log((x+2)(x-1))=1\\
    &\log((x+2)(x-1))=\log10\\
    &(x+2)(x-1)=10\\
    &x^2+x-2=10\\
    &x^2+x-12=0\\
    &(x+4)(x-3)=0\\
    &x=-4,\,x=3\\
    &-4\ngeq 1\therefore\,x=-4\text{ is extraneous}\\
    &\Ra x=3
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex3: }&2\log_2(x-1)=1-\log_2(x+2)\\
    &\text{Restrictions: }x-1>0\Ra x>1\text{ and }x+2>0\Ra x>-2\\
    &\log_2(x-1)^2=\log_22-\log_2(x+2)\\
    &\log_2(x-1)^2=\log_2\left(\frac{2}{x+2}\right)\\
    &(x-1)^2=\frac{2}{x+2}\\
    &(x^2-2x+1)(x+2)=2\\
    &x^3+2x^2-2x^2-4x+x+2=2\\
    &x^3-3x=0\\
    &x(x+\sqrt{3})(x-\sqrt{3})=0\\
    &x=0,\pm\sqrt{3}\\
    &\text{by restrictions, }x=\sqrt{3}
\end{aligned}

$$

## Applications

Exponential growth/decay model:
$F=Ir^{\frac{t}{T}}$ where $F$ is the final amount, $I$ is the initial amount, $r$ is the rate of growth/decay per time interval $T$. $t$ is time.
Ex: A bacteria doubles every 4 hours. If there were 100 to start, when will there be 500,000?

$$
\begin{aligned}
    &500000=100(2)^{\frac{t}{4}}\\
    &5000=2^\frac{t}{4}\\
    &\log5000=\frac{t}{4}\log2\\
    &t=\frac{4\log5000}{\log2}\approx49.15\text{ hours}
\end{aligned}

$$

Compound growth model:
$A=I\left(1+\frac{r}{n}\right)^{nt}$ where $A$ is the final amount, $I$ is the initial amount, $r$ is the rate per year, $t$ is times, and $n$ is the number of compound periods per year.
Ex: $\$15000$ is invested at $5.5\%$ APR, compounded monthly. How long will it take to grow to $\$450000$?

$$
\begin{aligned}
    &450000=15000\left(1+\frac{0.055}{12}\right)^{12t}\\
    &30=\left(1+\frac{0.055}{12}\right)^{12t}\\
    &\log30=12t\log\left(1+\frac{0.055}{12}\right)\\
    &t=\frac{\log30}{12\log\left(1+\frac{0.055}{12}\right)}\approx61.98\text{ years}
\end{aligned}

$$
