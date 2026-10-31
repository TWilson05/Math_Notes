# Differentiation Techniques

<!-- Source: [Sections/Differential_Calculus/Differentiation_Techniques.tex](../../Sections/Differential_Calculus/Differentiation_Techniques.tex) -->

## Implicit Differentiation

Implicit differentiation allows us to calculate the derivative of an implicitly given function without solving for $y$ explicitly.

$$
\begin{aligned}
    \text{Ex: }&4xy^2+3x^2y=2\\
    &\frac{d}{dx}(4xy^2)+\frac{d}{dx}(3x^2y)=\frac{d}{dx}2\\
    &4x(2yy')+4y^2+4x^2y'+3y(2x)=0\\
    &8xyy'+6x^2y'=-4y^2-6xy\\
    &y'(8xy+6x^2)=-4y^2-6xy\\
    &y'=\frac{-4y^2-6xy}{8xy+6x^2}
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex2: }&x^2+y^2=1\\
    &2x+2yy'=0\\
    &2yy'=-2x\\
    &y'=-\frac{x}{y}
\end{aligned}

$$

## Inverse Functions

Recall that the inverse of a function is a reflection across the line $y=x$
For where $g(x)=f^{-1}(x)$,

$$
g'(f(a))=\frac{1}{f'(a)}

$$

Ex: Find the derivative of the inverse of $y=x^4$ at $x=2$

$$
\begin{aligned}
    &f'(x)=4x^3\\
    &f'(2)=32\\
    &\therefore\,g'(f(2))=\frac{1}{32}\\
    &\text{Proof:}\\
    &g(x)=f^{-1}(x)=x^{\frac{1}{4}}\\
    &g'(x)=\frac{1}{4}x^{-\frac{3}{4}}\\
    &f(2)=16\\
    &g'(16)=\frac{1}{32}
\end{aligned}

$$

Ex2: For $g(x)=x+e^{(x+1)^3}$, evaluate $(g^{-1})'(c)$ for where $g^{-1}(c)=-1$

$$
\begin{aligned}
    &g(x)=x+e^{(x+1)^3}\\
    &x=g^{-1}(g(x))\\
    &1=(g^{-1})'(g(x))g'(x)\\
    &(g^{-1})'(g(x))=\frac{1}{g'(x)}\\
    &g^{-1}(c)=-1\Ra c=g(-1)\\
    &(g^{-1})'(c)=(g^{-1})'(g(-1))=\frac{1}{g'(-1)}\\
    &g'(x)=1+3(x+1)^2e^{(x+1)^3}\\
    &g'(-1)=1\\
    &(g^{-1})'(c)=\frac{1}{1}=1
\end{aligned}

$$

## The Exponential Function

Derivative of the exponential function $y=a^x$:

$$
\begin{aligned}
    &\frac{d}{dx}a^x=\lim_{h\to 0}\frac{a^{x+h}-a^x}{h}\\
    &f'(x)=a^x\lim_{h\to 0}\frac{a^h-1}{h}\\
    &\text{where }\lim_{h\to 0}\frac{a^h-1}{h}=f'(0)\\
    &\text{so }f'(x)=f'(0)f(x)
\end{aligned}

$$

By observation, we know by the graph of the function that the derivative $f'(0)$ exists so the derivative of the exponential is itself times some constant.
If we want to define a function such that $f'(x)=f(x)$ we need to find the $a$ value that corresponds with a constant of 1.

$$
\begin{aligned}
    &f'(0)=\lim_{h\to 0}\frac{a^h-1}{h}\\
    &\text{let }k=a^h-1\\
    &\lim_{h\to 0}=\lim_{k\to 0}\\
    &a^h=k+1\Ra h=\log_a(k+1)\\
    &f'(0)=\lim_{k\to 0}\frac{k}{\log_a(k+1)}=\lim_{k\to 0}\frac{1}{\log_a(k+1)^{1/k}}=1\\
    &\Ra\lim_{k\to 0}\log_a(k+1)^{1/k}=1\\
    &a=\lim_{k\to 0}(k+1)^{1/k}
\end{aligned}

$$

Solving this limit is a somewhat circular argument as we need to know what $a$ is to compute it algebraically. Fortunately, we can take small values of $k$ and estimate the limit to be $2.71828\ldots$
We will call this value Euler's constant, $e$.
So, $\dfrac{d}{dx}e^x=e^x$
Euler's constant shows up in a few interesting cases. One common case is in compounding interest:

$$
e=\lim_{n\to \infty}\brround{1+\frac{1}{n}}^n

$$

**Applications**
Ex: Carbon Dating
There is a constant amount of Carbon-14 present in organic matter. Once an organism dies, it stops acquiring Carbon-14. If a plant dies at time $t=0$, the number of micrograms of Carbon-14 is $f(t)=10e^{-kt}$ with the half-life of Carbon-14 being 5730 years. If $1\mu g$ of Carbon-14 remains, when did it die?

$$
\begin{aligned}
    &f(5730)=10e^{-5730k}=5\\
    &\frac{1}{2}=e^{-5730k}\\
    &5730k=\ln 2\\
    &k=\frac{\ln 2}{5730}\\
    &10e^{-\frac{\ln 2}{5730}t}=1\\
    &e^{-\frac{\ln 2}{5730}t}=\frac{1}{10}\\
    &\frac{\ln 2}{5730}t=\ln10\\
    &t=5730\frac{\ln10}{\ln2}\approx19030\text{ years}
\end{aligned}

$$

Ex2: Newton's Law of Cooling

$$
T(t)=(T(0)-A)e^{kt}+A

$$

where $A$ is the temperature of the surroundings.
A body is discovered at 3:45pm in a locked room held at $20^\circ$. The body's temperature is $27^\circ$. By 5:45pm its temperature has dropped to $25.3^\circ$. When did the person die?

$$
\begin{aligned}
    &T(t)=(27-20)e^{kt}+20=7e^{kt}+20\\
    &7e^{2k}+20=25.3\\
    &e^{2k}=\frac{5.3}{7}\\
    &e^k=\sqrt{\frac{5.3}{7}}\\
    &T(t)=7\brround{\frac{5.3}{7}}^{t/2}+20=37\\
    &\brround{\frac{5.3}{7}}^{t/2}=\frac{17}{7}\\
    &t=\frac{2\ln\brround{\frac{17}{7}}}{\ln\brround{\frac{5.3}{7}}}\approx-6.4
\end{aligned}

$$

So the person died 6 hours and 24 minutes before 3:45pm.
## Logarithmic Differentiation

We found that the derivative of $e^x$ is $e^x$. We can use this to determine the derivative of $\ln x$:

$$
\begin{aligned}
    &y=\ln x\\
    &x=e^y\\
    &1=e^yy'\\
    &y'=\frac{1}{e^y}\\
    &y'=\frac{1}{x}\\
    &\Ra\frac{d}{dx}\ln x=\frac{1}{x}
\end{aligned}

$$

The properties of natural logarithms can be useful to find derivatives of difficult functions.
We can introduce a method called logarthmic differentiation:

- Write the equation in the form $y=f(x)$
- Take the natural log of both sides
- Use properties of logs to simplify the expression
- Differentiate the equation implicitly with respect to x
- Solve for $y'$

$$
\begin{aligned}
    \text{Ex: }y&=\frac{x^2\sqrt{x^2+7}}{\sqrt[3]{x+5}}\\
    \ln y&=\ln\left(\frac{x^2\sqrt{x^2+7}}{\sqrt[3]{x+5}}\right)=\ln x^2+\ln(x^2+7)^\frac{1}{2}-\ln(x+5)^\frac{1}{3}=2\ln x+\frac{1}{2}\ln(x^2+7)-\frac{1}{3}\ln(x+5)\\
    \frac{y'}{y}&=\frac{2}{x}+\frac{1}{2}\frac{2x}{x^2+7}-\frac{1}{3}\frac{1}{x+5}\\
    y'&=y\left(\frac{2}{x}+\frac{x}{x^2+7}-\frac{1}{3(x+5)}\right)=\frac{x^2\sqrt{x^2+7}}{\sqrt[3]{x+5}}\left(\frac{2}{x}+\frac{x}{x^2+7}-\frac{1}{3(x+5)}\right)
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex2: }&y=x^x\\
    &\ln y=x\ln x\\
    &\frac{y'}{y}=x\frac{1}{x}+\ln x=1+\ln x\\
    &y'=y(1+\ln x)\\
    &y'=x^x(1+\ln x)
\end{aligned}

$$

So far, we have just dealt with logs and exponentials with base $e$. Using logarithmic differentiation, we can define the derivatives for more general cases:

$$
\begin{aligned}
    \text{Ex: }&y=a^x\\
    &\ln y=x\ln a\\
    &\frac{y'}{y}=\ln a\\
    &y'=y\ln a\\
    &y'=a^x\ln a
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex2: }&y=\log_ax\\
    &y=\frac{\ln x}{\ln a}\\
    &y'=\frac{1}{x\ln a}
\end{aligned}

$$

## Derivatives of Inverse Trigonometric Functions

Derivatives of Inverse Trig Functions:

$$
\begin{aligned}
    &\frac{d}{dx}\arcsin x=\frac{1}{\sqrt{1-x^2}}\\
    &\frac{d}{dx}\arccos x=-\frac{1}{\sqrt{1-x^2}}\\
    &\frac{d}{dx}\arctan x=\frac{1}{1+x^2}\\
    &\frac{d}{dx}\arccot x=-\frac{1}{1+x^2}\\
    &\frac{d}{dx}\arcsec x=\frac{1}{|x|\sqrt{x^2-1}}\\
    &\frac{d}{dx}\arccsc x=-\frac{1}{|x|\sqrt{x^2-1}}
\end{aligned}

$$

Derivations:

$$
\begin{aligned}
    &\frac{d}{dx}\arcsin x\\
    &y=\arcsin x\Ra x=\sin y\\
    &1=\cos (y)y'\\
    &y'=\frac{1}{\cos y}=\frac{1}{\cos(\arcsin x)}\\
    &y'=\frac{1}{\sqrt{1-x^2}}
\end{aligned}

$$

$$
\begin{aligned}
    &\frac{d}{dx}\arctan x\\
    &y=\arctan x\Ra x=\tan y\\
    &1=\sec^2(y)y'\\
    &y'=\frac{1}{\sec^2y}=\frac{1}{\sec^2(\arctan x)}\\
    &y'=\frac{1}{1+x^2}
\end{aligned}

$$

$$
\begin{aligned}
    &\frac{d}{dx}\arcsec x\\
    &y=\arcsec x\Ra x=\sec y\\
    &1=\tan(y)\sec(y)y'\\
    &y'=\frac{1}{\sec y\tan y}=\frac{1}{\sec(\arcsec x)\tan(\arcsec x)}\\
    &y'=\frac{1}{|x|\sqrt{x^2-1}}
\end{aligned}

$$

Note that we have $|x|$ because there $\sgn(\sec y)=\sgn(\tan y)$ for where $\arcsec x$ is defined. This means that the denominator must always be positive.
