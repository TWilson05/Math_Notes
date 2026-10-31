# Matrices

<!-- Source: [Sections/Linear_Algebra/Matrices.tex](../../Sections/Linear_Algebra/Matrices.tex) -->

## Matrix Operations

$$
\matrixx{a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots& \\a_{m1}&a_{m2}& &a_{mn}}=\matrixx{a_{ij}}_{m\times n}

$$

*$m$ represents the number of rows and $n$ represents the number of columns. $ij$ represents the current subscripts.
For a matrix $A$ to multiply a matrix $B$, the number of columns of $A$ must match the number of rows of $B$. Ex: $A_{4\times2}B_{2\times3}$ is allowed because the bottom middle numbers are both $2$.
The method for matrix multiplication, $AB$, is to dot the rows of $A$ with the columns of $B$

$$
\begin{aligned}
    \text{Ex: }&\matrixx{2&1\\1&2}\matrixx{1&0&5\\2&3&1}\\
    &=\matrixx{2+2&0+3&2\cdot5+1\\1+2\cdot2&0+2\cdot3&5+2}\\
    &=\matrixx{4&3&11\\5&6&7}
\end{aligned}

$$

*note that in general, $AB\neq BA$
A matrix of particular interest is the identity matrix. Multiplying by this matrix is the same as multiplying by 1.

$$
I=\matrixx{1&0&\cdots&0\\0&1&\cdots&0\\\vdots&\vdots&\ddots& \\0&0& &1}

$$

Transpose of a Matrix:
The transpose is an operation that makes the rows become columns and the columns become rows and is expressed as $A^T$.

$$
\begin{aligned}
    \text{Ex: }&\text{ if }A=\matrixx{1&2\\3&4\\5&6}\text{ then }A^T=\matrixx{1&3&5\\2&4&6}
\end{aligned}

$$

If $A=A^T$ then we consider $A$ to be a symmetric matrix.
Properties of the transpose:

$$
\begin{aligned}
    &\brround{A^T}^T=a\\
    &\brround{A+B}^T=A^T+B^T\\
    &\brround{sA}^T=sA^T\\
    &\brround{AB}^T=B^TA^T
\end{aligned}

$$

## Linear Transformations

We can express vectors as matrices: A $m\times 1$ matrix is a column vector and a $1\times n$ matrix is a row vector.
In the case of column vectors, we can multiply them by a matrix and get out another vector.

$$
\matrixx{a_{11}&a_{12}\\a_{21}&a_{22}}\matrixx{x_1\\x_2}=\matrixx{a_{11}x_1+a_{12}x_2\\a_{21}x_1+a_{22}x_2}=\matrixx{b_1\\b_2}

$$

$$
A\vec{x}=\vec{b}

$$

We can think of this matrix $A$ as some function applied to $\vec{x}$. $\vec{f}(\vec{x})=A\vec{x}=\vec{b}$
This is represented as

$$
T(\vec{x})=A\vec{x}=\vec{b}

$$

and has the properties that

$$
T(\vec{x}+\vec{y})=T(\vec{x})+T(\vec{y})\text{ and }T(s\vec{x})=sT(\vec{x})

$$

We can take advantage of these identities and express the transformation matrix in the form

$$
A=\matrixx{|&|& &|\\T(\vec{e}_1)&T(\vec{e}_2)&\cdots&T(\vec{e}_n)\\|&|& &|}

$$

where $\vec{e}_1=\hat{i},\,\vec{e}_2=\hat{j},\,\ldots$

$$
\begin{aligned}
    \text{Ex: }&T\brround{\matrixx{1\\0}}=\matrixx{2\\3}\text{ and }T\brround{\matrixx{1\\1}}=\matrixx{2\\1}\text{. Find }T\brround{\matrixx{3\\2}}\\
    &T(\vec{e}_1)=T\brround{\matrixx{1\\0}}=\matrixx{2\\3}\\
    &T(\vec{e}_2)=T\brround{\matrixx{1\\1}}-T\brround{\matrixx{1\\0}}=\matrixx{2\\1}-\matrixx{2\\3}=\matrixx{0\\-2}\\
    &\Ra A=\matrixx{2&0\\3&-2}\\
    &T\brround{\matrixx{3\\2}}=\matrixx{2&0\\3&-2}\matrixx{3\\2}=\matrixx{6\\5}
\end{aligned}

$$

If we have a composition of transformations, $S(\vec{x})=B\vec{x}$ and $T(\vec{x})=A\vec{x}$, then $S(T(\vec{x}))=BA\vec{x}$.
2D Rotation Matrix:

$$
\Rot_{\theta}(\vec{x})=\matrixx{\cos\theta&-\sin\theta\\\sin\theta&\cos\theta}\matrixx{x_1\\x_2}\\

$$

$$
\begin{aligned}
    \text{Ex: }\Rot_{\pi/2}=\matrixx{0&-1\\1&0}\to\Rot_{\pi/2}\matrixx{a_1\\a_2}=\matrixx{-a_2\\a_1}=\vec{a}^\perp
\end{aligned}

$$

2D Projection Matrix:

$$
\proj_{\hat{a}}(\vec{x})=\matrixx{a_1^2&a_1a_2\\a_1a_2&a_2^2}\matrixx{x_1\\x_2}

$$

where $\hat{a}$ is the unit vector of the line that the vector $\vec{x}$ is projected onto.
Proof:

$$
\begin{aligned}

```latex
    &\proj_{\hat{a}}(\vec{x})=(\vec{x}\cdot\hat{a})\hat{a}=(x_1a_1+x_2a_2)\matrixx{a_1\\a_2}=\matrixx{(x_1a_1+x_2a_2)a_1\\(x_1a_1+x_2a_2)a_2}=\matrixx{x_1a_1^2+x_2a_1a_2\\x_1a_1a_2+x_2a_2^2}\\
```

    &=\matrixx{a_1^2&a_1a_2\\a_1a_2&a_2^2}\matrixx{x_1\\x_2}
\end{aligned}

$$

We can also express the line of projection as the angle of a line.
If $\hat{a}=\brangle{\cos\theta,\sin\theta},\,\theta\in[0,2\pi)$ we can then denote $\proj_{\hat{a}}=\proj_\theta$ where

$$
\proj_\theta=\matrixx{\cos^2\theta&\cos\theta\sin\theta\\\cos\theta\sin\theta&\sin^2\theta}

$$

Ex: Find the matrix that represents the projection onto the line $y=x$.

$$
\begin{aligned}
    &\vec{a}=\brangle{1,1}\Ra \|\vec{a}\|=\sqrt{2}\\
    &\hat{a}=\brangle{\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}}\\
    &\proj_{\hat{a}}=\matrixx{\frac{1}{2}&\frac{1}{2}\\\frac{1}{2}&\frac{1}{2}}
\end{aligned}

$$

2D Reflection Matrix:
$\Reflection_{\theta}$ is the reflection across the line making an angle $\theta$ with the x-axis.

$$
\Reflection_\theta(\vec{x})=2\proj_{\theta}(\vec{x})-\vec{x}=\matrixx{\cos(2\theta)&\sin(2\theta)\\\sin(2\theta)&-\cos(2\theta)}\matrixx{x_1\\x_2}

$$

## Inverse of a Matrix

Consider a linear system $ax=b$. Its solution will be $x=a^{-1}b$. The same sort of thing can be done with matrices and we can take the inverse of a matrix.
One way to do this is using a super-augmented matrix.

$$
\matrixx{A|I}\to\matrixx{I|A}

$$

Also, it is important to note that $A^{-1}$ only exists if $\det A\neq 0$.

$$
\begin{aligned}
    \text{Ex: }&\text{Find the inverse of }\matrixx{1&1&1\\1&2&3\\1&4&9}\\
    &\augmatrix{1&1&1\\1&2&3\\1&4&9}{1&0&0\\0&1&0\\0&0&1}\to\augmatrix{1&1&1\\0&1&2\\0&3&8}{1&0&0\\-1&1&0\\-1&0&1}\to\augmatrix{1&1&1\\0&1&2\\0&0&2}{1&0&0\\-1&1&0\\2&-3&1}\\
    &\to\augmatrix{1&1&1\\0&1&2\\0&0&1}{1&0&0\\-1&1&0\\1&-\frac{3}{2}&\frac{1}{2}}\to\augmatrix{1&1&0\\0&1&0\\0&0&1}{0&\frac{3}{2}&-\frac{1}{2}\\-3&4&-1\\1&-\frac{3}{2}&\frac{1}{2}}\to\augmatrix{1&0&0\\0&1&0\\0&0&1}{3&-\frac{5}{2}&\frac{1}{2}\\-3&4&1\\1&-\frac{3}{2}&\frac{1}{2}}\\
    &A^{-1}=\matrixx{3&-\frac{5}{2}&\frac{1}{2}\\-3&4&1\\1&-\frac{3}{2}&\frac{1}{2}}
\end{aligned}

$$

Another way to find the inverse is to use the method

$$
A^{-1}=\frac{\mathrm{adj}(A)}{\det(A)}

$$

This method is more complex but can be quicker in some cases.
The adjoint of a matrix is calculated by finding the cofactors of each entry and then taking the transpose of the cofactor matrix.

$$
\adj(A)=C^T=\matrixx{C_{11}&C_{21}&C_{31}\\C_{12}&C_{22}&C_{32}\\C_{13}&C_{23}&C_{33}}

$$

where

$$
C_{ij}=(-1)^{i+j}M_{ij}

$$

$M_{ij}$ is the minor which is defined to be the determinant of the entries not in the row $i$ and column $j$.

$$
\begin{aligned}
    \text{Ex: }&\text{The minor of cell \ensuremath{32} in a 3x3 matrix, }\matrixx{a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}}\text{ is }\det\matrixx{a_{11}&a_{13}\\a_{21}&a_{23}}
\end{aligned}

$$

The cofactors are calculated similarly to how determinants are calculated.
This method leads to a handy formula for 2x2 matrices

$$
\begin{aligned}
    &A=\matrixx{a_{11}&a_{12}\\a_{21}&a_{22}}\\
    &C=\matrixx{a_{22}&-a_{21}\\-a_{12}&a_{11}}\\
    &\adj(A)=\matrixx{a_{22}&-a_{12}\\-a_{21}&a_{11}}\\
    &A^{-1}=\frac{1}{a_{11}a_{22}-a_{12}a_{21}}\matrixx{a_{22}&-a_{12}\\-a_{21}&a_{11}}
\end{aligned}

$$

Larger matrices don't have a nice formula but still use the same method.

$$
\begin{aligned}
    \text{Ex: }&A=\matrixx{1&3&1\\0&3&1\\4&2&0}\\
    &C_{11}=\detmatrix{3&1\\2&0}=2\\
    &C_{12}=-\detmatrix{0&1\\4&0}=4\\
    &C_{13}=\detmatrix{0&3\\4&2}=-12\\
    &C_{21}=-\detmatrix{3&1\\2&0}=2\\
    &C_{22}=\detmatrix{1&1\\4&0}=-4\\
    &C_{23}=-\detmatrix{1&3\\4&2}=10\\
    &C_{31}=\detmatrix{3&1\\3&1}=0\\
    &C_{32}=-\detmatrix{1&1\\0&1}=-1\\
    &C_{33}=\detmatrix{1&3\\0&3}=3\\
    &C=\matrixx{-2&4&-12\\2&-4&10\\0&-1&3}\\
    &\adj(A)=C^T=\matrixx{-2&2&0\\4&-4&-1\\-12&10&3}\\
    &\det(A)=\detmatrix{3&1\\2&0}-3\detmatrix{0&1\\4&0}+\detmatrix{0&3\\4&2}=-2+12-12=-2\\
    &A^{-1}=\frac{\adj(A)}{\det(A)}=\matrixx{1&-1&0\\-2&2&\frac{1}{2}\\6&-5&-\frac{3}{2}}
\end{aligned}

$$

One use for matrix inverses is to give an alternative way to solve systems of equations.

$$
\begin{aligned}
    \text{Ex: }&\eqnsystem{x+3y=5\\2x+4y=6}\\
    &AX=B\\
    &A^{-1}AX=A^{-1}B\\
    &X=A^{-1}B\\
    &A^{-1}=-\frac{1}{2}\matrixx{4&-3\\-2&1}\\
    &X=-\frac{1}{2}\matrixx{4&-3\\-2&1}\matrixx{5\\6}=\matrixx{-1\\2}
\end{aligned}

$$

Inverse Properties:

$$
\begin{aligned}
    &AA^{-1}=A^{-1}A=I\\
    &\brround{A^{-1}}^{-1}=A\\
    &\brround{kA}^{-1}=\frac{1}{k}A^{-1}\\
    &\brround{AB}^{-1}=B^{-1}A^{-1}\\
    &\brround{A^{-1}}^T=\brround{A^T}^{-1}
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex: }&\text{Simplify }(AB^TB)^{-1}(BB^TBA^T)^T(A^TB^{-1})^T\\
    &(B^TB)^{-1}A^{-1}(BA^T)^T(BB^T)^T(B^{-1})^TA\\
    &B^{-1}(B^T)^{-1}A^{-1}AB^TBB^T(B^{-1})^TA\\
    &B^{-1}(B^T)^{-1}B^TBA\\
    &B^{-1}BA\\
    &A
\end{aligned}

$$

## Determinants

While we know how to calculate determinants already, there are some tricks that make calculating them easier, especially larger determinants.
If $A$ is an upper or lower triangular matrix then $\det(A)$ is the product of the diagonals.
Also, $\det(A)=\det(A^T)$
We can also perform row operations on determinants to simplify them as much as possible.

- Swap Rows: $\det(B)=-\det(A)$
- Multiply a Row by a Constant, $k$: $\det(B)=k\det(A)$
- Add a Multiple of One Row to Another: $\det(B)=\det(A)$

$$
\begin{aligned}
    \text{Ex: }&\det\matrixx{1&2&-2&-7\\1&2&-1&-5\\0&3&0&-3\\-1&4&1&1}\\
    &\detmatrix{1&2&-2&-7\\1&2&-1&-5\\0&3&0&-3\\-1&4&1&1}=\detmatrix{1&2&-2&-7\\0&0&1&2\\0&3&0&-3\\-1&4&1&1}=\detmatrix{1&2&-2&-7\\0&0&1&2\\0&3&0&-3\\0&6&-1&-6}=\detmatrix{1&2&-2&-7\\0&0&1&2\\0&3&0&-3\\0&0&-1&0}\\
    &=-\detmatrix{1&2&-2&-7\\0&3&0&-3\\0&0&1&2\\0&0&-1&0}=-\detmatrix{1&2&-2&-7\\0&3&0&-3\\0&0&1&2\\0&0&0&2}=-(1)(3)(1)(2)=-6
\end{aligned}

$$

Some properties of determinants are as follows:

$$
\begin{aligned}
    &\det(A)\det(A^T)\\
    &\det(A^{-1})=\frac{1}{\det(A)}\\
    &\det(A^x)=(\det(A))^x\\
    &\det(AB)=\det(A)\det(B)\\
    &\det(kA)=k^n\det(A)\text{ where \ensuremath{n} is the matrix size}
\end{aligned}

$$

## LU Decomposition

We can express a matrix as the multiplication between a lower and upper triangular matrix, $L$ and $U$ respectively.

$$
A=LU

$$

Such that $L$ is a matrix representation of row operations and $U$ is the matrix $A$ in reduced echelon form.
A lower triangular matrix is a matrix with zeros above the diagonal:

$$
\begin{aligned}
    &\matrixx{* & & \\ * & * & \\ * & * & *\\ * & * & *}
\end{aligned}

$$

An upper triangular matrix is a matrix with zeros below the diagonal:

$$
\begin{aligned}
    &\matrixx{* & * & *\\ & * & *\\ & & *\\ & & }
\end{aligned}

$$

A unit triangular matrix is a square triangular matrix with ones on the diagonal
We can express the elementary row operations (as performed in Gaussian elimination) can be expressed as matrix multiplications:

- Interchange rows $i$ and $j$:
    Ex: Switch rows 2 and 4

$$
\begin{aligned}
        &\matrixx{1 &0&0&0&0\\0& 0 &0&1&0\\0&0&1&0&0\\0&1&0&0&0\\0&0&0&0& 1}
\end{aligned}

$$

    Corresponds to the identity matrix but with $a_{i,i}=a_{j,j}=0$ and $a_{i,j}=a_{j,i}=1$
- Multiply row $i$ by a scalar $k$:
    Ex: multiply row 3 by $k$

$$
\begin{aligned}
       &\matrixx{1 & & & \\ & 1 & & \\ & & k & \\ & & & 1}
\end{aligned}

$$

    Corresponds to the identity matrix but with $a_{i,i}=k$
- Add $c$ times row $j$ to row $i$:
    Ex: Add 5 times row 1 to row 4

$$
\begin{aligned}
        &E=\matrixx{1&0&0&0\\0&1&0&0\\0&0&1&0\\5&0&0&1}
\end{aligned}

$$

    Corresponds to the identity matrix but with $a_{i,j}=c$
    To find the inverse, we merely flip the sign

$$
\begin{aligned}
        &E^{-1}=\matrixx{1&0&0&0\\0&1&0&0\\0&0&1&0\\-5&0&0&1}
\end{aligned}

$$


We can multiply these matrices to a matrix $A$ to get the desired result.
If we can write a matrix in row echelon form using only row operations, it will have an $LU$ decomposition and we can express $L$ as the product of these matrix row operations.

$$
\begin{aligned}
    &E_3E_2E_1A=U\Ra A=(E_3E_2E_1)^{-1}U=E_1^{-1}E_2^{-1}E_3^{-1}U=LU
\end{aligned}

$$

Ex: Find the $LU$ decomposition

$$
\begin{aligned}
    &A=\matrixx{1 & 1 & 2\\ 3 & 1 & 3\\ -1& 3 & 5}\\
    &R_2\to -3R_1+R_2\\
    &E_1A=\matrixx{1 &0 & 0\\ -3& 1 & 0\\ 0 & 0 & 1}\matrixx{1 & 1 & 2\\ 3 & 1 & 3\\ -1& 3 & 5}=\matrixx{1 & 1 & 2\\ 0 & -2 & -3\\ -1 & 3 & 5}\\
    &R_3\to R_1+R_3\\
    &E_2(E_1A)=\matrixx{1 & 0 & 0\\ 0 & 1 & 0\\ 1 & 0 & 1}\matrixx{1 & 1 & 2\\ 0 & -2 & -3\\ -1 & 3 & 5}=\matrixx{1 & 1 & 2\\ 0 & -2 & -3\\ 0 & 4 & 7}\\
    &R_3\to 2R_2+R_3\\
    &E_3(E_2E_1A)=\matrixx{1 &0 & 0\\ 0 & 1 & 0\\ 0 & 2 & 1}\matrixx{1 & 1 & 2\\ 0 & -2 & -3\\ 0 & 4 & 7}=\matrixx{1 & 1& 2\\ 0 & -2 & -3\\ 0 & 0 & 1}=U\\
    &L=E_1^{-1}E_2^{-1}E_3^{-1}=\matrixx{1 &0 & 0\\ 3& 1 & 0\\ 0 & 0 & 1}\matrixx{1 & 0 & 0\\ 0 & 1 & 0\\ -1 & 0 & 1}\matrixx{1 &0 & 0\\ 0 & 1 & 0\\ 0 & -2 & 1}=\matrixx{1 & 0 & 0\\ 3 & 1 & 0\\ -1 & -2 & 1}\\
    &A=LU=\matrixx{1 & 0 & 0\\ 3 & 1 & 0\\ -1 & -2 & 1}\matrixx{1 & 1& 2\\ 0 & -2 & -3\\ 0 & 0 & 1}
\end{aligned}

$$

In order to receive a lower triangular matrix we require that $i<j$ for where we add $i$ times row $j$ to row $i$.
We are not always able to find an $LU$ decomposition. If we interchange row, we can come up with a $PLU$ decomposition where $P$ is a permutation matrix.
If we want to solve a linear system, $A\vec{x}=\vec{b}$, using $LU$ decomposition, we would use the following method:

$$
\begin{aligned}
    &A\vec{x}=LU\vec{x}=\vec{b}\\
    &\text{Set }U\vec{x}=\vec{y}\\
    &\text{Solve }L\vec{y}=\vec{b}\text{ for }\vec{y}\\
    &\text{Solve }U\vec{x}=\vec{y}\text{ for }\vec{x}
\end{aligned}

$$

Some properties of $LU$ decomposition:

- $\rank(A)=\rank(U)$
- $\det(A)=\det(U)$ where $A$ is a square matrix

## Error Analysis

The norm of a matrix (operator norm) is given by

$$
\|A\|=\max_{\vec{x}\neq0}\brcurly{\frac{\|A\vec{x}\|}{\|\vec{x}\|}}=\max\{\|A\hat{x}\|\}

$$

If $D$ is a diagonal matrix with entries $d_i$ then $\|D\|=\max\limits_i\brcurly{|d_i|}$
For an inverse matrix, the norm is given by

$$
\|A^{-1}\|=\frac{1}{\min\brcurly{\|A\hat{x}\|}}

$$

and similarly, if $D$ is diagonal, $\|D^{-1}\|=\frac{1}{\min\limits_i\brcurly{|d_i|}}$
The norm of a matrix is the maximum stretch of a unit vector by that matrix and the norm of the inverse is 1 over the maximum compression of a unit vector by the matrix.
The condition number $\cond(A)$ tells us how sensitive the solution $\vec{x}$ is to the changes in $\vec{b}$ and is defined to be

$$
\cond(A)=\|A\|\|A^{-1}\|=\frac{\max\brcurly{\|A\hat{x}\|}}{\min\brcurly{\|A\hat{x}\|}}

$$

By convention, if $\det(A)=0$ we define $\cond(A)=\infty$.
Suppose a small error, $\Delta \vec{b}$, produces a change in the solution, $\Delta \vec{x}$. We want to know how large that error will be

$$
\frac{\|\Delta \vec{x}\|}{\|\vec{x}\|}\leq\cond(A)\frac{\|\Delta\vec{b}\|}{\|\vec{b}\|}

$$

Proof:

$$
\begin{aligned}
    &A\vec{x}=\vec{b}\text{ and }A\Delta\vec{x}=\Delta\vec{b}\\
    &\|A\vec{x}\|=\|\vec{b}\|\\
    &\Delta x=A^{-1}\vec{b}\Ra \|\Delta x\|=\|A^{-1}\vec{b}\|\\
    &\|A^{-1}\Delta\vec{b}\|\|A\vec{x}\|=\|\Delta x\|\|\vec{b}\|\\
    &\|A^{-1}\|\|\Delta \vec{b}\|\|A\|\|\vec{x}\|\geq\|\Delta\vec{x}\|\|\vec{b}\|\\
    &\frac{\|\Delta\vec{x} \|}{\|\vec{x}\|}\leq\|A\|\|A^{-1}\|\frac{\|\Delta\vec{b}\|}{\|\vec{b}\|}\\
    &\frac{\|\Delta \vec{x}\|}{\|\vec{x}\|}\leq\cond(A)\frac{\|\Delta\vec{b}\|}{\|\vec{b}\|}
\end{aligned}

$$

This implies that if $\cond(A)$ is large then small changes in $\vec{b}$ may result in very large changes in $\vec{x}$.
