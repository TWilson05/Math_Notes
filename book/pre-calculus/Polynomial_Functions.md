# Polynomial Functions

<!-- Source: [Sections/Pre-Calculus/Polynomial_Functions.tex](../../Sections/Pre-Calculus/Polynomial_Functions.tex) -->

## Polynomials

A polynomial function is a function in the form of $f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0$
Definitions: degree of a polynomial is the highest exponent of $x$ in the function. End behavior is the y-values as $|x|$ gets increasingly large. Even/odd polynomials refers to the highest degree. Even polynomials will always start and end in the same direction (as in start above the x-axis and end above the x-axis). Odd polynomials will keep the same path and will always cross over the x-axis, ensuring that they will always have at least one solution.
## Polynomial Division

Any polynomial divided by another polynomial to get a quotient and a remainder.
Long Division Method:
The goal is to elliminate the head term each time/ To do this, multiply the polynomial by a LCM and write what we had to multiply it by in each case above.
Ex: $\dfrac{6x^3-2x^2+x+3}{x^2-x+1}$
\polylongdiv[style=A]{6x^3-2x^2+x+3}{x^2-x+1}
$\dfrac{6x^3-2x^2+x+3}{x^2-x+1}=6x+4+\dfrac{x-1}{x^2-x+1}$

Synthetic Division Method:
We set it up taking the coefficients of each x-term in the top row of the box and the solution of the binomial on the outside.
We bring the first number down and then multiply it by $3$ and bring it up.
Then we take the $15$ and add it with the $-12$ and bring the sum to the bottom. The process is repeated and the coefficients on the bottom will form the answer as well as the remainder.
Ex: $\dfrac{4x^3+15x^2+7x-10}{x+3}$
 \polyhornerscheme[x=-3]{4x^3+15x^2+7x-10}
 $\dfrac{4x^3+15x^2+7x-10}{x+3}=4x^2+3x-2-\dfrac{4}{x+3}$

## Factoring Polynomials

Remainder Theorem:
When a polynomial, $P(x)$, is divided by a binomial of the form $x-a$, the remainder is $P(a)$. A polynomial divided by one of its factors will have no remainder. So $P(a)=0$ for where $a$ is a solution.
Factor Theorem:
$x-a$ is a factor of $P(x)$ if and only if $P(a)=0$.
Integral Zero Theorem:
If $x-a$ is a factor of $P(x)$, $a$ is a factor of the constant term.
Ex: possible factors of $x^2+2x-10$ could include $a$ values of $\{\pm1,\pm2,\pm5,\pm10\}$.
When there is a coefficient in front of the leading term, you must take factors of the constant term divided by the coefficient.
Ex: Possible $a$-values of $4x^3+39x^2+54x-16$:
Factors of $-16$: $\{\pm1,\pm2,\pm4,\pm8,\pm16\}$
Factors of $4$: $\{\pm1,\pm2,\pm4\}$
$\dfrac{\text{Factors of }-16}{\text{Factors of }4}:\,\{\pm1,\pm\frac{1}{4},\pm\frac{1}{2},\pm2,\pm4,\pm8,\pm16\}$
By using the remainder theorem and polynomial division, we can fully factor any degree polynomial.
Ex: Factor $x^4+4x^3-10x^2-28x-15$

$$
\begin{aligned}
    &\text{Factors of }-15:\,\{\pm1,\pm3,\pm5,\pm15\}\\
    &P(-1)=(-1)^4+4(-1)^3-10(-1)^2-28(-1)-15=0\therefore x+1\text{ is a factor}
\end{aligned}

$$

\polyhornerscheme[x=-1]{x^4+4x^3-10x^2-28x-15}

$$
\begin{aligned}
    &x^4+4x^3-10x^2-28x-15=(x+1)(x^3+3x^2-13x-15)\\
    &\text{Factors of }-15:\,\{\pm1,\pm3,\pm5,\pm15\}\\
    &P(3)=(3)^3+3(3)^2-13(3)-15=0\therefore x-3\text{ is a factor}
\end{aligned}

$$

\polyhornerscheme[x=3]{x^3+3x^2-13x-15}

$$
\begin{aligned}
    &x^4+4x^3-10x^2-28x-15=(x+1)(x-3)(x^2+6x+5)\\
    &=(x+1)(x-3)(x+5)(x+1)\\
    &=(x+5)(x-3)(x+1)^2\\
    &x=-5,-1,3
\end{aligned}

$$

## Graphs

All polynomials are continuous functions.
Multiplicity refers to the number of times the zero of a function occurs.
Ex: $(x-1)^2$ has a multiplicity of 2.
When a function has an odd multiplicity, it crosses the x-axis. When it has an even multiplicity, it touches the x-axis and "bounces off", coming back in the same direction.
To graph a polynomial, first factor it and plot the zeros. Then look at the end behavior and the multiplicity. You can use calculus to find the locations of the peaks and valleys.
