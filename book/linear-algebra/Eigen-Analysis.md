# Eigen-analysis

<!-- Source: [Sections/Linear_Algebra/Eigen-Analysis.tex](../../Sections/Linear_Algebra/Eigen-Analysis.tex) -->

## Eigenvalues and Eigenvectors

If we think of a matrix $A$ as a linear transformation, an eigenvector is a nonzero vector that's direction is unchanged by the transformation. This can be expressed as

$$
A\vec{v}=\lambda\vec{v}

$$

or more generally as,

$$
A^n\vec{v}=\lambda^n\vec{v}

$$

The value $\lambda$ is called the *eigenvalue* that corresponds to the given eigenvector.
To solve for these eigenvalues, we can do the following,

$$
\begin{aligned}
    &A\vec{v}=\lambda\vec{v}\\
    &A\vec{v}=\lambda I\vec{v}\\
    &A\vec{v}-\lambda I\vec{v}=0\\
    &(A-\lambda I)\vec{v}=0\\
    &\Ra \det(A-\lambda I)=0
\end{aligned}

$$

To then find the eigenvectors, we can solve the homogeneous system for each $\lambda_i$ formed by $(A-\lambda_i I)\vec{v}=0$
This will give a solution space of a line for $\vec{v}_i$. Because we only care about the direction of the eigenvectors, we can take the simplest eigenvector.

$$
\begin{aligned}
    \text{Ex: }&\text{Compute eigenvectors for the matrix }A=\matrixx{2&1\\1&2}\\
    &\det(A-\lambda I)=\det\matrixx{2-\lambda&1\\1&2-\lambda}=(2-\lambda)(2-\lambda)-1=\lambda^2-4\lambda+3=(\lambda-3)(\lambda-1)=0\\
    &\lambda_1=1,\,\lambda_2=3\\
    &\lambda_1:\,A-\lambda_1I=\matrixx{1&1\\1&1}\to\matrixx{1&1\\0&0}\Ra x_1+x_2=0\Ra x_1=-x_2\Ra \eqnsystem{x_1=-t\\x_2=t}\\
    &\vec{v}_1=\brsquare{1,-1}^T\\
    &\lambda_2:\,A-\lambda_2 I=\matrixx{-1&1\\1&-1}\to\matrixx{-1&1\\0&0}\Ra -x_1+x_2=0\Ra x_1=x_2\Ra \eqnsystem{x_1=t\\x_2=t}\\
    &\vec{v}_2=\brsquare{1,1}^T
\end{aligned}

$$

The eigenvectors of a matrix also form a basis, meaning that we can express any vector in that space as a linear combination of eigenvectors. This makes eigen-analysis very helpful for computing large powers of matrices.

$$
\begin{aligned}
    &\text{Using the matrix from the above example, compute }A^{10}\matrixx{2\\3}\\
    &\matrixx{2\\3}=c_1\vec{v}_1+c_2\vec{v}_2=c_1\matrixx{1\\-1}+c_2\matrixx{1\\1}\\
    &\matrixx{1&1\\-1&1}\matrixx{c_1\\c_2}=\matrixx{2\\3}\\
    &\augmatrix{1&1\\-1&1}{2\\3}\to\augmatrix{1&1\\0&2}{2\\5}\to\augmatrix{1&1\\0&1}{2\\\frac{5}{2}}\to\augmatrix{1&0\\0&1}{-\frac{1}{2}\\\frac{5}{2}}\\
    &\matrixx{c_1\\c_2}=\matrixx{-\frac{1}{2}\\\frac{5}{2}}\\
    &\matrixx{2\\3}=-\frac{1}{2}\vec{v}_1+\frac{5}{2}\vec{v}_2\\
    &A^{10}\matrixx{2\\3}=A^{10}\brround{-\frac{1}{2}\vec{v}_1+\frac{5}{2}\vec{v}_2}=A^{10}\brround{-\frac{1}{2}\vec{v}_1}+A^{10}\brround{\frac{5}{2}\vec{v}_2}\\
    &\text{recall }A^n\vec{v}=\lambda^n\vec{v}\\
    &A^{10}\matrixx{2\\3}=-\frac{1}{2}(1^{10}\vec{v}_1)+\frac{5}{2}(3^{10}\vec{v}_2)=\matrixx{-\frac{1}{2}+\frac{5}{2}\cdot 3^{10}\\\frac{1}{2}+\frac{5}{2}\cdot 3^{10}}=\matrixx{147622\\147623}
\end{aligned}

$$

A handy method for finding/checking eigenvalues is to use the trace and determinant of the matrix. (Trace is the sum of the diagonal elements)

$$
\trace(A)=\sum_{i=1}^n\lambda_i

$$

$$
\det(A)=\prod_{i=1}^n\lambda_i

$$

## Complex Eigen-Analysis

If $A$ is a real matrix with complex eigenvalues then the complex eigenvalues and eigenvectors will always come in conjugate pairs.
This will also lead to the coefficients being conjugate pairs and allows us to express these conjugate pairs as,

$$
2\Re(c_i\lambda_i^n\vec{v}_i)

$$

We can do this because the imaginary components in a real matrix will always cancel.

$$
\begin{aligned}
    \text{Ex: for the matrix }A=\matrixx{0&0&3\\1&0&-1\\0&1&3}\text{ compute }A^{13}\matrixx{1\\0\\0}
\end{aligned}

$$

$$
\begin{aligned}
    &\det(A-\lambda I)=\det\matrixx{-\lambda&0&3\\1&-\lambda&-1\\0&1&3-\lambda}=-\lambda\detmatrix{-\lambda&-1\\1&3-\lambda}+3\detmatrix{1&-\lambda\\0&1}\\
    &=-\lambda(-\lambda(3-\lambda)+1)+3=-\lambda^3+3\lambda^2-\lambda+3=0\\
    &\Ra (\lambda-3)(-\lambda^2-1)=0\Ra \eqnsystem{\lambda_1=3\\\lambda_2=i\\\lambda_3=-i}\\
    &\lambda_1:\,A-3I=\matrixx{-3&0&3\\1&-3&-1\\0&1&0}\to\matrixx{1&0&-1\\0&-3&0\\0&1&0}\to\matrixx{1&0&-1\\0&1&0\\0&0&0}\\
    &\Ra \vec{v}_1=\matrixx{1&0&1}^T\\
    &\lambda_2:\,A-iI=\matrixx{-i&0&3\\1&-i&-1\\0&1&3-i}\to\matrixx{1&-i&-1\\0&1&3-i\\0&0&0}\\
    &\Ra \vec{v}_2=\matrixx{-3i&-3+i&1}^T\\
    &\therefore\,\vec{v}_3=\matrixx{3i&-3-i&1}^T\\
    &\matrixx{1\\0\\0}=c_1\vec{v}_1+c_2\vec{v}_2+c_3\vec{v}_3=c_1\matrixx{1\\0\\1}+c_2\matrixx{-3i\\-3+i\\1}+c_3\matrixx{3i\\-3-i\\1}\\
    &\matrixx{1&-3i&3i\\0&-3+i&-3-i\\1&1&1}\matrixx{c_1\\c_2\\c_3}=\matrixx{1\\0\\0}\\
    &\augmatrix{1&-3i&3i\\0&-3+i&-3-i\\1&1&1}{1\\0\\0}\leadsto\vec{c}=\matrixx{1\\-\frac{1}{20}+\frac{3}{20}i\\\-\frac{1}{20}-\frac{3}{20}i}\\
    &A^{13}\matrixx{1\\0\\0}=c_1\lambda_1^{13}\vec{v}_1+c_2\lambda_2^{13}\vec{v}_2+c_3\lambda_3^{13}\vec{v}_3=c_1\lambda_1^{13}\vec{v}_1+2\Re(c_2\lambda_2^{13}\vec{v}_2)\\
    &\Re(c_2\lambda_2^{13}\vec{v}_2)=\Re\brround{\brround{-\frac{1}{20}+\frac{3}{20}i}\matrixx{-3i\\-3+i\\1}}=\matrixx{-\frac{3}{20}\\\frac{1}{2}\\-\frac{3}{20}}\\
    &A^{13}\matrixx{1\\0\\0}=3^{13}+2\matrixx{-\frac{3}{20}\\\frac{1}{2}\\-\frac{3}{20}}=\matrixx{3^{13}-\frac{3}{10}\\1\\3^{13}-\frac{3}{10}}
\end{aligned}

$$

If $A$ has repeated eigenvalues, it may or may not have a basis of eigenvectors. However, if $A$ is symmetric ($A=A^T$), it always has a basis of eigenvectors, even if eigenvalues are repeated, and all eigenvalues are real. This introduces the idea of eigenspaces.

## Eigenspaces

The eigenvalues of a matrix $A$ are the roots of the characteristic polynomial $c_A(\lambda)$. The eigenvalues are given by

$$
\det(A-\lambda I)=0

$$

If $\lambda$ is an eigenvalue of $A$ then the *eigenspace* for $\lambda$ is

$$
E_\lambda=\brcurly{\vec{v}\in\R^n:\ A\vec{v}=\lambda\vec{v}}=\Null(A-\lambda I)

$$

If we write the characteristic polynomial as

$$
\begin{aligned}
    c_A(x)=(x-\lambda_1)^{\alpha_1}(x-\lambda_2)^{\alpha_2}\cdots(x-\lambda_k)^{\alpha_k}
\end{aligned}

$$

then the value $\alpha_i$ is called the *algebraic multiplicity* of $\lambda_i$.
We can also define the *geometric multiplicity* of $\lambda_i$ to be $d_i$ which is the dimension of the eigenspace:

$$
d_i=\dim(E_{\lambda_i})=\dim(\Null(A-\lambda_iI))

$$

We will always have that the geometric multiplicity is less than or equal to the algebraic multiplicity

$$
d_i\leq\alpha_i

$$

The eigenvalue is called *defective* if $d_i<\alpha_i$
Ex:

$$
\begin{aligned}
    &A=\matrixx{5 & 1\\ -1 & 3}\\
    &\det(A-\lambda I)=\detmatrix{5-\lambda & 1\\ -1 & 3-\lambda}=(5-x)(3-x)+1=x^2-8x+16=(x-4)^2\Ra \lambda=4\\
    &\alpha_1=2\\
    &E_{\lambda}=\Null(A-4I)=\matrixx{1 & 1\\ -1 & -1}\to\matrixx{1 & 1\\ 0 & 0}\Ra \vec{v}=t\matrixx{-1\\1}\Ra E_\lambda=\spann\brcurly{\matrixx{-1\\1}}\\
    &d_1=1\\
    &d_1<\alpha_1\Ra \text{\ensuremath{A} is a defective matrix}
\end{aligned}

$$

Properties:

- An $n\times n$ matrix always has $n$ eigenvalues when counted with multiplicities. $\sum\limits_{i=1}^k\alpha_i=n$
- Every eigenvalue has at least one eigenvector, so $1\leq\dim(E_{\lambda_i})\leq \alpha_i$

## Diagonalization

If $A$ is an $n\times n$ matrix, there exists an invertible matrix $P$ and a diagonal matrix $D$ such that

$$
A=PDP^{-1}

$$

If $A$ is diagonalizable, then the columns of $P$ are eigenvectors of $A$ and the entries of $D$ are corresponding eigenvalues.

$$
\begin{aligned}
    &AP=PD=\matrixx{\vec{v}_1 & \cdots & \vec{v}_n}\matrixx{\lambda_1 & & \\ & \ddots & \\ & & \lambda_n}
\end{aligned}

$$

Ex:

$$
\begin{aligned}
    &A=\matrixx{1 & 3\\ 2 & 2},\ \begin{matrix}\lambda_1=4 & E_{\lambda_1}=\spann\brcurly{\matrixx{1\\1}}\\ \lambda_2 = -1 & E_{\lambda_2}=\spann\brcurly{\matrixx{-3\\2}}\end{matrix}\\
    &AP=PD=\matrixx{1 & -3\\ 1 & 2}\matrixx{4 & 0\\ 0 & -1}\\
    &A=\matrixx{1 & -3\\ 1 & 2}\matrixx{4 & 0\\ 0 & -1}\matrixx{1 & -3\\ 1 & 2}^{-1}
\end{aligned}

$$

Note that the diagonalization is not unique - we can switch the order of our eigenvalues/eigenvectors as long as we're consistent.
Also note that a matrix is only diagonalizable if $A$ has $n$ linearly independent eigenvectors. This is identical to saying that the algebraic and geometric multiplicities are equal for all eigenvalues of $A$.
Properties of real symmetric matrices:

- $A$ has only real eigenvalues
- For $\lambda_1\neq\lambda_2$, $E_{\lambda_1}\perp E_{\lambda_2}$
- Diagonalization is possible for symmetric matrices
- $AA^T$ and $A^TA$ are symmetric matrices

$$
\begin{aligned}
        &AA^T=PD_1P^T\\
        &A^TA=QD_2Q^T
\end{aligned}

$$


## Transition Matrices

Transition matrices, also known as random walks or probability matrices, are matrices that have every column sum to 1.
Take a 3x3 probability matrix. It will have 3 states, 1, 2, and 3 and there will be some probability that an object from one state moves to another state. The probability it goes from state $i$ to state $j$ is represented as $P_{ij}$. We can represent these probabilities in a matrix as shown

$$
P=\matrixx{P_{11}&P_{12}&P_{13}\\P_{21}&P_{22}&P_{23}\\P_{31}&P_{32}&P_{33}}

$$

We let the vector $\vec{x}^{(n)}$ be the probability that an object is in each state at the time $n$. So $x_1^{(0)}$ would be the probability it is in state 1 at time 0. Using $\vec{x}^{(0)}$ as the starting probability, we can find $\vec{x}^{(n)}$ through

$$
\vec{x}^{(n)}=P^n\vec{x}^{(0)}

$$

If $\lim\limits_{n\to\infty}P^n\vec{x}_0=\vec{p}$ for every $\vec{x}_0$, we say the transition matrix has an *equilibrium probability vector*, $\vec{p}$.
A matrix will only contain $\vec{p}$ if it has an eigenvalue $\lambda=1$. In this case, $\vec{p}$ can be found by scaling the eigenvector associated with $\lambda=1$ such that the sum of its components is 1.

$$
\begin{aligned}
    \text{Ex: }&\text{Find \ensuremath{\vec{p}} for the random walk }P=\matrixx{\frac{1}{2}&\frac{2}{3}\\\frac{1}{2}&\frac{1}{3}}\\
    &\trace(P)=\frac{5}{6}=\lambda_1+\lambda_2\\
    &\det(P)=-\frac{1}{6}=\lambda_1\lambda_2\\
    &\Ra \lambda_1=1,\,\lambda_2=-\frac{1}{6}\\
    &\lambda_1=1:\,\matrixx{-\frac{1}{2}&\frac{2}{3}\\\frac{1}{2}&-\frac{2}{3}}\to\matrixx{-\frac{1}{2}&\frac{2}{3}\\0&0}\to\matrixx{-3&4\\0&0}\to\vec{v}_1=\matrixx{4,3}^T\\
    &\sum\vec{v}_1=7\Ra\vec{p}=\frac{1}{7}\vec{v}_1\\
    &\therefore\,\vec{p}=\matrixx{\frac{4}{7}\\\frac{3}{7}}
\end{aligned}

$$

Trends of Transition Matrices:

- $|\lambda|\leq 1$ for all transition matrices
- Every transition matrix with all nonzero entries will contain $\lambda=1$
- The term with $\lambda=1$ will always tend to $\vec{p}$

## Singular Value Decomposition

We may not always be able to get the diagonalization of a matrix, however, we can always get the singular value decomposition of a matrix.

$$
A=P\Sigma Q^T

$$

where

$$
\Sigma=\matrixx{\sigma_1 & & & 0\\ & \ddots & & \vdots\\ & & \sigma_r & 0\\ 0 & \cdots & 0 & 0}

$$

Note that $\Sigma$ is a diagonal matrix that is zero-padded to be of size $m\times n$ ($\Sigma$ will always be the same size as $A$).
The values $\sigma_1\geq \sigma_2\geq\cdots\geq \sigma_r\geq 0$ are the *singular values* of $A$.
The decomposition comes from $AA^T=PD_1P^T$ and $A^TA=QD_2Q^T$.
The set  of eigenvalues for $AA^T$ and $A^TA$ are equal and contains only positive eigenvalues.
So we can write the singular values in terms of these eigenvalues of $A^TA$ or $AA^T$ as

$$
\sigma_k=\sqrt{\lambda_k}

$$

We can construct the matrix $Q$ as

$$
Q=\matrixx{\vec{q}_1 & \cdots & \vec{q}_n}_{n\times n}

$$

where $\vec{q}_1,\ldots,\vec{q}_r$ are the orthonormal eigenvectors of $A^TA$ and $\vec{q}_{r+1},\ldots,\vec{q}_n$ are found as an orthonormal basis of the nullspace of $A^TA$
We can construct the matrix $P$ as

$$
P=\matrixx{\vec{p}_1 & \cdots & \vec{p}_m}_{m\times m}

$$

where $\vec{p}_1,\ldots,\vec{p}_r$ are the orthonormal eigenvectors of $AA^T$ and $\vec{p}_{r+1},\ldots,\vec{p}_n$ are found as an orthonormal basis of the nullspace of $AA^T$.
We can solve for either $P$ or $Q$ and then quickly get the one from the other using these relationships;

$$
\vec{p}_k=\frac{1}{\sigma_k}A\vec{q}_k

$$

$$
\vec{q}_k=\frac{1}{\sigma_k}A^T\vec{p}_k

$$

Note that $P$ and $Q$ must be orthonormal. The reason we are able to find the vectors without using Gram-Schmidt is because the eigenvectors of a symmetric matrix will be orthogonal already.
Ex: Find the singular value decomposition of

$$
\begin{aligned}
    &A=\matrixx{1 & 0\\ -2 & 2\\ 0 & 1}
\end{aligned}

$$

We can choose to compute $A^TA$ or $AA^T$. Let's choose $A^TA$ so we can work with a 2x2 matrix.

$$
\begin{aligned}
    &A^TA=\matrixx{1 & -2 & 0\\ 0 & 2 & 1}\matrixx{1 & 0\\ -2 & 2\\ 0 & 1}=\matrixx{5 & -4\\ -4 & 5}
\end{aligned}

$$

Now we find the eigenvalues and construct $\Sigma$

$$
\begin{aligned}
    &\detmatrix{5-\lambda & -4\\ -4 & 5-\lambda}=0\\
    &(5-\lambda)^2-16=\lambda^2-10\lambda+9=0\Ra (\lambda-1)(\lambda-9)=0\\
    &\lambda=1,9\\
    &\sigma_1=\sqrt{9}=3,\quad \sigma_2=\sqrt{1}=1\\
    &\Sigma=\matrixx{3 & 0\\ 0 & 1\\ 0 & 0}
\end{aligned}

$$

Now we can construct $Q$.
First we find eigenvectors of $A^TA$

$$
\begin{aligned}
    &\lambda=1:\ A^TA-I=\matrixx{4 & -4\\ -4 & 4}\Ra \vec{v}_1=\matrixx{1\\1}\\
    &\Ra \vec{q}_2=\frac{1}{\sqrt{2}}\matrixx{1\\1}\\
    &\lambda=9:\ A^TA-9I=\matrixx{-4 & -4\\ -4 & -4}\Ra \vec{v}=\matrixx{-1\\1}\\
    &\Ra \vec{q}_1=\frac{1}{\sqrt{2}}\matrixx{-1\\1}\\
    &Q=\matrixx{\vec{q}_1 & \vec{q}_2}=\matrixx{-1/\sqrt{2} & 1/\sqrt{2}\\ 1/\sqrt{2} & 1/\sqrt{2}}
\end{aligned}

$$

Now we construct $P$

$$
\begin{aligned}
    &\vec{p}_1=\frac{1}{\sigma_1}A\vec{q}_1=\frac{1}{3}\matrixx{1 & 0\\ -2 & 2\\ 0 & 1}\frac{1}{\sqrt{2}}\matrixx{-1\\1}=\frac{1}{3\sqrt{2}}\matrixx{-1\\4\\1}\\
    &\vec{p}_2=\frac{1}{\sigma_2}A\vec{q}_2=\frac{1}{1}\matrixx{1 & 0\\ -2 & 2\\ 0 & 1}\frac{1}{\sqrt{2}}\matrixx{1\\1}=\frac{1}{\sqrt{2}}\matrixx{1\\0\\1}
\end{aligned}

$$

We require one more column vector for $P$ (needs to be a square matrix). This will be a basis of the nullspace of $AA^T$. Because we know that $P$ is an orthonormal matrix, we can also get it from the orthogonal complement of $\vec{p}_1$ and $\vec{p}_2$

$$
\begin{aligned}
    &\vec{p}_3\in\spann\brcurly{\vec{p}_1,\vec{p}_2}^\perp\\
    &\matrixx{-1 & 4 & 1\\ 1 & 0 & 1}\to\matrixx{1 & 0 & 1\\ 0 & 2 & 1}\to \vec{v}=\matrixx{-1\\-1/2\\1}\\
    &\vec{p}_3=\frac{1}{3}\matrixx{-2\\-1\\2}\\
    &P=\matrixx{-\frac{1}{3\sqrt{2}} & \frac{1}{\sqrt{2}} & -\frac{2}{3}\\ \frac{4}{3\sqrt{2}} & 0 & -\frac{1}{3}\\ \frac{1}{3\sqrt{2}} & \frac{1}{\sqrt{2}} & \frac{2}{3}}
\end{aligned}

$$

A nice property of the SVD is that the magnitude of $A$ is the largest singular value.

$$
\|A\|=\sigma_1

$$

Proof:

$$
\begin{aligned}
    &\|A\|=\max\|A\hat{x}\|=\max\|P\Sigma Q^T\hat{x}\|=\max\|\Sigma Q^T\hat{x}\|\\
    &\hat{y}=Q^T\hat{x}\\
    &\|A\|=\max\|\Sigma\hat{y}\|=\|\Sigma\|=\sigma_1
\end{aligned}

$$

The inverse of $\Sigma$ is given to be

$$
\Sigma^{-1}=\matrixx{\frac{1}{\sigma_1} & & \\ & \ddots & \\ & & \frac{1}{\sigma_n}}

$$

By a similar proof, we can get that the magnitude of $A^{-1}$ is

$$
\|A^{-1}\|=\frac{1}{\sigma_n}

$$

And so the condition number can be expressed as

$$
\cond(A)=\frac{\sigma_1}{\sigma_n}

$$

Another property is that the number of singular values is equal to the rank of the matrix. This comes from the fact that the $P$ and $Q$ matrices are invertible and, therefore, full rank.
The four fundamental subspaces can also be gotten from the SVD decomposition

- $\Range(A)=\spann\brcurly{\vec{p}_1,\ldots,\vec{p}_r}$
- $\Range(A)^\perp=\spann\brcurly{\vec{p}_{r+1},\ldots,\vec{p}_m}$
- $\Null(A)^\perp=\brcurly{\vec{q}_1,\ldots,\vec{q}_r}$
- $\Null(A)=\spann\brcurly{\vec{q}_{r+1},\ldots,\vec{q}_n}$

One nice use for the SVD decomposition is that we can compress data stored in a matrix by taking only the largest singular values. For example, if our matrix represents the data that displays an image, the largest singular values capture the most ``essence" of the image while the smaller singular values caputure fine details.
Normally we have

$$
A=P\Sigma Q^T=\sum_{k=1}^r\sigma_k\vec{p}_k\vec{q}_k^T

$$

The compressed form of the matrix can be written as

$$
A\approx \sum_{k=1}^s\sigma_k\vec{p}_k\vec{q}_k^T,\quad\quad 1\leq s\leq r

$$

## Principal Component Analysis

Principal component analysis (PCA) looks at a matrix of data and will create a basis of vectors that capture the most information from the data. The fist basis vector (or weight vector) will be projected in the direction that has the largest standard deviation in the data. The second weight vector will be perpendicular to the first one and projected in the direction of the next most standard deviation and so on.
For our computations, we can assume that the data will be normalized: $\sum\limits_{k=1}^n\vec{x}_k=\vec{0}$
We wish to find the vector, $\vec{w}_1$ which captures the most variance in the data. This will be the unit vector $\vec{w}_1$ which maximizes

$$
\sum_{k=1}^n\|\proj_{\vec{w}_1}(\vec{x}_k)\|=\sum_{k=1}^n\brangle{\vec{x}_k,\vec{w}_1}^2=\|X\vec{w_1}\|

$$

where $X$ is called the data matrix

$$
X=\matrixx{\vec{x}_1^T\\ \vdots\\\vec{x}_n^T}

$$

$\vec{w}_1$ is called the first weight vector. More generally, given the weight vectors $\vec{w}_1,\ldots,\vec{w}_{k-1}$, the $k$th weight vector $\vec{w}_k$ is the weight vector which maximizes $\|X_k\vec{w}_k\|^2$ where $X_k$ is the projection of the data matrix onto $\spann\brcurly{\vec{w}_1,\ldots,\vec{w}_k}^\perp$

$$
X_k=X-\sum_{i=1}^{k-1}X\vec{w}_i\vec{w}_i^T

$$

We can say that the weight vectors are right singular vectors of $X$ which means that $\vec{w}_k=\vec{q}_k$ in the SVD decomposition.
For general $k$, we can show that

$$
X_k=P\matrixx{0 & & & & & \\ & \ddots & & & & \\ & & 0 & & & \\ & & & \sigma_k & & \\ & & & & \ddots & \\ & & & & & \sigma_p}Q^T

$$

So the largest remaining singular value is $\sigma_k$ and $\|X_k\vec{w}_k\|^2$ is maximum when $\vec{w}_k=\vec{q}_k$. Using this, we are able to find the weight vectors for a given data matrix.
Ex: Find weight vectors for the data $(-2,2),(-1,1),(0,-1),(1,2),(2,0)$

$$
\begin{aligned}
    &X=\matrixx{-2&-2\\-1&1\\0&-1\\1&2\\2&0}\\
    &X^TX=\matrixx{10 & 5\\ 5& 10}\\
    &\leadsto \lambda=15,5\\
    &\lambda=15:\ \matrixx{-5&5\\5&-5}\Ra \vec{v}=\matrixx{1\\1}\Ra \vec{w}_1=\frac{1}{\sqrt{2}}\matrixx{1\\1}\\
    &\lambda=5:\ \matrixx{5&5\\5&5}\Ra \vec{v}=\matrixx{1\\-1}\Ra \vec{w}_2=\frac{1}{\sqrt{2}}\matrixx{1\\-1}
\end{aligned}

$$

## Pseudoinverse

If $A$ is invertible then we can solve $A\vec{x}=\vec{b}$ as $\vec{x}=A^{-1}\vec{b}$. For a general $A$ that isn't necessarily invertible, we can approximate the solution to $A\vec{x}=\vec{b}$ using the pseudoinverse $\vec{x}=A^+\vec{b}$.
If we consider the SVD decomposition of $A$, $A=P\Sigma Q^T$ the the SVD of $A^{-1}$ will be $A^{-1}=Q\Sigma^{-1}P^T$. The pseudoinverse of $A$ can be written as $A^+=Q\Sigma^+P^T$ where

$$
\Sigma^+=\matrixx{\frac{1}{\sigma_1} & & & 0\\ & \ddots & & \vdots\\ & & \frac{1}{\sigma_r} & 0\\ 0 & \cdots & 0 & 0}_{n\times m}

$$

If $A$ is invertible then $A^+=A^{-1}$
The pseudoinverse has the property that

- $AA^+A=A$ and $A^+AA^+=A^+$

The pseudoinverse also gives a very simple solution to the least squares approximation.
$\vec{x}=A^+\vec{b}$ solves the least squares problem $A\vec{x}\approx\vec{b}$
The pseudoinverse is computed by using the SVD decomposition of $A$ and written as

$$
A^+=Q\Sigma^+ P^T

$$

where $\Sigma^+$ is the same size as $A^{-1}$

## Computing Eigenvalues

For large matrices, computing eigenvalues can be challenging as it involves solving an $n$ degree polynomial. There are many numerical methods, however, that we can use to approximate eigenvalues.

**Power method:**
An eigenvalue is dominant if $\lambda$ has an algebraic multiplicity of 1 and $|\lambda|>|\lambda_k|$ for all other eigenvalues.
We can pick out this dominant eigenvalue through iterative matrix multiplication.
We can choose a random vector $\vec{x}_0$ and repeatedly multiply it by $A$ and the result will tend toward the dominant eigenvector.

$$
\begin{aligned}
    &\vec{x}_{k+1}=A\vec{x}_k\\
    &\Ra \vec{x}_k=A^k\vec{x}_0
\end{aligned}

$$

$$
\lim_{k\to\infty}\frac{A^k\vec{x}_0}{\lambda_1^k}=c_1\vec{v}_1

$$

**Rayleigh quotient:**
Another computational method is given by the formula below:

$$
\lim_{k\to\infty}\frac{\vec{x}_k^TA\vec{x}_k}{\vec{x}_k^T\vec{x}_k}=\lambda_1

$$
