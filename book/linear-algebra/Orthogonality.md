# Orthogonality

<!-- Source: [Sections/Linear_Algebra/Orthogonality.tex](../../Sections/Linear_Algebra/Orthogonality.tex) -->

## Subspaces

Definitions:
A subset $U\in\R^n$ is a subspace if:

- $U$ contains the zero vector, $\vec{0}$
- $\vec{u}_1+\vec{u}_2\in U$ for all $\vec{u}_1,\vec{u}_2\in U$
- $c\vec{u}\in U$ for all $c\in\R,\ \vec{u}\in U$

The linear combination of vectors $\vec{u}_1,\ldots,\vec{u}_m\in\R^n$ is given by $c_1\vec{u}_1+\cdots+c_m\vec{u}_m$
The span of a set of vectors is the set of all linear combinations of them.
A set of vectors $\brcurly{\vec{u}_1,\ldots,\vec{u}_m}\subset\R^n$ forms a linearly independent set if the vectors satisfy the property $c_1\vec{u}_1+\cdots c_m\vec{u}_m=\vec{0}$ if and only if $c_1=\cdots c_m=0$
We can determine if the vectors are linearly independent by setting up a matrix where the columns are the vectors.

$$
A=\matrixx{| & & |\\ \vec{u}_1 & \cdots & \vec{u}_m\\ | & & |}

$$

If the only solution is the trivial solution, $\vec{x}=\vec{0}$ then the vectors are linearly independent.
If $U\subseteq\R^n$ is a subspace then a set of vectors $\brcurly{\vec{u}_1,\ldots,\vec{u}_m}$ forms a basis of $U$ if:

- $\brcurly{\vec{u}_1,\ldots,\vec{u}_m}$ is a linearly independent set
- $\spann\brcurly{\vec{u}_1,\ldots,\vec{u}_m}=U$

There are infinitely many different bases of a subspace $U$ but each basis of $U$ has the same number of vectors.
The dimension of $U$ is the number of vectors in a basis of $U$. We write this as $\dim(U)$
Ex: Find a basis and dimension of $U$

$$
\begin{aligned}
    &U=\spann\brcurly{\matrixx{1\\1\\1\\1},\matrixx{1\\2\\2\\1},\matrixx{1\\-1\\1\\-1},\matrixx{1\\-2\\0\\-1}}
\end{aligned}

$$

check if $\vec{u}_1,\vec{u}_2,\vec{u}_3,\vec{u}_4$ are linearly independent

$$
\begin{aligned}
    &\matrixx{1 & 1 & 1 & 1\\ 1 & 2 & -1 & -2\\ 1 & 2 & 1 & 0\\ 1 & 1 & -1 & -1}\leadsto\matrixx{1 & 1 & 1 & 1\\ 0 & 1 & -2 & -3\\ 0 & 0 & 2 & 2\\ 0 & 0 & 0 & 0}
\end{aligned}

$$

If we choose a smaller set of $\brcurly{\vec{u}_1,\vec{u}_2,\vec{u}_3}$ then we get

$$
\begin{aligned}
    &\matrixx{1 & 1 & 1\\ 0 & 1 & -2\\ 0 & 0 & 2\\ 0 & 0 & 0}\to \text{unique solution to }A\vec{c}=\vec{0}\\
    &\therefore \brcurly{\vec{u}_1,\vec{u}_2,\vec{u}_3}\text{ is a basis of }U,\ \dim(U)=3
\end{aligned}

$$

Nullspace:
Let $A$ be an $m\times n$ matrix. The nullspace of $A$ is $\Null(A)=\brcurly{\vec{x}\in\R^n:\ A\vec{x}=\vec{0}}$
What this means is that the nullspace is all the values that get mapped to $\vec{0}$ under the linear transformation of $A$.
$\Null(A)$ is a subspace of $\R^n$. This is because the nullspace is determined based on the input vectors which are elements in $\R^n$
Ex: Find a basis of $\Null(A)$

$$
\begin{aligned}
    &A=\matrixx{1 & 4 & -1 & -2\\ -2 & -6 & 2 & 8\\ 1 & 5 & -1 & 0}\\
    &\leadsto \matrixx{1 & 4 & -1 & -2\\ 0 & 2 & 0 & 4\\ 0 & 0 & 0 & 0}\\
    &x_3=s,\ x_4=t\\
    &2x_2+4t=0\Ra x_2=-2t\\
    &x_1+4x_2-s-2t=0\Ra x_1=s+10t\\
    &\vec{x}=s\matrixx{1\\0\\1\\0}+t\matrixx{10\\-2\\0\\1}\\
    &N(A)=\spann\brcurly{\matrixx{1\\0\\1\\0},\matrixx{10\\-2\\0\\1}},\ \dim(N(A))=2
\end{aligned}

$$

Range:
Let $A$ be an $m\times n$ matrix. The range of $A$ is $\Range(A)=\brcurly{\vec{y}\in\R^m:\ A\vec{x}=\vec{y},\ \vec{x}\in\R^n}$
This means that $\Range(A)$ is the span of all vectors that can result from the linear transformation of $A$.
Note: $\Range(A)$ is also called the image of $A$ of the column space of $A$.
$\Range(A)$ is a subspace of $\R^m$. This is because the range is determined by the outputs of $A\vec{x}$ which are elements in $\R^m$.
We will also have that

$$
\dim(\Range(A))=\rank(A)

$$

$$
\begin{aligned}
    &A\vec{x}=\matrixx{| & | & & |\\ \vec{a}_1 & \vec{a}_2 & \cdots & \vec{a}_n\\ | & | & & |}\matrixx{x_1\\x_2\\\vdots\\ x_n}=x_1\vec{a}_1+x_2\vec{a}_2+\cdots+x_n\vec{a}_n
\end{aligned}

$$

This means that $\Range(A)=\spann\brcurly{\vec{a}_1,\vec{a}_2,\ldots,\vec{a}_n}$
Ex: find a basis of $\Range(A)$

$$
\begin{aligned}
    &A=\matrixx{1 & 4 & -1 & -2\\ -2 & -6 & 2 & 8\\ 1 & 5 &-1 & 0}\\
    &\leadsto \matrixx{1 & 4 & -1 & -2\\ 0 & 2 & 0 & 4\\ 0 & 0 & 0 & 0}\\
    &\text{take }\vec{a}_1\text{ and }\vec{a}_2\\
    &\matrixx{1 & 4\\ -2 & -6\\ 1 & 5}\leadsto\matrixx{1 & 4\\ 0 & 2\\ 0 & 0}
\end{aligned}

$$

unique solution so $\vec{a}_1$ and $\vec{a}_2$ are linearly independent

$$
\begin{aligned}
    &\Ra R(A)=\spann\brcurly{\matrixx{1\\-2\\1},\matrixx{4\\-6\\5}}
\end{aligned}

$$

Given an $m\times n$ matrix, the Rank-Nullity theorem is given by

$$
\dim(\Range(A))+\dim(\Null(A))=n

$$

We also have that for an $LU$ decomposition of $A$ with column vectors of $L$ being $\vec{l}_1,\ldots,\vec{l}_n$ and $r=\rank(A)$ then

$$
\Range(A)=\spann\brcurly{\vec{l}_1,\ldots,\vec{l}_r}

$$

Related to $LU$ decomposition, we will have the following identities;

- $\Range(A)=\Range(L)$
- $\Null(A)=\Null(U)$
- $\Range(A^T)=\Range(U^T)$
- $\Null(A^T)=\Null(L^T)$

(note that $L$ must only be the matrix containing the first $r$ columns for these properties to hold)

## Inner Product and Orthogonality

The inner product of two vectors, $\vec{x},\ \vec{y}\in\R^n$ is defined to be

$$
\brangle{\vec{x},\vec{y}}=\sum_{k=1}^nx_ky_k=x_1y_1+x_2y_2+\cdots x_ny_n

$$

The inner product is also called the dot product, written as $\vec{x}\cdot\vec{y}$
For complex vectors, $\vec{x},\ \vec{y}\in \C^n$, we conjugate the 2nd vector in the inner product.

$$
\brangle{\vec{x},\vec{y}}=\sum_{k=1}^nx_k\bar{y}_k=x_1\bar{y}_1+\cdots x_n\bar{y}_n

$$

Some properties of the dot inner product

- $\brangle{a\vec{x}+b\vec{y},\vec{z}}=a\brangle{\vec{x},\vec{z}}+b\brangle{\vec{y},\vec{z}}$
- $\brangle{\vec{x},\vec{y}}=\brangle{\vec{y},\vec{x}}$
- $\brangle{\vec{x},\vec{x}}=\|\vec{x}\|^2\geq0$
- $\brangle{\vec{x},\vec{y}}=\|\vec{x}\|\|\vec{y}\|\cos\theta$ where $\theta$ is the angle between vectors
- $\brangle{\vec{x},\vec{y}}=\vec{x}^T\vec{y}$

A less intuitive property is that

$$
\brangle{A\vec{x},\vec{y}}=\brangle{\vec{x},A^T\vec{y}}

$$

Proof:

$$
\begin{aligned}
    &\brangle{A\vec{x},\vec{y}}=(A\vec{x})^T\vec{y}=\vec{x}^TA^T\vec{y}=\brangle{\vec{x},A^T\vec{y}}
\end{aligned}

$$

Two vectors $\vec{x},\ \vec{y}\in\R^n$ are *orthogonal* if $\brangle{\vec{x},\vec{y}}=0$
We can define an *orthogonal set* if we have $\brcurly{\vec{x}_1,\ldots,\vec{x}_m}\subseteq\R^n$ such that $\brangle{\vec{x}_i,\vec{x}_j}=0$ for all $i\neq j$
If each of these vectors in the set has magnitude 1 (set of unit vectors) then the set is considered to be *orthonormal*.
Naturally, if a set is orthogonal, then they are linearly independent.
We can say that two sets are orthogonal if $\brangle{\vec{x},\vec{y}}=0\ \forall\vec{x}\in S_1\wedge\vec{y}\in S_2$. We write this as $S_1\perp S_2$.

This idea of the inner product and orthogonality can be extended to functions as well. The vectors we're used to dealing with exist in what's called Euclidean space which is a finite dimensional vector space.
A function will have infinite inputs and so cannot be expressed in Euclidean space. What we can do instead is create a new vector space that has an inifnite dimensional product space. This is called the *Hilbert space*.
Using this, we will have an infinite sum representing the infinte input values that are contained in this vector space. This implies that the definition of the inner product will involve integration instead of differentiation.
And so the inner product between two real functions can be defined as

$$
\boxed{\brangle{f,g}=\int_{-\infty}^\infty f(x)g(x)dx}

$$

For functions that are $2\pi$ periodic, we can define the inner product over a different domain

$$
\brangle{f,g}=\int_0^{2\pi}f(x)g(x)dx

$$

Two functions are said to be orthogonal if their inner product gives 0.
Orthogonal functions are particularly useful when aiming to create a set of basis functions. In particular, trigonometric functions have some nice orthogonality properties:
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

Note that this result makes use of the fact that $\sin(kx)=0$ for where $k\in\Z$, hence why some terms appear to drop out. This also means that these specific orthogonality calculations only hold for integer values of $m$ and $n$.

## Orthogonal Complement

Def: If $U\in\R^n$ is a subspace, then the *orthogonal complement* of $U$ is the set $U^\perp=\brcurly{\vec{x}\in\R^n:\ \brangle{\vec{x},\vec{u}}=0\ \forall\vec{u}\in U}$
What this means is that the orthogonal complement of $U$ is the subspace that contains all of the vectors that are not contained in $U$ within $\R^n$.
This means that if $U\in\R^n$

$$
\dim(U)+\dim(U^\perp)=n

$$

To find $U^\perp$, we use a basis of $U$. Let $\brcurly{\vec{u}_1,\ldots,\vec{u}_m}$ be a basis of $U$. A vector $\vec{x}$ is an element of $U^\perp$ if the inner product with $\vec{x}$ and every basis vector is 0

$$
\begin{aligned}
    &\vec{x}\in U^\perp\Ra \eqnsystem{\brangle{\vec{x},\vec{u}_1}=0\\ \vdots\\ \brangle{\vec{x},\vec{u}_m}=0}=\eqnsystem{\vec{u}_1^T\vec{x}=0\\ \vdots\\ \vec{u}_m^T\vec{x}=0}=\matrixx{\vec{u}_1^T\\ \vdots\\ \vec{u}_m^T}\vec{x}=0
\end{aligned}

$$

If we define

$$
\begin{aligned}
    &A=\matrixx{\vec{u}_1 & \cdots & \vec{u}_m}
\end{aligned}

$$

Then the transpose is

$$
\begin{aligned}
    &A^T=\matrixx{\vec{u}_1^T\\ \vdots\\ \vec{u}_m^T}
\end{aligned}

$$

And so we get that $\vec{x}\in U^\perp$ iff $A^T\vec{x}=0$. This implies that $U^\perp=\Null(A^T)$. If you notice that $U$ in this case is the same as the range of $A$, we can write a more general formula

$$
\Range(A)^\perp=\Null(A^T)

$$

We can rearrange this formula to get 3 more identities:

$$
\Null(A)=\Range(A^T)^\perp

$$

$$
\Null(A)^\perp=\Range(A^T)

$$

$$
\Range(A)=\Null(A^T)^\perp

$$

Note that the dimensions of these fundamental subspaces will be as follows for an $m\times n$ matrix $A$.

$$
\dim(\Range(A))+\dim(\Range(A)^\perp)=n

$$

$$
\dim(\Null(A))+\dim(\Null(A)^\perp)=m

$$

(the nullspace corresponds to the dimension of the input of $A$ and the range corresponds to the dimension of the output of $A$)
Ex: Find a basis for $U^\perp$ where

$$
\begin{aligned}
    &U=\spann\brcurly{\matrixx{1\\2\\3},\matrixx{-2\\1\\-1},\matrixx{3\\1\\4}}\\
    &U^\perp=\Null(A^T)\text{ where }A^T=\matrixx{1 & 2 & 3\\ -2 & 1 & -1\\ 3 & 1 &4}\\
    &\text{Find all }\ensuremath{\vec{x}}\text{ such that }A^T\ensuremath{\vec{x}}=0\\
    &\augmatrix{1 & 2& 3\\ -2 & 1 & -1\\ 3 & 1 & 4}{0\\0\\0}\to\matrixx{1 & 2 & 3\\ 0 & 5 & 5\\ 0 & 0 & 0}\Ra \vec{x}=t\matrixx{-1\\-1\\1}\\
    &U^\perp=\spann\brcurly{\matrixx{-1\\-1\\1}}
\end{aligned}

$$

Ex2: Find the dimensions of $\Null(A),\Range(A),\Null(A^T),\Range(A^T)$

$$
\begin{aligned}
    &A=\matrixx{1 &0 & 0\\ 1& 1 & 0\\ 1& -2 & 1}\matrixx{2 & 3& 1 & 4\\ 0 & -1 & 0 & 1\\ 0 & 0 & 0 &2}\\
    &\dim(A)=\rank(U)=3=\dim(\Range(A))\\
    &\Range(A)\in\R^3\\
    &\Null(A^T)=\Range(A)^\perp\\
    &\dim(\Range(A)^\perp)+\dim(\Range(A))=3\Ra \dim(\Range(A)^\perp)=\dim(\Null(A^T))=0\\
    &\dim(\Null(A))+\dim(\Range(A))=4\Ra \dim(\Null(A))=1\\
    &\Null(A)^\perp=\Range(A^T)\\
    &\Null(A)^\perp=\Range(A^T)\\
    &\dim(\Null(A))+\dim(\Null(A)^\perp)=4\Ra \dim(\Null(A)^\perp)=3\\
    &\Null(A)^\perp=\Range(A^T)\Ra \dim(\Range(A^T))=3
\end{aligned}

$$

A handy identity is that $\rank(A)=\rank(A^T)$
Proof:

$$
\begin{aligned}
    &\rank(A)=\dim(\Range(A))=n-\dim(\Null(A))\\
    &\Null(A)\in\R^n\\
    &\dim(\Null(A))+\dim(\Null(A)^\perp)=n\\
    &\dim(\Null(A))=n-\dim(\Null(A)^\perp)\\
    &\Null(A)^\perp=\Range(A^T)\\
    &\dim(\Null(A))=n-\dim(\Range(A^T))\\
    &\rank(A)=n-\brround{n-\dim(\Range(A^T))}\\
    &\rank(A)=\rank(A^T)\ \square
\end{aligned}

$$

## Orthogonal Projection

The projection of a vector $\vec{x}\in\R^n$ onto another vector $\vec{u}\in\R^n$ is given by

$$
\proj_{\vec{u}}(\vec{x})=\frac{\brangle{\vec{x},\vec{u}}}{\brangle{\vec{u},\vec{u}}}\vec{u}

$$

We can write $\proj_{\vec{u}}(\vec{x})$ as a matrix multiplication:

$$
\begin{aligned}
    &\proj_{\vec{u}}(\vec{x})=\frac{\brangle{\vec{x},\vec{u}}}{\brangle{\vec{u},\vec{u}}}\vec{u}=\frac{1}{\brangle{\vec{u},\vec{u}}}\vec{u}\brangle{\vec{x},\vec{u}}=\frac{1}{\|\vec{u}\|^2}\vec{u}\vec{u}^T\vec{x}=P\vec{x}\\
    &P=\frac{1}{\|\vec{u}\|^2}\vec{u}\vec{u}^T=\frac{1}{\|\vec{u}\|^2}\matrixx{u_1u_1 & \cdots & u_1u_n\\ \vdots & \ddots & \vdots\\ u_nu_1 & \cdots & u_nu_n}
\end{aligned}

$$

Properties of the projection matrix

- $P^T=P$ (symmetric matrix)
- $P^2=P$ (eigenpotent matrix)
- $\rank(P)=1$

An *orthogonal basis* of $U$ is a basis of $U$ that consists of orthogonal vectors. If these vectors all have a magnitude of 1, then it is called an *orthonormal basis*.
To find an orthogonal basis, we can use the Gram-Schmidt algorithm. The algorithm produces the following vectors from the basis vectors $\brcurly{\vec{u}_1,\ldots,\vec{u}_m}$

$$
\begin{aligned}
    &\vec{v}_1=\vec{u}_1\\
    &\vec{v}_2=\vec{u}_2-\proj_{\vec{v}_1}(\vec{u}_2)\\
    &\vec{v}_3=\vec{u}_3-\proj_{\vec{v}_1}-\proj_{\vec{v}_2}(\vec{u}_2)\\
    &\vdots\\
    &\vec{v}_m=\vec{u}_m-\proj_{\vec{v}_1}(\vec{u}_m)-\cdots-\proj_{\vec{v}_{m-1}}(\vec{u}_m)
\end{aligned}

$$

The vectors $\brcurly{\vec{v}_1,\ldots,\vec{v}_m}$ will form an orthogonal basis of $U$.
We can also normalize the vectors, such that $\vec{w}_i=\frac{\vec{v}_i}{\|\vec{v}_i\|}$ so that $\brcurly{\vec{w}_1,\ldots,\vec{w}_m}$ forms an orthonormal basis of $U$.
Ex: Construct an orthonormal basis of

$$
\begin{aligned}
    &U=\spann\brcurly{\matrixx{1\\0\\1\\0},\matrixx{2\\1\\0\\-2},\matrixx{3\\5\\-1\\1}}\subseteq\R^4\\
    &\vec{v}_1=\vec{u}_1=\matrixx{1\\0\\1\\0}\\
    &\vec{v}_2=\vec{u}_2-\proj_{\vec{v}_1}(\vec{u}_2)=\matrixx{2\\1\\0\\-2}-\frac{\brangle{\vec{u}_2,\vec{v}_1}}{\brangle{\vec{v}_1,\vec{v}_1}}\vec{v_1}=\matrixx{2\\1\\0\\-2}-\frac{2}{2}\matrixx{1\\0\\1\\0}=\matrixx{1\\1\\-1\\-2}\\
    &\vec{v}_3=\vec{u}_3-\frac{\brangle{\vec{u}_3,\vec{v}_2}}{\brangle{\vec{v}_2,\vec{v}_2}}\vec{v}_2-\frac{\brangle{\vec{u}_3,\vec{v}_1}}{\brangle{\vec{v}_1,\vec{v}_1}}\vec{v}_1=\matrixx{3\\5\\-1\\1}-\frac{7}{7}\matrixx{1\\1\\-1\\-2}-\frac{2}{2}\matrixx{1\\0\\1\\0}=\matrixx{1\\4\\-1\\3}\\
    &\brcurly{\vec{v}_1,\vec{v}_2,\vec{v}_3}\text{ forms an orthogonal basis}\\
    &\text{normalize to get}\\
    &\brcurly{\frac{1}{\sqrt{2}}\matrixx{1\\0\\1\\0},\frac{1}{\sqrt{7}}\matrixx{1\\1\\-1\\-2},\frac{1}{3\sqrt{3}}\matrixx{1\\4\\-1\\3}}
\end{aligned}

$$

If $\brcurly{\vec{u}_1,\ldots,\vec{u}_m}$ forms an orthonormal basis of $U\subseteq\R^n$ then the orthogonal projection of $\vec{x}\in\R^n$ onto the subspace $U$ is given by the sum of the projections onto the basis vectors

$$
\proj_{U}(\vec{x})=\sum_{i=1}^m\proj_{\vec{u}_i}(\vec{x})=\sum_{i=1}^m\frac{\brangle{\vec{x},\vec{u}_i}}{\brangle{\vec{u}_i,\vec{u}_i}}\vec{u}_i

$$

The projection matrix is given by $\proj_U(\vec{x})=P\vec{x}$ where

$$
P=\sum_{i=1}^m\frac{1}{\|\vec{u}_i\|^2}\vec{u}_i\vec{u}_i^T

$$

This projection matrix will have the properties

- $P^T=P$
- $P^2=P$
- $\rank(P)=\dim(U)$

We can also write $P$ as $Q_1Q_1^T$.
If $U\subseteq\R^n$ is a subspace then any $\vec{x}\in\R^n$ can be written as $\vec{x}=\vec{u}+\vec{v}$ for some $\vec{u}\in U$ and $\vec{v}\in U^\perp$.
This means that we can write any vector as the sum of orthogonal projections

$$
\vec{x}=\proj_{U}(\vec{x})+\proj_{U^\perp}(\vec{x})

$$

This allows us to express the projection onto the orthogonal complement of $U$ as

$$
P^\perp=P-I

$$

Ex: Find the projection matrix that projects onto $U$ for where

$$
\begin{aligned}
    &U=\spann\brcurly{\matrixx{1\\1\\1\\1},\matrixx{1\\2\\0\\1},\matrixx{-1\\0\\1\\1}}\\
    &\text{find an orthonormal basis of \ensuremath{U}}\\
    &\vec{v}_1=\vec{u}_1=\matrixx{1\\1\\1\\1}\\
    &\vec{v}_2=\vec{u}_2-\frac{\brangle{\vec{u}_2,\vec{v}_1}}{\brangle{\vec{v}_1,\vec{v}_1}}\vec{v_1}=\matrixx{1\\2\\0\\1}-\frac{4}{4}\matrixx{1\\1\\1\\1}=\matrixx{0\\1\\-1\\0}\\
    &\vec{v}_3=\vec{u}_3-\frac{\brangle{\vec{u}_3,\vec{v}_1}}{\brangle{\vec{v}_1,\vec{v}_1}}\vec{v}_1-\frac{\brangle{\vec{u}_3,\vec{v}_2}}{\brangle{\vec{v}_2,\vec{v}_2}}\vec{v}_2=\matrixx{-1\\0\\1\\1}-\frac{1}{4}\matrixx{1\\1\\1\\1}-\frac{-1}{2}\matrixx{0\\1\\-1\\0}=\matrixx{-\frac{5}{4}\\\frac{1}{4}\\\frac{1}{4}\\\frac{3}{4}}\\
    &\Ra \brcurly{\matrixx{1\\1\\1\\1},\matrixx{0\\1\\-1\\0},\matrixx{-5\\1\\1\\3}}\text{ is an orthogonal basis}\\
    &P=\frac{1}{\|\vec{v}_1\|^2}\vec{v}_1\vec{v}_1^T+\frac{1}{\|\vec{v}_2\|^2}\vec{v}_2\vec{v}_2^T+\frac{1}{\|\vec{v}_3\|^2}\vec{v}_3\vec{v}_3^T\\
    &P=\frac{1}{4}\matrixx{1 & 1& 1 & 1\\ 1 & 1 & 1 & 1\\ 1 & 1 & 1 & 1\\ 1 & 1 & 1 & 1}+\frac{1}{2}\matrixx{0 & 0 & 0 & 0\\ 0 & 1 & -1 & 0\\ 0 & -1 & 1 & 0\\ 0 & 0 & 0 & 0}+\frac{1}{36}\matrixx{25 & -5 & -5 & -15\\ -5 & 1 & 1 & 3\\ -5 & 1 & 1 & 3\\ -15 & 3 & 3 & 9}\\
    &P=\frac{1}{36}\matrixx{34 & 4 & 4 -6\\ 4 & 28 & -8 & 12\\ 4 & -8 & 28 & 12\\ -6 & 12 & 12 & 18}
\end{aligned}

$$

This was quite computationally intensive. It may be easier in some cases to instead find $P^\perp$ and then use $P=I-P_\perp$ to get $P$.
We can say that $U=\Range(A)$ where

$$
\begin{aligned}
    &A=\matrixx{1 & 1 & -1\\ 1& 2 & 0\\ 1 & 0 & 1\\ 1 & 1 & 1}\\
    &U^\perp=\Range(A)^\perp=\Null(A^T)\\
    &A^T=\matrixx{1 & 1 & 1 &\\ 1 & 2 & 0 & 1\\ -1 & 0 & 1 & 1}\to\matrixx{1 & 1 & 1 & 1\\ 0 & 1 & -1 & 0\\ 0 & 1 & -2 & 2}\to \matrixx{1 & 1 & 1 & 1\\ 0 & 1 & -1 & 0\\ 0 & 0 & 3 & 2}\\
    &x_4=t\Ra x_3=-\frac{2}{3}t\Ra x_2=-\frac{2}{3}t\Ra x_1=\frac{1}{3}t\\
    &\vec{x}=\frac{t}{3}\matrixx{1\\-2\\-2\\3}\Ra U^\perp=\spann\matrixx{1\\-2\\-2\\3}\\
    &P_\perp=\frac{1}{\|\vec{v}_1\|^2}\vec{v}_1\vec{v}_1^T=\frac{1}{18}\matrixx{1 & -2 & -2 & 3\\ -2 & 4 & 4 & -6\\ 2 & 4 & 4 & -6\\ 3 & -6 & -6 & 9}\\
    &P=I-P_\perp=\frac{1}{18}\matrixx{17 & 2 & 2 & -3\\ 2 & 14 & -4 & 6\\ 2 & -4 & 14 & 6\\ -3 & 6 & 6 & 9}
\end{aligned}

$$

We can find the shortest distance between a vector and a subspace using projections.
The vector distance $\|\vec{x}-\proj_U(\vec{x})\|=\|\proj_{U^\perp}(\vec{x})\|$ will be the shortest distance between the vector $\vec{x}$ and the subspace $U$.
Ex: Find the shortest distance between $\vec{x}$ and $U$ for

$$
\begin{aligned}
    &\vec{x}=\matrixx{1\\1\\-2\\1}\text{ and }U=\spann\brcurly{\matrixx{1\\1\\1\\1},\matrixx{1\\2\\0\\1},\matrixx{-1\\0\\1\\1}}\\
    &\text{from the previous example, we found that}\\
    &U^\perp=\spann\brcurly{\matrixx{1\\-2\\-2\\3}}\\
    &\|\proj_{U^\perp}(\vec{x})\|=\left\|\frac{\brangle{\vec{x},\vec{w}}}{\brangle{\vec{w},\vec{w}}}\vec{w}\right\|=\brvertical{\frac{\brangle{\vec{x},\vec{w}}}{\brangle{\vec{w},\vec{w}}}}\|\vec{w}\|=\brvertical{\frac{6}{18}}\sqrt{18}=\sqrt{2}
\end{aligned}

$$

## QR Decomposition

The idea behind a QR decomposition is to form a decomposition that contains orthonormal bases of both $\Range(A)$ and $\Range(A)^\perp$.
A matrix $Q$ is orthogonal if

- $Q^TQ=I$
- $QQ^T=I$

This can more simply be written as

$$
Q^T=Q^{-1}

$$

An orthogonal matrix is square and invertible.
A matrix is orthogonal if the columns are orthonormal ($Q^TQ=I$) and the rows are orthonormal ($QQ^T=I$).
Note that the norm of an orthonormal matrix is 1:

$$
\|Q\|=1

$$

We will also have the condition number of an orthogonal matrix is 1.
Some examples of orthogonal matrices include rotations and reflections.

$$
\begin{aligned}
    &\mathrm{Rot}_\theta=\matrixx{\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta}\\
    &\mathrm{Ref}=2P-I
\end{aligned}

$$

We can write the QR decomposition of $A$ as $A=QR$, where $Q$ is an orthogonal matrix and $R$ is an upper triangular matrix.
We can do this a few different ways. One way is using Gram-Schmidt.
If we let the column vectors of $A$ be $\brcurly{\vec{a}_1,\ldots,\vec{a}_n}$ and we let $\brcurly{\vec{w}_1,\ldots,\vec{w}_n}$ be an orthonormal basis of $\Range(A)$ then we can express each $\vec{a}_k$ as the sum of its projections onto $\Range(A)$.

$$
\begin{aligned}
    &\vec{a}_1=\brangle{\vec{a},\vec{w}_1}\vec{w}_1\\
    &\vec{a}_2=\brangle{\vec{a}_2,\vec{w}_1}\vec{w}_1+\brangle{\vec{a}_2,\vec{w}_2}\vec{w}_2\\
    &\vdots\\
    &\vec{a}_n=\brangle{\vec{a}_n,\vec{w}_1}\vec{w}_1+\cdots+\brangle{\vec{a}_n,\vec{w}_n}\vec{w}_n
\end{aligned}

$$

(note that we don't need to normalize because the norm of $\vec{w}_i$ is 1)
We can write this as matrix multiplication;

$$
\begin{aligned}
    &A=\underbrace{{\matrixx{\vec{w}_1 & \cdots & \vec{w}_n}}}_{{Q_1}_{m\times n}}\underbrace{\matrixx{\brangle{\vec{w}_1,\vec{a}_1} & \brangle{\vec{w}_1,\vec{a}_2} & \cdots & \brangle{\vec{w}_1,\vec{a}_n}\\ 0 & \brangle{\vec{w}_2,\vec{a}_2} & \cdots & \brangle{\vec{w}_2,\vec{a}_n}\\ \vdots & \vdots & \ddots & \vdots\\ 0 & 0 & \cdots & \brangle{\vec{w}_n,\vec{a}_n}}}_{{R_1}_{n\times m}}
\end{aligned}

$$

$A=Q_1R_1$ is called the *thin QR decomposition* (or reduced QR) of $A$.
Ex: Find the QR decomposition of

$$
\begin{aligned}
    &A=\matrixx{1 & 3 & 1\\ 0 & 2 & 3\\ -1 & -1 & -1\\ 0 & -2 & -1}\\
    &\vec{v}_1=\vec{a}_1=\matrixx{1\\0\\-1\\0}\\
    &\vec{v}_2=\vec{a}_2-\frac{\brangle{\vec{a}_2,\vec{v}_1}}{\brangle{\vec{v}_1,\vec{v}_1}}\vec{v}_1=\matrixx{3\\2\\-1\\-2}-\frac{4}{2}\matrixx{1\\0\\-1\\0}=\matrixx{1\\2\\1\\-2}\\
    &\vec{v}_3=\vec{a}_3-\frac{\brangle{\vec{a}_3,\vec{v}_1}}{\brangle{\vec{v}_1,\vec{v}_1}}\vec{v}_1-\frac{\brangle{\vec{a}_3,\vec{v}_2}}{\brangle{\vec{v}_2,\vec{v}_2}}\vec{v}_2=\matrixx{1\\3\\1\\-1}-0\vec{v}_1-\frac{10}{10}\matrixx{1\\2\\1\\-2}=\matrixx{0\\1\\0\\1}\\
    &\text{normalize to get}\\
    &\vec{w}_1=\frac{1}{\sqrt{2}}\matrixx{1\\0\\-1\\0},\ \vec{w}_2=\frac{1}{\sqrt{10}}\matrixx{1\\2\\1\\-2},\ \vec{w}_3=\frac{1}{\sqrt{2}}\matrixx{0\\1\\0\\1}\\
    &Q_1=\matrixx{\vec{w}_1 & \vec{w}_2 & \vec{w}_3}=\matrixx{\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{10}} & 0\\ 0 & \frac{2}{\sqrt{10}} & \frac{1}{\sqrt{2}}\\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{10}} & 0\\ 0 & -\frac{2}{\sqrt{10}} & \frac{1}{\sqrt{2}}}\\
    &R_1=\matrixx{\brangle{\vec{w}_1,\vec{a}_1} & \brangle{\vec{w_1},\vec{a}_2} & \brangle{\vec{w}_3,\vec{a}_3}\\ 0 & \brangle{\vec{w}_2,\vec{a}_2} & \brangle{\vec{w}_2,\vec{a}_3}\\ 0 & 0 & \brangle{\vec{w}_3,\vec{a}_3}}=\matrixx{\sqrt{2} & 2\sqrt{2} & 0\\ 0 &\sqrt{10} & \sqrt{10}\\ 0 & 0 & \sqrt{2}}
\end{aligned}

$$

For the full QR decomposition, we continue by extending $\brcurly{\vec{w}_1,\ldots,\vec{w}_n}$ to an orthonormal basis of $\R^m$.

$$
\begin{aligned}
    &\underbrace{\vec{w}_1,\ldots,\vec{w}_n}_{\text{orthonormal basis of \ensuremath{\Range(A)}}},\underbrace{\vec{w}_{n+1},\ldots,\vec{w}_m}_{\text{orthonormal basis of \ensuremath{\Range(A)^\perp}}}
\end{aligned}

$$

Then we get that

$$
A=\matrixx{Q_1 & Q_2}\matrixx{R_1\\0}

$$

For the full QR, we extend $\brcurly{\vec{w}_1,\vec{w}_2,\vec{w}_3}$ to an orthonormal basis of $\R^n$

$$
\begin{aligned}
    &\Range(A)^\perp=\Null(A^T)\\
    &A^T=\matrixx{1 & 0 & -1 & 0\\ 3 & 2 & -1 & -2\\ 1 & 3 & 1 & -1}\to \matrixx{1 & 0 & -1 & 0\\ 0 & 1 & 1 & -1\\ 0 & 0 & -1 & 2}\Ra \vec{x}=t\matrixx{2\\-1\\2\\1}\\
    &\vec{w}_n=\frac{1}{\sqrt{10}}\matrixx{2\\-1\\2\\1}\\
    &Q=\matrixx{\vec{w}_1 & \vec{w}_2 & \vec{w}_3 & \vec{w}_n}=\matrixx{\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{10}} & 0 & \frac{2}{\sqrt{10}}\\ 0 & \frac{2}{\sqrt{10}} & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{10}}\\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{10}} & 0 & \frac{2}{\sqrt{10}}\\ 0 & -\frac{2}{\sqrt{10}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{10}}}\\
    &R=\matrixx{\sqrt{2} & 2\sqrt{2} & 0\\ 0 &\sqrt{10} & \sqrt{10}\\ 0 & 0 & \sqrt{2}\\ 0 & 0 & 0}
\end{aligned}

$$

## Least Squares Approximation

Say we want to fit a large collection of data points to some function (often we use a linear function), we can use the least squares approximation.
We want to find the vector $\vec{x}$ that minimizes the least squares error, $\|A\vec{x}-\vec{b}\|$. where $\vec{b}$ represents the y-data, $A$ represents the x-data for each coefficient, and $\vec{x}$ contains the coefficients.
For any $\vec{x}\in\R^n$ we have that $A\vec{x}\in\Range(A)$. The projection theorem states that the vector in $\Range(A)$ nearest to $\vec{b}$ is the orthogonal projection of $\vec{b}$ onto $\Range(A)$.

$$
\begin{aligned}
    &A\vec{x}=\proj_{\Range(A)}(\vec{b})\\
    &\vec{b}-A\vec{x}\in\Range(A)^\perp=\Null(A^T)\\
    &\Ra A^T(\vec{b}-A\vec{x})=\vec{0}\\
    &A^TA\vec{x}=A^T\vec{b}
\end{aligned}

$$

Thus, the least squares approximation to $A\vec{x}=\vec{b}$ will be the given by the vector $\vec{x}$ that solves

$$
A^TA\vec{x}=A^T\vec{b}

$$


- $A$ is $m\times n$ with $\rank(A)=n$
- $A^TA$ is $n\times n$ with $\rank(A^TA)=n$

$A$ is full rank which implies $A^TA$ is a square matrix with full rank. This means that $A^TA$ is invertible, implying that there is a unique solution for $\vec{x}$.
We can also solve the least squares approximation using QR decomposition.
We can say $Q^T\vec{b}=\matrixx{\vec{c}_1vec{c}_2}$ and that $Q_1\vec{b}=\vec{c}_1$.

$$
\begin{aligned}
    &\|A\vec{x}-\vec{b}\|^2=\|QR\vec{x}-QQ^T\|^2=\|Q(R\vec{x}-Q^T\vec{b})\|^2=\|R\vec{x}-Q^T\vec{b}\|^2\\
    &=\left\|\matrixx{R_1\vec{x}\\\vec{0}}-\matrixx{\vec{c}_1\\\vec{c}_2}\right\|^2=\left\|\matrixx{R_1\vec{x}-\vec{c}_1\\\vec{0}}+\matrixx{\vec{0}\\-\vec{c}_2}\right\|^2=\left\|\matrixx{R_1\vec{x}-\vec{c}_1\\\vec{0}}\right\|^2+\left\|\matrixx{\vec{0}\\-\vec{c}_2}\right\|^2\\
    &=\|R_1\vec{x}-\vec{c}\|^2+\|\vec{c}_2\|^2
\end{aligned}

$$

This means that $\|A\vec{x}-\vec{b}\|$ is minimal when

$$
R_1\vec{x}=\vec{c}_1

$$

Ex: Find the least squares approximation to $A\vec{x}=\vec{b}$ where

$$
\begin{aligned}
    &A=\matrixx{1 & 1\\ 1 & 2\\ 1 & 3},\ \vec{b}=\matrixx{0\\3\\1}
\end{aligned}

$$

Using normal equations: $A^TA\vec{x}=A^T\vec{b}$

$$
\begin{aligned}
    &A^TA=\matrixx{1 & 1 & 1\\ 1 & 2 & 3}\matrixx{1 & 1\\ 1 & 2 \\ 1 & 3}=\matrixx{3 & 6\\ 6 & 14}\\
    &A^T\vec{b}=\matrixx{1 & 1 & 1\\ 1 & 2 & 3}\matrixx{0\\3\\1}=\matrixx{4\\9}\\
    &\augmatrix{3 & 6\\ 6 & 14}{4\\9}\to\augmatrix{3 & 6\\ 0 & 2}{4\\1}\Ra x_2=\frac{1}{2}\Ra x_1=\frac{1}{3}\Ra \vec{x}=\matrixx{1/3\\1/2}
\end{aligned}

$$

Using QR decomposition $R_1\vec{x}=Q_1^T\vec{b}$

$$
\begin{aligned}
    &\vec{v}_1=\matrixx{1\\1\\1}\\
    &\vec{v}_2=\matrixx{1\\2\\3}-\frac{6}{3}\matrixx{1\\1\\1}=\matrixx{-1\\0\\1}\\
    &A=Q_1R_1=\matrixx{\frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{2}}\\ \frac{1}{\sqrt{3}} & 0\\ \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{2}}}\matrixx{\sqrt{3} & 2\sqrt{3}\\ 0 & \sqrt{2}}\\
    &\vec{c}_1=Q_1^T\vec{b}=\matrixx{\frac{4}{\sqrt{3}}\\\frac{1}{\sqrt{2}}}\\
    &R_1\vec{x}=Q_1^T\vec{b}\\
    &\augmatrix{\sqrt{3} & 2\sqrt{3}\\ 0 & \sqrt{2}}{\frac{4}{\sqrt{3}}\\ \frac{1}{\sqrt{2}}}\to\augmatrix{3 & 6\\ 0 & 2}{4\\1}\Ra \vec{x}=\matrixx{1/3\\1/2}
\end{aligned}

$$
