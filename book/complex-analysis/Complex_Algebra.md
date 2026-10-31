# Complex Algebra

<!-- Source: [Sections/Complex_Analysis/Complex_Algebra.tex](../../Sections/Complex_Analysis/Complex_Algebra.tex) -->

Complex numbers arise from the roots of polynomials.
Ex: $x^2+1=0\Ra x^2=-1 \Ra x=\pm\sqrt{-1}$. This polynomial has no real roots, however, we can introduce an imaginary number $i$ such that $i^2=-1$. Then we will have the solution $x=\pm i$
We can introduce *complex numbers* which are numbers in the form $z=x+iy$, where $x$ is the real part of $z$, $\Re(z)$, and $y$ is the imaginary part of $z$, $\Im(z)$.
These numbers can also be expressed in vector notation along the complex plane.

## Complex Arithmetic

Addition, subtraction, and multiplication work the same, just with the addition of the fact $i^2=-1$. For division, we require what is called the conjugate.
The conjugate of a complex number is the same number, just with the sign of the imaginary component flipped.

$$
\overline{z}=x-yi

$$

where $\overline{z}$ is the conjugate of $z$.
Similarly to vectors, we can also define the modulus (length) of a complex number

$$
|z|^2=x^2+y^2=z\cdot\overline{z}

$$

Using this, we can define the division of a complex number and also define the real and imaginary components of a complex number.
The general expression for division is:

$$
\begin{aligned}
    &\frac{u}{z}=\frac{s+it}{x+iy}=\frac{(s+it)(x-iy)}{(x+iy)(x-iy)}=\frac{u\overline{z}}{x^2+y^2}=\frac{u\overline{z}}{|z|^2}
\end{aligned}

$$

The real and imaginary components can be computed as

$$
\begin{aligned}
    &z=x+iy\\
    &\overline{z}=x-iy\\
    &\Re(z)=\frac{z+\overline{z}}{2}\\
    &\Im(z)=\frac{z-\overline{z}}{2i}
\end{aligned}

$$

Ex1: Simplify $(1+2i)(3+i)(2-3i)$

$$
\begin{aligned}
    &(1+2i)(3+i)(2-3i)=(3+i+6i-2)(2-3i)=(1+7i)(2-3i)\\
    &=2-3i+14i+21\\
    &=23+11i
\end{aligned}

$$

Ex2: Simplify $\bfrac{2+i}{1+i}^2$

$$
\begin{aligned}
    &\bfrac{2+i}{1+i}^2=\brround{\frac{(2+i)(1-i)}{(1+i)(1-i)}}^2=\bfrac{2+i-2i+1}{2}^2=\bfrac{3-i}{2}^2=\frac{9-6i-1}{4}\\
    &=2-\frac{3}{2}i
\end{aligned}

$$

Ex3: Simplify $(1+2i)^5$

$$
\begin{aligned}
    &(1+2i)^5=1^5+5(1)^4(2i)+10(1)^3(2i)^2+10(1)^2(2i)^3+5(1)(2i)^4+(2i)^5\\
    &=1+10i+10(-4)+10(-8i)+5(16)+32i\\
    &=1+10i-40-80i+80+32i\\
    &=41-38i
\end{aligned}

$$

Ex4: Prove

$$
 \text{if }|z|=1\text{ then }\Re\bfrac{1}{1+z}=\frac{1}{2} 

$$

\begin{proof}

$$
\begin{aligned}
    &\Re(w)=\frac{w+\overline{w}}{2}\\
    &\overline{\frac{1}{1+z}}=\frac{1}{1+\overline{z}}\\
    &\Re\bfrac{1}{1+z}=\frac{\frac{1}{1+z}+\frac{1}{1+\overline{z}}}{2}=\frac{1+\overline{z}+1+z}{2(1+z)(1+\overline{z})}=\frac{2+z+\overline{z}}{2(1+z+\overline{z}+|z|^2)}\\
    &|z|=1\Ra \Re\bfrac{1}{1+z}=\frac{2+z+\overline{z}}{2(2+z+\overline{z})}=\frac{1}{2}
\end{aligned}

$$

\end{proof}
Some properties of $\overline{z}$:

- $\overline{\overline{z}}=z$
- $\overline{z_1z_2}=\overline{z}_1\overline{z}_2$
- $|z_1z_2|=|z_1||z_2|$

Some common inequalities come from the triangle inequality:
$|z_1+z_2|\leq |z_1|+|z_2|$
\begin{proof}

$$
\begin{aligned}
    &|z_1+z_2|\leq |z_1|+|z_2|\\
    &|z_1+z_2|=\sqrt{(x_1+x_2)^2+(y_1+y_2)^2}\\
    &\sqrt{(x_1+x_2)^2+(y_1+y_2)^2}\leq \sqrt{x_1^2+y_1^2}+\sqrt{x_2^2+y_2^2}\\
    &|z_1+z_2|\leq |z_1|+|z_2|
\end{aligned}

$$

\end{proof}

$$
\Ra |z_1\pm z_2|\geq ||z_1|-|z_2||

$$

This leads to a general upper and lower bound that can be derived from these inequalities:

$$
||z_1|-|z_2||\leq|z_1\pm z_2|\leq |z_1|+|z_2|

$$

## Polar Form of Complex Numbers

Another way to represent complex numbers is through polar form. To use this we must first introduce Euler's identity:

$$
e^{i\varphi}=\cos\varphi+i\sin\varphi

$$

This then helps us with the equation for the polar form

$$
z=a+ib=|z|(\cos\varphi+i\sin\varphi)=|z|e^{i\varphi}

$$

For $z=re^{i\varphi}$ We call $r$ the magnitude of the complex number and $\varphi$ is the argument. This can be especially useful for simplifying some complex numbers.
Ex:

$$
\begin{aligned}
    &\brvertical{\frac{(1+\sqrt{3}i)^{100}}{(\sqrt{3}-i)^{100}}}=\frac{|1+\sqrt{3}i|^{100}}{|\sqrt{3}-i|^{100}}=\frac{2^{100}}{2^{100}}=1
\end{aligned}

$$

Note that because sinusoidal functions are periodic every $2\pi$ this means that there infinite ways to express a function in polar coordinates.

$$
e^{i2\pi k}=1,\ k\in\Z\Ra z=re^{i(\varphi+2\pi k)}

$$

To get around the issue of having infinite possible polar forms for every complex number we define what's called the principal argument to be

$$
\Arg(z)=\varphi\in(-\pi,\pi]

$$

We define the regular argument to be

$$
\arg(z)=\Arg(z)+2k\pi,\ k\in\Z

$$

Note that $\Arg(z)$ is singular valued while $\arg(z)$ is multi-valued.
We can define $\Arg(z)$ in terms of the real and imaginary parts ($x$ and $y$) as

$$
\Arg(z)=\arctan(\tfrac{y}{x})\pm k\pi

$$

What it is specifically depends on what quadrant of the complex plane the point lies in.

- QI: $\Arg(z)=\arctan(\tfrac{y}{x})$
- QII: $\Arg(z)=\arctan(\tfrac{y}{x})+\pi$
- QIII: $\Arg(z)=\arctan(\tfrac{y}{x})-\pi$
- QIV: $\Arg(z)=\arctan(\tfrac{y}{x})$

Ex:

$$
\begin{aligned}
    &\Arg(-1-\sqrt{3}i)=\arctan(\sqrt{3})-\pi=-\frac{2\pi}{3}
\end{aligned}

$$

Ex2:

$$
\begin{aligned}
    &\arg(1-\sqrt{3}i)\\
    &\Arg(1-\sqrt{3}i)=-\frac{\pi}{3}\\
    &\arg(1-\sqrt{3})=-\frac{\pi}{3}+2k\pi,\ k\in\Z
\end{aligned}

$$

Ex3:

$$
\begin{aligned}
    &\arg(-1+2i)\\
    &\Arg(-1+2i)=\arctan(-2)+\pi\\
    &\arg(-1+2i)=\pi-\arctan(2)+2k\pi
\end{aligned}

$$

Ex4: Simplify

$$
\begin{aligned}
    &z=-3+3i\\
    &\Arg(z)=\arctan\bfrac{3}{-3}+\pi=\frac{3\pi}{4}\\
    &|z|=3\sqrt{2}\\
    &z=3\sqrt{2}e^{\frac{3\pi}{4}i}
\end{aligned}

$$

Ex5: Simplify

$$
\begin{aligned}
    &z=-3-3i\\
    &\Arg(z)=\arctan\bfrac{-3}{-3}-\pi=-\frac{3\pi}{4}\\
    &|z|=3\sqrt{2}\\
    &z=3\sqrt{2}e^{-\frac{3\pi}{4}i}
\end{aligned}

$$

Ex6: Simplify

$$
\begin{aligned}
    &z=\frac{1-i}{-\sqrt{3}+i}=\frac{u}{v}\\
    &\arg(z)=\arg(u)-\arg(v)=\arctan\bfrac{-1}{1}-\brround{\arctan\bfrac{1}{-\sqrt{3}}+\pi}+2k\pi\\
    &=-\frac{\pi}{4}-\frac{5\pi}{6}+2k\pi=-\frac{13\pi}{12}+2k\pi\\
    &\Arg(z)=\frac{11\pi}{12}\\
    &|z|=\frac{|u|}{|v|}=\frac{\sqrt{2}}{2}=\frac{1}{\sqrt{2}}\\
    &z=\frac{e^{\frac{11\pi}{12}i}}{\sqrt{2}}
\end{aligned}

$$

Ex7: Simplify

$$
\begin{aligned}
    &z=(\sqrt{3}-i)^2=w^2\\
    &\arg(w)=\arctan\bfrac{-1}{\sqrt{3}}+2k\pi=-\frac{\pi}{6}\\
    &\Ra \arg(z)=2\arg(w)=-\frac{\pi}{3}+4k\pi\\
    &\Arg(z)=-\frac{\pi}{3}\\
    &|w|=2\Ra |z|=|w|^2=4\\
    &z=4e^{-\frac{\pi}{3}i}
\end{aligned}

$$

Ex8: Solve for all values of $z$

$$
\begin{aligned}
    &e^z=-1-\sqrt{3}i\\
    &e^z=2e^{-i\frac{2\pi}{3}+2\pi ik}=e^{\ln 2-i\frac{2\pi}{3}+2\pi ik}\\
    &z=\ln2-i\frac{2\pi}{3}+2\pi ik,\ \forall k\in\Z
\end{aligned}

$$

Properties of $\Arg(z)$ and $\arg(z)$

- $\Arg(z_1z_2)\neq\Arg(z_1)+\Arg(z_2)$
\begin{proof}
Proof by contradiction: assume that $\Arg(z_1z_2)=\Arg(z_1)+\Arg(z_2)$ is true.
Take $z_1=z_2=-1$.

$$
\begin{aligned}
    &\Arg(z_1)=\Arg(z_2)=\pi\\
    &\Ra \Arg(z_1)+\Arg(z_2)=2\pi\\
    &\Arg(z_1z_2)=\Arg(1)=0\\
    &\Arg(z_1z_2)\neq\Arg(z_1)+\Arg(z_2)\ \forall z_1,z_2\neq0\in\C
\end{aligned}

$$

\end{proof}
- $\arg(z_1z_2)=\arg(z_1)+\arg(z_2)$
- $ \Arg(\overline{z})\neq-\Arg(z) $
\begin{proof}
Proof by contradiction: assume that $\Arg(\overline{z})=-\Arg(z)$ is true.
Take $z=-1$

$$
\begin{aligned}
    &\overline{z}=z=-1\\
    &\Arg(z)=\pi\\
    &\Arg(\overline{z})=\pi\\
    &-\Arg(z)=-\pi\\
    &\Ra \Arg(\overline{z})\neq-\Arg(z)\ \forall z\in\C
\end{aligned}

$$

\end{proof}
- $ \arg(z)=-\arg(\overline{z}) $
\begin{proof}

$$
\begin{aligned}
    &z=|z|e^{i\arg(z)}\ \forall z\in\C\\
    &\overline{z}=|z|e^{-i\arg(z)}\\
    &\Ra \arg(\overline{z})=-\arg(z)
\end{aligned}

$$

\end{proof}

## De Moirre's Formula

Using Euler's identity we can derive a powerful formula called De Moirre's Formula as follows:

$$
\begin{aligned}
    &e^{iN\varphi}=\cos(N\varphi)+i\sin(N\varphi)\\
    &e^{iN\varphi}=(e^{i\varphi})^N=(\cos\varphi+i\sin\varphi)^N\\
    &(\cos\varphi+i\sin\varphi)^N=\cos(N\varphi)+i\sin(N\varphi)
\end{aligned}

$$

Applications of De Moirre's Formula:
Binomial expansion:

$$
\begin{aligned}
    &N=2:\\
    &\cos(2\theta)=\cos^2\theta-\sin^2\theta\\
    &\sin(2\theta)=2\cos\theta\sin\theta\\
    &N=3:\\
    &(\cos\theta+i\sin\theta)^3=\cos^3\theta+3\cos^2\theta(i\sin\theta)+3\cos\theta(i\sin\theta)^2+(i\sin\theta)^3\\
    &\cos(3\theta)=\cos^3\theta-3\cos\theta\sin^2\theta\\
    &\sin(3\theta)=3\cos^2\theta\sin\theta-\sin^3\theta
\end{aligned}

$$

Ex: Prove

$$
 \sin(3\theta)=3\sin\theta-4\sin^3\theta 

$$

\begin{proof}
Using De Moivre's formula with $N=3$

$$
\begin{aligned}
    &(\cos\theta+i\sin\theta)^3=\cos(3\theta)+i\sin(3\theta)\\
    &(\cos\theta)^3+3(\cos\theta)^2(i\sin\theta)+3\cos\theta(i\sin\theta)^2+(i\sin\theta)^3=\cos(3\theta)+i\sin(3\theta)\\
    &\cos^3\theta-3\cos\theta\sin^2\theta+i(3\cos^2\theta\sin\theta-\sin^3\theta)=\cos(3\theta)+i\sin(3\theta)\\
    &\Im\brcurly{\cos^3\theta-3\cos\theta\sin^2\theta+i(3\cos^2\theta\sin\theta-\sin^3\theta)}=\Im\brcurly{\cos(3\theta)+i\sin(3\theta)}\\
    &3\cos^2\theta\sin\theta-\sin^3\theta=\sin(3\theta)\\
    &\sin^2\theta+\cos^2\theta=1\Ra \cos^2\theta=1-\sin^2\theta\\
    &3(1-\sin^2\theta)\sin\theta-\sin^3\theta=\sin(3\theta)\\
    &3\sin\theta-3\sin^3\theta-\sin^3\theta=\sin(3\theta)\\
    &3\sin\theta-4\sin^3\theta=\sin(3\theta)
\end{aligned}

$$

\end{proof}
Computing trigonometric integrals:
Ex:

$$
\begin{aligned}
    &\int_0^{2\pi}\cos^8\varphi d\varphi\\
    &e^{i\varphi}=\cos\varphi+i\sin\varphi\\
    &e^{-i\varphi}=\cos\varphi-i\sin\varphi\\
    &\cos\varphi=\frac{e^{i\varphi}+e^{-i\varphi}}{2}\\
    &\sin\varphi=\frac{e^{i\varphi}-e^{-i\varphi}}{2i}\\
    &\int_0^{2\pi}\brround{\frac{e^{i\varphi}+e^{-i\varphi}}{2}}^8d\varphi=\frac{1}{2^8}\int_0^{2\pi}\brround{e^{i\varphi}+e^{-i\varphi}}^8d\varphi\\
    &=\frac{1}{2^8}\int_0^{2\pi}\brround{e^{i8\varphi}+\comb{1}{8}e^{i7\varphi}e^{-i\varphi}+\cdots+\comb{7}{8}e^{i\varphi}e^{-i7\varphi}+e^{-i8\varphi}}d\varphi\\
    &=\frac{1}{2^8}\brround{0+\cdots+\comb{4}{8}2\pi+\cdots+0}=\frac{\comb{4}{8}}{2^7}\pi
\end{aligned}

$$

Ex2:

$$
\begin{aligned}
    &\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2}\\
    &\int_0^{2\pi}\cos^6\theta d\theta=\int_0^{2\pi}\brround{\frac{e^{i\theta}+e^{-i\theta}}{2}}\\
    &=\frac{1}{2^6}\int_0^{2\pi}\sum_{k=0}^6\combm{k}{6}e^{i\theta k}e^{-i\theta(6-k)}d\theta\\
    &=\frac{1}{2^6}\sum_{k=0}^6\combm{k}{6}\int_0^{2\pi}e^{i\theta(2k-6)}d\theta\\
    &\int_0^{2\pi}e^{ik\theta}d\theta=\frac{e^{ik\theta}}{ik}\eval_0^{2\pi}=\frac{e^{2\pi ik}-1}{ik}\\
    &e^{2\pi ik}=1,\ k\in\Z\Ra \int_0^{2\pi}e^{ik\theta}d\theta=0,\ k\neq0\in\Z\\
    &\Ra \int_0^{2\pi}\cos^6\theta d\theta=\frac{1}{2^6}\combm{3}{6}\int_0^{2\pi}d\theta=\frac{(20)(2\pi)}{2^6}=\frac{5\pi}{8}
\end{aligned}

$$

Ex3:

$$
\begin{aligned}
    &\int_0^{2\pi}\sin^6(2\theta)d\theta\\
    &\sin(2\theta)=\frac{e^{2i\theta}-e^{-2i\theta}}{2i}\\
    &\int_0^{2\pi}\sin^6(2\theta)d\theta=\int_0^{2\pi}\brround{\frac{e^{2i\theta}-e^{-2i\theta}}{2i}}^6d\theta\\
    &=\frac{1}{(2i)^6}\int_0^{2\pi}\sum_{k=0}^6\combm{k}{6}(-1)^{6-k}e^{2ik\theta}e^{-2i\theta(6-k)}d\theta\\
    &=-\frac{1}{2^6}\sum_{k=0}^6\combm{k}{6}(-1)^{6-k}\int_0^{2\pi}e^{i\theta(4k-12)}d\theta\\
    &\int_0^{2\pi}e^{ik\theta}d\theta=\frac{e^{ik\theta}}{ik}\eval_0^{2\pi}=\frac{e^{2\pi ik}-1}{ik}\\
    &e^{2\pi ik}=1,\ k\in\Z\Ra \int_0^{2\pi}e^{ik\theta}d\theta=0,\ k\neq0\in\Z\\
    &\Ra \int_0^{2\pi}\sin^6(2\theta)d\theta=-\frac{1}{2^6}\combm{3}{6}(-1)^3\int_0^{2\pi} d\theta\\
    &=\frac{5\pi}{8}
\end{aligned}

$$

Ex4: Prove

$$
 \sum_{k=0}^n\cos(k\theta)=\frac{1}{2}+\frac{\sin\brround{\brround{n+\frac{1}{2}}\theta}}{2\sin\brround{\frac{\theta}{2}}} 

$$

\begin{proof}
De Moivre's formula states

$$
 (\cos\theta+i\sin\theta)^n=\cos(n\theta)+i\sin(n\theta) 

$$

If we take the conjugate of both sides we get

$$
 (\cos\theta-i\sin\theta)^n=\cos(n\theta)-i\sin(n\theta) 

$$

Summing these two equations gives

$$
\begin{aligned}
    &(\cos\theta+i\sin\theta)^k+(\cos\theta-i\sin\theta)^k=2\cos(k\theta)\\
    &\cos\theta\pm i\sin\theta=e^{\pm i\theta}\\
    &2\cos(k\theta)=(e^{i\theta})^k+(e^{-i\theta})^k
\end{aligned}

$$

We can sum both sides of this to get

$$
 2\sum_{k=0}^n\cos(k\theta)=\sum_{k=0}^n(e^{i\theta})^k+\sum_{k=0}^n(e^{-i\theta})^k 

$$

The formula for the geometric sum is

$$
 \sum_{k=0}^n z^k=\frac{1-z^{n+1}}{1-z} 

$$

Applying this we get

$$
\begin{aligned}
    &2\sum_{k=0}^n\cos(k\theta)=\frac{1-(e^{i\theta})^{n+1}}{1-e^{i\theta}}+\frac{1-(e^{-i\theta})^{n+1}}{1-e^{-i\theta}}\\
    &2\sum_{k=0}^n\cos(k\theta)=\frac{(1-e^{i\theta(n+1)})(1-e^{-i\theta})+(1-e^{-i\theta(n+1)})(1-e^{i\theta})}{(1-e^{i\theta})(1-e^{-i\theta})}\\
    &2\sum_{k=0}^n\cos(k\theta)=\frac{1-e^{i\theta(n+1)}-e^{i\theta}+e^{i\theta n}+1-e^{-i\theta(n+1)}-e^{-i\theta}+e^{-i\theta n}}{1-e^{i\theta}-e^{-i\theta}+1}\\
    &2\sum_{k=0}^n\cos(k\theta)=1+\frac{e^{i\theta n}+e^{-i\theta n}-e^{i\theta(n+1)}-e^{-i\theta(n+1)}}{2-e^{i\theta}-e^{-i\theta}}\\
    &2\sum_{k=0}^n\cos(k\theta)=1+\frac{e^{i\frac{\theta}{2}}\brround{e^{-i\theta(n+\frac{1}{2})}-e^{i\theta(n+\frac{1}{2})}}+e^{-i\frac{\theta}{2}}\brround{e^{i\theta(n+\frac{1}{2})}-e^{i\theta(n+\frac{1}{2})}}}{e^{i\frac{\theta}{2}}\brround{e^{-i\frac{\theta}{2}}-e^{i\frac{\theta}{2}}}+e^{-i\frac{\theta}{2}}\brround{e^{i\frac{\theta}{2}}-e^{-i\frac{\theta}{2}}}}\\
    &2\sum_{k=0}^n\cos(k\theta)=1+\frac{\brround{e^{-i\frac{\theta}{2}}-e^{i\frac{\theta}{2}}}\brround{e^{i\theta(n+\frac{1}{2})}-e^{-i\theta(n+\frac{1}{2})}}}{-\brround{e^{-i\frac{\theta}{2}}-e^{i\frac{\theta}{2}}}^2}\\
    &2\sum_{k=0}^n\cos(k\theta)=1+\frac{e^{i\theta(n+\frac{1}{2})}-e^{-i\theta(n+\frac{1}{2})}}{e^{i\frac{\theta}{2}}-e^{-i\frac{\theta}{2}}}\\
    &2\sum_{k=0}^n\cos(k\theta)=1+\frac{\frac{1}{2i}\brround{e^{i\theta(n+\frac{1}{2})}-e^{-i\theta(n+\frac{1}{2})}}}{\frac{1}{2i}\brround{e^{i\frac{\theta}{2}}-e^{-i\frac{\theta}{2}}}}\\
    &\sin(x)=\frac{e^{ix}-e^{-ix}}{2i}\\
    &2\sum_{k=0}^n\cos(k\theta)=1+\frac{\sin\brround{\theta(n+\frac{1}{2})}}{\sin\brround{\frac{\theta}{2}}}\\
    &\sum_{k=0}^n\cos(k\theta)=\frac{1}{2}+\frac{\sin\brround{\brround{n+\frac{1}{2}}\theta}}{2\sin\brround{\frac{\theta}{2}}}
\end{aligned}

$$

\end{proof}

## Geometry in the Complex Plane

Using the notation such that $z=x+iy$ where $\Re(z)=x$ and $\Im(z)=y$ we can define a circle in the complex plane as

$$
(x-x_0)^2+(y-y_0)^2=r_0^2

$$

This is analogous to writing

$$
|z-z_0|=r_0

$$

The two can be related as follows:

$$
\begin{aligned}
    &|z-z_0|=r_0\\
    &|x+iy-x_0-iy_0|=r_0\\
    &\sqrt{(x-x_0)^2+(y-y_0)^2}=r_0\\
    &(x-x_0)^2+(y-y_0)^2=r_0^2
\end{aligned}

$$

Ex: describe the circle formed by $2|z|=|z+1|$

$$
\begin{aligned}
    &2|z|=|z+1|\\
    &4|z|^2=|z+1|^2\\
    &4x^2+4y^2=(x+1)^2+y^2\\
    &4x^2+4y^2=x^2+2x+1+y^2\\
    &3x^2+3y^2-2x-1=0\\
    &3x^2-2x+\frac{1}{3}+3y^2-\frac{4}{3}=0\\
    &3\brround{x-\frac{1}{3}}^2+3y^2=\frac{4}{3}\\
    &\brround{x-\frac{1}{3}}^2+y^2=\frac{4}{9}
\end{aligned}

$$

A line in the complex plane can be written as

$$
ax+by=c \longleftrightarrow a\frac{z+\overline{z}}{2}+b\frac{z-\overline{z}}{2i}=c

$$

Ex: describe the line formed by $|z-1+i|=|z-2i|$

$$
\begin{aligned}
    &|z-1+i|=|z-2i|\\
    &|z-1+i|^2=|z-2i|^2\\
    &(x-1)^2+(y+1)^2=x^2+(y-2)^2\\
    &x^2-2x+1+y^2+2y+1=x^2+y^2-4y+4\\
    &-2x+2+2y=-4y+4\\
    &6y=2x+2\\
    &y=\frac{1}{3}(x+1)
\end{aligned}

$$

We can define an ellipse in the complex plane as

$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}=1

$$

If we have $a>b$ then we will have a horizontal ellipse and if $b>a$ then we will have a vertical ellipse.
Assuming that $a>b$ then we can define the foci points to be at

$$
\begin{aligned}
    &+F=(\sqrt{a^2-b^2}, 0)\\
    &-F=(-\sqrt{a^2-b^2}, 0)
\end{aligned}

$$

The equation of an ellipse can also be described by

$$
|z-F|+|z+F|=2a

$$

Ex: describe the ellipse formed by $|z-1|+|z+1|=4$

$$
\begin{aligned}
    &|z-1|+|z+1|=4\\
    &|z-F|+|z+F|=2a\Ra 2a=4\Ra a=2\\
    &F=\sqrt{a^2-b^2}=1\Ra 1=4-b^2\Ra b^2=3\\
    &\frac{x^2}{4}+\frac{y^2}{3}=1
\end{aligned}

$$

Ex2: describe the ellipse formed by $|z-1|+|z+3|=6$

$$
\begin{aligned}
    &|z-1|+|z+3|=6\\
    &\text{note that this ellipse is not centered at the origin so we need to shift it}\\
    &|z+1-2|+|z+1+2|=6\\
    &2a=6\Ra a=3\\
    &F=2=\sqrt{a^2-b^2}\Ra 4=9-b^2\Ra b^2=5\\
    &\frac{(x+1)^2}{9}+\frac{y^2}{5}=1
\end{aligned}

$$

## Roots of a Complex Number

Given $z_0=r_0e^{i\varphi_0}$, what is $z_0^\frac{1}{n}$?
If we let $w=z_0^\frac{1}{n}$ then $w^n=z_0$

$$
\begin{aligned}
    &w=re^{i\varphi},\ w_n=r^ne^{in\varphi}\\
    &w^n=z_0\Ra r^ne^{in\varphi}=r_0e^{i\varphi_0}\\
    &\Ra r^n=r_0\Ra r_0^\frac{1}{n}\\
    &e^{in\varphi}=e^{i\varphi_0}\Ra n\varphi=\varphi_0+2k\pi\\
    &\varphi=\frac{\varphi}{n}+\frac{2k\pi}{n}
\end{aligned}

$$

So all solutions to $w^n=z_0$ are given by

$$
w=r_0^\frac{1}{n}e^{i\brround{\frac{\varphi_0}{n}+\frac{2k\pi}{n}}},\ k\in\Z

$$

If we normalize $\varphi_0=\Arg(z_0)$ then $k$ will be in the range $k\in\brcurly{0,1,\ldots,n-1}$.
Note that the expression

$$
w=r_0^\frac{1}{n}e^{i\brround{\frac{\varphi_0}{n}+\frac{2k\pi}{n}}},\ k\in\Z

$$

is multi-valued. If we want to avoid this, we can take what's called the principal value which is the value when $k=0$:

$$
z_0^\frac{1}{n}=r_0^\frac{1}{n}e^{i\frac{\varphi_0}{n}}

$$

Ex: Compute $(-1)^\frac{1}{2}$

$$
\begin{aligned}
    &z_0=-1=1^{\frac{1}{2}}e^{i(\frac{\pi}{2}+\frac{2k\pi}{2})}=e^{i(\frac{\pi}{2}+k\pi)}=\brcurly{\ldots,e^{-i\frac{3\pi}{2}},e^{-i\frac{\pi}{2}},e^{i\frac{\pi}{2}},e^{i\frac{3\pi}{2}},e^{i\frac{5\pi}{2}},\ldots}\\
    &\text{note that there are only 2 unique values}\\
    &(-1)^\frac{1}{2}=e^{i(\frac{\pi}{2}+k\pi)},\ k\in\brcurly{0,1}
\end{aligned}

$$

The principal value (when $k=0$) of this equation works out to be $i$.
Ex2: Find all solutions to

$$
\begin{aligned}
    &z^7=i-1\\
    &z^7=\sqrt{2}e^{i(\frac{3\pi}{4}+2\pi k)}\\
    &z=2^{1/14}e^{i(\frac{3\pi}{28}+\frac{2\pi}{7} k)},\ k\in\brcurly{0,1,2,3,4,5,6}
\end{aligned}

$$

Ex3: Find all solutions to

$$
\begin{aligned}
    &z^5=\frac{2i}{-1-\sqrt{3}i}\\
    &z^5=\frac{2e^{i\frac{\pi}{2}}}{2e^{-i\frac{2\pi}{3}}}=e^{i\frac{7\pi}{6}}=e^{-i(\frac{5\pi}{6}+2\pi k)}\\
    &z=e^{-i(\frac{\pi}{6}+\frac{2\pi}{5}k)},\ k\in\brcurly{0,1,2,3,4}
\end{aligned}

$$

Ex4: Find all solutions to

$$
\begin{aligned}
    &\bfrac{z}{z+1}^2=i\\
    &\bfrac{z}{z+1}^2=e^{i(\frac{\pi}{2}+2\pi k)}\\
    &\frac{z}{z+1}=e^{i(\frac{\pi}{4}+\pi k)},\ k\in\brcurly{0,1}\\
    &e^{i(\frac{\pi}{4}+\pi k)}=\brcurly{\frac{1}{\sqrt{2}}(1+i),\frac{1}{\sqrt{2}}(-1-i)}\\
    &z=e^{i(\frac{\pi}{4}+k\pi)}(z+1)\\
    &z=\frac{e^{i(\frac{\pi}{4}+k\pi)}}{1-e^{i(\frac{\pi}{4}+k\pi)}}=\brcurly{\frac{1+i}{\sqrt{2}-1-i},\frac{-1-i}{\sqrt{2}+1+i}}
\end{aligned}

$$

Ex5: Find all solutions to

$$
\begin{aligned}
    &z^2+4iz+1=0\\
    &(z^2+4iz-4)+4+1=0\\
    &(z+2i)^2+5=0\\
    &(z+2i)^2=-5=5e^{i(\pi+2\pi k)}\\
    &z+2i=\sqrt{5}e^{i(\frac{\pi}{2}+\pi k)}=\brcurly{\sqrt{5}i,-\sqrt{5}i}\\
    &z=\brcurly{(\sqrt{5}-2)i,-(\sqrt{5}+2)i}
\end{aligned}

$$

Ex6: Find all solutions to $(z+1)^4=(1-i)z^4$

$$
\begin{aligned}
    &(1-i)z^4=\sqrt{2}e^{-i\frac{\pi}{4}+2\pi ki}z^4\\
    &z+1=2^{1/8}e^{-i\frac{\pi}{16}+i\frac{\pi k}{2}}z\\
    &z=\frac{-2^{1/8}}{1-e^{-i\frac{\pi}{16}+i\frac{\pi k}{2}}},\ k\in\brcurly{0,1,2,3}
\end{aligned}

$$
