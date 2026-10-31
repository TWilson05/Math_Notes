# Approximations

<!-- Source: [Sections/Differential_Calculus/Approximations.tex](../../Sections/Differential_Calculus/Approximations.tex) -->

## Differentials

This stems from the approximation $f'(x)\approx \frac{\Delta y}{\Delta x}$ which implies $\Delta y\approx f'(x)\Delta x$. Put into differential form we get that, $dy=f'(x)dx$
They are computed the same way as derivatives.
Ex: for $y=x^2$, $dy=2xdx$
One useful application of this is error approximation. We can think of $dx$ and $dy$ as some error in the measurements of $x$ and $y$ related by the equation $f(x)$.
Ex: The radius of a sphere ball is measured to be $1.5cm$ with a possible error of $\pm 0.1cm$. Estimate the possible error of the volume.

$$
\begin{aligned}
    &V=\frac{4}{3}\pi r^3\\
    &dV=4\pi r^2dr\\
    &dV=4\pi(1.5)^2(0.1)=\pm2.83cm^3
\end{aligned}

$$

Ex2: if the radius and height of a cylinder are measured with relative error of $1\%$, what is the relative error of the volume of the cylinder?

$$
\begin{aligned}
    V&=\pi r^2h\\
    dV&=\pi(r^2dh+2hrdr)\\
    \frac{dV}{V}&=\frac{\pi r^2dh}{\pi r^2h}+\frac{2\pi rhdr}{\pi r^2h}\\
    &=\frac{dh}{h}+2\frac{dr}{r}\\
    &=1\%+2\%=3\%
\end{aligned}

$$

## Linear Approximations

Similar to differentials, we can use the approximation $f'(x)\approx \dfrac{\Delta y}{\Delta x}$. This can be reworked to give an approximation for the value of $f(x)$

$$
\begin{aligned}
    &y=f(x)\\
    &y=f(a)+\Delta y\\
    &\frac{\Delta y}{\Delta x}=\frac{f(x)-f(a)}{x-a}\\
    &f'(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}\text{ so assuming }x\approx a,\, \frac{\Delta y}{\Delta x}\approx f'(a)\\
    &\Delta y\approx f'(a)\Delta x\\
    &y=f(a)+\Delta \approx f(a)+f'(a)\Delta x\\
    &f(x)\approx f(a)+f'(a)(x-a)
\end{aligned}

$$

where $a$ is some estimate of $x$.
Ex: approximate $\sqrt{5}$

$$
\begin{aligned}
    &f(x)=\sqrt{x}\\
    &x=5,\,x_0=4\\
    &f'(x)=\frac{1}{2\sqrt{x}}\\
    &f(x)\approx f(4)+\frac{1}{2\sqrt{4}}(5-4)\\
    &f(x)\approx 2+\frac{1}{4}=\frac{9}{4}=2.25
\end{aligned}

$$

This is pretty close to the actual value of $\sqrt{5}$ which is $2.236\ldots$
Often we are concerned with approximating functions at 0. Some common examples are as follows:

$$
\begin{aligned}
    \text{Ex: }&\sin x\\
    &f'(x)=\cos x,\,f(0)=0,\,f'(0)=1\\
    &\sin(x)\approx x\\
    \text{Ex2: }&\cos x\\
    &f'(x)=-\sin x,\,f(0)=1,\,f'(0)=0\\
    &\cos(x)\approx 1\\
    \text{Ex3: }&e^x\\
    &f'(x)=e^x,\,f(0)=1,\,f'(0)=1\\
    &e^x\approx 1+x\\
    \text{Ex4: }&\ln(1+x)\\
    &f'(x)=\frac{1}{1+x},\,f(0)=0,\,f'(0)=1\\
    &\ln(1+x)\approx 1\\
    \text{Ex5: }&(a+x)^r\\
    &f'(x)=r(a+x)^{r-1},\,f(0)=a,\,f'(0)=ra\\
    &(a+x)^r\approx a+arx
\end{aligned}

$$

## Taylor Polynomials

Quadratic Approximation:
Similar to how we define the linear approximation to be the best fit line to the function at the point $x_0$, we can define a quadratic approximation to be the best fit parabola at the point $x_0$. By defining $f(x)$ to be in the form $c_1+c_2(x-x_0)+c_3(x-x_0)^2$, we can compute derivatives to find $c_1,\,c_2,\,c_3$ to get the quadratic approximation:

$$
f(x)\approx f(x_0)+f'(x_0)+\frac{f''(x_0)}{2}(x-x_0)^2

$$

Taylor Polynomials:
We can actually do much better than the quadratic approximation. We can define a cubic approximation or even higher orders. This is known more generally as the Taylor Series approximations

$$
f(x)\approx f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2}(x-x_0)^2+\frac{f'''(x_0)}{6}(x-x_0)^3+\cdots

$$

The $n^\text{th}$ order Taylor approximation of $x$ about $a$ is denoted as $T_n(x)$.

$$
T_n(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k

$$

Taylor polynomials with $a=0$ are called Maclaurin Polynomials.
A useful application of Taylor Series is that they can be used to express functions as polynomials.
Ex: Maclaurin series of $y=e^x$

$$
\begin{aligned}
    &f(x)=e^x\\
    &f^{(n)}(x)=e^x\\
    &f^{(n)}(0)=e^0=1\\
    &T_\infty(x)=e^x=\sum_{n=0}^\infty\frac{1}{n!}(x-0)^n\\
    &e^x=\sum_{n=0}^\infty\frac{x^n}{n!}
\end{aligned}

$$

Error Range:
The error that comes from approximations will always be the difference between the actual value and the approximation. $E_n=f(a)-T_n(a)$
For Taylor series, the error can be expressed using the formula

$$
E_n=f(x)-T_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}

$$

where $c$ is some number between $x$ and $a$
*note: taking $n=0$ will give the mean value theorem
Ex: Find the error using a degree 2 polynomial approximation at $a=81$ for $\sqrt[4]{81.2}$

$$
\begin{aligned}
    &f(x)=x^{1/4},\,f'(x)=\frac{1}{4}x^{-3/4},\,f''(x)=\frac{3}{16}x^{-7/4},\,f'''(x)=\frac{21}{64}x^{-11/4}\\
    &E_2=\frac{f'''(c)}{3!}(81.2-81)=\frac{1}{6}\cdot\frac{21}{64}c^{-11/4}\brround{\frac{1}{5}}^3\text{ for \ensuremath{81<c<81.2}}
\end{aligned}

$$

we want to choose $c$ such that it maximizes the error. This gives us an upper bound, basically telling us that our estimate is no worse than that upper bound.

$$
\begin{aligned}
    &\text{set }c=81\\
    &E_2<\frac{1}{6}\cdot\frac{21}{64}\cdot\frac{1}{81^{11/4}}\cdot\frac{1}{5^3}\approx2.4\times10^{-8}
\end{aligned}

$$

Note that when $E>0$ it will be an underestimate because the difference $f(x)-T(x)$ is positive, indicating $f(x)>T(x)$.
Similarly if $E<0$ then it is an overestimate.
Ex2: Which degree Taylor polynmial can estimate $e$ with an error of less than 0.001?

$$
\begin{aligned}
    &f(x)=e^x,\,a=0,\text{ at \ensuremath{x=1}}\\
    &\text{we use a=0 because we know \ensuremath{e^0=1}}\\
    &|E|=\left|\frac{f^{(n+1)}(c)}{(n+1)!}(1-0)^{n+1}\right|=\frac{e^c}{(n+1)!}\text{ for \ensuremath{0<c<1}}\\
    &\text{assume upper bound \ensuremath{e^1<3}}\\
    &\therefore\,1<e^c<3\\
    &E<\frac{3}{(n+1)!}\\
    &0.001<\frac{3}{(n+1)!}\Ra (n+1)!>3000\\
    &6!=720\not> 3000\\
    &7!=5040>3000\Ra (n+1)!=7!\\
    &\Ra n=6
\end{aligned}

$$

## Newton's Method

This approximation is useful for finding x-intercepts is based on the assumption that the tangent line near the point will cross the x-axis in nearly the same place.

$$
\begin{aligned}
    &y-y_0=m(x-x_0)\\
    &0-y_0=m(x-x_0)\\
    &x=x_0-\frac{y_0}{m}\\
    &x_1=x_0-\frac{f(x_0)}{f'(x_0)}
\end{aligned}

$$

$x_0$ is some initial guess at where the intercept is and $x_1$ is an improved approximation.
We can then use $x_1$ as our new initial guess to get an even better approximation, $x_2$.
The general equation will be:

$$
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}

$$

As we perform inititley many iterations, we value $x_n$ will approach the exact value of the intercept.

$$
\begin{aligned}
    \text{Ex: }&y=x^2-5\\
    &\text{take }x_0=2\\
    &f'(x)=2x\\
    &f(2)=4,\,f'(2)=1\\
    &x_1=x_0-\frac{x_0^2-5}{2x_0}=2+\frac{1}{4}=\frac{9}{4}\\
    &x_2=\frac{9}{4}-\frac{\brround{\frac{9}{4}}-5}{2\brround{\frac{9}{4}}}=\frac{161}{72}=2.236\overline{1}\\
    &x_3=2.236068\ldots
\end{aligned}

$$

The actual value of $x$ is $\sqrt{5}=2.236068\ldots$ so it doesn't take many iterations to give a very good approximation.
This becomes very useful when evaluating functions with no simple solution.

$$
\begin{aligned}
    \text{Ex2: }&2\cos x=3x\\
    &\text{take }x_0=\frac{\pi}{6}\\
    &f(x)=2\cos x-3x\\
    &f'(x)=-2\sin x-3\\
    &x_1=\frac{\pi}{6}-\frac{\sqrt{3}-\frac{\pi}{2}}{-1-3}\approx 0.56391\\
    &x_2\approx 0.56357
\end{aligned}

$$

Note that this method may fail if $f'(x)=0$ or if you get caught in an infinite loop such as what may occur with a cubic where $x_0\to x_1\to x_0\to x_1$

$$
\begin{aligned}
    \text{Ex: }&y=x^3-x\text{ with }x_0=\sqrt{0.2}\\
    &x_1=x_0-\frac{x_0^3-x}{3x_0^2-1}=-\sqrt{2}\\
    &x_2=\sqrt{2}=x_0
\end{aligned}

$$
