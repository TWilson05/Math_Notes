# Complex Functions

<!-- Source: [Sections/Complex_Analysis/Complex_Functions.tex](../../Sections/Complex_Analysis/Complex_Functions.tex) -->

## Mapping Properties of Simple Functions

Similar to how functions with real variables map values to a different set of values, complex functions do the same. The main difference is that with complex functions we're mapping a 2 dimensional set of inputs to a 2 dimensional set of outputs.

$$
w=f(z)=u+iv

$$

We define $z\in \mathcal{S}$ the image of $\mathcal{S}$ under $w$.
Some common mappings:

- The identity map

$$
\begin{aligned}
        &w=f(z)=z\\
        &\eqnsystem{u=x\\ v=y}
\end{aligned}

$$

- Translation by $z_0$

$$
\begin{aligned}
        &w=f(z)=z+z_0\\
        &\eqnsystem{u=x+x_0\\ v=y+y_0}
\end{aligned}

$$

- Stretching ($a>1$) or contraction ($a<1$)

$$
\begin{aligned}
        &w=f(z)=az=are^{i\varphi},\ a\in\R\\
        &\eqnsystem{u=ax\\ v=ay}
\end{aligned}

$$

- Rotation by $\varphi_0$

$$
\begin{aligned}
        &w=f(z)=e^{i\varphi_0}z=e^{i(\varphi+\varphi_0)}
\end{aligned}

$$


Using these basic mapping principles we are able to lay the foundation for some more complicated mappings.
Ex: Find the image of $S=\brcurly{|z-1|\geq1}$ under the mapping $f(z)=\frac{1}{z}$
\begin{tikzpicture}

    \fill[blue!30, domain=-2:0.5, variable=\x]
        (-2, -1) -- plot ({\x}, {2}) -- (0.5, -1) -- cycle;

    \draw[->] (-2,0) -- (2,0) node[right] {$u$};
    \draw[->] (0,-1) -- (0,2) node[above] {$v$};

    \draw[dashed] (0.5, -1) -- (0.5, 2) node[right] {$u=\frac{1}{2}$};
\end{tikzpicture}

$$
\begin{aligned}
    &z=\frac{1}{w}=\frac{1}{u+iv}=\frac{u-iv}{u^2+v^2}\\
    &x=\frac{u}{u^2+v^2}\\
    &y=-\frac{v}{u^2+v^2}\\
    &|z-1|\geq1\Ra\brvertical{\frac{1}{w}-1}\geq1\\
    &\frac{1-w}{w}\geq1\\
    &|1-w|\geq|w|\\
    &|1-w|^2\geq|w|^2\\
    &(1-u)^2+v^2\geq u^2+v^2\\
    &-2u+1\geq 0\\
    &u\leq\frac{1}{2}\\
    &S'=\brcurly{u\leq\frac{1}{2}}
\end{aligned}

$$

\begin{tikzpicture}

    \fill[blue!30] (-2,-2) rectangle (3,2);

    \fill[blue!30, domain=-1:1, variable=\x]
        (-2, 0) -- plot ({1+\x}, {sqrt(1 - \x*\x)}) -- (2, 0) -- cycle;
    \fill[blue!30, domain=-1:1, variable=\x]
        (-2, 0) -- plot ({1+\x}, {-sqrt(1 - \x*\x)}) -- (2, 0) -- cycle;

    \draw[fill=white, dashed] (1, 0) circle (1);

    \node at (1, 1.5) {$|z-1|=1$};

    \draw[->] (-2,0) -- (3,0) node[right] {$x$};
    \draw[->] (0,-2) -- (0,2) node[above] {$y$};
\end{tikzpicture}

Ex2: Find the image of $S=\brcurly{x\leq1}$ under the mapping $f(z)=\frac{1}{z}$

\begin{tikzpicture}

    \fill[blue!30, domain=-2:1, variable=\x]
        (-2, -1) -- plot ({\x}, {2}) -- (1, -1) -- cycle;

    \draw[->] (-2,0) -- (2,0) node[right] {$x$};
    \draw[->] (0,-1) -- (0,2) node[above] {$y$};

    \draw[dashed] (1, -1) -- (1, 2) node[right] {$x=1$};
\end{tikzpicture}

$$
\begin{aligned}
    &z=\frac{1}{w}=\frac{1}{u+iv}=\frac{u-iv}{u^2+v^2}\\
    &x=\frac{u}{u^2+v^2}\\
    &x\leq1\Ra \frac{u}{u^2+v^2}\leq1\Ra u^2+v^2\geq u\\
    &(u-\tfrac{1}{2})^2+v^2\geq\tfrac{1}{4}
\end{aligned}

$$

\begin{tikzpicture}

    \fill[blue!30] (-2,-2) rectangle (3,2);

    \fill[blue!30, domain=-1:1, variable=\x]
        (-2, 0) -- plot ({1+\x}, {sqrt(1 - \x*\x)}) -- (2, 0) -- cycle;
    \fill[blue!30, domain=-1:1, variable=\x]
        (-2, 0) -- plot ({1+\x}, {-sqrt(1 - \x*\x)}) -- (2, 0) -- cycle;

    \draw[fill=white, dashed] (1, 0) circle (1);

    \node at (1, 1.5) {$|z-\tfrac{1}{2}|=\tfrac{1}{2}$};

    \draw[->] (-2,0) -- (3,0) node[right] {$x$};
    \draw[->] (0,-2) -- (0,2) node[above] {$y$};
\end{tikzpicture}
We see from the previous two examples that circles map to lines and lines map to circles. Let's see why this is the case.

$$
\begin{aligned}
    &a(x^2+y^2)+bx+cy+d=0\\
    &a|z|^2+b\frac{z+\bar{z}}{2}+c\frac{z-\bar{z}}{2i}+d=0
\end{aligned}

$$

In the case where $a=0$, we have a line. In the case where $a\neq0$, we have a circle.

$$
\begin{aligned}
    &w=\frac{1}{z}\Ra z=\frac{1}{w}\\
    &z\bar{z}=|z|^2=\frac{1}{|w|^2}=\frac{1}{w\bar{w}}\\
    &a\frac{1}{w\bar{w}}+b\frac{z+\bar{z}}{2}+c\frac{z-\bar{z}}{2i}+d=0\\
    &a\frac{1}{w\bar{w}}+\frac{b}{2}\brround{\frac{1}{w}+\frac{1}{\bar{w}}}+\frac{c}{2i}\brround{\frac{1}{w}-\frac{1}{\bar{w}}}+d=0\\
    &a+\frac{b}{2}\brround{w+\bar{w}}+\frac{c}{2i}\brround{w-\bar{w}}+d\brround{w\bar{w}}=0\\
\end{aligned}

$$

If we have a linear transformation of the form $az+b$ it corresponds to the scaling and translation of the set only. A line will map to a line and a circle will map to a circle.
We can combine this with the $w=\frac{1}{z}$ transformation property to get a more general transformation. We call this the *Mobius transformation*:

$$
f(z)=\frac{az+b}{cz+d}=\frac{a}{c}+\frac{b-\tfrac{ad}{c}}{cz+d}

$$

where $a,b,c,d\in\C$

Ex: Find the mapping of $f(z)=\frac{1}{z+1}$ on the set $S=\brcurly{\Re(z)>0}$

$$
\begin{aligned}
    &u+iv=\frac{1}{x+1+iy}\Ra x+1+iy=\frac{1}{u+iv}\\
    &x+1=\frac{u}{u^2+v^2}\\
    &x>0\Ra x+1>1\\
    &\frac{u}{u^2+v^2}>1\Ra u>u^2+v^2\\
    &u^2+v^2-u+\frac{1}{4}<\frac{1}{4}\\
    &\brround{u-\frac{1}{2}}^2+v^2<\frac{1}{4}\\
    &S'=\brcurly{w=u+iv\Bigg\vert\brround{u-\frac{1}{2}}^2+v^2<\bfrac{1}{2}^2}
\end{aligned}

$$

Ex2: Find the mapping of $f(z)=\frac{z-i}{z+i}$ on $S=\brcurly{|z|<3}$

$$
\begin{aligned}
    &wz+iw=z-i\Ra z(w-1)=-i-iw\Ra z=\frac{i(w+1)}{1-w}\\
    &|z|=\frac{|w+1|}{|w-1|}<3\\
    &|w+1|<3|w-1|\Ra |w+1|^2<9|w-1|^2\\
    &(u+1)^2+v^2<9(u-1)^2+9v^2\\
    &u^2+2u+1+v^2<9u^2-18u+9+9v^2\\
    &0<8u^2-20u+8+8v^2\Ra 0<u^2-\frac{5}{2}u+1+v^2\\
    &\frac{9}{16}<u^2-\frac{5}{2}u+\frac{25}{16}+v^2\\
    &\frac{9}{16}<\brround{u-\frac{5}{4}}^2+v^2\\
    &S'=\brcurly{w=u+iv\Bigg\vert\brround{u-\frac{5}{4}}^2+v^2>\bfrac{3}{4}^2}
\end{aligned}

$$

Another common mapping is the $f(z)=z^2$ or more generally $f(z)=z^n$ mapping.
For $w=z^2$,

$$
w=z^2=r^2e^{2i\varphi}\Ra \eqnsystem{|w|=|z|^2\\ \arg(w)=2\arg(z)}

$$

This mapping scales the magnitude but more notably, it doubles the argument. This means that the mapping of a half circle will now be a full circle.

Ex: Find the mapping of $f(z)=z^2$ on $S=\brcurly{0\leq \Re(z)\leq1,\Im(z)=1}$

$$
\begin{aligned}
    &w=x^2+i2xy-y^2\\
    &u=x^2-y^2=x^2-1\Ra -1\leq u\leq 0\\
    &v=2xy=2x\Ra 0\leq v\leq 2\\
    &S'=\brcurly{w=u+iv|-1\leq u\leq 0,\ 0\leq v\leq 2}
\end{aligned}

$$

Ex2: Find the mapping of $f(z)=-2z^5$ on $S=\brcurly{|z|<1,0<\Arg(z)<\frac{\pi}{2}}$

$$
\begin{aligned}
    &z^5=-\frac{w}{2}\Ra |z|^5=\frac{|w|}{2}<1\Ra |w|<2\\
    &5\arg(z)=\arg(w)\pm\pi \\
    &0<\arg(w)\pm\pi <\frac{5\pi}{2}\\
    &-\pi<\arg(w)<\frac{3\pi}{2}\\
    &S'=\brcurly{|w|<2}
\end{aligned}

$$

Another common mapping is the $f(z)=e^z$ mapping.

$$
\begin{aligned}
    &w=e^z=e^{x+iy}=e^xe^{iy}\\
    &\eqnsystem{|w|=e^x\\ \arg(w)=y}
\end{aligned}

$$

```{figure} ../figures/original/ComplexAnalysisPictures/ExponentialMapping.png
:name: fig-differential-exponentialmapping
:alt: Existing mathematics notes figure (ExponentialMapping). Review provenance before publication.
:width: 85%

Existing source figure: `Images/ComplexAnalysisPictures/ExponentialMapping.png`. It is preserved for review and is not assumed publication-cleared.
```

This mapping has the property that the magnitude is only dependent on $x$ and the argument is exactly $y$.
Ex: Find the mapping of $f(z)=e^z$ on $S=\brcurly{\Re(z)=1}$

$$
\begin{aligned}
    &w=e^xe^{iy}\\
    &|w|=e,\ \arg(w)=y\\
    &S'=\brcurly{|w|=e}
\end{aligned}

$$

Ex2: Find the mapping of $f(z)=e^z$ on $S=\brcurly{0\leq \Im(z)\leq\frac{\pi}{4}}$

$$
\begin{aligned}
    &|w|=x\\
    &\arg(w)=y\Ra 0\leq \arg(w)\leq \frac{\pi}{4}\\
    &S'=\brcurly{0\leq \Arg(w)\leq \frac{\pi}{4}}
\end{aligned}

$$

Ex3: Find the mapping of $f(z)=e^{iz}$ on $S=\brcurly{z: -\frac{\pi}{2}\leq \Re(z)\leq \pi,-1\leq\Im(z)\leq1}$
(Note that multiplying $z$ by $i$ rotates it by $90^\circ$)

$$
\begin{aligned}
    &w=e^{iz}=e^{ix}e^{-y}\\
    &|w|=e^{-y}\Ra e^{-1}\leq|w|\leq e\\
    &\arg(w)=x\Ra -\frac{\pi}{2}\leq \arg(w)\leq\pi\\
    &S'=\brcurly{w\Bigg\vert e^{-1}\leq|w|\leq e,-\frac{\pi}{2}\leq \arg(w)\leq\pi}
\end{aligned}

$$

Ex4: Prove

$$
 |e^{-z^3}|\leq 1\ \forall \brcurly{z\Bigg\vert-\frac{\pi}{6}\leq\Arg(z)\leq\frac{\pi}{6}} 

$$

\begin{proof}
We can express $-z^3$ as some complex number $a+ib$ where $a=\Re(-z^3)$ and $b=\Im(-z^3)$. Taking the magnitude gives

$$
 |e^{-z^3}|=|e^{a+ib}|=|e^ae^{ib}|=|e^a||e^{ib}|=|e^a|=|e^{\Re(-z^3)}| 

$$

$z$ can be written as

$$
\begin{aligned}
    &z=|z|e^{i\Arg(z)}\\
    &z^3=|z|^3e^{i3\Arg(z)}=|z|^3\brround{\cos(3\Arg(z))+i\sin(3\Arg(z))}\\
    &-z^3=-|z|^3\brround{\cos(3\Arg(z))+i\sin(3\Arg(z))}\\
    &\Re(-z^3)=-|z|^3\cos(3\Arg(z))\\
    &\Arg(z)\in\brsquare{-\frac{\pi}{6},\frac{\pi}{6}}\\
    &\Ra 3\Arg(z)\in\brsquare{-\frac{\pi}{2},\frac{\pi}{2}}\\
    &\cos(3\Arg(z))\in\brsquare{0,1}\\
    &|z|^3\in\brcurly{x\in\R|x\geq0}\\
    &\Re(-z^3)=-|z|^3\cos(3\Arg(z))\in\brcurly{x\in\R|x\leq0}\\
    &e^{\Re(-z^3)}\in[0,1]\\
    &\Ra |e^{-z^3}|\leq1
\end{aligned}

$$

\end{proof}

## Calculus of Complex Functions

We define the limit of a complex function to be

$$
\begin{aligned}
    &w=f(z)=u+iv\\
    &\lim_{z\to z_0}f(z)=\lim_{(x,y)\to(x_0,y_0)}u(x,y)+i\lim_{(x,y)\to(x_0,y_0)}v(x,y)
\end{aligned}

$$

Note that the notation $(x,y)\to(x_0,y_0)$ means that the limit is taken as $(x,y)$ approaches $(x_0,y_0)$ along *any* path.
The usual limit arithmetic rules are able to be applied as with real numbers.
In order for
$\lim\limits_{z\to z_0}f(z)$
to exist, we require that both $\lim\limits_{(x,y)\to(x_0,y_0)}u(x,y)$ and $\lim\limits_{(x,y)\to(x_0,y_0)}v(x,y)$ exist.
If we define $z_0=x_0+iy_0$ then we can define the derivative of a complex function as

$$
f'(z_0)=\lim_{z\to z_0}\frac{f(z)-f(z_0)}{z-z_0}=\lim_{\Delta z\to0}\frac{f(z_0+\Delta z)-f(z_0)}{\Delta z}

$$

If this limit exists then the function is said to be differentiable at $z_0$.
Ex: $f(z)=z$

$$
\begin{aligned}
    &f'(z_0)=\lim_{\Delta z\to0}\frac{f(z_0+\Delta z)-f(z_0)}{\Delta z}=\frac{z_0+\Delta z-z_0}{\Delta z}=1\\
    &\Ra f'(z_0)=1
\end{aligned}

$$

Ex2: $f(z)=\bar{z}$

$$
\begin{aligned}
    &f'(z)=\lim_{\Delta z\to0}\frac{f(z+\Delta z)-f(z)}{\Delta z}=\lim_{\Delta z\to0}\frac{\overline{\Delta z}}{\Delta z}\\
    &\Delta z=h_1+ih_2\Ra \overline{\Delta z}=h_1-ih_2\\
    &h_2=0:\ \lim_{\Delta z\to0}\frac{\overline{\Delta z}}{\Delta z}=\lim_{h_1\to0}\frac{h_1}{h_1}=1\\
    &h_1=0:\ \lim_{\Delta z\to0}\frac{\overline{\Delta z}}{\Delta z}=\lim_{h_2\to0}\frac{-ih_2}{ih_2}=-1\\
    &\lim_{h_1\to0}\frac{h_1}{h_1}\neq\lim_{h_2\to0}\frac{-ih_2}{ih_2}\ \therefore\text{ the derivative does not exist}
\end{aligned}

$$

An easy way to determine if a function is differentiable is to use the Cauchy-Riemann equations.
Any path that can be taken to approach $z_0$ can be written as a linear combination of the paths $\Delta z=\Delta x$ and $\Delta z = i\Delta y$ so the derivative must satisfy both of these paths.

$$
\begin{aligned}
    &f'(z_0)=\lim_{\Delta z\to0}\frac{f(z_0+\Delta z)-f(z_0)}{\Delta z}\\
    &f(z_0)=u(x_0,y_0)+iv(x_0,y_0)\\
    &\text{Define }\Delta z=\Delta x\\
    &f'(z_0)=\lim_{\Delta x\to 0}\frac{u(x_0+\Delta x, y_0)+iv(x_0+\Delta x, y_0)-u(x_0,y_0)-iv(x_0,y_0)}{\Delta x}\\
    &f'(z_0)=\lim_{\Delta x\to 0}\frac{u(x_0+\Delta x, y_0)-u(x_0,y_0)}{\Delta x}+i\lim_{\Delta x\to 0}\frac{v(x_0+\Delta x, y_0)-v(x_0,y_0)}{\Delta x}\\
    &f'(z_0)=\pdx[u]{x}(x_0,y_0)+i\pdx[v]{x}(x_0,y_0)\\
    &\text{Define }\Delta z=i\Delta y\\
    &f'(z_0)=\lim_{\Delta y\to 0}\frac{u(x_0, y_0+\Delta y)+iv(x_0, y_0+\Delta y)-u(x_0,y_0)-iv(x_0,y_0)}{i\Delta y}\\
    &f'(z_0)=\lim_{\Delta y\to 0}\frac{u(x_0, y_0+\Delta y)-u(x_0,y_0)}{i\Delta y}+i\lim_{\Delta y\to 0}\frac{v(x_0, y_0+\Delta y)-v(x_0,y_0)}{i\Delta y}\\
    &f'(z_0)=-i\pdx[u]{y}(x_0,y_0)+\pdx[v]{y}(x_0,y_0)\\
    &\Ra\pdx[u]{x}(x_0,y_0)+i\pdx[v]{x}(x_0,y_0)=-i\pdx[u]{y}(x_0,y_0)+\pdx[v]{y}(x_0,y_0)
\end{aligned}

$$

Splitting the real and imaginary parts we get that the Cauchy-Riemann equations are

$$
\eqnsystem{u_x=v_y\\ u_y=-v_x}

$$

If the Cauchy-Riemann equations are satisfied and the partial derivatives are continuous then the function is differentiable.
Some functions are not differentiable everywhere, but are differentiable at a point or a set of points.

- If $f(z)$ is differentiable everywhere in the complex plane then it is said to be **entire**.
- If $f(z)$ is differentiable in some region $R$ then it is said to be **analytic** in $R$.
    (note that this region cannot be a single point, as the Cauchy-Riemann equations require the partial derivatives to be continuous)

Ex: Show using the Cauchy-Riemann equations that $f(z)=\bar{z}$ is not differentiable anywhere.

$$
\begin{aligned}
    &\overline{z}=x-iy\\
    &u_x=1\neq v_y=-1
\end{aligned}

$$

Ex2: Show that $f(z)=z^2$ is entire

$$
\begin{aligned}
    &f(z)=z^2=(x+iy)^2=x^2-y^2+2ixy\\
    &u(x,y)=x^2-y^2\\
    &v(x,y)=2xy\\
    &u_x=2x=v_y\\
    &u_y=-2y=-v_x
\end{aligned}

$$

Ex3: Show that $f(z)=\bar{z}$ is differentiable but not analytic at $z_0=0$

$$
\begin{aligned}
    &|z|^2+2z=x^2+2x+y^2+i2y\\
    &u_x=2x+2=v_y=2\Ra x=0\\
    &u_y=2y=-v_x=0\Ra y=0\\
    &\text{differentiable but not analytic on }z=\brcurly{0}
\end{aligned}

$$

## Conformal Mappings

Using the Cauch-Riemann equations,

$$
\eqnsystem{u_x=v_y\\ u_y=-v_x}

$$

we can get the Laplacian of $u$ and $v$,

$$
\begin{aligned}
    &u_{xx}+u_{yy}=v_{yx}-v_{xy}=0\\
    &v_{xx}+v_{yy}=-(u_{yx}+u_{xy})=0
\end{aligned}

$$

If the Laplacian of $u$ and $v$ are both zero then the function is said to be **harmonic**.
If $\nabla^2u=0$ then we can use the Cauchy-Riemann equations to find its harmonic conjugate $v$.
Ex: Find the harmonic conjugate of $u=xy-x+y$

$$
\begin{aligned}
    &u_x=y-1=v_y\\
    &v=\int y-1 dy=\frac{y^2}{2}-y+h(x)\\
    &u_y=x+1=-v_x=-h'(x)\\
    &h(x)=\int -x-1 dx=-\frac{x^2}{2}-x+C\\
    &v=\frac{y^2}{2}-\frac{x^2}{2}-y-x+C
\end{aligned}

$$

Ex2: Find the harmonic conjugate of $u=\ln\sqrt{x^2+y^2}$

$$
\begin{aligned}
    &u_x=\frac{x}{x^2+y^2}=v_y\\
    &v=\int\frac{x}{x^2+y^2}dy=\int\frac{1/x}{1+\frac{y^2}{x^2}}dy=\arctan\bfrac{y}{x}+h(x)\\
    &u_y=\frac{y}{x^2+y^2}=-v_x=-\frac{y}{1+\frac{y^2}{x^2}}\bfrac{-1}{x^2}-h'(x)=\frac{y}{x^2+y^2}-h'(x)\Ra h'(x)=0\\
    &h(x)=C\\
    &v=\arctan\bfrac{y}{x}+C\\
    &v=\arg(z)+C
\end{aligned}

$$

Ex3: Find the harmonic conjugate of $u=\sin x\cosh y$

$$
\begin{aligned}
    &u=\sin x\cosh y\\
    &u_x=\cos x\cosh y=v_y\\
    &v=\int \cos x\cosh y dy=\cos x\sinh y+h(x)\\
    &u_y=\sin x\sinh y=-v_x=-(-\sin x\sinh y)-h'(x)\Ra h'(x)=0\\
    &h(x)=C\\
    &v=\cos x\sinh y+C
\end{aligned}

$$

Another property is that

$$
|f'(z)|^2=|\nabla u|^2=|\nabla v|^2

$$

This also implies that

$$
\nabla u\cdot \nabla v=0

$$

$$
\begin{aligned}
    &f'(z)=u_x+iv_x=\frac{1}{i}(u_y+iv_y)\\
    &|f'(z)|^2=u_x^2+v_x^2=u_y^2+v_y^2=|\nabla u|^2=|\nabla v|^2\\
    &\nabla u\cdot \nabla v=u_xu_y+v_xv_y=u_xv_x+(-v_x)(u_x)=0
\end{aligned}

$$

A conformal mapping is a mapping between two regions that preserves angles. If we have some function $f(z)=u+iv$ that is analytic then the can create a function of a function as

$$
\Phi(u(x,y),v(x,y))=\phi(x,y)

$$

where $\phi(x,y)$ is a conformal mapping.
A conformal mapping will have the property that

$$
\phi_{xx}+\phi_{yy}=|f'(z)|^2(\Phi_{uu}+\Phi_{vv})

$$

where $|f'(z)|^2$ is known as the *conformal factor*.
This can be shown as follows:

$$
\begin{aligned}
    &\phi_x=\Phi_uu_x+\Phi_vv_x\\
    &\phi_{xx}=u_{xx}\Phi_u^2+2u_xv_x\Phi_u\Phi_v+v_{xx}\Phi_v^2+\Phi_uu_{xx}+\Phi_vv_{xx}\\
    &\phi_y=\Phi_uu_y+\Phi_vv_y\\
    &\phi_{yy}=u_{yy}\Phi_u^2+2u_yv_y\Phi_u\Phi_v+v_{yy}\Phi_v^2+\Phi_uu_{yy}+\Phi_vv_{yy}\\
    &\phi_{xx}+\phi_{yy}=\Phi_u\nabla^2u+\Phi_v\nabla^2v+\Phi_{uu}|\nabla u|^2+2\Phi_u\Phi_v\nabla u\cdot\nabla v+\Phi_{vv}|\nabla v|^2\\
    &\phi_{xx}+\phi_{yy}=|f'(z)|^2(\Phi_{uu}+\Phi_{vv})
\end{aligned}

$$

Ex: $f(z)=z^2$ under $\Phi(u,v)=e^u+v^2$

$$
\begin{aligned}
    &f(z)=x^2-y^2+i(2xy)\\
    &u=x^2-y^2\\
    &v=2xy\\
    &\phi(x,y)=e^{x^2-y^2}+(2xy)^2\\
    &\phi_{xx}+\phi_{yy}=4|z|^2(e^u+2)
\end{aligned}

$$

$f(z)$ is considered a conformal mapping if $f$ is analytic and $f'(z)\neq0$. As a consequence, if $\phi_{xx}+\phi_{yy}=0$ then $\Phi_{uu}+\Phi_{vv}=0$.
If $f$ is a conformal mapping then it will preserve angles.
If we have two curves $C_1$ and $C_2$ described by the parametrized functions $z_1(t)$ and $z_2(t)$ that intersect at a point $z_0$ then the angle between the two curves is given by $\theta=\arg(z_2'(t))-\arg(z_1'(t))$.
If we then apply a conformal mapping $w=f(z)$ to the curves then we get $w_1(t)=f(z_1(t))$ and $w_2(t)=f(z_2(t))$ and the angle between the two curves is given by $\theta_w=\arg(w_2'(t))-\arg(w_1'(t))$.

$$
\begin{aligned}
    &\theta_{w}=\arg(f'(z_2)z_2'(t))-\arg(f'(z_1)z_1'(t))\\
    &\theta_{w}=\arg(f'(z_2))-\arg(f'(z_1))+\arg(z_2'(t))-\arg(z_1'(t))\\
    &\arg(f'(z_1))=\arg(f'(z_2))\\
    &\Ra \theta_w=\arg(z_2'(t))-\arg(z_1'(t))=\theta
\end{aligned}

$$

So the angle between the two curves is preserved under a conformal mapping.
Note that $f'(z)\neq0$ is a necessary condition in this proof.
If we have a nonconformal mapping then the angle between the two curves will not be preserved. One such case is that of $f(z)=z^2$ at $z_0=0$. At this point, $f'(z_0)=0$ and the angle between the two curves is doubled.

Conformal mappings also have the property that they map Neumann boundary conditions to Neumann boundary conditions.
If we let $\hat{n}$ represent the normal vector to the curve $\phi(x,y)$ then they are related by

$$
\pdx[\phi]{n}=\nabla\phi\cdot\hat{n}

$$

and the mapping is similarly related brcurly

$$
\begin{aligned}
    &\pdx[\Phi]{n'}=\nabla\Phi\cdot \hat{n}'\\
    &\pdx[\phi]{n}=|f'(z)|\pdx[\Phi]{n'}
\end{aligned}

$$

So for Neumann bounday conditions, we will have

$$
\pdx[\phi]{n}=0\Ra\pdx[\Phi]{n'}=0

$$

Some examples of conformal mappings come from harmonic functions (having the property that $\nabla^2\phi=0$).
Some common harmonic functions are:

- $\phi=C$
- $\phi=ax+by+c$
- $\ln\sqrt{x^2+y^2},\ \C\backslash0$
- $\phi=\Arg(z),\ \C\backslash(-\infty]$
- $\phi=x^2-y^2$

## Conformal Mapping to Solve Laplace's Equation

Given the useful properties of matching boundary conditions, we can use conformal mappings to help us solve Laplace's equation for a given region.
Ex: Given $\nabla^2\phi=0$ for $1<x^2-y^2<4$ and $\phi=1$ on $x^2-y^2=1$ and $\phi=3$ on $x^2-y^2=4$, find $\phi(x,y)$.

$$
\begin{aligned}
    &\text{choose }\phi=x^2-y^2\\
    &\text{choose }\Phi(u,v)=Au+B\\
    &\eqnsystem{A(1)+B=1\\ A(4)+B=3}\Ra A=\frac{2}{3},\ B=\frac{1}{3}\\
    &\Phi(u,v)=\frac{2}{3}u+\frac{1}{3}\\
    &u=x^2-y^2\\
    &\phi(x,y)=\frac{2}{3}(x^2-y^2)+\frac{1}{3}
\end{aligned}

$$

Ex2: Given $\nabla^2\phi=0$ within the circular region $\mathcal{D}=\brcurly{1<x^2+y^2<4}$ with $\phi=1$ on $x^2+y^2=1$ and $\phi=-2$ on $x^2+y^2=4$, find $\phi(x,y)$.

$$
\begin{aligned}
    &\phi(x,y)=A_1\ln r+A_2\\
    &r=\sqrt{x^2+y^2}\\
    &r=1:\ \phi=1\Ra A_1\ln(1)+A_2=1\\
    &r=2:\ \phi=-2\Ra A_1\ln(2)+A_2=-2\\
    &\Ra A_2=1,\ A_1=-\frac{3}{\ln 2}\\
    &\phi(x,y)=-\frac{3}{\ln 2}\ln\sqrt{x^2+y^2}+1
\end{aligned}

$$

Ex3: Given $\nabla^2=0$ within the strip described by $\brcurly{z:-3\leq 3\Re(z)-4\Im(z)\leq 2}$ with $\phi=0$ for $\brcurly{z:-3=3\Re(z)-4\Im(z)}$ and $\phi=4$ for $\brcurly{z:3\Re(z)-4\Im(z)= 2}$ find $\phi(x,y)$

$$
\begin{aligned}
    &u=3x-4y\\
    &u(-3)=0,\ u(2)=4\\
    &\Phi=Au+B\\
    &\Phi(-3)=-3A+B=0\Ra B=3A\\
    &\Phi(2)=2A+3A=5A=4\Ra A=\frac{4}{5}\Ra B=\frac{12}{5}\\
    &\phi(x,y)=\frac{4}{5}(3x-4y)+\frac{12}{5}
\end{aligned}

$$

Ex4: Given $\nabla^2\phi=0$ for the upper half-plane described by $\brcurly{y>0\wedge x\in\R}$ with the boundary conditions along the x-axis given by

$$
\phi(x,0)=\eqnsystem{-1 & x<-5\\ 0 & -5<x<-1\\ 2 & -1<x<2\\ 1 & x>2}

$$

find $\phi(x,y)$.
```{figure} ../figures/original/ComplexAnalysisPictures/ArgumentLaplacian.png
:name: fig-differential-argumentlaplacian
:alt: Existing mathematics notes figure (ArgumentLaplacian). Review provenance before publication.
:width: 85%

Existing source figure: `Images/ComplexAnalysisPictures/ArgumentLaplacian.png`. It is preserved for review and is not assumed publication-cleared.
```

One trick to solve a problem like this is to choose a linear combination of functions of the form $\Arg(z-z_0)$ with a different point $z_0$ for every place where the boundary condition changes along the x-axis.

$$
\begin{aligned}
    &\phi=A_1\Arg(z+5)+A_2\Arg(z+1)+A_3\Arg(z-2)+A_4\\
    &\phi(x>2,0)=A_4=1\\
    &\phi(-1<x<2,0)=\pi A_3+1=2\Ra A_3=\frac{1}{\pi}\\
    &\phi(-5<x<-1,0)=\pi A_2+1+1=0\Ra A_2=-\frac{2}{\pi}\\
    &\phi(x<-5,0)=\pi A_1-2+2=-1\Ra A_1=-\frac{1}{\pi}\\
    &\phi(x,y)=-\frac{1}{\pi}\Arg(z+5)-\frac{2}{\pi}\Arg(z+1)+\frac{1}{\pi}\Arg(z-2)+1
\end{aligned}

$$

We can also apply these techniques to other types of boundary conditions in some cases.
Ex5: Given $\nabla^2\phi=0$ in the circular region $\brcurly{z: 1\leq |z|\leq 2}$ with the boundary conditions $\phi=1$ for $|z|=1$ and $\pdx[\phi]{r}=2$ for $|z|=2$, find $\phi(x,y)$

$$
\begin{aligned}
    &\phi=A\ln r+B\\
    &\phi(1)=B=1\\
    &\pdx[\phi(2)]{r}=\frac{A}{2}=2\Ra A=4\\
    &\phi=4\ln r+1\\
    &\phi(x,y)=4\ln\sqrt{x^2+y^2}+1
\end{aligned}

$$

If we have a region that has a semicircle in it we can use the Joukowski mapping to transform it into a region that is easier to work with.
```{figure} ../figures/original/ComplexAnalysisPictures/JoukowskiMap.png
:name: fig-differential-joukowskimap
:alt: Existing mathematics notes figure (JoukowskiMap). Review provenance before publication.
:width: 95%

Existing source figure: `Images/ComplexAnalysisPictures/JoukowskiMap.png`. It is preserved for review and is not assumed publication-cleared.
```

Ex6: Given $\nabla^2\phi=0$ in the upper region of the plane described by $\brcurly{y>0\wedge x^2+y^2>9}$ with the boundary conditions $\phi=-1$ for $x<3$, $\phi=0$ for $x^2+y^2=9$, and $\phi=2$ for $x>3$, find $\phi(x,y)$.

$$
\begin{aligned}
    &\eqnsystem{\phi(x,0)=-1 & x<-3\\ \phi(x,y)=0 & x^2+y^2=9\\ \phi(x,0)=2 & x>3}\\
    &w=\frac{1}{2}\brround{\frac{z}{3}+\frac{3}{z}}=u+iv\\
    &\Phi=A_1\Arg(w+1)+A_2\Arg(w-1)+A_3\\
    &\Phi(u>1,v)=A_3=2\\
    &\Phi(-1<u<1,v)=\pi A_2+2=0\Ra A_2=-\frac{2}{\pi}\\
    &\Phi(u<-1,v)=\pi A_1-2+2=-1\Ra A_1=-\frac{1}{\pi}\\
    &\Phi=-\frac{1}{\pi}\Arg(w+1)-\frac{2}{\pi}\Arg(w-1)+2\\
    &\phi(z)=-\frac{1}{\pi}\Arg\brround{\frac{1}{2}\brround{\frac{z}{3}+\frac{3}{z}}+1}-\frac{2}{\pi}\Arg\brround{\frac{1}{2}\brround{\frac{z}{3}+\frac{3}{z}}-1}+2
\end{aligned}

$$

In the case that we have a semicircle not of radius 1 we can apply a scaling before the Joukowski mapping to get the correct radius.
```{figure} ../figures/original/ComplexAnalysisPictures/JoukowskiShift.png
:name: fig-differential-joukowskishift
:alt: Existing mathematics notes figure (JoukowskiShift). Review provenance before publication.
:width: 95%

Existing source figure: `Images/ComplexAnalysisPictures/JoukowskiShift.png`. It is preserved for review and is not assumed publication-cleared.
```

$$
w=\frac{1}{2}\brround{\frac{z}{a}+\frac{a}{z}}

$$

## Sinusoidal Functions

If we recall Euler's formula $e^{ix}=\cos x+i\sin x$ we can use with complex numbers to get the following identities for complex sinusoidals:

- $\sin z=\frac{e^{iz}-e^{-iz}}{2i}$
- $\cos z=\frac{e^{iz}+e^{-iz}}{2}$
- $\sinh z=\frac{e^z-e^{-z}}{2}$
- $\cosh z=\frac{e^z+e^{-z}}{2}$
- $\cos z=\sin\brround{\tfrac{\pi}{2}-z}$
- $\sinh z=-i\sin\brround{iz}$
- $\cosh z=\cos\brround{iz}=\sin\brround{\tfrac{\pi}{2}-iz}$
- $\ddx{z}\sin z=\cos z$
- $\ddx{z}\cos z=-\sin z$
- $\cos^2z+\sin^2z=1$
- $\ddx{z}\sinh z=\cosh z$
- $\ddx{z}\cosh z=\sinh z$
- $\cosh^2z-\sinh^2z=1$

The most notable difference between the real and complex versions of these functions is that $|\sin z|\not\leq1$. We will see cases of this soon but it is easy to see once we write out the real and imaginary components of $\sin z$.

$$
\begin{aligned}
    &\sin z=\sin(x+iy)=\frac{e^{i(x+iy)-e^{-i(x+iy)}}}{2i}=\frac{e^{-y}e^{ix}-e^ye^{-ix}}{2i}\\
    &\sin z = \frac{e^{-y}\brround{\cos x+i\sin x}-e^y\brround{\cos x-i\sin x}}{2i}=\frac{e^{-y}-e^y}{2}\cos x+\frac{e^{-y}+e^y}{2i}\sin x\\
    &\sin z = \sin x\cosh y+i\cos x\sinh y
\end{aligned}

$$

Ex: Show that if $|z|<1$ then $|\sin z|<2$.
\begin{proof}

$$
 |\sin z|<2,\ |z|<1 

$$

$$
\begin{aligned}
        &\sin z=\sin x\cosh y+i\cos x\sinh y\\
        &|\sin z|=\sqrt{\sin^2x\cosh^2y+\cos^2x\sinh^2y}\\
        &\cosh^2y-\sinh^2y=1\Ra \sinh^2y=\cosh^2y-1\\
        &|\sin z|=\sqrt{\sin^2x\cosh^2y+\cos^2x(\cosh^2y-1)}\\
        &|\sin z|=\sqrt{\sin^2x\cosh^2y+\cos^2x\cosh^2y-\cos^2x}\\
        &|\sin z|=\sqrt{\cosh^2y-\cos^2x}\leq \cosh y\\
        &|z|=\sqrt{x^2+y^2}<1\Ra y<1\\
        &\cosh y<\cosh 1=\frac{e+e^{-1}}{2}\approx 1.54<2\\
        &|\sin z|<2
\end{aligned}

$$

\end{proof}
Ex2: Find all solutions to $\sin z=4i$

$$
\begin{aligned}
    &\sin(z)=4i=\sin x\cosh y+i\cos x\sinh y\\
    &\sin x\cosh y=0\Ra \sin x=0\Ra x=n\pi\\
    &\text{Case 1: }n=2k:\ \cos x=1\\
    &4=\cos(2k\pi)\sinh(y)=\sinh y\\
    &\text{Case 2: }n=2k+1:\ \cos x=-1\\
    &4=\cos((2k+1)\pi)\sinh y=-\sinh y\\
    &\sinh y=\frac{e^{y}-e^{-y}}{2}\\
    &2\sinh y=e^y-e^{-y}\\
    &e^{2y}-2\sinh y e^{y}-1=0\\
    &e^y=\frac{2\sinh y\pm\sqrt{4\sinh^2y+4}}{2}=\sinh y\pm \sqrt{\sinh^2y+1}\\
    &n=2k:\\
    &y=\ln\brround{4\pm\sqrt{17}}=\ln\brround{4+\sqrt{17}}\\
    &n=2k+1:\\
    &y=\ln\brround{-4\pm\sqrt{17}}=\ln\brround{\sqrt{17}-4}\\
    &z=\brcurly{(x,y)\Bigg\vert\brround{2k\pi,\ln\brround{4+\sqrt{17}}},\brround{(2k+1)\pi,\ln\brround{\sqrt{17}-4},k\in\Z}}
\end{aligned}

$$

Ex3: Find all solutions to $\cos z=0$

$$
\begin{aligned}
    &\cos(z^4)=0\\
    &z^4=\pi n+\frac{\pi}{2}=\brround{\pi n+\frac{\pi}{2}}e^{2\pi il}\\
    &z=\brround{\pi n+\frac{\pi}{2}}^{1/4}e^{i\frac{\pi l}{2}},\ l=\brcurly{0,1,2,3},\ n\in\Z
\end{aligned}

$$

**Mapping properties of $\sin z$**
$\sin z$ will map the box $-\frac{\pi}{2}\leq x\leq\frac{\pi}{2},\ 0\leq y<\infty$ to the half plane $v>0$.
```{figure} ../figures/original/ComplexAnalysisPictures/SinMapping.png
:name: fig-differential-sinmapping
:alt: Existing mathematics notes figure (SinMapping). Review provenance before publication.
:width: 95%

Existing source figure: `Images/ComplexAnalysisPictures/SinMapping.png`. It is preserved for review and is not assumed publication-cleared.
```

Ex: Find the mapping of $\sin z$ on $S=\brcurly{-\frac{\pi}{2}<x<\frac{\pi}{2},0<y<1}$

$$
\begin{aligned}
    &u=\sin x\cosh y\\
    &\sin x\in(-1,1)\\
    &\cosh y \in (0,\cosh(1))\\
    &u\in (-\cosh(1),\cosh(1))\\
    &v=\cos x\sinh y\\
    &\cos x\in (0,1]\\
    &\sinh y\in (0,\sinh(1))\\
    &v\in(0,\sinh(1))\\
    &S'=\brcurly{(u,v)|-\cosh(1)<u<\cosh(1),0<v<\sinh(1)}
\end{aligned}

$$

If the box is offcenter we can also apply a composition of mappings to shift it into the usual form.
```{figure} ../figures/original/ComplexAnalysisPictures/TranslateSinMap.png
:name: fig-differential-translatesinmap
:alt: Existing mathematics notes figure (TranslateSinMap). Review provenance before publication.
:width: 85%

Existing source figure: `Images/ComplexAnalysisPictures/TranslateSinMap.png`. It is preserved for review and is not assumed publication-cleared.
```

Ex2: Find the mapping of $\sin z$ on $S=\brcurly{-1<x<1,y>0}$

$$
\begin{aligned}
    &u=\sin x\cosh y\\
    &\sin x \in(-\sin(1),\sin(1))\\
    &\cosh y\in (1,\infty)\\
    &u\in \R\\
    &v=\cos x\sinh y\\
    &\cos x\in (\cos(1),1]\\
    &\sinh y \in (0,\infty)\\
    &v\in (0,\infty)\\
    &S'=\brcurly{(u,v)|v>0}
\end{aligned}

$$

Ex3: Solve the Laplace equation $\nabla^2u=0$ in the region $S=\brcurly{0\leq x\leq 2,0\leq y<\infty}$ with boundary conditions $\phi=0$ on $x=0$ and $\phi=1$ on $y=0$ and $\phi=-2$ on $x=2$.

$$
\begin{aligned}
    &\text{Map to the half plane using }w=\sin\brround{\frac{\pi}{2}(z-1)}\\
    &\phi(z)=\Phi(w)=A_1\Arg(w+1)+A_2\Arg(w-1)+A_3\\
    &u>1:\ \Phi=-2=A_3\\
    &-1<u<1:\ \Phi=1=A_2\pi-2\Ra A_2=\frac{3}{\pi}\\
    &u<-1:\ \Phi=0=A_1\pi+\frac{3}{\pi}\pi-2\Ra A_1=-\frac{1}{\pi}\\
    &\phi(z)=-\frac{1}{\pi}\Arg\brround{\sin\brround{\frac{\pi}{2}(z-1)}+1}+\frac{3}{\pi}\Arg\brround{\sin\brround{\frac{\pi}{2}(z-1)}-1}-2
\end{aligned}

$$

## Logarithmic Functions

$\log z$ is defined as the inverse of $e^z$.

$$
\begin{aligned}
    &e^w=z\Ra w=\log z\\
    &w=u+iv\\
    &z=re^{i\Arg(z)}\\
    &e^ue^{iv}=re^{i\Arg(z)}\\
    &e^u=r\Ra u=\ln r\\
    &e^{iv}=e^{i\Arg(z)}\Ra v=\Arg(z)+2k\pi\\
    &\log(z)=w=\ln r+i(\Arg z+2k\pi),\ k\in\Z\\
    &\log(z)=\brcurly{w|e^w=z}=\ln r+i(\Arg z+2k\pi)=\ln r+i\arg z\\
    &\Log(z)=\ln r+i\Arg z
\end{aligned}

$$

Note that $\log(z)=\ln r+i\arg z$ is a multi-valued function and $\Log(z)=\ln r+i\Arg z$ is the principal value of $\log z$.
Ex: Find all values for $\log 2$ and $\Log 2$.

$$
\begin{aligned}
    &z=2=2e^{i0}\\
    &\log 2=\ln 2+i(0+2k\pi)=\ln 2+2k\pi i,\ k\in\Z\\
    &\Log 2=\ln 2+i(0)=\ln 2
\end{aligned}

$$

Ex2: Find all values for $\log(-1-\sqrt{3}i)$ and $\Log(-1-\sqrt{3}i)$.

$$
\begin{aligned}
    &z=-1-\sqrt{3}i=2e^{i\frac{2\pi}{3}}\\
    &\log(-1-\sqrt{3}i)=\ln 2+i\brround{-\frac{2\pi}{3}+2k\pi},\ k\in\Z\\
    &\Log(-1-\sqrt{3}i)=\ln 2+i\brround{-\frac{2\pi}{3}}
\end{aligned}

$$

Ex3: Find all values for $\log(e^{1+5i})$ and $\Log(e^{1+5i})$.

$$
\begin{aligned}
    &z=e^{1+5i}=ee^{5i}=ee^{i(5+2k\pi)}\\
    &5+2k\pi\in(-\pi,\pi]\Ra k=-1\\
    &\Arg(e^{1+5i})=5-2\pi\\
    &\log(e^{1+5i})=\ln e+i(5-2\pi+2k\pi)=1+i(5-2\pi+2k\pi),\ k\in\Z\\
    &\Log(e^{1+5i})=\ln e+i(5-2\pi)=1+i(5-2\pi)
\end{aligned}

$$

Ex4: Find all values for $\log(-i)$ and $\Log(-i)$.

$$
\begin{aligned}
    &-i=e^{-i\frac{\pi}{2}}\\
    &\arg(-i)=-\frac{\pi}{2}+2\pi k\\
    &\log(-i)=-i\frac{\pi}{2}+i2\pi k\\
    &\Log(-i)=-i\frac{\pi}{2}
\end{aligned}

$$

Properties of $\log z$ and $\Log z$:

- $\log(z_1z_2)=\log z_1+\log z_2$
    $\Log(z_1z_2)\neq\Log z_1+\Log z_2$ (same as why $\Arg(z_1z_2)\neq\Arg(z_1)+\Arg(z_2)$)
- $e^{\log z}=z$ and $e^{\Log z}=z$
    but $\log(e^z)\neq z$ and $\Log(e^z)\neq z$
    Ex: $z=0$: $\log(e^0)=\log(1)=\ln1+i(0+2k\pi)=i2k\pi\neq0$
    $\Log(e^{5i})=i(5-2\pi)\neq 5i$
    rather $z\in\log(e^z)$
- $\log z^n\neq n\log z$

$$
\begin{aligned}
        &z=1,\ n=2:\ \log z^2=\log 1=i2k\pi\\
        &2\log z=2\log 1=2i(2k')\pi
\end{aligned}

$$

    but $\log z^\frac{1}{n}=\frac{1}{n}\log z$
- $\Log z$ is analytic in $\C\backslash(-\infty,0]$
```{figure} ../figures/original/ComplexAnalysisPictures/BranchCut.png
:name: fig-differential-branchcut
:alt: Existing mathematics notes figure (BranchCut). Review provenance before publication.
:width: 85%

Existing source figure: `Images/ComplexAnalysisPictures/BranchCut.png`. It is preserved for review and is not assumed publication-cleared.
```

    $\Log z=\ln|z|+i\Arg z,\ -\pi<\Arg z<\pi$

Ex: Find all solutions to $e^z=-1-i$

$$
\begin{aligned}
    &z=\log(-1-i)\\
    &-1-i=\sqrt{2}e^{-i\frac{3\pi}{4}}\\
    &z=\frac{1}{2}\ln(2)-i\frac{3\pi}{4}+i2\pi k
\end{aligned}

$$

Ex2: Find the principal value of $(1+i)^i=e^{i\Log(1+i)}$

$$
\begin{aligned}
    &1+i=\sqrt{2}e^{i\frac{\pi}{4}}\\
    &\Log(1+i)=\frac{1}{2}\ln(2)+i\frac{\pi}{4}\\
    &(1+i)^i=e^{-\frac{\pi}{4}+i\frac{1}{2}\ln(2)}
\end{aligned}

$$

Ex3: Find the principle value of $z^i=1+i$

$$
\begin{aligned}
    &1+i=\sqrt{2}e^{i\frac{\pi}{4}+i2\pi k}=e^{\ln(\sqrt{2})+i\frac{\pi}{4}+i2\pi k}\\
    &z=(1+i)^{1/i}=(1+i)^{-i}=e^{\frac{\pi}{4}+2\pi k}e^{-i\ln(\sqrt{2})}\\
    &z=e^{\frac{\pi}{4}}e^{-i\frac{1}{2}\ln(2)}
\end{aligned}

$$

Ex4: Find the principal value of $i^i$.

$$
\begin{aligned}
    &i^i=(e^{i\frac{\pi}{2}+i2\pi k})^i=e^{-\frac{\pi}{2}-2\pi k}=e^{-\frac{\pi}{2}}
\end{aligned}

$$

Ex5: Find all solutions to $\Log(z^2-1)=\frac{i\pi}{2}$

$$
\begin{aligned}
    &z^2-1=e^{i\frac{\pi}{2}}=i\\
    &z^2=i+1=\sqrt{2}e^{i\frac{\pi}{4}+i2\pi k}\\
    &z=2^{1/4}e^{i\frac{\pi}{8}+i\pi k}
\end{aligned}

$$

Ex6: Find all solutions to $e^{2z}+e^z+1=0$

$$
\begin{aligned}
    &e^z=\frac{-1\pm\sqrt{1-4}}{2}=-\frac{1}{2}\pm i\frac{\sqrt{3}}{2}\\
    &e^z=e^{i\pi\pm i\frac{\pi}{3}+i2\pi k}\\
    &z=i\pi\pm i\frac{\pi}{3}+i2\pi k\\
    &z=\pm i\frac{2\pi}{3}+i2\pi k
\end{aligned}

$$

*Derivative of $\log z$ and $\Log z$*

$$
\begin{aligned}
    &(\Log z)'=\frac{1}{z}\\
    &\Log z=\ln\sqrt{x^2+y^2}+i\Arg z=u+iv\\
    &(\Log z)'=u_x+iv_x\\
    &\Log z=\ln|z|+i\varphi,\ -\pi<\varphi<\pi
\end{aligned}

$$

## Branch Cuts

There are many different analytic functions for $\log z$ depending on the branch cut we choose. For example we can choose:

$$
\begin{aligned}
    &\Log z=\ln r +i\varphi,\ -\pi<\varphi<\pi,\ \C\backslash(-\infty,0]\\
    &\log z=\ln r +i\varphi,\ 0<\varphi<2\pi,\ \C\backslash[0,\infty)\\
    &\log z=\ln r +i\varphi,\ -\frac{\pi}{2}<\varphi<\frac{5\pi}{2},\ \C\backslash i[0,\infty)
\end{aligned}

$$

Ex: Specify a branch cut for $\log z$ such that it is analytic at $z=-1,-i,1$

$$
\log z=\ln r+i\varphi,\ \frac{\pi}{2}<\varphi<\frac{5\pi}{2}

$$

The reason we have branch cuts is so that we can define a single-valued analytic function. This is important for functions such as $\sqrt{z}$ and $\log z$ as one input can correspond to multiple outputs. For example, $\sqrt{1}=1$ and $\sqrt{1}=-1$. This is why we need to specify a branch cut for $\sqrt{z}$ and $\log z$.
Ex: Construct $f(z)=z^{1/2}$ such that it is analytic in $\C\backslash(-\infty,0]$ and $f(1)=-1$.

$$
\begin{aligned}
    &z^\frac{1}{2}=e^{\frac{1}{2}\log z}=e^{\frac{1}{2}\ln r+i\frac{1}{2}\varphi}=r^\frac{1}{2}e^{i\frac{\varphi}{2}},\ -\pi<\varphi<\pi\\
    &f(1)=r^\frac{1}{2}e^{i\frac{\varphi}{2}}=1e^{i0}=1\\
    &z^\frac{1}{2}=r^\frac{1}{2}e^{i\frac{\varphi}{2}},\ \pi<\varphi<3\pi\\
    &\to f(1)=1^\frac{1}{2}e^{\frac{2\pi}{2}}=-1
\end{aligned}

$$

Ex2: Find all solutions to $z^{1/2}+1-i=0$ where $z^{1/2}$ is the principal branch of $z^{1/2}$.

$$
\begin{aligned}
    &z^{1/2}=|z|^{1/2}e^{i\frac{\varphi}{2}}=i-1=\sqrt{2}e^{i\frac{3\pi}{4}+i2\pi k}\\
    &|z|e^{i\varphi}=2e^{i\frac{3\pi}{2}+i4\pi k}\\
    &|z|=2\\
    &\varphi=\frac{3\pi}{2}+4\pi k\not\in(-\pi,\pi]\\
    &\therefore\text{ no solutions}
\end{aligned}

$$

Ex3: Find all solutions to $z^{1/2}+1-i=0$

$$
\begin{aligned}
    &\\
    &z^{1/2}=|z|^{1/2}e^{i\frac{\varphi}{2}+i\pi k_1}i-1=\sqrt{2}e^{i\frac{3\pi}{4}+i2\pi k_2}\\
    &|z|e^{i\varphi+i2\pi k_1}=2e^{i\frac{3\pi}{2}+i4\pi k_2}\\
    &|z|=2\\
    &\varphi+2\pi k_1=\frac{3\pi}{2}+4\pi k_2\\
    &\varphi=\frac{3\pi}{2}+2\pi k_3\\
    &z=2e^{-i\frac{\pi}{2}}=-2i
\end{aligned}

$$

Ex4: Find where $\Log(1+z^2)$ is analytic

$$
\begin{aligned}
    &w=1+z^2\\
    &\text{not analytic on }\Re(w)\leq0\ \wedge \Im(w)=0\\
    &x^2-y^2+1\leq0\\
    &2xy=0\Ra x=0 \vee y=0\\
    &y=0:\ x^2+1\leq 0\Ra \nexists x\in\R\text{ s.t. }x^2\leq-1\\
    &x=0:\ y^2\geq 1\Ra |y|\geq 1
\end{aligned}

$$

Analytic on the domain

$$
 \C\backslash\brcurly{(x,y):x=0,|y|\geq1} 

$$

Ex5: Find where $\Log\bfrac{1-z}{1+z}$ is analytic

$$
\begin{aligned}
    &w=\frac{1-z}{1+z}\\
    &\text{not analytic on }\Re(w)\leq 0\ \wedge\Im(w)=0\\
    &w=\frac{(1-z)(1+\overline{z})}{(1+z)(1+\overline{z})}=\frac{1-|z|^2-z+\overline{z}}{1+|z|^2+z+\overline{z}}=\frac{1-x^2-y^2-2iy}{1+x^2+y^2+2x}\\
    &y=0\\
    &\frac{1-x^2}{1+x^2+2x}\leq0\Ra 1\leq x^2\Ra |x|\geq 1
\end{aligned}

$$

Analytic on

$$
 \C\backslash\brcurly{(x,y):y=0,|x|\geq1} 

$$

Ex6: Find where $f(z)=\Log(1-z^3)$ is analytic

$$
\begin{aligned}
    &\Re(1-z^3)\leq 0\quad\quad\Im(1-z^3)=0\\
    &z^3=r^3e^{3i\varphi}=r^3=r^3\brround{\cos(3\varphi)+i\sin(3\varphi)}\\
    &\Im(1-z^3)=r^3\sin(3\varphi)=0\Ra 3\varphi=n\pi\\
    &\varphi=\frac{n\pi}{3}\\
    &\Re(1-z^3)=1-r^3\cos(3\varphi)\leq0\\
    &n=2k:\ \cos(3\varphi)=1\Ra 1-r^3\leq0\Ra 1\leq r\\
    &n=2k+1:\ \cos(3\varphi)=-1\Ra 1+r^3\leq 0\Ra 1\leq -r\Ra -1\geq r\\
    &\text{can't have }r\leq -1\text{ so can't have }n=2k+1\\
    &\Ra \varphi=\frac{2k\pi}{3},\ 1\leq r\\
    &\text{Analytic in }\C\backslash\brcurly{|z|\geq 1,\ \arg(z)=\frac{2k\pi}{3},\ k\in\Z}
\end{aligned}

$$

Ex7: Find a branch cut for $f(z)=\sqrt{z(z-1)}$ such that it is analytic for $\brcurly{(x,y)|y=0,x<0}$ such that $f(2)=\sqrt{2}$

$$
\begin{aligned}
    &\sqrt{z(z-1)}=|z|^{1/2}e^{i\frac{\varphi_1}{2}}|z-1|^{1/2}e^{i\frac{\varphi_2}{2}}=(|z||z-1|)^{1/2}e^{i\frac{\varphi_1+\varphi_2}{2}}\\
    &\varphi_1\in(-\pi,\pi),\ \varphi_2\in(-\pi,\pi)\\
    &\lim_{\varphi_1\to\pi}\lim_{\varphi_2\to\pi}e^{i\frac{\varphi_1+\varphi_2}{2}}=e^{\pi i}\\
    &\lim_{\varphi_1\to-\pi}\lim_{\varphi_2\to-\pi}e^{i\frac{\varphi_1+\varphi_2}{2}}=e^{-\pi i}=e^{\pi i}\\
    &\therefore \text{ continuous for }\brcurly{(x,y)|y=0,x<0}\\
    &z=2:\ \varphi_1=0,\ \varphi_2=0\Ra \sqrt{z(z-1)}=\sqrt{2}
\end{aligned}

$$

Ex8: Find a branch cut for $f(z)=\sqrt{z(z-1)}$ such that it is analytic for $\brcurly{(x,y)|y=0,x<0}$ such that $f(2)=-\sqrt{2}$

$$
\begin{aligned}
    &\sqrt{z(z-1)}=|z|^{1/2}e^{i\frac{\varphi_1}{2}}|z-1|^{1/2}e^{i\frac{\varphi_2}{2}}=(|z||z-1|)^{1/2}e^{i\frac{\varphi_1+\varphi_2}{2}}\\
    &\varphi_1\in(-\pi,\pi),\ \varphi_2\in(-3\pi,-\pi)\\
    &\lim_{\varphi_1\to\pi}\lim_{\varphi_2\to-\pi}e^{i\frac{\varphi_1+\varphi_2}{2}}=e^{-2\pi i}\\
    &\lim_{\varphi_1\to-\pi}\lim_{\varphi_2\to-3\pi}e^{i\frac{\varphi_1+\varphi_2}{2}}=e^{0}=e^{-2\pi i}\\
    &\therefore \text{ continuous for }\brcurly{(x,y)|y=0,x<0}\\
    &z=2:\ \varphi_1=0,\ \varphi_2=-2\pi\Ra \sqrt{z(z-1)}=\sqrt{2}e^{-i\pi}=-\sqrt{2}
\end{aligned}

$$

Ex9: Find a branch cut for $f(z)=\log(z^2+2z+2)$ such that it is analytic for $\brcurly{(x,y)|x>-1}$ such that $\ddx{z}f(-1)=0$

$$
\begin{aligned}
    &\log(z^2+2z+2)\\
    &z=\frac{-2\pm\sqrt{4-8}}{2}=-1\pm i\\
    &\log(z^2+2z+2)=\ln(|z-z_1||z-z_2|)+i(\varphi_1+\varphi_2)\\
    &-\pi<\varphi_1<\pi,\ -\pi<\varphi_2<\pi\\
    &z=-1:\ \varphi_1=-\frac{\pi}{2},\ \varphi_2=\frac{\pi}{2}\\
    &\log(z^2+2z+2)\eval_{z=-1}=0+i\brround{-\frac{\pi}{2}+\frac{\pi}{2}}=0\\
    &\ddx{z}\log(z^2+2z+2)\eval_{z=-1}=\frac{2z+2}{z^2+2z+2}\eval_{z=-1}=0
\end{aligned}

$$

If we have a function such as $f(z)=\sqrt{z^2-1}$ then we will have two branch points at $z=\pm1$. If two of these branch cuts overlap then they have the property of cancelling out. Note that if we have a cube root then we require three overlapping branch cuts to cancel out. For an $n$th root we require $n$ overlapping branch cuts to cancel out.
Ex: Find a branch cut for $f(z)=\sqrt{4+z^2}$ such that it is analytic for $\C\backslash\brcurly{x=0,-2\leq y\leq 2}$.

$$
\begin{aligned}
    &(4+z^2)^{1/2},\ \C\backslash\brcurly{x=0,-2\leq y\leq 2}\\
    &4+z^2=0\Ra z=\pm2i\\
    &(4+z^2)^{1/2}=|z+2i|^{1/2}|z-2i|^{1/2}e^{i\bfrac{\varphi_1+\varphi_2}{2}}
\end{aligned}

$$

```{figure} ../figures/original/ComplexAnalysisPictures/2a.png
:name: fig-differential-2a
:alt: Existing mathematics notes figure (2a). Review provenance before publication.
:width: 85%

Existing source figure: `Images/ComplexAnalysisPictures/2a.png`. It is preserved for review and is not assumed publication-cleared.
```

Choose $\frac{\pi}{2}<\varphi_1<\frac{5\pi}{2}$ and $\frac{\pi}{2}<\varphi_2<\frac{5\pi}{2}$
Check continuity at $y>2$:

$$
\begin{array}{c|ccc}
     & \varphi_1 & \varphi_2 & e^{i\bfrac{\varphi_1+\varphi_2}{2}}\\
     \hline
     A & \frac{5\pi}{2} & \frac{5\pi}{2} & e^{i\frac{5\pi}{2}}=i\\
     A' & \frac{\pi}{2} & \frac{\pi}{2} & e^{i\frac{\pi}{2}}=i
\end{array}

$$

Ex2: Find a branch cut for $f(z)=(z^4-1)^{1/2}$ such that it is analytic for $|z|>1$.

$$
\begin{aligned}
    &(z^4-1)^{1/2},\ \brcurly{|z|>1}\\
    &z^4-1=0\Ra z=\pm1,\pm i\\
    &(z^4-1)^{1/2}=|z+1|^{1/2}|z-1|^{1/2}|z+i|^{1/2}|z-i|^{1/2}e^{i\bfrac{\varphi_1+\varphi_2+\varphi_3+\varphi_4}{2}}
\end{aligned}

$$

```{figure} ../figures/original/ComplexAnalysisPictures/2b.png
:name: fig-differential-2b
:alt: Existing mathematics notes figure (2b). Review provenance before publication.
:width: 85%

Existing source figure: `Images/ComplexAnalysisPictures/2b.png`. It is preserved for review and is not assumed publication-cleared.
```

Choose $-\pi<\varphi_1<\pi$, $\frac{\pi}{2}<\varphi_2<\frac{5\pi}{2}$, $-\pi<\varphi_3<\pi$, and $\frac{\pi}{2}<\varphi_4<\frac{5\pi}{2}$
Check continuity at $y>1$:

$$
\begin{array}{c|ccc}
     & \varphi_2 & \varphi_4 & e^{i\bfrac{\varphi_1+\varphi_2+\varphi_3+\varphi_4}{2}}\\
     \hline
     A & \frac{5\pi}{2} & \frac{5\pi}{2} & e^{i\frac{5\pi}{2}}e^{i\bfrac{\varphi_1+\varphi_3}{2}}=ie^{i\bfrac{\varphi_1+\varphi_3}{2}}\\
     A' & \frac{\pi}{2} & \frac{\pi}{2} & e^{i\frac{\pi}{2}}e^{i\bfrac{\varphi_1+\varphi_3}{2}}=ie^{i\bfrac{\varphi_1+\varphi_3}{2}}
\end{array}

$$

Check continuity at $x<1$:

$$
\begin{array}{c|ccc}
     & \varphi_1 & \varphi_3 & e^{i\bfrac{\varphi_1+\varphi_2+\varphi_3+\varphi_4}{2}}\\
     \hline
     B & \pi & \pi & e^{i\pi}e^{i\bfrac{\varphi_2+\varphi_4}{2}}=-e^{i\bfrac{\varphi_2+\varphi_4}{2}}\\
     B' & -\pi & -\pi & e^{-i\pi}=-e^{i\bfrac{\varphi_2+\varphi_4}{2}}
\end{array}

$$

## Inverse Functions

To get a one-to-one function we often need to restrict the domain of the function.
Inverse of $e^z$ is $z=\Log(w)$ or a branch cut of $\log(w)$
```{figure} ../figures/original/ComplexAnalysisPictures/ExponentialInverse.png
:name: fig-differential-exponentialinverse
:alt: Existing mathematics notes figure (ExponentialInverse). Review provenance before publication.
:width: 85%

Existing source figure: `Images/ComplexAnalysisPictures/ExponentialInverse.png`. It is preserved for review and is not assumed publication-cleared.
```

$$
\begin{aligned}
    &e^z:\ \brcurly{-\pi<y<\pi}\to\C\backslash(-\infty,0]\\
    &\Log(z):\ \C\backslash(-\infty,0]\to\brcurly{-\pi<v<\pi}
\end{aligned}

$$

The inverse of $e^z$ over $\brcurly{0<y<2\pi}$ is $\log z=\ln r+i\varphi,\ 0<\varphi<2\pi$.
```{figure} ../figures/original/ComplexAnalysisPictures/ExponentialInverse2.png
:name: fig-differential-exponentialinverse2
:alt: Existing mathematics notes figure (ExponentialInverse2). Review provenance before publication.
:width: 85%

Existing source figure: `Images/ComplexAnalysisPictures/ExponentialInverse2.png`. It is preserved for review and is not assumed publication-cleared.
```

The inverse function for $z^2$ over $\brcurly{x>0}$ is $z^\frac{1}{2}=e^{\frac{1}{2}\Log(z)}$
```{figure} ../figures/original/ComplexAnalysisPictures/QuadraticInverse.png
:name: fig-differential-quadraticinverse
:alt: Existing mathematics notes figure (QuadraticInverse). Review provenance before publication.
:width: 85%

Existing source figure: `Images/ComplexAnalysisPictures/QuadraticInverse.png`. It is preserved for review and is not assumed publication-cleared.
```

$$
\begin{aligned}
    &z^2:\ \brcurly{x>0}\to\C\backslash(-\infty,0]
\end{aligned}

$$

The inverse function for $z^2$ over $\brcurly{y>0}$ is $z^\frac{1}{2}=e^{\frac{1}{2}\log(z)},\ 0<\varphi<2\pi$
```{figure} ../figures/original/ComplexAnalysisPictures/QuadraticInverse2.png
:name: fig-differential-quadraticinverse2
:alt: Existing mathematics notes figure (QuadraticInverse2). Review provenance before publication.
:width: 85%

Existing source figure: `Images/ComplexAnalysisPictures/QuadraticInverse2.png`. It is preserved for review and is not assumed publication-cleared.
```

$$
\begin{aligned}
    &z^2:\ \brcurly{y>0}\to\C\backslash[0,\infty)
\end{aligned}

$$

Ex: Find the inverse function of $e^z$ on the domain $\brcurly{\frac{\pi}{4}<y<\frac{9\pi}{4}}$

$$
\begin{aligned}
    &w=e^{x}e^{iy}\\
    &\log(w)=\ln(e^x)+iy=x+iy=z\\
    &\log(w)\\
    &f^{-1}(z)=\log(z),\ \brcurly{\frac{\pi}{4}<\arg(z)<\frac{9\pi}{4}}
\end{aligned}

$$

Ex2: Find the inverse function of $z^4$ on the domain $\brcurly{x>0,y>0}$

$$
\begin{aligned}
    &z=w^{1/4}=|w|^{1/4}e^{i\frac{\arg(w)}{4}}\\
    &0<\arg(z)<\frac{\pi}{2}\Ra 0<\frac{\arg(w)}{4}<\frac{\pi}{2}\Ra 0<\arg(w)<2\pi\\
    &f^{-1}(z)=z^{1/4},\ \brcurly{0<\arg(z)<2\pi}
\end{aligned}

$$

The inverse of $\sin z$ is a little bit less obvious. Let us find all inverse functions for $\sin z$.

$$
\begin{aligned}
    &\sin w=z\\
    &\frac{e^{iw}-e^{-iw}}{2i}=z\\
    &e^{iw}-e^{-iw}=2iz\\
    &e^{2iw}-2ize^{iw}-1=0\\
    &e^{iw}=\frac{2iz\pm\sqrt{(-2iz)^2+4}}{2}\\
    &e^{iw}=iz\pm\sqrt{1-z^2}\\
    &e^{iw}=iz+i(z^2-1)^\frac{1}{2}\\
    &iw=\log\brround{iz+i(z^2-1)^\frac{1}{2}}\\
    &w=-i\log\brround{iz+i(z^2-1)^\frac{1}{2}}
\end{aligned}

$$

The general solutions to $\sin w=z$ are given by the above expression. This expression contains two multivalued parts, $\log$ and $(z^2-1)^\frac{1}{2}$.
Ex: Find all solutions to $\sin w=-i$

$$
\begin{aligned}
    &\sin(w)=-i\\
    &\sin x\cosh y+i\cos x\sinh y=-i\\
    &\sin x\cosh y=0\Ra x=n\pi\\
    &\cos x\sinh y =-1\\
    &n=2k:\\
    &\sinh y =-1\\
    &n=2k+1:\\
    &-\sinh y=-1\Ra \sinh y=1\\
    &\sinh y=\frac{e^y-e^{-y}}{2}\\
    &e^{2y}-2\sinh y e^y-1=0\\
    &e^{y}=\frac{2\sinh y\pm\sqrt{4\sinh^2y+4}}{2}=\sinh y\pm \sqrt{\sinh^2y+1}\\
    &y=\ln\brround{\sinh y\pm\sqrt{\sinh^2 y+1}}\\
    &n=2k:\\
    &y=\ln\brround{-1\pm\sqrt{2}}=\ln\brround{\sqrt{2}-1}\\
    &n=2k+1:\\
    &y=\ln\brround{1\pm\sqrt{2}}=\ln\brround{1+\sqrt{2}}\\
    &w=\brcurly{2k_1\pi+i\ln\brround{\sqrt{2}-1},(2k_2+1)\pi+i\ln\brround{1+\sqrt{2}},k_1,k_2\in\Z}
\end{aligned}

$$

Ex2: Find all solutions to $\cos w=-i$

$$
\begin{aligned}
    &\cos(w)=-i\\
    &\cos(w)=\cos x\cosh y-i\sin x\sinh y\\
    &\cos x\cosh y=0\Ra x=\frac{\pi}{2}+n\pi\\
    &n=2k:\\
    &-\sinh y=-1\Ra \sinh y=1\\
    &n=2k+1:\\
    &\sinh y=-1\\
    &\sinh y=\frac{e^y-e^{-y}}{2}\\
    &e^{2y}-2\sinh ye^y-1=0\\
    &e^y=\frac{2\sinh y\pm\sqrt{4\sinh^2 y+4}}{2}=\sinh y\pm\sqrt{\sinh^2y+1}\\
    &y=\ln\brround{\sinh y\pm\sqrt{\sinh^2y+1}}\\
    &n=2k:\\
    &y=\ln\brround{1\pm\sqrt{2}}=\ln\brround{1+\sqrt{2}}\\
    &n=2k+1:\\
    &y=\ln\brround{-1\pm\sqrt{2}}=\ln\brround{\sqrt{2}-1}\\
    &z=\brcurly{\frac{\pi}{2}+2k_1\pi+i\ln\brround{1+\sqrt{2}},\frac{\pi}{2}+(2k_2+1)\pi+i\ln\brround{\sqrt{2}-1},\ k_1,k_2\in\Z}
\end{aligned}

$$

The principal value of the inverse function of $\sin z$ is called $f(z)=\arcsin z$ and is defined such that $f(0)=0$.
The principal value of the inverse function of $\cos z$ is called $f(z)=\arccos z$ and is defined such that $f(0)=\frac{\pi}{2}$.
These functions are defined as

$$
\begin{aligned}
    &\arcsin z=-i\Log\brround{iz+i(z^2-1)^\frac{1}{2}}\\
    &\text{where }(z^2-1)^\frac{1}{2}=|z-1|^\frac{1}{2}|z+1|^\frac{1}{2}e^{i\frac{\arg(z-1)+\arg(z+1)}{2}}\\
    &\text{such that }0<\arg(z-1)<2\pi\text{ and }\pi<\arg(z+1)<3\pi\\
    &\arccos z=-i\Log\brround{z+(z^2-1)^\frac{1}{2}}\\
    &\text{where }(z^2-1)^\frac{1}{2}=|z-1|^\frac{1}{2}|z+1|^\frac{1}{2}e^{i\frac{\arg(z-1)+\arg(z+1)}{2}}\\
\end{aligned}

$$

Ex: Find all solutions to $w=\arcsin(-i)$

$$
\begin{aligned}
    &w=\arcsin(-i)\\
    &\arcsin(z)=-i\Log(iz+i(z^2-1)^{1/2})\\
    &(z^2-1)^{1/2}=|z+1|^{1/2}|z-1|^{1/2}e^{i\bfrac{\varphi_1+\varphi_2}{2}},\ \varphi_1\in(0,2\pi),\ \varphi_2\in(\pi,3\pi)\\
    &(z^2-1)^{1/2}\eval_{z=-i}\Ra \varphi_1=\frac{5\pi}{4},\ \varphi_2=\frac{3\pi}{4}+\pi\\
    &(z^2-1)^{1/2}\eval_{z=-i}=\sqrt{2}e^{i\frac{3\pi}{2}}=-\sqrt{2}i\\
    &\arcsin(-i)=-i\Log(1+i(-\sqrt{2}i))=-i\Log(1+\sqrt{2})\\
    &\arcsin(-i)=-i\ln\brround{1+\sqrt{2}}
\end{aligned}

$$

Ex2: Find all solutions to $w=\arccos(-i)$

$$
\begin{aligned}
    &w=\arccos(-i)\\
    &w=-i\Log(z+(z^2-1)^{1/2})\\
    &(z^2-1)^{1/2}=|z+1|^{1/2}|z-1|^{1/2}e^{i\bfrac{\varphi_1+\varphi_2}{2}},\ \varphi_1\in(0,2\pi),\ \varphi_2\in(-\pi,\pi)\\
    &(z^2-1)^{1/2}\eval_{z=-i}\Ra \varphi_1=\frac{5\pi}{4},\ \varphi_2=-\frac{\pi}{4}\\
    &(z^2-1)^{1/2}\eval_{z=-i}=\sqrt{2}e^{i\frac{\pi}{2}}=\sqrt{2}i\\
    &w=-i\Log(-i+\sqrt{2}i)=-i\Log((\sqrt{2}-1)e^{i\frac{\pi}{2}})=-i\brround{\ln(\sqrt{2}-1)+i\frac{\pi}{2}}\\
    &w=\frac{\pi}{2}-i\ln\brround{\sqrt{2}-1}
\end{aligned}

$$

Mapping properties of $\sin z$ and $\arcsin z$:
```{figure} ../figures/original/ComplexAnalysisPictures/SineInverse.png
:name: fig-differential-sineinverse
:alt: Existing mathematics notes figure (SineInverse). Review provenance before publication.
:width: 85%

Existing source figure: `Images/ComplexAnalysisPictures/SineInverse.png`. It is preserved for review and is not assumed publication-cleared.
```

We can also apply this mapping to solve Laplace's equation.
Ex:

$$
\begin{aligned}
    &\Delta \phi=0,\ \brcurly{x>0,y>0}\\
    &\mathrm{BCs}:\ \eqnsystem{\phi=1 & x=0,y>0\\ \phi_y=0 & 0<x<1,y=0\\ \phi=2 & x>1,y=0}\\
    &w=\arcsin(z)\\
    &\Phi=Au+B\\
    &\Phi(u=0)=1\Ra B=1\\
    &\Phi\brround{u=\frac{\pi}{2}}=2=A\frac{\pi}{2}+1\Ra A=\frac{2}{\pi}\\
    &\Phi=\frac{2}{\pi}u+1\\
    &u+iv=\arcsin(x+iy)\\
    &\sin(u+iv)=x+iy\\
    &\eqnsystem{x=\sin u\cosh v\\y=\cos u\sinh v}\Ra\eqnsystem{\cosh v=\frac{x}{\sin u}\\ \sinh v=\frac{y}{\cos u}}\Ra \cosh^2v-\sinh^2v=\frac{x^2}{\sin^2u}-\frac{y^2}{\cos^2u}=1\\
    &t=\sin^2u\\
    &\sin^2u+\cos^2u=1\Ra \cos^2u=1-t\\
    &\frac{x^2}{t}-\frac{y^2}{1-t}=1\\
    &t(1-t)=(1-t)x^2-ty^2\\
    &t-t^2=x^2-tx^2-ty^2\\
    &t^2+t(-x^2-y^2-1)+x^2\\
    &t=\frac{x^2+y^2+1\pm\sqrt{(x^2+y^2+1)^2-4x^2}}{2}\\
    &0\leq\sin^2 u\leq1\Ra 0\leq t\leq1\Ra t=\frac{x^2+y^2+1-\sqrt{(x^2+y^2+1)^2-4x^2}}{2}\\
    &\sin^2 u=\frac{x^2+y^2+1-\sqrt{(x^2+y^2+1)^2-4x^2}}{2}\\
    &0<u<\frac{\pi}{2}\Ra 0<\sin u<1\\
    &\sin u=\sqrt{\frac{x^2+y^2+1-\sqrt{(x^2+y^2+1)^2-4x^2}}{2}}\\
    &u=\arcsin\brround{\sqrt{\frac{x^2+y^2+1-\sqrt{(x^2+y^2+1)^2-4x^2}}{2}}}\\
    &\phi=\frac{2}{\pi}\arcsin\brround{\sqrt{\frac{x^2+y^2+1-\sqrt{(x^2+y^2+1)^2-4x^2}}{2}}}+1
\end{aligned}

$$

We can also define inverse functions for $\sinh z$ and $\cosh z$ using the same method as for $\sin z$ and $\cos z$.
Ex: Find the inverse of $\sinh(z)$ such that $f^{-1}(0)=\ln(1)$.

$$
\begin{aligned}
    &w=\sinh(z)=\frac{e^z-e^{-z}}{2}\\
    &2w=e^z-e^{-z}\\
    &e^{2z}-2we^z-1\\
    &e^z=\frac{2w\pm\sqrt{4w^2+4}}{2}=w\pm\sqrt{w^2+1}\\
    &|e^z|>0\Ra |w\pm\sqrt{w^2+1}|\\
    &\log(e^z)=\ln(e^x)+i(y+2\pi k)=\log\brround{w\pm(w^2+1)^{1/2}}\\
    &z=\log\brround{w+(w^2+1)^{1/2}}\\
    &(w^2+1)^{1/2}=|w+i|^{1/2}|w-i|^{1/2}e^{i\bfrac{\varphi_1+\varphi_2}{2}},\ \varphi_1\in\brround{\frac{\pi}{2},\frac{5\pi}{2}},\ \varphi_2\in\brround{\frac{3\pi}{2},\frac{7\pi}{2}}\\
    &(w^2+1)^{1/2}\eval_{w=0}\Ra \varphi_1=\frac{3\pi}{2},\ \varphi_2=\frac{5\pi}{2}\\
    &(w^2+1)^{1/2}\eval_{w=0}=e^{i2\pi}=1\\
    &0=\log(1)=\ln(1)+i2\pi k\\
    &f^{-1}(z)=\Log\brround{z+|z+i|^{1/2}|z-i|^{1/2}e^{i\bfrac{\varphi_1+\varphi_2}{2}}},\ \varphi_1\in\brround{\frac{\pi}{2},\frac{5\pi}{2}},\ \varphi_2\in\brround{\frac{3\pi}{2},\frac{7\pi}{2}}
\end{aligned}

$$
