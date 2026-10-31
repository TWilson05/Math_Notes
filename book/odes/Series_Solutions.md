# Series Solutions

<!-- Source: [Sections/ODEs/Series_Solutions.tex](../../Sections/ODEs/Series_Solutions.tex) -->

## Power Series Solutions

We can express the solution to many ODEs in the form of a power series. For some differential equation

$$
P(x)y''+Q(x)y'+R(x)y=0

$$

we can express the general solution about some point $x_0$ as

$$
y=\sum_{n=0}^\infty a_n(x-x_0)^n

$$

This method is best shown through examples.
Ex:

$$
\begin{aligned}
    &y'-y-2xy=0\\
    &y=\sum_{n=0}^\infty a_nx^n\\
    &y'=\sum_{n=1}^\infty a_n nx^{n-1}\\
    &\sum_{n=1}^\infty a_nnx^{n-1}+\sum_{n=0}^\infty a_nx^n-2\sum_{n=0}^\infty a_nx^{n+1}=0
\end{aligned}

$$

Now we want to combine the three sums into one summation. We can do this by changing the indexes so that they all have matching $x^m$ terms and then peel off the lower terms in the sum so they all start at the same point.

$$
\begin{aligned}
    &\underbrace{\sum_{n=1}^\infty a_nnx^{n-1}}_{m=n-1}+\underbrace{\sum_{n=0}^\infty a_nx^n}_{m=n}-2\underbrace{\sum_{n=0}^\infty a_nx^{n+1}}_{m=n+1}=0\\
    &\sum_{m=0}^\infty a_{m+1}(m+1)x^m+\sum_{m=0}^\infty a_mx^m-2\sum_{m=1}^\infty a_{m-1}x^m=0\\
    &a_0+a_1+\sum_{m=1}^\infty\brround{a_{m+1}(m+1)+a_m-2a_{m-1}}x^m=0
\end{aligned}

$$

Because each $x^2,\ x^3,\ x^4,\ldots$ term is linearly independent of one another we will have each of these terms sum to 0

$$
\begin{aligned}
    &x^0\text{ terms: }a_0+a_1=0\Ra a_1=-a_0\\
    &x^1\text{ terms: }a_2(2)+a_1-2a_0=0\Ra a_2=\frac{2a_0-a_1}{2}\\
    &x^m\text{ terms: }a_{m+1}(m+1)+a_m-2a_{m-1}=0\Ra a_{m+1}=\frac{2a_{m-1}-a_m}{m+1}
\end{aligned}

$$

This gives a recursive formula we can use to solve for each $a_m$ term.

$$
\begin{aligned}
    &m=1:\ a_2=\frac{2a_0-a_1}{2}=\frac{2a_0+a_0}{2}=\frac{3}{2}a_0\\
    &m=2:\ a_3=\frac{2a_1-a_2}{3}=\frac{-2a_0-\frac{3}{2}a_0}{3}=-\frac{7}{6}a_0\\
    &\vdots\\
    &y(x)=a_0+a_1x+a_2x^2+\cdots\\
    &y(x)=a_0\brround{1-x+\frac{3}{2}x^2-\frac{7}{6}x^3+\cdots}
\end{aligned}

$$

Note that the soluyion is in terms of an arbitrary constant $a_0$. For 2nd order ODEs the solution will be in terms of two arbitrary constants (usually $a_0$ and $a_1$).
Ex2:

$$
\begin{aligned}
    &(1+x^3)y''+12xy=0\\
    &y=\sum_{n=0}^\infty a_nx^n,\ y'=\sum_{n=1}^\infty a_nnx^{n-1},\ y''=\sum_{n=2}^\infty a_nn(n-1)x^{n-2}\\
    &\sum_{n=2}^\infty a_nn(n-1)x^{n-2}+\sum_{n=2}^\infty a_nn(n-1)x^{n+1}+12\sum_{n=0}^\infty a_nx^{n+1}=0\\
    &\sum_{m=0}^\infty a_{m+2}(m+2)(m+1)x^m+\sum_{m=3}^\infty a_{m-1}(m-1)(m-2)x^m+12\sum_{m=1}^\infty a_{m-1}x^m=0\\
    &2a_2+6a_3x+12a_4x^2+12a_0x+12a_1x^2+\sum_{m=3}^\infty\brround{a_{m+2}(m+2)(m+1)+a_{m-1}(m-1)(m-2)+12a_{m-1}}x^m\\
    &2a_2=0\\
    &6a_3+12a_0=0\Ra a_3=-2a_0\\
    &12a_4+12a_1\Ra a_4=-a_1\\
    &a_{m+2}(m+2)(m+1)+a_{m-1}(m-1)(m-2)+12a_{m-1}=0\\
    &a_{m+2}(m+2)(m+1)=-a_{m-1}(m^2-3m+14)\\
    &a_{m+2}=-a_{m-1}\frac{m^2-3m+14}{(m+2)(m+1)}\\
    &a_5=-\frac{14a_2}{20}=0\\
    &a_6=-a_3\brround{\frac{18}{30}}=\frac{36a_0}{30}=\frac{6a_0}{5}\\
    &a_7=-a_4\brround{\frac{24}{42}}=\frac{4a_1}{7}\\
    &a_8=0\\
    &a_9=-a_6\brround{\frac{42}{72}}=-\frac{7a_0}{10}\\
    &a_{10}=-a_7\frac{54}{90}=-\frac{12a_1}{35}\\
    &a_{12}=-a_9\frac{84}{132}=\frac{49a_0}{110}\\
    &a_{13}=-a_{10}\frac{102}{156}=\frac{102a_1}{455}\\
    &y=a_0\brround{1-2x^3+\frac{6}{5}x^6-\frac{7}{10}x^9+\cdots}+a_1\brround{x-x^4+\frac{4}{7}x^7-\frac{12}{35}x^{10}+\cdots}
\end{aligned}

$$

Something to note when we are using power series is the radius of convergence. If we rewrite the ODE $P(x)y''+Q(x)y'+R(x)y=0$ as

$$
y''+\frac{Q(x)}{P(x)}y'+\frac{R(x)}{P(x)}y=0

$$

then it will be nonsensical for where $P(x)=0$. Points where this happens are called *singular points*. So in our previous example we had $(1+x^3)y''+12xy=0$ so our singular points would be

$$
x=-1,\ x=\frac{1}{2}\pm i\frac{\sqrt{3}}{2}

$$

More rigorously, singular points are defined to be where the function is not analytic. This is the case where the function or the derivative of the function is divided by 0.
For example, $y''+\sqrt{x}y'-y=0$ would have a singular point at $x=0$.
Our power series solution is only valid so long as we don't pass any singular points. This will mean that there is some radius of convergence within where the solution is valid. This radius of convergence can be found as the distance (in real and imaginary space) between the expansion point, $x_0$, and the nearest singular point.
So in our previous example, our expansion point was $x_0=0$ and our singular points are all of a distance $R=1$ away so we find that our radius of convergence is $R=1$. This means that our solution is only valid for $|x|<1$ or more generally,

$$
|x-x_0|<R

$$

Another way to show this is using the ratio test for the recursive $a_m$

$$
\begin{aligned}
    &\lim_{m\to\infty}\brvertical{\frac{a_{m+2}}{a_{m-1}}x}=\lim_{m\to\infty}\brvertical{\frac{-a_{m-1}\frac{m^2-3m+3}{(m+2)(m+1)}}{a_{m-1}}x}=\lim_{m\to\infty}\brvertical{\frac{m^2-3m+3}{(m+2)(m+1)}x}=|x|<1\\
    &\therefore R=1
\end{aligned}

$$

## Frobenius Solutions

When we have a singular point we are not able to expand about that point using power series. One way to get around this is to use Frobenius series.
Because the Cauchy-Euler equation gives a solution for equations with singular points we can try to mimic it with the Frobenius series. We can take an arbitrary ODE and manipulate it to get it into the form of a Cauchy-Euler equation.

$$
\begin{aligned}
    &P(x)y''+Q(x)y'+R(x)y=0\\
    &y''+\frac{Q(x)}{P(x)}y'+\frac{R(x)}{P(x)}y=0\\
    &(x-x_0)^2y''+(x-x_0)^2\frac{Q(x)}{P(x)}y'+(x-x_0)^2\frac{R(x)}{P(x)}y=0\\
    &\text{let }\alpha(x)=(x-x_0)\frac{Q(x)}{P(x)},\ \beta(x)=(x-x_0)^2\frac{R(x)}{P(x)}\\
    &(x-x_0)^2y''+(x-x_0)\alpha(x)y'+(x-x_0)^2\beta(x)y=0
\end{aligned}

$$

So long as $\lim\limits_{x\to x_0}\alpha(x)$ and $\lim\limits_{x\to x_0}\beta(x)$ are both finite then the point we are expanding about is considered to be a *regular singular point* and we are able to apply the Frobenius series.
The Frobenius series looks similar to the power series and is of the form

$$
y=(x-x_0)^r\sum_{n=0}^\infty(x-x_0)^n=\sum_{n=0}a_n(x-x_0)^{n+r}

$$

Finding the solution using Frobenius series works out very similar to using power series but with a few slight differences.
Ex:

$$
\begin{aligned}
    &6x^2(1+x)y''+5xy'-y=0\text{ about }x_0=0
\end{aligned}

$$

We must first see if the point we are expanding about is a regular singular point

$$
\begin{aligned}
    &\lim_{x\to0}\frac{5x^2}{6x^2(1+x)}=\lim_{x\to0}\frac{5}{6(x+1)}=\frac{5}{6}\\
    &\lim_{x\to0}\frac{-x^2}{6x^2(x+1)}=\lim_{x\to0}\frac{-1}{6(x+1)}=-\frac{1}{6}\\
    &\therefore\text{ \ensuremath{x_0=0} is a regular singular point}
\end{aligned}

$$

These limits that we found give the terms $\alpha_0$ and $\beta_0$. We can use these terms to craft what we call the indicial equation which allow us to solve for the two $r$ values that will show up in our solution (similar to how we solved for $r$ in Cauchy-Euler).

$$
\begin{aligned}
    &x^2y_c''+\alpha_0 x y_c'+\beta_0 y_c=0\\
    &x^2y_c''+\frac{5}{6}xy_c'-\frac{1}{6}y_c=0\\
    &y_c=x^r,\ y_c'=rx^{r-1},\ y_c''=r(r-1)x^{r-2}\\
    &r(r-1)+\frac{5}{6}r-\frac{1}{6}=0\\
    &6r^2-r-1=0\\
    &r=\frac{1\pm\sqrt{1+24}}{12}=\frac{1}{2},-\frac{1}{3}\\
    &y_1=\sum_{n=0}^\infty a_nx^{\frac{1}{2}+n}\\
    &y_2=\sum_{n=0}^\infty a_nx^{n-\frac{1}{3}}
\end{aligned}

$$

The rest follows very similarly to finding a power series solution

$$
\begin{aligned}
    &y=\sum_{n=0}^\infty a_nx^{n+r}\\
    &y'=\sum_{n=0}^\infty a_n(n+r)x^{n+r-1}\\
    &y''=\sum_{n=0}^\infty a_n(n+r)(n+r-1)x^{n+r-2}\\
    &6\sum_{n=0}^\infty a_n(n+r)(n+r-1)x^{n+r}+6\sum_{n=0}^\infty a_n(n+r)(n+r-1)x^{n+r+1}\\
    &+5\sum_{n=0}^\infty a_n(n+r)x^{n+r}-\sum_{n=0}^\infty a_nx^{n+r}\\
    &6\sum_{m=0}^\infty a_m(m+r)(m+r-1)x^{m+r}+6\sum_{m=1}^\infty a_{m-1}(m+r-1)(m+r-2)x^{m+r}\\
    &+5\sum_{m=0}^\infty a_m(m+r)x^{m+r}-\sum_{m=0}^\infty a_{m}x^{m+r}\\
    &6a_0(r)(r-1)x^r+5a_0(r)x^r-a_0x^r\\
    &+\sum_{m=1}^\infty\brround{6a_m(m+r)(m+r-1)+6a_{m-1}(m+r-1)(m+r)+5a_m(m+r)-a_{m}}x^{m+r}\\
    &\Ra r=\frac{1}{2},-\frac{1}{3}\\
    &a_m(6(m+r)(m+r-1)+5(m+r)-1)=-6a_{m-1}(m+r-1)(m+r-2)\\
    &a_m=\frac{-6a_{m-1}(m+r-1)(m+r-2)}{6(m+r)(m+r-1)+5(m+r)-1}\\
    &r=\frac{1}{2}:\ a_m=-a_{m-1}\frac{3(2m-1)(2m-3)}{2m(6m+5)}\\
    &a_1=\frac{3}{22}a_0\\
    &a_2=-\frac{9}{68}a_1=-\frac{27}{1496}a_0\\
    &r=-\frac{1}{3}:\ a_m=\frac{2(3m-4)(3m-7)}{3m(6m-5)}\\
    &a_1=-\frac{8}{3}a_0\\
    &a_2=a_1\frac{2}{21}=-\frac{16}{63}a_0\\
    &y=C_1x^{1/2}\brround{1+\frac{3}{22}x-\frac{27}{1496}x^2+\cdots}+C_2x^{-\frac{1}{3}}\brround{1-\frac{8}{3}x-\frac{16}{63}x^2+\cdots}
\end{aligned}

$$

Ex2: Special case of the Bessel equation

$$
\begin{aligned}
    &x^2y''+xy'+(x^2-\nu^2)y=0,\ \nu=\frac{1}{2}\\
    &\text{SP: }x=0\\
    &\alpha=1\\
    &\alpha'=0\\
    &\beta=x^2-\nu^2\\
    &\beta'=2x\\
    &\lim_{x\to0}1=1\\
    &\lim_{x\to0}x^2-\nu^2=-\nu^2=-\frac{1}{4}
\end{aligned}

$$

So $x=0$ is a regular singular point

$$
\begin{aligned}
    &r(r-1)+r-\frac{1}{4}=0\\
    &r^2-\frac{1}{4}=0\\
    &\brround{r-\frac{1}{2}}\brround{r+\frac{1}{2}}\Ra r=\pm\frac{1}{2}
\end{aligned}

$$

$$
\begin{aligned}
    &y=\sum_{n=0}^\infty a_nx^{n+r}\\
    &y'=\sum_{n=0}^\infty a_n(n+r)x^{n+r-1}\\
    &y''=\sum_{n=0}^\infty a_n(n+r)(n+r-1)x^{n+r-1}\\
    &\sum_{n=0}^\infty a_n(n+r)(n+r-1)x^{n+r}+\sum_{n=0}^\infty a_n(n+r)x^{n+r}+\sum_{n=0}^\infty a_n x^{n+r+2}-\nu^2\sum_{n=0}^\infty a_n x^{n+r}=0\\
    &\sum_{m=0}^\infty a_m(m+r)(m+r-1)x^{m+r}+\sum_{m=0}^\infty a_m(m+r)x^{m+r}+\sum_{m=2}^\infty a_{m-2}x^{m+r}-\nu^2\sum_{m=0}^\infty a_m x^{m+r}=0\\
    &a_0(r)(r-1)x^r+a_0rx^r-\nu^2 a_0 x^r+a_1(1+r)(r)x^{1+r}+a_1(1+r)x^{1+r}-\nu^2a_1 x^{1+r}\\
    &+\sum_{m=2}^\infty \brround{a_m(m+r)(m+r-1)+a_m(m+r)+a_{m-2}-\nu^2a_m}x^{m+r}=0\\
    &a_0r(r-1)+a_0r-\nu^2a_0=0\Ra a_0(r^2-\nu^2)=0\Ra r^2=\nu^2=\pm\frac{1}{2}\\
    &a_1(1+r)r+a_1(1+r)-a_1\nu^2=0\Ra a_1\brround{r^2+2r+1-\nu^2}=a_1(2r+1)\\
    &\Ra a_1=0\text{ or }r=-\frac{1}{2}\\
    &a_m=\frac{-a_{m-2}}{(m+r)^2-\nu^2}\\
    &r_1=\frac{1}{2}:\ a_1=0\\
    &a_m=\frac{-a_{m-2}}{m(m+1)}\\
    &m=2:\ a_2=-\frac{a_0}{3\cdot2}=-\frac{a_0}{3!}\\
    &m=3:\ a_3=-\frac{a_1}{3\cdot4}=0\\
    &m=4:\ a_4=-\frac{a_2}{5\cdot4}=\frac{a_0}{5!}\\
    &y_1=a_0x^{1/2}\brround{1-\frac{x^2}{3!}+\frac{x^4}{5!}+\cdots}\\
    &y_1=a_0x^{-1/2}\brround{x-\frac{x^3}{3!}+\frac{x^5}{5!}+\cdots}\\
    &y_1=a_0x^{-1/2}\sin x\\
    &r=-\frac{1}{2}\\
    &a_m=\frac{-a_{m-2}}{m(m-1)}\\
    &m=2:\ a_2=-\frac{a_0}{2\cdot1}=-\frac{a_0}{2!}\\
    &m=3:\ a_3=-\frac{a_1}{3\cdot2}=-\frac{a_1}{3!}\\
    &m=4:\ a_4=-\frac{a_2}{4\cdot3}=\frac{a_0}{4!}\\
    &m=5:\ a_5=-\frac{a_3}{5\cdot4}=\frac{a_1}{5!}\\
    &y_2=a_0x^{-1/2}\brround{1-\frac{x^2}{2!}+\frac{x^4}{4!}+\cdots}+a_1x^{-1/2}\brround{x-\frac{x^3}{3!}+\frac{x^5}{5!}+\cdots}\\
    &y_2=a_0x^{-1/2}\cos x+a_1x^{-1/2}\sin x\\
    &y(x)=y_1+y_2=x^{-1/2}\brround{A\sin x+B\cos x}
\end{aligned}

$$

Ex3:

$$
\begin{aligned}
    &(1-x^2)y''-xy'+\alpha^2y=0\text{ about \ensuremath{x=1}}\\
    &\lim_{x\to1}(x-1)\frac{-x}{1-x^2}=\lim_{x\to1}\frac{x}{1+x}=\frac{1}{2}\\
    &\lim_{x\to1}(x-1)^2\frac{\alpha^2}{1-x^2}=\lim_{x\to1}(x-1)\frac{\alpha^2}{1+x}=0
\end{aligned}

$$

So $x=1$ is a regular singular point

$$
\begin{aligned}
    &\text{At }x=1\\
    &r(r-1)+\frac{1}{2}r=0\\
    &r^2+\frac{1}{2}r=0\Ra r=0,\ \frac{1}{2}
\end{aligned}

$$

\begin{small}

$$
\begin{aligned}
    &\text{let }t=x-1,\ dt=dx\Ra \frac{dy}{dx}=\frac{dy}{dt}\\
    &(1-x)(1+x)y''-xy'+\alpha^2y=0\\
    &-t(t+2)y''-(t+1)y'+\alpha^2y=0\\
    &y=\sum_{n=0}^\infty a_nt^{n+r}\\
    &y'=\sum_{n=0}^\infty a_n(n+r)t^{n+r-1}\\
    &y''=\sum_{n=0}^\infty a_n(n+r)(n+r-1)t^{n+r-1}\\
    &-\sum_{n=0}^\infty a_n(n+r)(n+r-1)t^{n+r}-2\sum_{n=0}^\infty a_n(n+r)(n+r-1)t^{n+r-1}-\sum_{n=0}^\infty a_n(n+r)t^{n+r}\\
    &-\sum_{n=0}^\infty a_n(n+r)t^{n+r-1}+\alpha^2\sum_{n=0}^\infty a_nt^{n+r}=0\\
    &n=m+1\Ra m=n-1\\
    &-\sum_{m=0}^\infty a_m(m+r)(m+r-1)t^{m+r}-2\sum_{m=-1}^\infty a_{m+1}(m+r+1)(m+r)t^{m+r}-\sum_{m=0}^\infty a_m(m+r)t^{m+r}\\
    &-\sum_{m=-1}^\infty a_{m+1}(m+r+1)t^{m+r}+\alpha^2\sum_{m=0}^\infty a_mt^{m+r}=0\\
    &-2a_0(r)(r-1)t^{r-1}-a_0(r)t^{r-1}\\
    &+\sum_{m=0}^\infty \brround{-a_m(m+r)(m+r-1)-2a_{m+1}(m+r+1)(m+r)-a_m(m+r)-a_{m+1}(m+r+1)+\alpha^2 a_m}t^{m+r}\\
    &-2r(r-1)-r=0\Ra -2r^2+r=0\Ra r(1-2r)=0\Ra r=0,\ \frac{1}{2}\\
    &a_m\brround{-(m+r)(m+r-1)-(m+r)+\alpha^2}=a_{m+1}\brround{2(m+r+1)(m+r)+(m+r+1)}\\
    &a_{m+1}=a_m\frac{\alpha^2-(m+r)(m+r-1)-(m+r)}{2(m+r+1)(m+r)+(m+r+1)}\\
    &r=0:\ a_{m+1}=a_m\frac{\alpha^2-m(m-1)-m}{2(m+1)(m)+(m+1)}=a_m\frac{\alpha^2-m^2}{2m^2+3m+1}\\
    &m=0:\ a_1=\alpha^2a_0\\
    &m=1:\ a_2=\frac{\alpha^2-1}{6}a_1=\frac{(\alpha^2-1)\alpha^2}{6}a_0\\
    &m=2:\ a_3=\frac{\alpha^2-4}{15}a_2=\frac{(\alpha^2-4)(\alpha^2-1)\alpha^2}{90}a_0\\
    &y_1(t)=a_0\brround{1+\alpha^2t+\frac{(\alpha^2-1)\alpha^2}{6}t^2+\frac{(\alpha^2-4)(\alpha^2-1)\alpha^2}{90}t^3+\cdots}\\
    &y_1(x)=a_0\brround{1+\alpha^2(x-1)+\frac{(\alpha^2-1)\alpha^2}{6}(x-1)^2+\frac{(\alpha^2-4)(\alpha^2-1)\alpha^2}{90}(x-1)^3+\cdots}\\
    &r=\frac{1}{2}:\ a_{m+1}=a_m\frac{\alpha^2-(m+\frac{1}{2})(m-\frac{1}{2})-(m+\frac{1}{2})}{2(m+\frac{3}{2})(m+\frac{1}{2})+(m+\frac{3}{2})}=a_m\frac{4\alpha^2-(2m+1)(2m-1)-2(2m+1)}{2(2m+3)(2m+1)+2(2m+3)}\\
    &m=0:\ a_1=\frac{\alpha^2+1-2}{6+6}a_0=\frac{4\alpha^2-1}{12}a_0\\
    &m=1:\ a_2=\frac{4\alpha^2-(3)(1)-2(3)}{2(5)(3)+2(5)}a_1=\frac{4\alpha^2-9}{40}a_1=\frac{(4\alpha^2-9)(4\alpha^2-1)}{480}a_0\\
    &m=2:\ a_3=\frac{\alpha^2-(5)(3)-2(5)}{2(7)(5)+2(7)}a_2=\frac{\alpha^2-25}{84}a_2=\frac{(\alpha^2-9)(\alpha^2-4)(\alpha^2-1)}{40320}\\
    &y_2(t)=a_0\brround{t^{1/2}+\frac{4\alpha^2-1}{12}t^{3/2}+\frac{(4\alpha^2-9)(4\alpha^2-1)}{480}t^{5/2}+\frac{(\alpha^2-9)(\alpha^2-4)(\alpha^2-1)}{40320}t^{7/2}+\cdots}\\
    &y_2(x)=a_0\brround{(x-1)^{1/2}+\frac{4\alpha^2-1}{12}(x-1)^{3/2}+\frac{(4\alpha^2-9)(4\alpha^2-1)}{480}(x-1)^{5/2}+\cdots}\\
    &y=A+B(x-1)^{1/2}+\sum_{n=1}^\infty\brround{A(x-1)^n\prod_{m=0}^{n-1}\brround{\frac{\alpha^2-m^2}{2m^2+3m+1}}+B(x-1)^{n+1/2}\prod_{m=0}^{n-1}\brround{\frac{4\alpha^2-(2m+1)^2}{4(2m^2+5m+3)}}}
\end{aligned}

$$

\end{small}

## Solution by Laplace Transforms

We can use the derivative properties of the Laplace transform to help solve differential equations. The expression $y''+ay'+by=f(t)$ can be solved using the following method:

$$
\begin{aligned}
    &\lap\{y''+ay'+by\}=\lap\{f(t)\}\\
    &\text{let }Y=\lap\{y(t)\}\\
    &s^2Y-sy(0)-y'(0)+saY-ay(0)+bY=\lap\{f(t)\}\\
    &Y=\frac{\lap\{f(t)\}+sy(0)+y(0)+y'(0)}{s^2+as+b}\\
    &y(t)=\lap^{-1}\{Y\}=\lap^{-1}\left\{\frac{\lap\{f(t)\}+sy(0)+y(0)+y'(0)}{s^2+as+b}\right\}
\end{aligned}

$$

Ex: $y''-2y'+2y=e^{-t},\ y(0)=0,\ y'(0)=1$

$$
\begin{aligned}
    &\lap\brcurly{y''-2y'+2y}=\lap\brcurly{e^{-t}}\\
    &s^2Y-1-2sY+2Y=\frac{1}{s+1}\\
    &Y(s^2-2s+2)=\frac{1}{s+1}+1=\frac{1}{s+1}+\frac{s+1}{s+1}=\frac{s+2}{s+1}\\
    &Y=\frac{s+2}{(s+1)(s^2-2s+2)}\\
    &y=\lap^{-1}\{y\}=\lap^{-1}\brcurly{\frac{s+2}{(s+1)(s^2-2s+2)}}\\
    &\frac{s+2}{(s+1)(s^2-2s+2)}=\frac{A}{s+1}+\frac{Bs+C}{s^2-2s+2}\\
    &As^2-2sA+2A+Bs^2+Cs+Bs+C=s+2\\
    &\eqnsystem{A+B=0\\-2A+C+B=1\\2A+C=2}\Ra A=-B\Ra \eqnsystem{3B+C=1\\-2B=2-C}\Ra B=-\frac{1}{5}\Ra A=\frac{1}{5}\Ra C=\frac{8}{5}\\
    &\frac{s+2}{(s+1)(s^2-2s+2)}=\frac{1/5}{s+1}+\frac{-s/5+8/5}{(s^2-2s+2)}\\
    &-\frac{1}{5}\frac{s-8}{s^2-2s+1+1}=-\frac{1}{5}\frac{s-2}{(s-1)^2+1}=-\frac{1}{5}\frac{s-1}{(s-1)^2+1}+\frac{7}{5}\frac{1}{(s-1)^2+1}\\
    &y=\lap^{-1}\brcurly{\frac{1/5}{s+1}-\frac{1}{5}\frac{s-1}{(s-1)^2+1}+\frac{7/5}{(s-1)^2+1}}\\
    &y=\frac{1}{5}e^{-t}-\frac{1}{5}e^t\cos(t)+\frac{7}{5}e^t\sin(t)\\
    &y(t)=\frac{1}{5}(e^{-t}-e^t\cos(t)+7e^t\sin(t))
\end{aligned}

$$

Ex2: $x'''+x=0,\ x(0)=1,\ x'(0)=0,\ x''(0)=0$

$$
\begin{aligned}
    &\lap\brcurly{x'''+x}=0\\
    &s^3X-s^2+X=0\Ra X(s^3+1)=s^2\\
    &X=\frac{s^2}{s^3+1}=\frac{s^2}{(s+1)(s^2-s+1)}=\frac{A}{s+1}+\frac{Bs+C}{s^2-s+1}\\
    &As^2-As+A+Bs^2+Cs+Bs+C=s^2\\
    &\eqnsystem{A+B=1\\-A+C+B=0\\A+C=0}\Ra A=-C\Ra \eqnsystem{-C+B=1\\2C=-B}\Ra C=-\frac{1}{3}\Ra B=\frac{2}{3}\Ra A=\frac{1}{3}\\
    &X=\frac{1/3}{s+1}+\frac{1}{3}\frac{2s-1}{s^2-s+1}\\
    &\frac{2s-1}{s^2-s+1}=\frac{2s-1}{\brround{s^2-s+\frac{1}{4}}+\frac{3}{4}}=\frac{2(s-\frac{1}{2})}{\brround{s-\frac{1}{2}}^2+\frac{3}{4}}\\
    &X=\frac{1/3}{s+1}+\frac{2}{3}\frac{\brround{s-\frac{1}{2}}}{\brround{s-\frac{1}{2}}^2+\frac{3}{4}}\\
    &x=\lap\{X\}=\frac{1}{3}e^{-t}+\frac{2}{3}e^{\frac{t}{2}}\cos\brround{\frac{\sqrt{3}}{2}t}
\end{aligned}

$$

This method also allows us to work with step functions and delta functions. This is particularly useful for dealing with piecewise functions.

$$
\begin{aligned}
    \text{Ex: }&\lap\brcurly{f(t)},\ f(t)=\eqnsystem{t&0\leq t<1\\2-t&1\leq t<2\\0&2\leq t}\\
    &f(t)=t(u(t)-u(t-1))+(2-t)(u(t-1)-u(t-2))\\
    &f(t)=tu(t)-2tu(t-1)+2u(t-1)-2u(t-2)+tu(t-2)\\
    &\text{use }\lap\brcurly{u(t-a)f(t-a)}=e^{-as}\lap\brround{f(t)}\\
    &f(t)=tu(t)-2(t-1)u(t-1)+(t-2)u(t-2)\\
    &\lap\brcurly{t-a}=\frac{1}{s^2},\ s>0\\
    &\lap\brcurly{f(t)}=\frac{1}{s^2}-2e^{-s}\brround{\frac{1}{s^2}}+e^{-2s}\brround{\frac{1}{s^2}},\ s>0
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex2: }&\lap^{-1}\brcurly{\frac{e^{-s}+e^{-2s}-e^{-3s}-e^{-4s}}{s}}=\lap^{-1}\brcurly{\frac{e^{-s}}{s}}+\lap^{-1}\brcurly{\frac{e^{-2s}}{s}}-\lap^{-1}\brcurly{\frac{e^{-3s}}{s}}-\lap^{-1}\brcurly{\frac{e^{-4s}}{s}}\\
    &=u(t-1)+u(t-2)-u(t-3)-u(t-4)
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex3: }&x''+4x'+3x=2\delta(t-\pi),\ x(0)=2,\ x'(0)=0\\
    &\lap\brcurly{x''+4x'+3x}=2\lap\brcurly{\delta(t-\pi)}\\
    &s^2X-2s+4sX-8+3X=2e^{-\pi s}\\
    &X=\frac{2e^{-\pi s}+2s+8}{s^2+4s+3}\\
    &X=2\brround{\frac{e^{-\pi s}}{(s+3)(s+1)}+\frac{s}{(s+3)(s+1)}+\frac{4}{(s+3)(s+1)}}\\
    &\frac{s}{(s+3)(s+1)}=\frac{A}{s+3}+\frac{B}{s+1}\\
    &sA+A+sB+3B=s\\
    &\eqnsystem{A+B=1\\A+3B=0}\Ra -3B+B=1\Ra B=-\frac{1}{2}\Ra A=\frac{3}{2}\\
    &\frac{1}{(s+3)(s+1)}=\frac{A}{s+3}+\frac{B}{s+1}\\
    &sA+A+sB+3B=1\\
    &\eqnsystem{A+B=0\\A+3B=1}\Ra -B+3B=1\Ra B=\frac{1}{2}\Ra A=-\frac{1}{2}\\
    &X=-\frac{e^{-\pi s}}{s+3}+\frac{e^{-\pi s}}{s+1}+\frac{3}{s+3}-\frac{1}{s+1}-\frac{4}{s+3}+\frac{4}{s+1}\\
    &x=-u(t-\pi)e^{-3(t-\pi)}+u(t-\pi)e^{-(t-\pi)}+3e^{-3t}-e^{-t}-4e^{-3t}+4e^{-t}
\end{aligned}

$$

Ex4: $\displaystyle{y''+y'+\frac{5}{4}y=\eqnsystem{\sin(t),&0\leq t\leq \pi0,&\pi\leq t},\ y(0)=0,\ y'(0)=0}$

$$
\begin{aligned}
    &g(t)=\sin(t)(u(t)-u(t-\pi))=u(t)\sin(t)+u(t-\pi)\sin(t-\pi)\\
    &\lap\brcurly{y''+y'+\frac{5}{4}y}=\lap\brcurly{u(t)\sin(t)+u(t-\pi)\sin(t-\pi)}\\
    &s^2Y+sY+\frac{5}{4}Y=\frac{1}{s^2+1}+\frac{e^{-\pi s}}{s^2+1}\\
    &Y=\brround{\frac{1}{s^2+s+\frac{5}{4}}}\brround{\frac{1}{s^2+1}+\frac{e^{-\pi s}}{s^2+1}}\\
    &Y=\frac{1}{(s^2+s+\frac{5}{4})(s^2+1)}+\frac{e^{-\pi s}}{(s^2+s+\frac{5}{4})(s^2+1)}\\
    &y=\lap^{-1}\brcurly{\frac{1}{(s^2+s+\frac{5}{4})(s^2+1)}}+u(t-\pi)\lap^{-1}\brcurly{\frac{1}{(s^2+s+\frac{5}{4})(s^2+1)}}\\
    &\frac{1}{(s^2+s+\frac{5}{4})(s^2+1)}=\frac{As+B}{s^2+s+\frac{5}{4}}+\frac{Cs+D}{s^2+1}\\
    &\leadsto\frac{4}{17}\frac{1-4s}{s^2+1}+\frac{4}{17}\frac{4s+3}{s^2+s+\frac{5}{4}}\\
    &\frac{1}{s^2+s+\frac{5}{4}}=\frac{1}{\brround{s+\frac{1}{2}}^2+1}\\
    &\frac{4}{17}\frac{1-4s}{s^2+1}+\frac{4}{17}\frac{4s+3}{s^2+s+\frac{5}{4}}=\frac{4}{17}\brround{\frac{1}{s^2+1}-\frac{4s}{s^2+1}+\frac{4s+2}{(s^2+\frac{1}{2})^2+1}+\frac{1}{(s+\frac{1}{2})^2+1}}\\
    &\frac{4}{17}\lap^{-1}\brcurly{\frac{1}{(s^2+s+\frac{5}{4})(s^2+1)}}=\frac{4}{17}\brround{\sin(t)-4\cos(t)+4e^{-\frac{t}{2}}\cos(t)+e^{-\frac{t}{2}}\sin(t)}\\
    &y=\frac{4}{17}\brround{\sin(t)-4\cos(t)+4e^{-\frac{t}{2}}\cos(t)+e^{-\frac{t}{2}}\sin(t)}\\
    &+\frac{4}{17}u(t-\pi)\brround{\sin(t-\pi)-4\cos(t-\pi)+4e^{-\frac{(t-\pi)}{2}}\cos(t-\pi)+e^{-\frac{(t-\pi)}{2}}\sin(t-\pi)}\\
\end{aligned}

$$
