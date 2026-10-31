# Complex Numbers

<!-- Source: [Sections/Pre-Calculus/Complex_Numbers.tex](../../Sections/Pre-Calculus/Complex_Numbers.tex) -->

Complex numbers arise from the roots of polynomials.
Ex: $x^2+1=0\Ra x^2=-1 \Ra x=\pm\sqrt{-1}$. This polynomial has no real roots, however, we can introduce an imaginary number $i$ such that $i^2=-1$. Then we will have the solution $x=\pm i$
We can introduce *complex numbers* which are numbers in the form $z=x+iy$, where $x$ is the real part of $z$, $\Re(z)$, and $y$ is the imaginary part of $z$, $\Im(z)$.
These numbers can also be expressed in vector notation along the complex plane.
Complex Arithmetic:
Addition, subtraction, and multiplication works the same, just with the addition of the fact $i^2=-1$. For division, we require what is called the conjugate.
The conjugate of a complex number is the same number, just with the sign of the imaginary component flipped.

$$
\overline{z}=x-yi

$$

where $\overline{z}$ is the conjugate of $z$.
Similarly to vectors, we can also define the modulus (length) of a complex number

$$
|z|^2=x^2+y^2=z\cdot\overline{z}

$$

Using this, we can define division of a complex number and also define the real and imaginary components of a complex number.

$$
\begin{aligned}
    &\frac{u}{z}=\frac{s+it}{x+iy}=\frac{(s+it)(x-iy)}{(x+iy)(x-iy)}=\frac{u\overline{z}}{x^2+y^2}=\frac{u\overline{z}}{|z|^2}
\end{aligned}

$$

Another way to represent complex numbers is through polar form. To use this we must first introduce Euler's identity:

$$
e^{i\theta}=\cos\theta+i\sin\theta

$$

This then helps us with the equation for polar form

$$
z=a+ib=|z|(\cos\theta+i\sin\theta)=|z|e^{i\theta}

$$

Ex: Represent $1+i$ in polar coordinates

$$
\begin{aligned}
    &|z|=\sqrt{2}\\
    &\theta=\arctan{\frac{b}{a}}=\arctan{1}=\frac{\pi}{4}\\
    &z=\sqrt{2}e^{\frac{\pi i}{4}+2n},\,n\in\R
\end{aligned}

$$

Ex2: Find the roots of $x^3=2$

$$
\begin{aligned}
    &x=|x|e^{i\theta}\\
    &|x|=\sqrt[3]{2}\\
    &x^3=2=2e^{3i\theta}\Ra 1=e^{3i\theta}=\cos(3\theta)+i\sin(3\theta)\\
    &\Ra \cos(3\theta)=1\\
    &3\theta=2\pi n,\,n\in\R\\
    &\theta=\frac{3\pi}{2}n,\,n\in\R\\
    &x=\eqnsystem{\sqrt[3]{2}\\\sqrt[3]{2}e^{i\frac{2\pi}{3}}\\\sqrt[3]{2}e^{i\frac{4\pi}{3}}}
\end{aligned}

$$
