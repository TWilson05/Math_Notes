# Complex Vector Spaces

<!-- Source: [Sections/Linear_Algebra/Complex_Vector_Spaces.tex](../../Sections/Linear_Algebra/Complex_Vector_Spaces.tex) -->

## Complex Operations

If we have vectors that contain complex values, they will exist in $\C^n$. This will change some of our definitions as we will see, however, we would like to keep some of our same properties. One such property is that the square of the length of a vector should be the inner product of that vector with itself.
If we take a complex vector and take the inner product with itself, using the traditional definition, there is a chance that we get a complex value

$$
\begin{aligned}
    &\matrixx{i+1 & 1}\matrixx{i+1\\1}=1+2i
\end{aligned}

$$

This doesn't fit with what we would expect as the length of our vector and so this definition doesn't hold. We can, however, take advantage of the property $z\overline{z}=|z|^2$. So what we can do is redefine the inner product for complex vectors:

$$
\boxed{\brangle{\vec{u},\vec{v}}=\vec{u}^T\vec{\overline{v}}}

$$

Ex:

$$
\begin{aligned}
    &\brangle{\matrixx{i\\1},\matrixx{i\\1}}=\matrixx{i & 1}\matrixx{-i\\1}=2
\end{aligned}

$$

Some properties of the complex inner product are as follows:

- $\brangle{c\vec{v},\vec{w}}=c\brangle{\vec{v},\vec{w}}$
- $\brangle{\vec{v},c\vec{w}}=\overline{c}\brangle{\vec{v},\vec{w}}$
- $\brangle{\vec{v},\vec{w}}=\overline{\brangle{\vec{w},\vec{v}}}$
- $\|\vec{v}\|^2=\brangle{\vec{v},\vec{v}}\geq0$

This implies that we will also have to introduce conjugates with some of our other definitions as well:
The conjugate transpose of a matrix is defined to be $A^*=\overline{A}^T$
A property of the inner product will be that

$$
\brangle{A\vec{u},\vec{v}}=\brangle{\vec{u},A^*\vec{v}}

$$

A matrix is said to be *hermitian* if

$$
\boxed{A=A^*}

$$

This is analogous to symmetric matrices.
Some properties are

- $\brangle{A\vec{x},\vec{y}}=\brangle{\vec{x},A\vec{y}}$
- $A$ has only real eigenvalues and $A$ is diagonalizable
- The diagonal entries are real numbers

A matrix is said to be *unitary* if

$$
\boxed{A^{-1}=A^*}

$$

This is analogous to orthogonal matrices.
It will have the properties

- $\brangle{A\vec{x},A\vec{y}}=\brangle{\vec{x},\vec{y}}$
- $\|A\vec{x}\|=\|\vec{x}\|$

Note that this conjugation also extends to the inner product definition of complex functions:

$$
\brangle{f,g}=\int_{-\infty}^\infty f(x)\overline{g(x)}dx

$$

## Roots of Unity

A complex number $\omega\in\C$ is an $N$th root of unity if $\omega^N=1$.
Ex: $N=2$

$$
\begin{aligned}
    &\omega^2=1\Ra \omega=\pm1
\end{aligned}

$$

so $1$ and $-1$ are 2nd roots of unity
Ex2: $N=3$

$$
\begin{aligned}
    &\omega^3=1\Ra (\omega-1)(\omega^2+\omega+1)=0\\
    &\omega=1,\ \omega=\frac{-1\pm i\sqrt{3}}{2}
\end{aligned}

$$

Ex3: $N=4$

$$
\begin{aligned}
    &\omega^4=1\Ra \omega^2=\pm1\\
    &\omega=\brcurly{1,-1,i,-i}
\end{aligned}

$$

For general $N$ we can express the roots of unity as

$$
\begin{aligned}
    &\omega_N^N=1=e^{2\pi i}\Ra \omega_N=e^{i\frac{2\pi}{N}}
\end{aligned}

$$

And so the roots of unity will be

$$
\omega_N=\brcurly{1,e^{i\frac{2\pi}{N}},e^{i\frac{2\pi(2)}{N}},\ldots,e^{i\frac{2\pi(N-1)}{N}}}

$$

Some properties of the roots of unity are

- $\omega_N^{N-1}=\overline{\omega_N}$

$$
 \omega_N^{N-1}=e^{i\frac{2\pi(N-1)}{N}}=e^{i2\pi}e^{-i\frac{2\pi}{N}}=e^{-i\frac{2\pi}{N}}=\overline{\omega_N} 

$$

- $\overline{\omega_N}=\omega_N^{-1}$

$$
 \omega_N\overline{\omega_N}=e^{i\frac{2\pi}{N}}e^{-i\frac{2\pi}{N}}=1 

$$

- $\sum\limits_{m=0}^{N-1}\omega_N^m=0$

## Discrete Fourier Transform

The standard basis of $\C^N$ is $\brcurly{\vec{c}_0,\vec{c}_1,\ldots,\vec{c_{N-1}}}$
where

$$
\vec{c}_0=\matrixx{1\\0\\\vdots\\0},\ \vec{c}_1=\matrixx{0\\1\\0\\\vdots\\0},\ldots

$$

We can define the Fourier basis of $\C^N$ to be $\brcurly{\vec{f}_0,\vec{f}_1,\ldots,\vec{f}_{N-1}}$
where

$$
\vec{f}_k=\matrixx{1\\ \omega_N^k\\ \omega_N^{2k}\\ \vdots\\ \omega_N^{(N-1)k}}

$$

Ex: The Fourier basis of $\C^4$ is given by

$$
\vec{f}_0=\matrixx{1\\1\\1\\1},\ \vec{f}_1=\matrixx{1\\i\\-1\\-i},\ \vec{f}_2=\matrixx{1\\-1\\1\\-1},\ \vec{f}_3=\matrixx{1\\-i\\-1\\ i}

$$

The Fourier basis forms an orthogonal basis of $\C^N$ with

$$
\brangle{\vec{f}_k,\vec{f}_m}=\eqnsystem{0 & k\neq m\\ N & k=m}

$$

Note that this is not an orthonormal basis as $\|\vec{f}_k\|=\sqrt{N}$
By the properties of the roots of unity we can get that

$$
\vec{\overline{f}}_k=\vec{f}_{N-k}

$$

which states that the Fourier basis vectors have conjugate symmetry about $N/2$.

The discrete Fourier transform (DTF) of $\vec{x}$ is the vector of coefficients of $\vec{x}$ with respect to the Fourier basis. Essentially, it takes a vector and projects it onto the Fourier basis. The resulting vector tells us what linear combination of Fourier basis vectors made up the original vector $\vec{x}$.
We can define the Fourier matrix as

$$
F_N=\matrixx{\vec{\overline{f}}_0^T\\ \vdots\\ \vec{\overline{f}}_{N-1}^T}=\matrixx{\vec{f}_0^T\\ \vec{f}_{N-1}^T\\ \vdots\\ \vec{f}_1^T}

$$

The discrete Fourier transform of $\vec{x}$ is given by

$$
\mathrm{DFT}(\vec{x})=F_N\vec{x}

$$

Ex: Compute $\mathrm{DFT}(\vec{x})$ for $\vec{x}=\matrixx{1 & 2 & 0 & 1}^T$

$$
\begin{aligned}
    &N=4\\
    &\vec{f}_0=\matrixx{1\\1\\1\\1},\ \vec{f}_1=\matrixx{1\\ i\\-1\\ -i},\ \vec{f}_2=\matrixx{1\\-1\\1\\-1},\ \vec{f}_3=\matrixx{1\\-i\\-1\\ i}\\
    &F_4=\matrixx{1 & 1 & 1 & 1\\ 1 & -i & -1 & i\\ 1 & -1 & 1 & -1\\ 1 & i & -1 & -i}\\
    &\mathrm{DFT}(\vec{x})=F_4\vec{x}=\matrixx{4\\ 1-i\\ -2\\ 1+i}
\end{aligned}

$$

The Fourier matrix has the property

$$
F_NF_N^T=NI

$$

and

$$
F_N^{-1}=\frac{1}{N}\overline{F}_N^T

$$

This implies that $\frac{1}{\sqrt{N}}F_N$ is a unitary matrix.

A sinusoid can be expressed as a vector of the form $\vec{x}=A\cos(2\pi k\vec{t}+\phi)$ where $A$ is the amplitude, $k$ is the frequency, and $\phi$ is the phase shift.

$$
\vec{x}=A\cos(2\pi k \vec{t}+\phi)=\matrixx{A\cos(\phi)\\ A\cos\brround{2\pi k\frac{1}{N}+\phi}\\ A\cos\brround{2\pi k\frac{2}{N} + \phi}\\ \vdots\\ A\cos\brround{2\pi k\frac{N-1}{N}+\phi}}

$$

Ex:

$$
 \vec{x}=2\cos\brround{4\pi \vec{t}+\frac{\pi}{2}}=\matrixx{0\\-2\\0\\2\\0\\-2\\0\\2} 

$$

We can easily express sinusoids using the Fourier basis. For a sinusoid $\vec{x}=A\cos(2\pi k\vec{t}+\phi)$ with $0<k<N$, we can write

$$
\mathrm{DFT}(\vec{x})=\frac{AN}{2}e^{i\phi}\vec{e}_k+\frac{AN}{2}e^{-i\phi}\vec{e}_{N-k}

$$

For $k=0$, $\mathrm{DFT}(\vec{x})=AN\vec{e}_0$
We can use the DFT to write the input signal as a sum of sinusoids:

- Look at the entry at index $k$ ($0\leq k\leq \frac{N}{2}$)
- If the number is nonzero, include a sinusoid with frequency $k$.
- The modulus divided by $\frac{N}{2}$ gives the amplitude of that sinusoid.
- The argument gives the phase shift.
- Entries at index 0 and $\frac{N}{2}$ (if $N$ is even) are a bit special. Both are always real numbers, and the amplitude is given by the modulus divided by $N$ instead
- If positive amplitude then $\phi=0$ and if negative amplitude, $\phi=\pi$
