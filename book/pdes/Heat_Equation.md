# Heat Equation

<!-- Source: [Sections/PDEs/Heat_Equation.tex](../../Sections/PDEs/Heat_Equation.tex) -->

## Finite Difference Approximations

We can approximate derivatives using Taylor approximations as follows:

$$
\begin{aligned}
    &f(x_0+\Delta x)=f(x_0)+f'(x_0)\Delta x+\mathcal{O}(\Delta x^2)\\
    &f'(x_0)=\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}+\mathcal{O}(\Delta x)
\end{aligned}

$$

$$
\begin{aligned}
    &f(x_0+\Delta x)=f(x_0)+\Delta xf'(x_0)+\frac{\Delta x^2}{2}f''(x_0)+\mathcal{O}(\Delta x^3)\\
    &f(x_0-\Delta x)=f(x_0)-\Delta xf'(x_0)+\frac{\Delta x^2}{2}f''(x_0)\\
    &f(x_0+\Delta x)+f(x_0-\Delta x)=2f(x_0)+\Delta x^2f''(x_0)+\mathcal{O}(\Delta x^4)\\
    &f''(x_0)=\frac{f(x_0+\Delta x)-2f(x_0)+f(x_0-\Delta x)}{\Delta x^2}+\mathcal{O}(\Delta x^2)
\end{aligned}

$$

This gives us approximate solutions of $f'(x_0)$ and $f''(x_0)$ which we can make use of in our PDE.

$$
\begin{aligned}
    &u_t=\alpha^2u_{xx}\\
    &u_t=\frac{u(x,t+\Delta t)-u(x,t)}{\Delta t}\\
    &u_{xx}=\frac{u(x,t+\Delta t)-2u(x,t)+u(x-\Delta x,t)}{\Delta x^2}\\
    &\Ra \frac{u(x,t+\Delta t)-u(x,t)}{\Delta t}=\alpha^2\frac{u(x,t+\Delta t)-2u(x,t)+u(x-\Delta x,t)}{\Delta x^2}
\end{aligned}

$$

Writing $u(x+\Delta x,t)$ and similar expressions over and over can get quite long and tedious so we can make use of index notation to clean this up.
If we write $x=i\Delta x$ and $t=k\Delta t$ where $i,k\in\Z$ then we can express each $u$ term as $u_i^k$ where $i$ is the node number and $k$ is the time step number.
So our expression above turns into

$$
\begin{aligned}
    &\frac{u_i^{k+1}-u_i^k}{\Delta t}=\alpha^2\frac{u_{i+1}^k-2u_i^k+u_{i-1}^k}{\Delta x^2}\\
    &u_i^{k+1}=\alpha^2\frac{\Delta t}{\Delta x^2}(u_{i+1}^k-2u_i^k+u_{i-1}^k)+u_i^k
\end{aligned}

$$

This now gives us an equation for time $k+1$ that is only dependent on time $k$ so as long as we have the initial positions at time $k$, we can calculate every position of time $k+1$.
Ex: Calculate $u(x,0.2)$ with $\Delta t=0.01$ and $\Delta x=0.2$ with boundary conditions $u(0,t)=u_x(1,t)=0$ and initial condition

$$
u(x,0)=\eqnsystem{0 & 0\leq x< 0.4\\1 & 0.4\leq x \leq 0.8\\0 & 0.8<x\leq 1}

$$

$$
\begin{aligned}
    &\frac{u_n^{k+1}-u_n^k}{\Delta t}=\frac{u_{n+1}^k-2u_n^k+u_{n-1}^k}{\Delta x^2}\\
    &u_n^{k+1}=\frac{\Delta t}{\Delta x^2}\brround{u_{n+1}^k-2u_n^k+u_{n-1}^k}+u_n^k\\
    &u_0^0=0,\ u_1^k=0,\ u_2^0=1,\ u_3^0=1,\ u_4^0=1,\ u_5^0=0,\ \frac{\Delta t}{\Delta x^2}=\frac{1}{4}\\
    &u_k^0=0\ \forall k\\
    &\frac{\partial}{\partial x}(1,t)=0=\frac{u_6^k-u_4^k}{2\Delta x}\Ra u_6^k=u_4^k\\
    &\Ra u_5^{k+1}=\frac{\Delta t}{\Delta x^2}\brround{2u_4^k-2u_5^k}+u_5^k\\
    &u_1^1=\frac{1}{4}(1-0+0)+0=\frac{1}{4}\\
    &u_2^1=\frac{1}{4}(1-2(1)+0)+1=\frac{3}{4}\\
    &u_3^1=\frac{1}{4}(1-2(1)+1)+1=1\\
    &u_4^1=\frac{1}{4}(0-2(1)+1)+1=\frac{3}{4}\\
    &u_5^1=\frac{1}{4}(2(1)-0)+0=\frac{1}{2}\\
    &u_1^2=\frac{1}{4}\brround{0-2\frac{1}{4}+\frac{3}{4}}+\frac{1}{4}=\frac{5}{16}\\
    &u_2^2=\frac{1}{4}\brround{\frac{1}{4}-2\frac{3}{4}+1}+\frac{3}{4}=\frac{11}{16}\\
    &u_3^2=\frac{1}{4}\brround{\frac{3}{4}-2(1)+\frac{3}{4}}+1=\frac{14}{16}\\
    &u_4^2=\frac{1}{4}\brround{\frac{1}{2}-2\frac{3}{4}+1}+\frac{3}{4}=\frac{12}{16}\\
    &u_5^2=\frac{2}{4}\brround{\frac{3}{4}-\frac{1}{2}}+\frac{1}{2}=\frac{10}{16}
\end{aligned}

$$

## Separation of Variables

In order to solve the heat equation, we require one initial condition and two boundary conditions.
The general form of the heat equation will be

$$
\frac{\partial u}{\partial t}=\alpha^2\frac{\partial^2u}{\partial x}

$$

where the domain is $0\leq x\leq L$ and $t>0$
We can solve this type of problem using separation of variables. This assumes that we will have a solution of the form $u(x,t)=X(x)T(t)$

$$
\begin{aligned}
    &u(x,t)=X(x)T(t)\\
    &u_t=\alpha^2 u_{xx}\\
    &XT'=\alpha^2X''T\\
\end{aligned}

$$

If we divide both sides by $XT$ then we get $X$ and $T$ on separate sides of the equation

$$
\begin{aligned}
    &\frac{T'}{T}=\alpha^2\frac{X''}{X}\Ra \frac{1}{\alpha^2}\frac{T'}{T}=\frac{X''}{X}
\end{aligned}

$$

This implies that the $x$ and $t$ are independent of one another which is why separation of variables is able to work. Because they are separate, we can also set this equation equal to a constant, $-\lambda$. (The negative sign is cleverly put in place to make the math a little nicer later)

$$
\begin{aligned}
    &\frac{1}{\alpha^2}\frac{T'}{T}=\frac{X''}{X}=-\lambda
\end{aligned}

$$

We can use this to write out an ODE for both $X$ and $T$.
The equation for $T$ works out to be a first order ODE and will always have the following result:

$$
\begin{aligned}
    &\frac{1}{\alpha^2}\frac{T'}{T}=-\lambda\Ra \frac{dT}{dt}=-\alpha^2\lambda T\Ra \int \frac{dT}{T}=-\int\alpha^2\lambda dt\\
    &T(t)=Ce^{-\lambda\alpha^2t}
\end{aligned}

$$

The equation for $X$ will be 2nd order and is subject to the boundary conditions of the problem.

$$
\begin{aligned}
    &\frac{X''}{X}=-\lambda X\Ra X''+\lambda X=0
\end{aligned}

$$

It is easy to see that $X(x)=0$ is a solution to this ODE, however, we are interested in finding the general solution to this ODE. This means finding values of $\lambda$ that give non-trivial (nonzero) solutions for $X(x)$ subject to the given boundary conditions.
There are 5 standard sets of boundary conditions for the initial boundary value problem (IBVP).

    \begin{multicols}{2}
- Dirichelt Problem
    $u(0,t)=u(L,t)=0$

$$
\begin{aligned}
        &\lambda_n=\brround{\frac{n\pi}{L}}^2\\
        &X_n=\sin\brround{\frac{n\pi x}{L}},\ n\geq1
\end{aligned}

$$

- Neumann Problem
    $u_x(0,t)=u_x(L,t)=0$

$$
\begin{aligned}
        &\lambda_n=0,\ \brround{\frac{n\pi}{L}}^2\\
        &X_n=1,\ \cos\brround{\frac{n\pi x}{L}},\ n\geq1
\end{aligned}

$$

- Periodic Boundary Conditions
    $u(0,t)=u(L,t)$ and $u_x(0,t)=u_x(L,t)$

$$
\begin{aligned}
        &\lambda_n=0,\ \brround{\frac{n\pi}{L}}^2\\
        &X_n=1,\ \sin\brround{\frac{n\pi x}{L}},\ \cos\brround{\frac{n\pi x}{L}},\ n\geq1
\end{aligned}

$$

    \vfill\null\columnbreak

- Mixed Type 1
    $u(0,t)=u_x(L,t)=0$

$$
\begin{aligned}
        &\lambda_n=\brround{\frac{2n-1}{2L}\pi}^2\\
        &X_n=\sin\brround{\frac{2n-1}{2L}\pi x},\ n\geq1
\end{aligned}

$$

- Mixed Type 2
    $u_x(0,t)=u(L,t)$

$$
\begin{aligned}
        &\lambda_n=\brround{\frac{2n-1}{2L}\pi}^2\\
        &X_n=\cos\brround{\frac{2n-1}{2L}\pi x},\ n\geq1
\end{aligned}

$$

    \end{multicols}

To go into how these values were determined, let's look at the Dirichlet problem.
We will start with

$$
\begin{aligned}
    &X''+\lambda X=0,\\
    &X(0)=X(L)=0
\end{aligned}

$$

Recall that for constant coefficient ODES, depending on the value of the eigenvalue, $\lambda$, we can have 3 different forms of solutions and so we must look at each case.

- $\lambda<0\Ra \lambda=-\mu^2$

$$
\begin{aligned}
        &X''-\mu^2X=0\Ra r^2-\mu^2=0\Ra r=\pm\mu\\
        &X(x)=C_1e^{-\mu x}+C_2e^{\mu x}
\end{aligned}

$$

    Alternatively, we can use the relationships $\sinh x=\frac{e^x-e^{-x}}{2}$ and $\cosh x=\frac{e^x+e^{-x}}{2}$ to rewrite the solution as

$$
\begin{aligned}
        &X(x)=A\sinh(\mu x)+B\cosh(\mu x)
\end{aligned}

$$

    Now, applying the boundary conditions,

$$
\begin{aligned}
        &X(0)=0\Ra B=0\\
        &X(L)=0\Ra A\sinh(\mu L)=0\Ra A=0\\
        &\therefore X(x)=0
\end{aligned}

$$

    This makes the solution trivial so $\lambda\nless0$.
    (In general, for the heat equation we will not have $\lambda<0$ so we can usually skip this case.)
- $\lambda=0$

$$
\begin{aligned}
        &X''=0\Ra X(x)=Ax+B
\end{aligned}

$$

    Applying the BCs;

$$
\begin{aligned}
        &X(0)=0\Ra B=0\\
        &X(L)=0\Ra A=0\\
        &\therefore X(x)=0
\end{aligned}

$$

    So the solution is trivial and $\lambda\neq 0$
- $\lambda>0\Ra \lambda=\mu^2$

$$
\begin{aligned}
        &X''+\mu^2X=0\Ra r=\pm i\mu\\
        &X(x)=A\sin(\mu x)+B\cos(\mu x)
\end{aligned}

$$

    Applying the BCs;

$$
\begin{aligned}
        &X(0)=0\Ra B=0\\
        &X(L)=0\Ra A\sin(\mu L)=0
\end{aligned}

$$

    This means that either $A=0$ or $\sin(\mu L)=0$. In order to have a non-trivial solution, we require that $\sin(\mu L)=0$. This gives

$$
\begin{aligned}
        &\mu L=n\pi,\ n\in\N\\
        &\mu=\frac{n\pi}{L},\ n\in\N
\end{aligned}

$$

    Note that we have $n\in\N$ and $n\geq1$ because we require that $\mu\neq 0$ and having negative $n$ would not give any new linearly independent solutions.
    And so our eigenvalues are

$$
\begin{aligned}
        &\lambda=\brround{\frac{n\pi}{L}}^2,\ n\in\N
\end{aligned}

$$

    and our eigenfunctions are

$$
\begin{aligned}
        &X_n(x)=A_n\sin\brround{\frac{n\pi x}{L}}
\end{aligned}

$$


This same process is done for each of the other 4 standard boundary conditions.

Keeping with the example of Dirichlet boundary conditions, we will have the general solution of

$$
\begin{aligned}
    &u_n(x,t)=X_nT_n\\
    &u_n(x,t)=A_n\sin\brround{\frac{n\pi x}{L}}e^{\alpha^2\brround{\frac{n\pi}{L}}^2t}
\end{aligned}

$$

This gives solutions for each value of $n$. We know that the specific solution is going to be some linear combination of each individual solution though so we can write the general solution as

$$
\begin{aligned}
    &u(x,t)=\sum_{n=1}^\infty A_n\sin\brround{\frac{n\pi x}{L}}e^{\alpha^2\brround{\frac{n\pi}{L}}^2t}
\end{aligned}

$$

## Fourier Series

To find the particular solution of a PDE, we require the use of Fourier series. At this point, we have the general solution expressed in terms of a sum with an unknown coefficient, $A_n$. We can use the initial condition to determine this coefficient. However, the initial condition will almost never be expressed as a sum so we need to make it into a sum. This is what Fourier series allows us to do.
The Fourier series expresses a function in terms of sines and cosines of different frequencies.

$$
f(x)=\sum_{n=0}^\infty a_n\cos\brround{\frac{n\pi x}{L}}+\sum_{n=1}^\infty b_n\sin\brround{\frac{n\pi x}{L}}=a_0+\sum_{n=1}^\infty\brround{a_n\cos\brround{\frac{n\pi x}{L}}+b_n\sin\brround{\frac{n\pi x}{L}}}

$$

This may seem a little messy and it turns out that there is a nicer way to express the Fourier series using complex numbers:
Right now we have

$$
\begin{aligned}
    &f(\alpha)=a_0+\sum_{n=1}^\infty a_n\cos(n\alpha)+\sum_{n=1}^\infty\sin(n\alpha)
\end{aligned}

$$

We can make use of the identities

$$
\begin{aligned}
    &\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2},\ \sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2}
\end{aligned}

$$

So we have

$$
\begin{aligned}
    &f(\alpha)=a_0+\sum_{n=1}^\infty\frac{a_n}{2}\brround{e^{in\alpha}+e^{-in\alpha}}+\sum_{n=1}^\infty\frac{b_n}{2}\brround{e^{in\alpha}-e^{-in\alpha}}\\
    &f(\alpha)=\sum_{n=1}^\infty\brround{\frac{a_n-ib_n}{2}}e^{in\alpha}+\sum_{n=1}^\infty\brround{\frac{a_n+ib_n}{2}}e^{-in\alpha}\\
    &f(\alpha)=\underbrace{a_0}_{c_0}+\sum_{n=1}^\infty\underbrace{\brround{\frac{a_n-ib_n}{2}}}_{c_n}e^{in\alpha}+\sum_{n=-\infty}^{-1}\underbrace{\brround{\frac{a_{-n}+ib_{-n}}{2}}}_{c_n}e^{in\alpha}\\
    &f(\alpha)=\sum_{n=-\infty}^\infty c_ne^{in\alpha},\ c_n=\frac{1}{2L}\int_{-L}^Lf(\alpha)e^{-in\alpha}d\alpha
\end{aligned}

$$

To match functions, we can use the concept of orthogonality.
$f(x)$ and $g(x)$ are orthogonal if $\displaystyle{\int_{-L}^Lf(x)g(x)dx=0}$
Trig functions have some particularly useful orthogonality properties.
For where $m,n\in\N$

$$
\begin{aligned}
    &\int_{-L}^L\sin\brround{\frac{n\pi x}{L}}\sin\brround{\frac{m\pi x}{L}}dx=\eqnsystem{0 & \text{if }m\neq n\\ L & \text{if }m=n}\\
    &\int_{-L}^L\cos\brround{\frac{n\pi x}{L}}\cos\brround{\frac{m\pi x}{L}}dx=\eqnsystem{0 & \text{if }m\neq n\\ L & \text{if }m=n\neq 0\\ 2L & \text{if }m=n=0}\\
    &\int_{-L}^L\sin\brround{\frac{n\pi x}{L}}\cos\brround{\frac{m\pi x}{L}}dx=0
\end{aligned}

$$

Derivation:

$$
\begin{aligned}
    &I=\int_{-L}^L\sin\brround{\frac{n\pi x}{L}}\sin\brround{\frac{m\pi x}{L}}dx\\
    &\text{case }m\neq n:\\
    &I=2\int_{0}^L\sin\brround{\frac{n\pi x}{L}}\sin\brround{\frac{m\pi x}{L}}dx\\
    &\cos(A-B)=\cos A\cos B+\sin A\sin B\\
    &\cos(A+B)=\cos A\cos B-\sin A\sin B\\
    &\sin A\sin B=\frac{1}{2}\brround{\cos(A-B)-\cos(A+B)}\\
    &I=\frac{2}{2}\int_0^L\brround{\cos\brround{\frac{n-m}{L}\pi x}-\cos\brround{\frac{n+m}{L}\pi x}}dx\\
    &I=\brsquare{\frac{L}{(n-m)\pi}\sin\brround{\frac{n-m}{L}\pi x}}_0^L-\brsquare{\frac{L}{(n+m)\pi}\sin\brround{\frac{n+m}{L}\pi x}}_0^L=0\\
    &\text{case }m=n:\\
    &I=2\int_0^L\sin^2\brround{\frac{n\pi x}{L}}dx\\
    &\cos 2A=1-\sin^2A\Ra \sin^2 A=\frac{1-\cos 2A}{2}\\
    &I=\frac{2}{2}\int_0^L\brround{1-\cos\brround{\frac{2n\pi x}{L}}}dx\\
    &I={x}\eval_0^L-{\frac{L}{2n\pi}\sin\brround{\frac{2n\pi x}{L}}}\eval_0^L=L
\end{aligned}

$$

Note that this result makes use of the fact that $\sin(kx)=0$ for where $k\in\Z$, hence why some terms appear to drop out. This also means that these specific orthogonality calculations only hold for integer values of $m$ and $n$. This is fine for use in Fourier series but it is something to be aware of.

So far, we have introduced what Fourier series is; now let's get into how to use it.
When using Fourier series, we are trying to solve for the unknown coefficients, $a_0,a_m,b_m$ in the series.
We can make use of the trig orthogonality rules we determined earlier to determine these coefficients.
To solve for $b_m$, we can multiply by $\sin\brround{\frac{m\pi x}{L}}$ and integrate from $-L$ to $L$.

$$
\begin{aligned}
    &f(x)=\sum_{n=0}^\infty a_n\cos\brround{\frac{n\pi x}{L}}+\sum_{n=1}^\infty\sin\brround{\frac{n\pi x}{L}}\\
    &\int_{-L}^L f(x)\sin\brround{\frac{m\pi x}{L}}dx=\sum_{n=0}^\infty a_n\underbrace{\int_{-L}^L\cos\brround{\frac{n\pi x}{L}}\sin\brround{\frac{m\pi x}{L}}dx}_{=0}+\sum_{n=1}^\infty b_n\underbrace{\int_{-L}^L\sin\brround{\frac{n\pi x}{L}}\sin\brround{\frac{m\pi x}{L}}dx}_{=L\text{ if }m=n}\\
    &\int_{-L}^Lf(x)\sin\brround{\frac{m\pi x}{L}}dx=b_mL\\
    &b_m=\frac{1}{L}\int_{-L}^L f(x)\sin\brround{\frac{m\pi x}{L}}dx
\end{aligned}

$$

To find $a_m$, we do the same thing but multiply by $\cos\brround{\frac{m\pi x}{L}}$

$$
\begin{aligned}
    &f(x)=\sum_{n=0}^\infty a_n\cos\brround{\frac{n\pi x}{L}}+\sum_{n=1}^\infty\sin\brround{\frac{n\pi x}{L}}\\
    &\int_{-L}^Lf(x)\cos\brround{\frac{m\pi x}{L}}dx=\sum_{n=0}^\infty a_n\underbrace{\int_{-L}^L\cos\brround{\frac{n\pi x}{L}}\cos\brround{\frac{m\pi x}{L}}dx}_{=\eqnsystem{2L & \text{if }m=0\\ L & \text{if }m=n}}+\sum_{n=1}^\infty b_n\underbrace{\int_{-L}^L\sin\brround{\frac{n\pi x}{L}}\sin\brround{\frac{m\pi x}{L}}dx}_{=0}\\
    &a_0=\frac{1}{2L}\int_{-L}^L f(x)dx\\
    &a_m=\frac{1}{L}\int_{-L}^L f(x)\cos\brround{\frac{m\pi x}{L}}dx
\end{aligned}

$$

If $f(x)$ is odd then

$$
\begin{aligned}
    &a_0=a_m=0\\
    &b_m=\frac{2}{L}\int_0^L f(x)\sin\brround{\frac{m\pi x}{L}}dx
\end{aligned}

$$

If $f(x)$ is even then

$$
\begin{aligned}
    &b_m=0\\
    &a_0=\frac{1}{L}\int_0^L f(x)dx\\
    &a_m=\frac{2}{L}\int_0^L f(x)\cos\brround{\frac{m\pi x}{L}}dx
\end{aligned}

$$

If you are trying to match a function that is only defined between $0$ and $L$ then you must make an odd or even extension.
Ex: for the function $1-x$ defined on $0\leq x\leq1$, the even extension would be

$$
\begin{aligned}
    &f^e(x)=\eqnsystem{1-x & x\geq 0\\ x+1 & x<0}
\end{aligned}

$$

The odd extension would be

$$
\begin{aligned}
    &f^e(x)=\eqnsystem{1-x & x>0\\ 0 & x=0\\ -1-x & x<0}
\end{aligned}

$$

Note that when there is a discontinuity, the function will take the average value of the limit from both sides, hence why $f^e(x)=0$ for where $x=0$ as we have

$$
\begin{aligned}
    &f^e(0)=\frac{1}{2}\brround{\lim_{x\to 0^-}f^e(x)+\lim_{x\to0^+}f^e(x)}=\frac{1}{2}\brround{-1+1}=0
\end{aligned}

$$

When dealing with a function that is neither even or odd, we will have to use the full Fourier series with both sines and cosines.

## Homogeneous Heat Equation

Now we are able to put it all together and solve the heat equation.
Any of the following forms of the heat equation are able to be solved using the separation of variables method (provided they have homogeneous BCs).

$$
\begin{aligned}
    &u_{t}=\alpha^2u_{xx}\\
    &u_{t}=\alpha^2u_{xx}-\gamma u\\
    &u_{t}=\alpha^2u_{xx}-\gamma(t)u\\
    &u_{t}=\alpha^2u_{xx}-\gamma(t)\\ &u_t+\eta(t)u
\end{aligned}

$$

Ex:

$$
\begin{aligned}
    &\eqnsystem{u_t=\alpha^2u_{xx},\ 0\leq x\leq L,\ t\geq 0\\ u(0,t)=u(L,t)=0\\ u(x,0)=f(x)=x(L-x),\ 0\leq x\leq L}\\
    &u(x,t)=X(x)T(t)\\
    &XT'=\alpha^2 X''T\Ra \frac{1}{\alpha^2}\frac{T'}{T}=\frac{X''}{X}=-\lambda\\
    &u(0,t)=0\Ra X(0)=0\\
    &u(L,t)=0\Ra X(L)=0\\
    &X''+\lambda X=0
\end{aligned}

$$

These are Dirichlet boundary conditions so we can skip some steps and get the eigenvalues and eigenfunctions to be

$$
\begin{aligned}
    &\lambda_n=\brround{\frac{n\pi }{L}}^2\\
    &X_n=\sin\brround{\frac{n\pi x}{L}},\ n\geq 1\\
    &T_n=e^{-\alpha^2\lambda_n t}=e^{-\alpha^2\brround{\frac{n\pi}{L}}^2t}\\
    &u_n(x,t)=X_n(x)T_n(t)=\sin\brround{\frac{n\pi x}{L}}e^{-\alpha^2\brround{\frac{n\pi}{L}}^2t}\\
    &u(x,t)=\sum_{n=1}^\infty c_n\sin\brround{\frac{n\pi x}{L}}e^{-\alpha^2\brround{\frac{n\pi}{L}}^2t}
\end{aligned}

$$

Now we can use the  initial condition to solve for $c_n$.

$$
\begin{aligned}
    &u(x,0)=\sum_{n=1}^\infty c_n\sin\brround{\frac{n\pi}{L}}
\end{aligned}

$$

Because we are working with a Fourier sine series, we will want the odd extension of our initial condition function.

$$
\begin{aligned}
    &f(x)=x(L-x)\\
    &f^e(x)=\eqnsystem{x(L-x) & x\geq 0\\ x(L+x) & x<0}\\
    &b_n=\frac{1}{L}\int_{-L}^Lf^e(x)\sin\brround{\frac{n\pi x}{L}}dx
\end{aligned}

$$

Recall that an odd function times an odd function gives an even function. Because both $f^e$ and $\sin$ are odd functions in this case, their product gives an even and so we are integrating an even function over a symmetric domain and thus, can simplify

$$
\begin{aligned}
    &b_n=\frac{2}{L}\int_0^Lf^e(x)\sin\brround{\frac{n\pi x}{L}}dx=\frac{2}{L}\int_0^Lf(x)\sin\brround{\frac{n\pi x}{L}}dx\\
    &b_n=\frac{2}{L}\int_0^Lx(L-x)\sin\brround{\frac{n\pi x}{L}}dx
\end{aligned}

$$

This integral works out to be

$$
\begin{aligned}
    &\frac{4L^2}{(n\pi)^3}\brround{(-1)^{n+1}+1}
\end{aligned}

$$

Note that the identity $\cos(n\pi)=(-1)^n$ was used in simplifying this integral. There will be a few occasions where we make use of integer or half-integer multiples of pi in the arguments of trig functions to simplify.
Putting everything together now, we get

$$
\begin{aligned}
    &u(x,t)=\sum_{n=1}^\infty\frac{4L^2}{(n\pi)^3}\brround{(-1)^{n+1}+1}\sin\brround{\frac{n\pi x}{L}}e^{-\alpha^2\brround{\frac{n\pi}{L}}^2t}
\end{aligned}

$$

Simple, right? (it gets much worse later)
Ex2:

$$
\begin{aligned}
    &\eqnsystem{u_t=u_{xx},\ -2\pi\leq x\leq 2\pi,\ t\geq0\\ u(-2\pi,t)=u(2\pi,t)\\ u_x(-2\pi,t)=u_x(2\pi,t)\\ u(x,0)=f(x)=\cos\brround{\frac{x}{2}}+\sin x}\\
    &u(x,t)=X(x)T(t)\\
    &\Ra \frac{T'}{T}=\frac{X''}{X}=-\lambda\\
    &X''+\lambda X=0
\end{aligned}

$$

We have periodic boundary conditions so the eigenvalues and eigenfunctions will be

$$
\begin{aligned}
    &\lambda_0=0,\ \lambda_n=\brround{\frac{n\pi}{L}}^2=\brround{\frac{n}{2}}^2\\
    &X_0=1,\ X_{n1}=\sin\brround{\frac{nx}{2}},\ X_{n2}=\cos\brround{\frac{nx}{2}}\\
    &T_0=1,\ T_n=e^{-\brround{\frac{n}{2}}^2t}\\
    &u_0(x,t)=1\\
    &u_{n1}(x,t)=\sin\brround{\frac{nx}{2}}e^{-\brround{\frac{n}{2}}^2t}\\
    &u_{n2}=\cos\brround{\frac{nx}{2}}e^{-\brround{\frac{n}{2}}^2t}\\
    &u(x,t)=a_0+\sum_{n=1}^\infty a_n\cos\brround{\frac{nx}{2}}e^{-\brround{\frac{n}{2}}^2t}+\sum_{n=1}^\infty b_n\sin\brround{\frac{nx}{2}}e^{-\brround{\frac{n}{2}}^2t}\\
    &u(x,0)=a_0+\sum_{n=1}^\infty a_n\cos\brround{\frac{nx}{2}}+\sum_{n=1}^\infty b_n\sin\brround{\frac{nx}{2}}=f(x)=\cos\brround{\frac{x}{2}}+\sin x
\end{aligned}

$$

Now, using Fourier series,

$$
\begin{aligned}
    &f(x)=a_0+\sum_{n=1}^\infty a_n\cos\brround{\frac{n\pi x}{L}}+\sum_{n=1}^\infty b_n\sin\brround{\frac{n\pi x}{L}}\\
    &a_0=\frac{1}{2L}\int_{-L}^L f(x)dx=\frac{1}{4\pi}\int_{-2\pi}^{2\pi}\brround{\cos\brround{\frac{x}{2}}+\sin x}dx=0\\
    &a_n=\frac{1}{L}\int_{-L}^L f(x)\cos\brround{\frac{n\pi x}{L}}dx=\frac{1}{2\pi}\int_{-2\pi}^{2\pi}\brround{\cos\brround{\frac{x}{2}}+\sin x}\cos\brround{\frac{nx}{2}}dx\\
    &a_n=\frac{1}{2\pi}\underbrace{\int_{-2\pi}^{2\pi}\sin x\cos\brround{\frac{nx}{2}}dx}_{=0}+\frac{1}{2\pi}\underbrace{\int_{-2\pi}^{2\pi}\cos\brround{\frac{x}{2}}\cos\brround{\frac{nx}{2}}dx}_{=2\pi\text{ if }n=1}\\
    &a_n=\eqnsystem{1 & n=1\\ 0 & n\neq 1}
\end{aligned}

$$

This follows the definition of the Kronecker delta function,

$$
\delta_{m,n}=\eqnsystem{1 & m=n\\ 0 & m\neq n}

$$

(not to be confused with the Dirac delta function which takes on an impulse of infinity, not 1)
This allows us to rewrite $a_n$ in a more compact manner.

$$
\begin{aligned}
    &a_n=\delta_{n,1}\\
    &b_n=\frac{1}{L}\int_{-L}^L f(x)\sin\brround{\frac{n\pi x}{L}}dx=\frac{1}{2\pi}\int_{-2\pi}^{2\pi}\brround{\cos\brround{\frac{x}{2}}+\sin x}\sin\brround{\frac{nx}{2}}dx\\
    &b_n=\frac{1}{2\pi}\underbrace{\int_{-2\pi}^{2\pi}\cos\brround{\frac{x}{2}}\sin\brround{\frac{nx}{2}}dx}_{=0}+\frac{1}{2\pi}\underbrace{\int_{-2\pi}^{2\pi}\sin x\sin\brround{\frac{nx}{2}}dx}_{=1\text{ if }n=2}\\
    &b_n=\eqnsystem{1 & n=2\\ 0 & n\neq 2}=\delta_{n,2}\\
    &u(x,t)=\sum_{n=1}^\infty\delta_{1,n}\cos\brround{\frac{nx}{2}}e^{-\brround{\frac{n}{2}}^2t}+\sum_{n=1}^\infty\delta_{2,n}\sin\brround{\frac{nx}{2}}e^{-\brround{\frac{n}{2}}^2t}
\end{aligned}

$$

From here, we can simplify using the delta functions, making the solution look a lot nicer

$$
\begin{aligned}
    &u(x,t)=\cos\brround{\frac{x}{2}}e^{-\frac{t}{4}}+\sin (x)e^{-t}
\end{aligned}

$$

You may notice that we didn't actually need to solve the integrals but could rather find the delta functions from the initial conditions by inspection. This is a nice benefit of having the initial condition consist of trig functions.

## Inhomogeneous Heat Equation

The inhomogeneous heat equation is of the general form

$$
\frac{\partial u}{\partial t}=\alpha^2\frac{\partial^2 u}{\partial x^2}+S(x,t)

$$

with $u(0,t)=A(t)$ and/or $u(L,t)=B(t)$
For the inhomogeneous heat equation, we cannot use separation of variables. There are a few different techniques we can use to solve them. With the exception of eigenfunction expansion, they all involve decomposing the solution into two functions: One ``guess" function to remove the inhomogeneous boundary conditions and one resulting function which can be solved using the homogeneous case. This best seen through some examples:

Ex: Regular inhomogeneous time-independent boundary conditions

$$
\begin{aligned}
    &u_t=\alpha^2u_{xx}\\
    &u(0,t)=u_0\neq0\\
    &u(L,t)=u_1\neq0\\
    &u(L,t)=B(t)
\end{aligned}

$$

Because the boundary conditions do not depend on time, we can assume that there will be a steady-state response in the solution so we can decompose the solution into a a time-dependent and a time-independent part:

$$
\begin{aligned}
    &u(x,t)=w(x)+v(x,t)
\end{aligned}

$$

$w(x)$ is called the steady-state solution and $v(x,t)$ is called the transient solution.
Because a superposition of solutions is also a solution, we can solve each part separately.

$$
\begin{aligned}
    &w_t=\alpha^2 w_{xx}\\
    &w_t=0\Ra w_{xx}=0\\
    &\Ra w(x)=Ax+B\\
    &w(0)=u_0\Ra B=u_0\\
    &w(L)=u_1\Ra u_1=AL+B\Ra A=\frac{u_1-u_0}{L}\\
    &w(x)=\frac{u_1-u_0}{L}x+u_0
\end{aligned}

$$

Now that we've solved for $w(x)$, we can use it to find a homogeneous PDE we can use to solve for $v(x,t)$.

$$
\begin{aligned}
    &u_t=\alpha^2u_{xx}\\
    &w_t+v_t=\alpha^2w_{xx}+\alpha^2v_{xx}\\
    &v_t=\alpha^2v_{xx}\\
    &u(0,t)=u_0\Ra w(0)+v(0,t)=u_0\Ra v(0,t)=0\\
    &u(L,0)=u_1\Ra w(L)+v(L,t)=u_1\Ra v(L,0)=0\\
    &u(x,0)=f(x)\Ra w(x)+v(x,0)=f(x)\Ra v(x,0)=f(x)-w(x)=f(x)-\brround{\frac{u_1-u_0}{L}x+u_0}=g(x)
\end{aligned}

$$

This now gives a homogeneous PDE for $v(x.t)$

$$
\begin{aligned}
    &v_t=\alpha^2v_{xx}\\
    &v(0,t)=v(L,t)=0\\
    &v(x,0)=f(x)-w(x)=g(x)
\end{aligned}

$$

Solving for $v(x,t)$ gives

$$
\begin{aligned}
    &v(x,t)=\sum_{n=1}^\infty b_n\sin\brround{\frac{n\pi x}{L}}e^{-\alpha^2\brround{\frac{n\pi}{L}}^2t},\\
    &b_n=\frac{2}{L}\int_0^L g(x)\sin\brround{\frac{n\pi x}{L}}dx
\end{aligned}

$$

Putting it all together we have the final solution of

$$
\begin{aligned}
    &u(x,t)=w(x)+v(x,t)=\frac{u_1-u_0}{L}x+u_0+\sum_{n=1}^\infty b_n\sin\brround{\frac{n\pi x}{L}}e^{-\alpha^2\brround{\frac{n\pi}{L}}^2t}
\end{aligned}

$$

Ex2: Regular inhomogeneous time-independent Neumann boundary conditions

$$
\begin{aligned}
    &u_t=\alpha^2 u_{xx}\\
    &u_x(0,t)=q_0\\
    &u_x(L,t)=q_1\\
    &u(x,0)=f(x)
\end{aligned}

$$

When we have Neumann boundary conditions, we are not able to do the exact same thing we did in the previous example. If we have the same guess $w(x)=Ax+B$ we see

$$
\begin{aligned}
    &w_x(0)=q_0\Ra A=q_0\\
    &w_x(L)=q_1\Ra A=q_1
\end{aligned}

$$

So unless $q_0=q_1$, there is no steady state solution. We've seen in ODE's that multiplying our guess by $x$ seems to work for constant coefficient equations and fortunately that works in this case as well with the addition of a time dependent term

$$
\begin{aligned}
    &w(x,t)=Ax^2+Bx+Ct\\
    &w_x(0,t)=q_0=B\\
    &w_x(L,t)=q_1=2AL+B\Ra A=\frac{q_1-q_0}{2L}\\
    &w_t=\alpha^2w_{xx}\\
    &C=\alpha^2(2A)\Ra C=\alpha^2\frac{q_1-q_0}{L}\\
    &w(x,t)=\frac{q_1-q_0}{2L}x^2+q_0x+\alpha^2\frac{q_1-q_0}{L}t
\end{aligned}

$$

From here, we follow the same steps to get an inhomogeneous PDE for $v(x,t)$

$$
\begin{aligned}
    &w_t+v_t=\alpha^2(w_{xx}+v_{xx})\Ra v_t=\alpha^2 v_{xx}\\
    &w_x(0,t)+v_x(0,t)=q_0\Ra v_x(0,t)=0\\
    &w_x(L,t)+v_x(L,t)=q_1\Ra v_x(L,t)=0\\
    &w(x,0)+v(x,0)=f(x)\Ra v(x,0)=f(x)-w(x,0)=g(x)
\end{aligned}

$$

Solving for $v(x,t)$ and putting it all together, we get

$$
\begin{aligned}
    &u(x,t)=w(x,t)+v(x,t)=\frac{q_1-q_0}{2L}x^2+q_0x+\alpha^2\frac{q_1-q_0}{L}t+a_0+\sum_{n=1}^\infty a_n\cos\brround{\frac{n\pi x}{L}}e^{-\alpha^2\brround{\frac{n\pi }{L}}^2t},\\
    &a_0=\frac{1}{L}\int_0^L g(x)dx,\ a_n=\frac{2}{L}\int_0^L g(x)\cos\brround{\frac{n\pi x}{L}}dx
\end{aligned}

$$

Ex3: Forcing Function/Irregular Equation

$$
\begin{aligned}
    &u_t=u_{xx}-u+x,\ 0<x<1,\ t>0\\
    &u_x(0,t)=1,\ u_x(1,t)=2\\
    &u(x,0)=x
\end{aligned}

$$

This case is similar to the first example but a bit more general, extending to different forms of the heat equation as well as those with a forcing function, $S(x)$.
We start by splitting up $u(x,t)$ and then solve for $w(x)$. This is often done by solving an ODE.

$$
\begin{aligned}
    &u(x,t)=w(x)+v(x,t)\\
    &w_t=w_{xx}-w+x=0\Ra w_{xx}-w=-x\\
    &r^2-1=0\Ra r=\pm1\\
    &w_c(x)=A\cosh(x)+B\sinh(x)\\
    &w_p=Ax+B,\ w_p'=A,\ w_p''=0\\
    &-(Ax+B)=-x\Ra A=1,\ B=0\\
    &w_p(x)=x\\
    &w(x)=A\cosh(x)+B\sinh(x)+x
\end{aligned}

$$

Now that we've found $w(x)$, we can find the equation for $v(x,t)$ and solve the rest of the PDE.

$$
\begin{aligned}
    &w_x=A\sinh(x)+B\cosh(x)+1\\
    &w_x(0)=1=B+1\Ra B=0\\
    &w_x(1)=2=A\sinh(1)+1\Ra A=\frac{1}{\sinh(1)}\\
    &w(x)=\frac{\cosh(x)}{\sinh(1)}+x\\
    &u_t=u_{xx}-u+x\\
    &v_t+w_t=v_{xx}+w_{xx}-v-w+x\Ra v_t=v_{xx}-v\\
    &u_x(0,t)=1\Ra v_x(0,t)+w_x(0)=1\Ra v_x(0,t)=0\\
    &u_x(1,t)=2\Ra v_x(1,t)+w_x(1)=2\Ra v_x(1,t)=0\\
    &u(x,0)=v(x,0)+w(x)=x\Ra v(x,0)=-\frac{\cosh(x)}{\sinh(1)}\equiv g(x)\\
    &v(x,t)=X(x)T(t)\\
    &XT'=X''T-XT\Ra \frac{T'}{T}+1=\frac{X''}{X}=-\lambda
\end{aligned}

$$

$v(x,t)$ has Neumann boundary conditions so it will have the following eigenvalues and eigenfunctions

$$
\begin{aligned}
    &\lambda_n=0,\ (n\pi)^2\\
    &X_n=1,\ \cos(n\pi x)\\
    &T'=-T(\lambda+1)\\
    &T_n=e^{-((n\pi)^2+1)t}\\
    &v(x,t)=a_0e^{-t}+\sum_{n=1}^\infty a_n\cos(n\pi x)e^{-((n\pi)^2+1)t}\\
    &a_0=\frac{1}{2}\int_{-1}^1g(x)dx=-\int_0^1\frac{\cosh(x)}{\sinh(1)}dx=-{\frac{\sinh(x)}{\sinh(1)}}\eval_0^1=-1\\
    &a_n=\frac{1}{1}\int_{-1}^1g(x)\cos(n\pi x)dx=-2\int_0^1\frac{\cosh(x)}{\sinh(1)}\cos(n\pi x)dx\\
    &\leadsto a_n=-\frac{2}{\sinh(1)}\brsquare{\frac{n\pi\cosh(x)\sin(n\pi x)+\sinh(x)\cos(n\pi x)}{(n\pi)^2+1}}_0^1=-\frac{2}{\sinh(1)}\brround{\frac{\sinh(1)(-1)^n}{(n\pi)^2+1}}\\
    &a_n=\frac{2(-1)^{n+1}}{(n\pi)^2+1}\\
    &v(x,t)=-e^{-t}+\sum_{n=1}^\infty\frac{2(-1)^{n+1}}{(n\pi)^2+1}\cos(n\pi x)e^{-((n\pi)^2+1)t}\\
    &u(x,t)=w(x)+v(x,t)\\
    &u(x,t)=\frac{\cosh(x)}{\sinh(1)}-e^{-t}+x+\sum_{n=1}^\infty\frac{2(-1)^{n+1}}{(n\pi)^2+1}\cos(n\pi x)e^{-((n\pi)^2+1)t}
\end{aligned}

$$

Ex4: Time dependent boundary conditions

$$
\begin{aligned}
    &u_t=u_{xx}-u+2x\\
    &u(0,t)=e^{-t}\\
    &u(1,t)=1\\
    &u(x,0)=\sin(6x)-\frac{\sinh(x)}{\sinh(1)}+x+1
\end{aligned}

$$

When we have time dependent boundary conditions we will always want to remove them with a guess solution before proceeding to the rest of the problem

$$
\begin{aligned}
    &u(x,t)=w(x,t)+v(x,t)
\end{aligned}

$$

We will always make the guess

$$
\begin{aligned}
    &w(x,t)=A(t)x+B(t)\\
    &u(0,t)=B(t)=e^{-t}\\
    &u(1,t)=A(t)+e^{-t}=1\Ra A(t)=1-e^{-t}\\
    &w(x,t)=(1-e^{-t})x+e^{-t}\
\end{aligned}

$$

Now that we solved for $w(x,t)$ we should be able to get a PDE for $v(x,t)$ with time-independent boundary conditions.

$$
\begin{aligned}
    &w_t+v_t=w_{xx}+v_{xx}-w-v+2x\\
    &e^{-t}x-e^{-t}+v_t=v_{xx}-x+e^{-t}-e^{-t}-v+2x\\
    &v_t=v_{xx}-v+x\\
    &u(x,0)=w(x,0)+v(x,0)=\sin(6x)-\frac{\sinh(x)}{\sinh(1)}+x+1\\
    &1+v(x,0)=\sin(6x)-\frac{\sinh(x)}{\sinh(1)}+x+1\Ra v(x,0)=\sin(6x)-\frac{\sinh(x)}{\sinh(1)}+x\\
    &v(0,t)=v(1,t)=0
\end{aligned}

$$

Now we have a PDE for $v(x,t)$, which we are able to solve. The rest of the steps follow from previous examples. Because $v(x,t)$ has a forcing function, we'll split it up as follows

$$
\begin{aligned}
    &v(x,t)=p(x)+q(x,t)\\
    &p_t=p_{xx}-p+x\Ra 0=p''-p+x\\
    &\leadsto p_c=A\cosh(x)+B\cosh(x)\\
    &p_p=x\Ra p(x)=A\cosh(x)+B\sinh(x)+x\\
    &p(0)=A=0\\
    &p(1)=B\sinh(1)+1=0\Ra B=-\frac{1}{\sinh(1)}\\
    &p(x)=-\frac{\sinh(x)}{\sinh(1)}+x
\end{aligned}

$$

Now we can find a PDE for $q(x,t)$

$$
\begin{aligned}
    &p_t+q_t=p_{xx}+q_{xx}-p-q+x\\
    &q_t=-\frac{\sinh(x)}{\sinh(1)}+q_{xx}+\frac{\sinh(x)}{\sinh(1)}-x-q+x\\
    &q_t=q_{xx}-q\\
    &v(0,t)=p(0)+q(0,t)=0\Ra q(0,t)=0\\
    &v(1,t)=p(1)+q(1,t)=0\Ra q(1,t)=0\\
    &v(x,0)=p(x)+q(x,0)=-\frac{\sinh(x)}{\sinh(1)}+x+q(x,0)=\sin(6x)
\end{aligned}

$$

Now we can solve for $q(x,t)$

$$
\begin{aligned}
    &q(x,t)=X(x)T(t)\\
    &XT'=X''T-XT\Ra \frac{T'}{T}=\frac{X''}{X}-1\\
    &\frac{T'}{T}+1=\frac{X''}{X}=-\lambda\\
    &\leadsto \lambda=(n\pi)^2\\
    &X_n=\sin(n\pi x)\\
    &T_n=e^{-((n\pi)^2+1)t}\\
    &q(x,t)=\sum_{n=1}^\infty b_n\sin(n\pi x)e^{-((n\pi)^2+1)t}\\
    &q(x,0)=\sin(6x)\Ra b_n=\delta_{6,n}\\
    &q(x,t)=\sin(6\pi x)e^{-(36\pi^2+1)t}
\end{aligned}

$$

Putting it all together we have

$$
\begin{aligned}
    &v(x,t)=p(x)+q(x,t)=-\frac{\sinh(x)}{\sinh(1)}+x+\sin(6\pi x)e^{-(36\pi^2+1)t}\\
    &u(x,t)=w(x,t)+v(x,t)=(1-e^{-t})x+e^{-t}-\frac{\sinh(x)}{\sinh(1)}+x+\sin(6\pi x)e^{-(36\pi^2+1)t}\\
    &=2x+(1-x)e^{-t}-\frac{\sinh(x)}{\sinh(1)}+\sin(6\pi x)e^{-(36\pi^2+1)t}
\end{aligned}

$$

Ex5: Eigenfunction expansion

$$
\begin{aligned}
    &u_t=u_{xx}+e^{-t}\cos\brround{\frac{3\pi}{2}x}+1,\ 0<x<1,\ t>0\\
    &u_x(0,t)=1,\ u(1,t)=t\\
    &u(x,0)=1
\end{aligned}

$$

When we have a time dependent source/sink term in the PDE, we will have to use the method of eigenfunction expansion. Eigenfunction expansion is a general approach to solving any of these more complicated PDEs.
We'll first start by removing the time-dependent boundary conditions and getting a homogeneous equation.

$$
\begin{aligned}
    &w(x,t)=A(t)x+B(t)\\
    &w_x(x,t)=A(t)\\
    &w_x(0,t)=1=A(t)\\
    &w(1,t)=t=1+B(t)\Ra B(t)=t-1\\
    &w(x,t)=x+t-1\\
    &w_t+v_t=w_{xx}+v_{xx}+e^{-t}\cos\brround{\frac{3\pi}{2}x}+1\\
    &1+v_t=v_{xx}+e^{-t}\cos\brround{\frac{3\pi}{2}x}+1\\
    &v_t=v_{xx}+e^{-t}\cos\brround{\frac{3\pi}{2}x}\\
    &u_x(0,t)=w_x(0,t)+v_x(0,t)=1\Ra v_x(0,t)=0\\
    &u(1,t)=w(1,t)+v(1,t)=t\Ra v(1,t)=0\\
    &u(x,0)=w(x,0)+v(x,0)=x-1+v(x,0)=1\Ra v(x,0)=2-x
\end{aligned}

$$

Now that we have a homogeneous equation for $v(x,t)$, we are able to apply the method of eigenfunction expansion.
The first step is to solve the for the eigenvalues of the PDE without the source term.

$$
\begin{aligned}
    &v_t=v_{xx}\\
    &v_x(0,t)=v(1,t)=0\\
    &v(x,0)=2-x
\end{aligned}

$$

Mixed type 2 so the eigenvalues and eigenfunctions are:

$$
\begin{aligned}
    &\lambda_n=\brround{\frac{2n-1}{2}\pi}^2\\
    &X_n=\cos\brround{\frac{2n-1}{2}\pi x}\\
    &v(x,t)=\sum_{n=1}^\infty V_n(t)\cos\brround{\frac{2n-1}{2}\pi x}
\end{aligned}

$$

Note that we did not put in the time-dependent eigenfunction into $v(x,t)$ but rather express it as some unknown function $V_n(t)$. We will get to solving this in a bit.
The next step is to expand the source term so that we are able to express it as a sum.

$$
\begin{aligned}
    &S(x,t)=e^{-t}\cos\brround{\frac{3\pi}{2}x}=\sum_{n=1}^\infty S_n(t)\cos\brround{\frac{2n-1}{2}\pi x}\\
    &S_n(t)=\delta_{2,n}e^{-t}\\
    &S(x,t)=\sum_{n=1}^\infty \delta_{2,n}e^{-t}\cos\brround{\frac{2n-1}{2}\pi x}
\end{aligned}

$$

Now that we have the source term expressed as a sum, we can write out $v_t$ and $v_{xx}$ and combine all of the summations.

$$
\begin{aligned}
    &v_t=\sum_{n=1}^\infty V_n'(t)\cos\brround{\frac{2n-1}{2}\pi x}\\
    &v_{xx}=\sum_{n=1}^\infty -V_n(t)\cos\brround{\frac{2n-1}{2}\pi x}\brround{\frac{2n-1}{2}\pi}^2\\
    &v_t-v_{xx}-S(x,t)=0\\
    &\sum_{n=1}^\infty\brround{V_n'(t)+V_n(t)\brround{\frac{2n-1}{2}\pi}^2-e^{-t}\delta_2(n)}\cos\brround{\frac{2n-1}{2}\pi x}=0
\end{aligned}

$$

This gives us an ODE for $V_n$ that we can solve.

$$
\begin{aligned}
    &V_n'(t)+V_n(t)\brround{\frac{2n-1}{2}\pi}^2-e^{-t}\delta_{2,n}=0\\
    &\mu=e^{\int \brround{\frac{2n-1}{2}\pi}^2dt}=e^{\brround{\frac{2n-1}{2}\pi}^2 t}\\
    &(V_n\mu)'=\mu e^{-t}\delta_{2,n}\\
    &V_n=\frac{1}{e^{\brround{\frac{2n-1}{2}\pi}^2 t}}\int e^{\brround{\brround{\frac{2n-1}{2}\pi}^2-1}t}\delta_{2,n}dt\\
    &V_n=\frac{1}{e^{\brround{\frac{2n-1}{2}\pi}^2 t}}\brround{\frac{1}{\brround{\frac{2n-1}{2}\pi}^2-1}e^{\brround{\brround{\frac{2n-1}{2}\pi}^2-1}t}\delta_{2,n}+C_n}\\
    &V_n=\frac{\delta_{2,n}}{\brround{\frac{2n-1}{2}\pi}^2-1}e^{-t}+C_ne^{-\brround{\frac{2n-1}{2}\pi}^2t}
\end{aligned}

$$

Now that we have solved for $V_n$, we can write a more complete form of $v(x,t)$ and then use Fourier series to solve for the last remaining constant. We will introduce a new constant, $D_n$, just to make computation slightly simpler.

$$
\begin{aligned}
    &v(x,t)=\sum_{n=1}^\infty\brround{\frac{\delta_{2,n}}{\brround{\frac{2n-1}{2}\pi}^2-1}e^{-t}+C_ne^{-\brround{\frac{2n-1}{2}\pi}^2t}}\cos\brround{\frac{2n-1}{2}\pi x}\\
    &v(x,0)=2-x=\sum_{n=1}^\infty\underbrace{\brround{\frac{\delta_{2,n}}{\brround{\frac{2n-1}{2}\pi}^2-1}+C_n}}_{D_n}\cos\brround{\frac{2n-1}{2}\pi x}
\end{aligned}

$$

Fourier series:

$$
\begin{aligned}
    &D_n=2\int_0^1(2-x)\cos\brround{\frac{2n-1}{2}\pi x}dx\\
    &D_n=\dfrac{4\left(\left(2{\pi}n-{\pi}\right)\sin\left(\frac{2{\pi}n-{\pi}}{2}\right)-2\cos\left(\frac{2{\pi}n-{\pi}}{2}\right)+2\right)}{{\pi}^2\cdot\left(4n^2-4n+1\right)}\\
    &D_n=\frac{4((2n-1)\pi(-1)^{n+1}+2)}{(2n-1)^2\pi^2}=\frac{(2n-1)(-1)^{n+1}\pi+2}{\brround{\frac{2n-1}{2}\pi}^2}\\
    &\Ra C_n=\frac{(2n-1)(-1)^{n+1}\pi+2}{\brround{\frac{2n-1}{2}\pi}^2}-\frac{\delta_2(n)}{\brround{\frac{2n-1}{2}\pi}^2-1}
\end{aligned}

$$

\begin{scriptsize}

$$
\begin{aligned}
    &v(x,t)=\sum_{n=1}^\infty\brround{\frac{\delta_2(n)}{\brround{\frac{2n-1}{2}\pi}^2-1}e^{-t}+\brround{\frac{(2n-1)(-1)^{n+1}\pi+2}{\brround{\frac{2n-1}{2}\pi}^2}-\frac{\delta_2(n)}{\brround{\frac{2n-1}{2}\pi}^2-1}}e^{-\brround{\frac{2n-1}{2}\pi}^2t}}\cos\brround{\frac{2n-1}{2}\pi x}\\
    &u(x,t)=x+t-1+\sum_{n=1}^\infty\brround{\frac{\delta_2(n)}{\brround{\frac{2n-1}{2}\pi}^2-1}e^{-t}+\brround{\frac{(2n-1)(-1)^{n+1}\pi+2}{\brround{\frac{2n-1}{2}\pi}^2}-\frac{\delta_2(n)}{\brround{\frac{2n-1}{2}\pi}^2-1}}e^{-\brround{\frac{2n-1}{2}\pi}^2t}}\cos\brround{\frac{2n-1}{2}\pi x}
\end{aligned}

$$

\end{scriptsize}

These examples covered a lot of information so here is an algorithmic summary of what the steps are for each method:


- Regular Inhomogeneous Boundary Conditions
    Form: $u_t=\alpha^2u_{xx}$ with $u(0,t)=u_0$ and $u(L,t)=u_1$ (or mixed BCs)
    Guess $w(x)=Ax+B$

- Use the BCs to solve for $A$ and $B$
- Plug $u=w+v$ into the PDE to find the homogeneous problem for $v(x,t)$ and solve for $v$

- Regular Inhomogeneous Boundary Conditions (Neumann)
    Form: $u_t=\alpha^2u_{xx}$ with $u_x(0,t)=q_0$ and $u_x(L,t)=q_1$
    Guess $w(x,t)=Ax^2+Bx+Ct$

- Use the BCs and plug into the PDE to get $C=2\alpha^2A$ and solve for $A,B,C$
- Plug $u=w+v$ into the PDE to find the homogeneous problem for $v(x,t)$ and solve for $v$

- Forcing Function/Irregular Equation
    Form: $u_t=\alpha^2u_{xx}-\gamma u+g(x)$ with constant boundary conditions
    Guess will be the $w(x)$ that solves the resulting ODE: $\alpha^2w_{xx}-\gamma w+g(x)=0$

- Use the BCs to solve for the unknown coefficients coming from the complementary solution of $w(x)$
- Plug $u=w+v$ into the PDE to find the homogeneous problem for $v(x,t)$ and solve for $v$

- Time Dependent Boundary Conditions:
    Form: when the 2 boundary conditions are functions of time, such as $u(0,t)=p(t)$ and $u(L,t)=q(t)$
    Guess $w(x,t)=A(t)x+B(t)$

- Use the BCs to find the functions $A(t)$ and $B(t)$
- Plug $u=w+v$ into the PDE to find a new PDE for $v(x,t)$ with time independent BCs. Note that $v(x,t)$ may still be inhomogeneous, requiring you to then solve for $v$ using one of the other methods

- Eigenfunction Expansion/Time Dependent Source/Sink (General solution of the heat equation)
    Form: $u_t=\alpha^2u_{xx}+S(x,t)$
    This is the most general solution and will always work


- First use one of the other methods to remove any inhomogeneous boundary conditions. This will provide a new PDE of the form $v_t=\alpha^2v_{xx}+S_2(x,t)$ with homogeneous boundary conditions.
- Find the general eigenfunctions of $X_n$ for the homogeneous heat equation, $v_t = \alpha^2 v_{xx}$  omitting the source term: $v_t=\alpha^2v_{xx}$
- Expand the source term in terms of $X_n$ and write the source term as:

$$
S_2(x,t)=\sum_{n=1}^\infty S_n(t)X_n(x)

$$

        Use the Fourier analysis $S_n(t) = \frac{2}{L}\int_0^{L} s(x,t)X_n(x)$ or intuition to solve for $S_n(t)$ given that you know $S_2(x,t)$
- Express the solution for $v$ as

$$
v(x,t)=\sum_{n=1}^\infty V_n(t)X_n(x)

$$

        where $V_n$ is an undetermined function.  Express $v_t$ and $v_{xx}$ as an infinite series as well.
- Substitute all values that are now in terms of $X_n$ back into the original PDE.

$$
\sum_{n=1}^\infty V_n'X_n = \sum_{n=1}^\infty V_n X_n'' + \sum_{n=1}^\infty S_nX_n

$$

        rearrange to get an expression of the form

$$
\sum_{n=1}^\infty [V_n'+\lambda_n V_n - S_n]X_n=0

$$

- Solve the ODE for $V_n$ inside the series: $V_n'(t)+\lambda_n V_n(t) - S_n(t)=0$ (Integrating factor technique will likely work well)
- The ODE will yield a general solution with an undetermined coefficient for the homogeneous portion of the ODE: $V_n(t) = f(n,t) + C_n g(n,t)$
- Use Fourier series and the initial condition $v(x,0)=h(x)$ to solve for the unknown constant that comes from the solution of $V_n$:

$$
v(x,t) = \sum_{n=1}^\infty[f(n,t) + C_n g(n,t)]X_n

$$

$$
v(x,0) = h(x) = \sum_{n=1}^\infty\underbrace{[f(n,0) + C_n g(n,0)]}_{D_n}X_n

$$

        Then $D_n = \frac{2}{L}\int_0^{L} h(x)X_n(x)dx$, solve for $C_n$ from $D_n$, then write out full solution.
