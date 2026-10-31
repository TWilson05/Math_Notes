# Variational Derivatives

<!-- Source: [Sections/Variational_Calculus/Definition.tex](../../Sections/Variational_Calculus/Definition.tex) -->

## Definition of the Variational Derivative

An action is a function of a function called a functional. This is best seen by example.
Using variational calculus we can prove that the shortest distance between two points is a straight line.
Let us define two points in $\R^2$, $(x_1,y_1)$ and $(x_2,y_2)$ and some function $f(x)$ that connects these points. This can be generalized to higher dimensions, but for simplicity we will stick to two dimensions for now.
\begin{tikzpicture}
\draw[->] (-1,0) -- (5,0) node[right] {$x$};
\draw[->] (0,-1) -- (0,5) node[above] {$y$};
\draw[thick] (0,0) -- (4,4);
\node[right] at (2,2) {$f(x)$};
\draw[fill] (0,0) circle [radius=0.05] node[below] {$(x_1,y_1)$};
\draw[fill] (4,4) circle [radius=0.05] node[above] {$(x_2,y_2)$};
\end{tikzpicture}
We can define an infinite possible functions that connect these two points. We want to find the specific function that minimizes the distance between these two points. So we will want a function with a minimum arc length.
\begin{tikzpicture}
\draw (0,0) -- (3,0);
\node[below] at (1.5,0) {$dx$};
\draw (0,0) -- (3,3);
\node[above] at (1.2,1.5) {$f(x)$};
\draw (3,0) -- (3,3);
\node[right] at (3,1.5) {$dy$};
\end{tikzpicture}
We can use the Pythagorean theorem to find the arc length of this function.

$$
\begin{aligned}
    &\frac{dy}{dx}=f'(x)\Ra dy=f'(x)dx\\
    &ds^2=dx^2+dy^2\\
    &ds=\sqrt{dx^2+dy^2}\\
    &ds=\sqrt{dx^2+(f'(x)dx)^2}\\
    &ds=\sqrt{1+f'(x)^2}dx\\
    &S=\int_{x_1}^{x_2}dx\sqrt{1+f'(x)^2},\ \eqnsystem{f(x_1)=y_1\\ f(x_2)=y_2}
\end{aligned}

$$

We define $S$, the arc length, as the action that we wish to minimize. It is also considered a functional as it is defiend as $S(f(x))$.
We define $\delta f(x)$ as some small change (or wiggle) in the function $f(x)$. It is important to note that $\delta f(x)$ is not some opperation on the original function $f(x)$ but is rather some new function of $x$ we call $\delta f(x)$ that contains very slight variations. We can then define the variation of the action as follows.
Recall that for a regular function $f(x)$, the derivative is defined as

$$
\begin{aligned}
    &\frac{df(x)}{dx}=\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}
\end{aligned}

$$

We can define the variational derivative in a similar manner.

$$
\begin{aligned}
    &\frac{\delta S}{\delta f(x)}=\lim_{\delta f(x)\to0}\frac{S(f(x)+\delta f(x))-S(f(x))}{\delta f(x)}
\end{aligned}

$$

Note that we usually just deal with the numerator of this expression and call it $\delta S$. We can also introduce a small parameter $\epsilon$ to make the expression easier to follow.

$$
\begin{aligned}
    &\delta S=\lim_{\epsilon\to0} \frac{S(f(x)+\epsilon\delta f(x))-S(f(x))}{\epsilon}
\end{aligned}

$$

We can now use this definition to find the variation of the action for our example.

$$
\begin{aligned}
    &\delta S=\lim_{\epsilon\to0} \frac{1}{\epsilon}\int_{x_1}^{x_2}dx\sqrt{1+(f'(x)+\epsilon\delta f'(x))^2}-\int_{x_1}^{x_2}dx\sqrt{1+f'(x)^2}\\
    &\delta S=\lim_{\epsilon\to0} \frac{1}{\epsilon}\int_{x_1}^{x_2}dx\left(\sqrt{1+(f'(x)+\epsilon\delta f'(x))^2}-\sqrt{1+f'(x)^2}\right)\\
    &\delta S=\lim_{\epsilon\to0} \frac{1}{\epsilon}\int_{x_1}^{x_2}dx\left(\sqrt{1+f'(x)^2+2f'(x)\epsilon\delta f'(x)+\epsilon^2\delta f'(x)^2}-\sqrt{1+f'(x)^2}\right)\\
\end{aligned}

$$

Because $\epsilon$ is a very small we can perform a Taylor expansion on the square root.

$$
\begin{aligned}
    &\sqrt{1+x}\eval_{x\approx0}=1+\frac{x}{2}+\mathcal{O}(x^2)\\
    &\sqrt{1+f'(x)^2+2f'(x)\epsilon \delta f(x)+\epsilon^2f'(x)^2}=\sqrt{1+f'(x)^2}\sqrt{1+\frac{2f'(x)\epsilon \delta f(x)+\epsilon^2f'(x)^2}{1+f'(x)^2}}\\
    &=\sqrt{1+f'(x)^2}\brround{1+\frac{1}{2}\frac{2f'(x)\epsilon \delta f(x)+\epsilon^2f'(x)^2}{1+f'(x)^2}}+\mathcal{O}\brround{\brround{\frac{2f'(x)\epsilon \delta f(x)+\epsilon^2f'(x)^2}{1+f'(x)^2}}^2}\\
    &=\sqrt{1+f'(x)^2}\brround{1+\epsilon\frac{f'(x)\delta f(x)}{1+f'(x)^2}+\mathcal{O}(\epsilon^2)}\\
    &=\sqrt{1+f'(x)^2}+\epsilon\frac{f'(x)\delta f(x)}{\sqrt{1+f'(x)^2}}+\mathcal{O}(\epsilon^2)
\end{aligned}

$$

Plugging this back into the original expression we get

$$
\begin{aligned}
    &\delta S=\lim_{\epsilon\to0}\frac{1}{\epsilon} \int_{x_1}^{x_2}dx\left(\sqrt{1+f'(x)^2}+\epsilon\frac{f'(x)\delta f'(x)}{\sqrt{1+f'(x)^2}}+\mathcal{O}(\epsilon^2)-\sqrt{1+f'(x)^2}\right)\\
    &\delta S=\lim_{\epsilon\to0}\frac{1}{\epsilon} \int_{x_1}^{x_2}dx\left(\epsilon\frac{f'(x)\delta f'(x)}{\sqrt{1+f'(x)^2}}+\mathcal{O}(\epsilon^2)\right)\\
    &\delta S=\lim_{\epsilon\to0}\int_{x_1}^{x_2}dx\brround{\frac{f'(x)\delta f'(x)}{\sqrt{1+f'(x)^2}}+\mathcal{O}(\epsilon)}\\
    &\delta S=\lim_{\epsilon\to0}\int_{x_1}^{x_2}dx\frac{f'(x)\delta f'(x)}{\sqrt{1+f'(x)^2}}+\lim_{\epsilon\to0}\int_{x_1}^{x_2}dx\mathcal{O}(\epsilon)
\end{aligned}

$$

If we take the limit as $\epsilon\to0$ then the $\mathcal{O}(\epsilon)$ term goes to zero and we are left with

$$
\begin{aligned}
    &\delta S=\int_{x_1}^{x_2}dx\frac{f'(x)\delta f'(x)}{\sqrt{1+f'(x)^2}}
\end{aligned}

$$

Using integration by parts we can rewrite this as

$$
\begin{aligned}
    &\delta S=\delta f(x)\frac{f'(x)}{\sqrt{1+f'(x)^2}}\eval_{x_1}^{x_2}-\int_{x_1}^{x_2}dx\delta x\brround{\frac{f'(x)}{\sqrt{1+f'(x)^2}}}'
\end{aligned}

$$

Note that the first term goes to zero because $\delta f(x_1)=\delta f(x_2)=0$ as we cannot have any variation in the start and end points. We can then rewrite this as

$$
\begin{aligned}
    &\delta S=-\int_{x_1}^{x_2}dx\delta x\brround{\frac{f'(x)}{\sqrt{1+f'(x)^2}}}'
\end{aligned}

$$

Because we are trying to find a minimum for the action, we can set $\delta S=0$ which gives us

$$
\begin{aligned}
    &\int_{x_1}^{x_2}dx\delta x\brround{\frac{f'(x)}{\sqrt{1+f'(x)^2}}}'=0\\
    &\ddx{x}\brround{\frac{f'(x)}{\sqrt{1+f'(x)^2}}}=0
\end{aligned}

$$

We now have an expression only in terms of $f(x)$ which we can use to solve for the function that minimizes the action $S$.

$$
\begin{aligned}
    &\frac{f'(x)}{\sqrt{1+f'(x)^2}}=C\\
    &f'(x)=C\sqrt{1+f'(x)^2}\\
    &f'(x)^2=C^2(1+f'(x)^2)\\
    &f'(x)^2-C^2f'(x)^2=C^2\\
    &(1-C^2)f'(x)^2=C^2\\
    &f'(x)=\pm\frac{C}{\sqrt{1-C^2}}=C_1\\
    &f(x)=C_1x+C_2
\end{aligned}

$$

And so we have proved that $f(x)$ is a linear function and so the shortest path between two points in $\R^2$ is a straight line.

Note that we can avoid the Taylor expansions for future problems by using the following identity. If we recall for functions of a single variable we have

$$
df=\lim_{x\to0}f(x+\Delta x)-f(x)=\frac{df}{dx}dx=f'(x)dx

$$

We can utilize this identity for functions of many variables as well. If we have a function $f(x_1,x_2,\dots,x_n)$ then we can write

$$
df=\sum_{i=1}^n\frac{\partial f}{\partial x_i}dx_i=\vec{\nabla}f\cdot d\vec{x}

$$

We can also extend this trick to functionals. If we have a functional $S[f(x)]$ then we can write

$$
\delta S[f(x)]=\frac{\delta S}{\delta f(x)}\delta f(x)

$$

If we have a functional of multiple functions then we can extend this further using the multivariable rule to get

$$
\delta[S(f_1,f_2,\ldots, f_n)]=\sum_{i=1}^n\frac{\delta S}{\delta f_i}\delta f_i

$$

## Functions of Many Variables

Intuitively the previous example should hold in higher dimensions as well (we know this to be true in $\R^3$). To show this we will use the same method as before but with a function of many variables.
Let us define some path $\vec{p}(t)$ in $\R^n$ where $\vec{p}(t)$ is a vector valued function such that $\vec{p}(t)\in\R^n$. (In $\R^3$ it would be analogous to $\vec{p}(t)=\brangle{x(t),y(t),z(t)}$). We can define the start and end points as $\vec{p}(t_1)=\vec{x}_1$ and $\vec{p}(t_2)=\vec{x}_2$. We can then define the action $S$ once again to be the arc length of the path $\vec{p}(t)$.

$$
\begin{aligned}
    &ds^2=dp_1^2+dp_2^2+\dots+dp_n^2=\sum_{i=1}^n dp_i^2\\
    &ds=\sqrt{\sum_{i=1}^n dp_i^2}=dt\sqrt{\sum_{i=1}^n\brround{\frac{dp_i}{dt}}^2}\\
    &S=\int_{t_1}^{t_2}dt\sqrt{\sum_{i=1}^n\brround{\frac{dp_i}{dt}}^2}
\end{aligned}

$$

For compactness we will define the following notation

$$
\ddx[p_i]{t}=\dot{p}_i

$$

We can then rewrite the action as

$$
\begin{aligned}
    &S=\int_{t_1}^{t_2}dt\sqrt{\sum_{i=1}^n\dot{p}_i^2}
\end{aligned}

$$

Note that the derivative of a function is a different function than the original function so the action $S$ will be a functional of $S[\dot{p}_1,\dot{p}_2,\ldots,\dot{p}_n]$. We can then define the variation of the action $\delta S$ as

$$
\begin{aligned}
    &\delta S=\sum_{i=1}^n\frac{\delta S}{\delta \dot{p}_i}\delta \dot{p}_i\\
    &\delta S=\sum_{i=1}^n\int_{t_0}^{t_1}dt\frac{\delta}{\delta \dot{p}_i}\brround{\sqrt{\sum_{j=1}^n\dot{p}_j^2}}\delta \dot{p}_i\\
    &\displaystyle\delta S=\sum_{i=1}^n\int_{t_0}^{t_1}dt\brround{\frac{\dot{p}_i}{\sqrt{\sum\limits_{j=1}^n \dot{p}_j^2}}}\delta \dot{p}_i
\end{aligned}

$$

Now using integration by parts we can rewrite this as

$$
\begin{aligned}
    &\delta S=\sum_{i=1}^n\brround{\frac{\dot{p}_i}{\sqrt{\sum\limits_{j=1}^n \dot{p}_j^2}}\delta p_i\eval_{t_0}^{t_1}-\int_{t_0}^{t_1}dt\ddx{t}\brround{\frac{\dot{p}_i}{\sqrt{\sum\limits_{j=1}^n \dot{p}_j^2}}}\delta p_i}\\
\end{aligned}

$$

Once again the first term will go to zero because $\delta p_i(t_0)=\delta p_i(t_1)=0$. We will also set $\delta S$ to zero again to minimize the action.

$$
\begin{aligned}
    &\sum_{i=1}^n\int_{t_0}^{t_1}dt\ddx{t}\brround{\frac{\dot{p}_i}{\sqrt{\sum\limits_{j=1}^n \dot{p}_j^2}}}\delta p_i=0\\
    &\sum_{i=1}^n\ddx{t}\brround{\frac{\dot{p}_i}{\sqrt{\sum\limits_{j=1}^n \dot{p}_j^2}}}=0
\end{aligned}

$$

This will give us $n$ equations of the form

$$
\begin{aligned}
    &\frac{\dot{p}_i}{\sqrt{\sum\limits_{j=1}^n \dot{p}_j^2}}=C_i\\
    &\dot{p}_i=C_i\sqrt{\sum\limits_{j=1}^n \dot{p}_j^2}\\
    &\dot{p}_i^2=C_i^2\sum\limits_{j=1}^n \dot{p}_j^2
\end{aligned}

$$

Note that all of the functions $\dot{p}_i$ are linearly independent of one another so we can get another system of $n$ equations from each of these equations. One of the form

$$
\begin{aligned}
    &\dot{p}_i(1-C_i^2)=0\Ra \dot{p}_i=0\Ra p_i(t)=C_it+D_i
\end{aligned}

$$

All others of the form

$$
\begin{aligned}
    &C_i^2\dot{p}_j^2=0\Ra \dot{p}_j=0\Ra p_j(t)=C_jt+D_j
\end{aligned}

$$

This implies that the solution if of the form

$$
\begin{aligned}
    &\vec{p}(t)=\vec{C}t+\vec{D}
\end{aligned}

$$

which forms a straight line in $n$ dimensional space.

If we have a problem such that we're trying to optimize something subject to some constraint then we can use the method of Lagrange multipliers. Let us say we have some function $f(x,y)$ that we want to optimize subject to the constraint $g(x,y)=C$. We can then define the action as $L(x,y,\lambda)=f(x,y)-\lambda(g(x,y)-C)$.
One such example of this to find the shape that forms the maximum area for a given perimeter.
We can get a generalized expression for the area by utilizing Stoke's theorem.

$$
\begin{aligned}
    &\oint_{\partial R}\vec{F}\cdot d\vec{l}=\iint_R(\nabla\times\vec{F})\cdot d\vec{a}\\
    &\nabla\times\vec{F}=\hat{n}\Ra \iint_R(\nabla\times\vec{F})\cdot d\vec{a}=A\\
    &\Ra \vec{F}=\frac{1}{2}\brangle{-y,x}\\
    &\vec{l}=\brangle{x(s),y(s)}\Ra d\vec{l}=\brangle{\dot{x},\dot{y}}ds\\
    &A=\oint ds\frac{1}{2}\brangle{-y,x}\cdot\brangle{\dot{x},\dot{y}}=\frac{1}{2}\oint ds\brround{x\dot{y}-y\dot{x}}
\end{aligned}

$$

The length of the curve our constant and is given by

$$
\begin{aligned}
    &L=2\pi r=\int_0^{2\pi r}dl=\int_0^{2\pi r}ds\sqrt{\dot{x}^2+\dot{y}^2}
\end{aligned}

$$

Our action that we will want to maximize is then given by

$$
\begin{aligned}
    &\lap(x,\dot{x},y,\dot{y})=A-\lambda L=\int_0^{2\pi r}ds\brround{\frac{1}{2}(x\dot{y}-y\dot{x})+\lambda\sqrt{\dot{x}^2+\dot{y}^2}}\\
    &\delta\lap=\int_0^{2\pi r}ds\brround{\frac{1}{2}\brround{\dot{y}\delta x-\dot{x}\delta y+x\dot{\delta y}-y\dot{\delta x}}+\lambda\frac{\dot{x}\dot{\delta x}}{\sqrt{\dot{x}^2+\dot{y}^2}}+\lambda\frac{\dot{y}\dot{\delta y}}{\sqrt{\dot{x}^2+\dot{y}^2}}}\\
    &\delta \lap=\int_0^{2\pi r}ds\brround{\frac{1}{2}\brround{\dot{y}\delta x-\dot{x}\delta y-\dot{x}\delta y+\dot{y}\delta x}-\lambda\frac{d}{dt}{\bfrac{\dot{x}}{\sqrt{\dot{x}^2+\dot{y}^2}}}\delta x-\lambda\frac{d}{dt}\bfrac{\dot{y}}{\sqrt{\dot{x}^2+\dot{y}^2}}\delta y}\\
    &\brround{\dot{y}-\lambda\frac{d}{dt}{\bfrac{\dot{x}}{\sqrt{\dot{x}^2+\dot{y}^2}}}}\delta x=0\Ra y+C_1=\frac{\lambda\dot{x}}{\sqrt{\dot{x}^2+\dot{y}^2}}\\
    &\brround{-\dot{x}-\lambda\frac{d}{dt}{\bfrac{\dot{y}}{\sqrt{\dot{x}^2+\dot{y}^2}}}}\delta y=0\Ra -x+C_2=\frac{\lambda\dot{y}}{\sqrt{\dot{x}^2+\dot{y}^2}}\\
    &(y+C_1)^2+(x+C_2)^2=\frac{\lambda^2\dot{x}^2}{\dot{x^2}+\dot{y^2}}+\frac{\lambda^2\dot{y}^2}{\dot{x}^2+\dot{y}^2}=\lambda^2
\end{aligned}

$$

The constants $C_1$ and $C_2$ are just translations in $x$ and $y$ so if we center our origin at that point we can take $C_1=C_2=0$ for simplicity. This gives the equation for a circle of radius $\lambda$

$$
 x^2+y^2=\lambda^2 

$$

We can get $\lambda$ from our constraint equation. The path length of a circle with radius $\lambda$ works out to

$$
 s=2\pi\lambda=2\pi r 

$$

So we see that $\lambda=r$ and we get the equation

$$
 x^2+y^2=r^2 

$$

The area of this will be the area of a circle which is

$$
 A=\pi r^2 

$$

So far we have used the integration by parts trick quite a few times. There is a more general form of this trick called the Euler-Lagrange equation.
If we have some action that is a functional of the form $S[f_1(t),f_2(t),\ldots,\dot{f}_1(t),\dot{f}_2(t),t]$ then we can express the variation of the action as

$$
\begin{aligned}
    &\delta S=\sum_{i}\int_a^bdt\brround{\pdx[S]{f_i}\delta f_i+\pdx[S]{\dot{f}_i}\delta\dot{f}_i}\\
    &\delta S=\sum_{i}\int_a^bdt\brround{\pdx[S]{f_i}-\frac{d}{dt}\brround{\pdx[S]{\dot{f}_i}}}\delta f_i+\sum_i\pdx[S]{\dot{f}_i}\delta f_i(t)\eval_a^b\\
    &\delta S=\sum_{i}\int_a^bdt\brround{\pdx[S]{f_i}-\frac{d}{dt}\brround{\pdx[S]{\dot{f}_i}}}\delta f_i
\end{aligned}

$$

This equation must equal 0 for all $i$ so we will have $n$ equations of the form

$$
\begin{aligned}
    &\int_a^bdt\brround{\pdx[S]{f_i}-\frac{d}{dt}\brround{\pdx[S]{\dot{f}_i}}}=0\\
    &\pdx[S]{f_i}-\frac{d}{dt}\brround{\pdx[S]{\dot{f}_i}}=0
\end{aligned}

$$

Rearranging gives us the Euler-Lagrange equation

$$
\pdx[S]{f_i}=\ddx{t}\brround{\pdx[S]{\dot{f}_i}}

$$

In many cases we can avoid many of the steps outlined above and simply plug in our action to the Euler-Lagrange equation and solve for the function we are interested in.
