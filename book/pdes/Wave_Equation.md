# Wave Equation

<!-- Source: [Sections/PDEs/Wave_Equation.tex](../../Sections/PDEs/Wave_Equation.tex) -->

## Separation of Variables

The general form of the wave equation is

$$
\frac{\partial^2 u}{\partial t^2}=c^2\frac{\partial^2u}{\partial x^2}

$$

In order to find a solution, we will again require two boundary conditions as well as two initial conditions: $u(x,0)$ and $u_t(x,0)$ normally.
We can use many of the same techniques to solve the wave equation as we did to solve the heat equation.
Ex:

$$
\begin{aligned}
    &u_{tt}=u_{xx},\ 0\leq x\leq \pi,\ t\geq 0\\
    &u_x(0,t)=u_x(\pi,t)=0\\
    &u(x,0)=f(x)=5\cos x\\
    &u_t(x,0)=g(x)=1-2\cos(2x)
\end{aligned}

$$

We will start by using separation of variables and finding the eigenvalues and eigenfunctions, the same as was done with the heat equation.

$$
\begin{aligned}
    &u(x,t)=X(x)T(t)\\
    &XT''=X''T\Ra \frac{T''}{T}=\frac{X''}{X}=-\lambda\\
    &X''+\lambda X=0,\ X'(0)=X'(\pi)=0\\
    &\leadsto \lambda_0=0,\ \lambda_n=\brround{\frac{n\pi}{L}}^2=n^2\\
    &X_0=1,\ X_n=\cos(nx)\\
    &T_n''+\lambda_n T_n=0\\
    &\lambda_0=0:\ T_0''=0\Ra T_0=A_0+B_0t\\
    &\lambda_n=n^2:\ T_n''+n^2T_n=0\Ra T_n=A_n\cos(nt)+B_n\sin(nt)\\
    &u(x,t)=A_0+B_0t+\sum_{n=1}^\infty\cos(nx)\brround{A_n\cos(nt)+B_n\sin(nt)}\\
    &u_t(x,t)=B_0+\sum_{n=1}^\infty\cos(nx)(n)\brround{-A_n\sin(nt)+B_n\cos(nt)}
\end{aligned}

$$

Now we can use our two initial conditions to solve for $A_0,A_n,B_0,B_n$

$$
\begin{aligned}
    &u(x,0)=5\cos x=A_0+\sum_{n=1}^\infty A_n\cos(nx)\\
    &\Ra A_0=0,\ A_n=5\delta_{1,n}\\
    &u_t(x,0)=1-2\cos(2x)=B_0+\sum_{n=1}^\infty(B_n n)\cos(nx)\\
    &\Ra B_0=1,\ B_n=-\delta_{n,2}\\
    &u(x,t)=t+\sum_{n=1}^\infty\brround{5\delta_{1,n}\cos(nt)-\delta_{2,n}\sin(nt)}\cos(nx)\\
    &u(x,t)=t+5\cos t\cos x-\sin(2t)\cos(2x)
\end{aligned}

$$

The separation of variables method will work for any of the following forms:

$$
\begin{aligned}
    &u_{tt}=c^2u_{xx}\\
    &u_{tt}=c^2u_{xx}-\gamma u\\
    &u_{tt}=c^2u_{xx}-\gamma(t)u\\
    &u_{tt}=c^2u_{xx}-\gamma u_t+\eta(t) u
\end{aligned}

$$

Ex2:

$$
\begin{aligned}
    &u_{tt}=u_{xx}-\gamma u,\ 0<x<1,\ t>0\\
    &u(0,t)=u(1,t)=0\\
    &u(x,0)=0,\ u_t(x,0)=g(x)\\
    &u(x,t)=X(x)T(t)\\
    &\frac{T''}{T}=\frac{X''}{X}-\gamma\Ra \frac{T''}{T}+\gamma=\frac{X''}{X}=-\lambda
\end{aligned}

$$

Dirichlet boundary conditions

$$
\begin{aligned}
    &\lambda_n=(n\pi)^2\\
    &X_n=\sin(n\pi x)\\
    &T_n''+T_n(\gamma+\lambda)=T_n''+T_n(\gamma+(n\pi)^2)=0\\
    &\text{assuming }\gamma\geq0,\ \mu_n=\sqrt{\gamma+(n\pi)^2}\\
    &T_n=A_n\cos(\mu_nt)+B_n\sin(\mu_nt)\\
    &u(x,t)=\sum_{n=1}^\infty\sin(n\pi x)\brround{A_n\cos(\mu_nt)+B_n\sin(\mu_nt)}\\
    &u_t(x,t)=\sum_{n=1}^\infty\sin(n\pi x)\brround{-A_n\mu_n\sin(\mu_nt)+B_n\mu_n\cos(\mu_nt)}\\
    &u(x,0)=\sum_{n=1}^\infty A_n\sin(n\pi x)=0\Ra A_n=0\\
    &u_t(x,0)=\sum_{n=1}^\infty B_n\mu_n\sin(n\pi x)=g(x)\\
    &B_n\mu_n=2\int_0^1g(x)\sin(n\pi x)dx\Ra B_n=\frac{2}{\mu_n}\int_0^1g(x)\sin(n\pi x)dx\\
    &u(x,t)=\sum_{n=1}^\infty B_n\sin(n\pi x)\sin(t\sqrt{\gamma+(n\pi)^2})=\sum_{n=1}^\infty\frac{2\sin(n\pi x)\sin(t\sqrt{\gamma+(n\pi)^2})}{\sqrt{\gamma+(n\pi)^2}}\int_0^1g(x)\sin(n\pi x)dx
\end{aligned}

$$

We can also use the same methods of dealing with inhomogeneous equations for the wave equation as we did with the heat equation.
Ex3:

$$
\begin{aligned}
    &u_{tt}=u_{xx},\ t>0,\ 0\leq x\leq 1\\
    &u(0,t)=0,\ u(1,t)=1\\
    &u(x,0)=\sin(\pi x)+x,\ u_t(x,0)=\sin(3\pi x)
\end{aligned}

$$

Steady state solution:

$$
\begin{aligned}
    &u(x,t)=w(x)+v(x,t)\\
    &w_{tt}=0=w_{xx}\Ra w(x)=Ax+B\\
    &w(0)=0\Ra B=0\\
    &w(1)=1=A\\
    &w(x)=x\\
    &w_{tt}+v_{tt}=w_{xx}+v_{xx}\Ra v_{tt}=v_{xx}\\
    &w(0)+v(0)=0\Ra v(0)=0\\
    &w(1)+v(1)=1\Ra v(1)=0\\
    &w(x)+v(x,0)=x+v(x,0)=\sin(\pi x)+x\Ra v(x,0)=\sin(\pi x)\\
    &w_t(x)+v_t(x,0)=\sin(3\pi x)\Ra v_t(x,0)=\sin(3\pi x)
\end{aligned}

$$

Separation of variables:
Dirichlet BCs

$$
\begin{aligned}
    &\lambda_n=(n\pi)^2\\
    &X_n=\sin(n\pi x)\\
    &T_n''+\lambda_nT_n=T_n''+(n\pi)^2T_n'=0\\
    &\Ra T_n=A_n\cos(n\pi t)+B_n\sin(n\pi t)\\
    &v(x,t)=\sum_{n=1}^\infty\sin(n\pi x)\brround{A_n\cos(n\pi t)+B_n\sin(n\pi t)}\\
    &v_t(x,t)=\sum_{n=1}^\infty\sin(n\pi x)\brround{-A_nn\pi\sin(n\pi t)+B_nn\pi\cos(n\pi t)}\\
    &v(x,0)=\sum_{n=1}^\infty A_n\sin(n\pi x)=\sin(\pi x)\\
    &A_n=\delta_{1,n}\\
    &v_t(x,0)=\sum_{n=1}B_nn\pi\sin(n\pi x)=\sin(3\pi x)\\
    &B_nn\pi=\delta_{3,n}\Ra B_n=\frac{\delta_{3,n}}{n\pi}\\
    &v(x,t)=\sin(\pi x)\cos(\pi t)+\frac{1}{3\pi}\sin(3\pi x)\sin(3\pi t)\\
    &u(x,t)=x+\sin(\pi x)\cos(\pi t)+\frac{1}{3\pi}\sin(3\pi x)\sin(3\pi t)
\end{aligned}

$$

Ex4:

$$
\begin{aligned}
    &u_{tt}=c^2u_{xx}+e^{-t}\cos(3x),\ 0<x<\frac{\pi}{2},\ t>0\\
    &u_x(0,t)=0,\ u\brround{\frac{\pi}{2},t}=t\\
    &u(x,0)=\cos x,\ u_t(x,0)=1+\cos(5x)
\end{aligned}

$$

Steady state solution:

$$
\begin{aligned}
    &u(x,t)=w(x,t)+v(x,t)\\
    &w(x,t)=A(t)x+B(t)\\
    &w_x(x,t)=A(t)\Ra w_x(0,t)=A(t)=0\\
    &w\brround{\frac{\pi}{2},t}=B(t)=t\\
    &w(x,t)=t\\
    &w_{tt}+v_{tt}=c^2w_{xx}+c^2v_{xx}+e^{-t}\cos(3x)\Ra v_{tt}=c^2v_{xx}+e^{-t}\cos(3x)\\
    &w_x(0,t)+v_x(0,t)=0\Ra v_x(0,t)=0\\
    &w\brround{\frac{\pi}{2},t}+v\brround{\frac{\pi}{2},t}=t\Ra v\brround{\frac{\pi}{2},t}=0\\
    &w(x,0)+v(x,0)=v(x,0)=\cos x\\
    &w_t(x,0)+v_t(x,0)=1+v_t(x,0)=1+\cos(5x)\Ra v_t(x,0)=\cos(5x)
\end{aligned}

$$

Eigenfunction expansion:
Mixed BCs:

$$
\begin{aligned}
    &\lambda_n=\brround{\frac{(2n-1)\pi}{2L}}^2=(2n-1)^2\\
    &X_n=\cos(\mu_nx),\ \mu_n=2n-1,\ n\geq1\\
    &v(x,t)=\sum_{n=1}^\infty V_n(t)\cos(\mu_nx)\\
    &S(x,t)=e^{-t}\cos(3x)=\sum_{n=1}^\infty S_n(t)\cos(\mu_n x)\\
    &\mu_n=2n-1=3\Ra n=2\\
    &S_n=e^{-t}\delta_{2,n}\\
    &v_{tt}=\sum_{n=1}^\infty V_n''(t)\cos(\mu_nx)\\
    &v_{xx}=\sum_{n=1}^\infty-V_n(t)\mu_n^2\cos(\mu_nx)\\
    &v_{tt}-c^2v_{xx}-S(x,t)=0\\
    &\sum_{n=1}^\infty\brround{V_n''+c^2\mu_n^2V_n-e^{-t}\delta_{2,n}}\cos(\mu_nx)=0
\end{aligned}

$$

2nd Order ODE:

$$
\begin{aligned}
    &V_n''+c^2\mu_n^2V_n=\delta_{2,n}e^{-t}\\
    &(V_n)_c=A_n\cos(c\mu_nt)+B_n\sin(c\mu_nt)\\
    &(V_n)_p=C_ne^{-t}= (V_n)_p''\\
    &C_ne^{-t}(1+c^2\mu_n^2)=\delta_{2,n}e^{-t}\\
    &C_n=\frac{\delta_{2,n}}{1+c^2\mu_n^2}\\
    &V_n(t)=A_n\cos(c\mu_nt)+B_n\sin(c\mu_nt)+\frac{\delta_{2,n}e^{-t}}{1+c^2\mu_n^2}
\end{aligned}

$$

Impose initial conditions:

$$
\begin{aligned}
    &v(x,t)=\sum_{n=1}^\infty\brround{A_n\cos(c\mu_nt)+B_n\sin(c\mu_nt)+\frac{\delta_{2,n}e^{-t}}{1+c^2\mu_n^2}}\cos(\mu_nx)\\
    &v_t(x,t)=\sum_{n=1}^\infty\brround{-A_nc\mu_n\sin(c\mu_nt)+B_nc\mu_n\cos(c\mu_nt)-\frac{\delta_{2,n}e^{-t}}{1+c^2\mu_n^2}}\cos(\mu_nx)\\
    &v(x,0)=\cos x=\sum_{n=1}^\infty\brround{A_n+\frac{\delta_{2,n}}{1+c^2\mu_n^2}}\cos(\mu_nx)\\
    &\mu_n=1=2n-1\Ra n=1\\
    &A_n+\frac{\delta_{2,n}}{1+c^2\mu_n^2}=\delta_{1,n}\Ra A_n=\delta_{1,n}-\frac{\delta_{2,n}}{1+c^2\mu_n^2}\\
    &v_t(x,0)=\cos(5x)=\sum_{n=1}^\infty \brround{B_nc\mu_n-\frac{\delta_{2,n}}{1+c^2\mu_n^2}}\cos(\mu_nx)\\
    &\mu_n=5=2n-1\Ra n=3\\
    &B_nc\mu_n-\frac{\delta_{2,n}}{1+c^2\mu_n^2}=\delta_{3,n}\Ra B_n=\frac{\delta_{3,n}}{c\mu_n}+\frac{\delta_{2,n}}{c\mu_n(1+c^2\mu_n^2)}\\
    &v(x,t)=\cos(ct)\cos(x)+\brround{\frac{e^{-t}-\cos(3ct)}{1+9c^2}+\frac{\sin(3ct)}{3c(1+9c^2)}}\cos(3x)+\frac{\sin(5ct)}{5c}\cos(5x)\\
    &u(x,t)=t+\cos(ct)\cos(x)+\brround{\frac{3ce^{-t}-3c\cos(3ct)+\sin(3ct)}{3c(1+9c^2)}}\cos(3x)+\frac{1}{5c}\sin(5ct)\cos(5x)
\end{aligned}

$$

## D'Alembert's Solution

We can think of the solution to the wave equation as two superimposed waves travelling in opposite directions. This is represented through d'Alembert's solution to the wave equation.
Derivation of formula:

$$
\begin{aligned}
    &u_{tt}=c^2u_{xx}\\
    &u_{tt}-c^2u_{xx}=0\\
    &(u_t-cu_x)(u_t+cu_x)=0
\end{aligned}

$$

We can show that any function of the form $F(x-ct)$ satisfies $u_t+cu_x=0$.

$$
\begin{aligned}
    &u(x,t)=F(x-ct)\\
    &\text{let }\xi=x-ct\\
    &u_t=\frac{dF}{d\xi}\frac{d\xi}{dt}=F'(-c)\\
    &u_x=\frac{dF}{d\xi}\frac{d\xi}{dx}=F'(1)\\
    &u_t+cu_x=-cF'+cF'=0
\end{aligned}

$$

$\therefore$ $F(x-ct)$ is a solution to $u_t+cu_x=0$
Any function $G(x+ct)$ is a solution to $u_t-cu_x=0$

$$
\begin{aligned}
    &\text{let }\eta=x+ct\\
    &u_t=\frac{dG}{d\eta}\frac{d\eta}{dt}=G'(c)\\
    &u_x=\frac{dG}{d\eta}\frac{d\eta}{dx}=G'(1)\\
    &\Ra G'(c)-cG'=0
\end{aligned}

$$

The solution to $u_{tt}=c^2u_{xx}$ is $u=F(x-ct)+G(x+ct)$.
Proving that it's a solution:

$$
\begin{aligned}
    &u_{tt}-c^2u_{xx}=0\\
    &u_t=\frac{dF}{d\xi}\frac{d\xi}{dt}+\frac{dG}{d\eta}\frac{d\eta}{dt}\\
    &u_{tt}=\frac{d^2F}{d\xi^2}\cdot c^2+\frac{d^2G}{d\eta^2}\cdot c^2\\
    &u_x=\frac{dF}{d\xi}\frac{d\xi}{dx}+\frac{dF}{d\eta}\frac{d\eta}{dx}\\
    &u_{xx}=\frac{d^2F}{d\xi^2}+\frac{d^2G}{d\eta^2}\\
    &u_{tt}-c^2u_{xx}=F''c^2+G''c^2-c^2(F''+G'')=0\\
    &u(x,t)=F(x-ct)+G(x+ct)\\
    &u(x,0)=f(x)\\
    &u_t(x,0)=g(x)\\
    &u(x,0)=f(x)=F(x)+G(x)\\
    &u_t(x,0)=g(x)=-cF'(x)+cG'(x)\\
    &-cF(x)+cG(x)=\int_0^x g(s)ds\\
    &2cG(x)=\int_0^xg(s)ds+cf(x)\\
    &G(x)=\frac{1}{2c}\int_0^xg(s)ds+\frac{1}{2}f(x)\\
    &2cF(x)=cf(x)-\int_0^x g(s)ds\\
    &\Ra F(x)=\frac{1}{2}f(x)-\frac{1}{2c}\int_0^x g(s)ds\\
    &u(x,t)=F(x-ct)+G(x+ct)\\
    &=\frac{1}{2}f(x-ct)-\frac{1}{2c}\int_0^{x-ct}g(s)ds+\frac{1}{2c}\int_0^{x+ct}g(s)ds+\frac{1}{2}f(x+ct)\\
    &=\frac{1}{2}f(x-ct)+\frac{1}{2}f(x+ct)+\frac{1}{2c}\int_0^{x+ct}g(s)ds+\frac{1}{2c}\int_{x-ct}^0 g(s)ds
\end{aligned}

$$

And so the final solution is of the form

$$
u(x,t)=\frac{1}{2}\brround{f(x-ct)+f(x+ct)}+\frac{1}{2c}\int_{x-ct}^{x+ct}g(s)ds

$$

Ex:

$$
\begin{aligned}
    &u_{tt}=u_{xx},\ t>0,\ 0\leq x\leq 1\\
    &u(0,t)=0,\ u(1,t)=1\\
    &u(x,0)=\sin(\pi x)+x,\ u_t(x,0)=\sin(3\pi x)
\end{aligned}

$$

D'Alembert's solution:
\begin{small}

$$
\begin{aligned}
    &u(x,t)=\frac{1}{2}\brround{f(x-ct)+f(x+ct)}+\frac{1}{2c}\int_{x-ct}^{x+ct}g(s)ds\\
    &u(x,t)=\frac{1}{2}\brround{(x-t)+\sin(\pi(x-t))+(x+t)+\sin(\pi(x+t))+\int_{x-t}^{x+t}\sin(3\pi s)ds}\\
    &=x+\frac{1}{2}\brround{\sin(\pi x)\cos(\pi t)-\cos(\pi x)\sin(\pi t)+\sin(\pi x)\cos(\pi t)+\cos(\pi x)\sin(\pi t)-\frac{1}{3\pi}\brsquare{\cos(3\pi s)}_{x-t}^{x+t}}\\
    &=x+\frac{1}{2}\brround{2\sin(\pi x)\cos(\pi t)-\frac{1}{3\pi}\brround{\cos(3\pi(x+t))-\cos(3\pi(x-t))}}\\
    &=x+\frac{1}{2}\brround{2\sin(\pi x)\cos(\pi t)-\frac{1}{3\pi}\brround{\cos(3\pi x)\cos(3\pi t)-\sin(3\pi x)\sin(3\pi t)-(\cos(3\pi x)\cos(3\pi t)+\sin(3\pi x)\sin(3\pi t))}}\\
    &=x+\frac{1}{2}\brround{2\sin(\pi x)\cos(\pi t)+\frac{2}{3\pi}\sin(3\pi x)\sin(3\pi t)}\\
    &u(x,t)=x+\sin(\pi x)\cos(\pi t)+\frac{1}{3\pi}\sin(3\pi x)\sin(3\pi t)
\end{aligned}

$$

\end{small}
