# Partial Derivatives

<!-- Source: [Sections/Multivariable_Calculus/Partial_Derivatives.tex](../../Sections/Multivariable_Calculus/Partial_Derivatives.tex) -->

## Partial Derivatives and the Gradient

Notation: $\dfrac{\partial f}{\partial x}=f_x$
Definition:

$$
\begin{aligned}
    &\text{for }z=f(x,y)\\
    &\frac{\partial f}{\partial x}=\lim_{h\to 0}\frac{f(x+h,y)-f(x,y)}{h}\\
    &\frac{\partial f}{\partial y}=\lim_{h\to 0}\frac{f(x,y+h)-f(x,y)}{h}
\end{aligned}

$$

Partial derivatives are effectively the same but where you hold the rest of the variables to be constants.

$$
\begin{aligned}
    &\text{Ex: }f(x,y)=x^3y+y^2\\
    &\frac{\partial f}{\partial x}=3x^2y\\
    &\frac{\partial f}{\partial y}=x^3+2y
\end{aligned}

$$

Note that the order of differentiation for higher order derivatives does not matter. $f_{xy}=f_{yx}$
Ex2: Find an expression for $\frac{\partial^2 z}{\partial x\partial y}$ for the function $2yz+x^2+y^2+z^4=18$

$$
\begin{aligned}
    &\frac{\partial}{\partial x}\brround{2yz+x^2+y^2+z^4=18}\\
    &2yz_x+2x+4z^3z_x=0\Ra (2y+4z^3)z_x=-2x\\
    &z_x=\frac{-x}{y+2z^3}\\
    &\frac{\partial }{\partial y}\brround{2yz+x^2+y^2+z^4=18}\\
    &2z+2yz_y+2y+4z^3z_y=0\\
    &(y+2z^3)z_y=-y-z\\
    &z_y=\frac{-y-z}{y+2z^3}\\
    &z_{xy}=\frac{\partial}{\partial y}\brround{\frac{-x}{y+2z^3}}=\frac{x}{(y+2z^3)^2}(1+6z^2z_y)=\frac{x}{(y+2z^3)^2}\brround{1+6z^2\brround{\frac{-y-z}{y+2z^3}}}\\
    &z_{xy}=\frac{xy-6xyz^2-4xz^3}{(y+2z^3)^3}
\end{aligned}

$$


Chain rule: $z=(x(t),y(t))$

$$
\frac{dz}{dt}=\frac{\partial z}{\partial x}\cdot\frac{dx}{dt}+\frac{\partial z}{\partial y}\cdot\frac{dy}{dt}

$$

Chain rule for functions of multiple variables: $z(u(s,t),v(s,t))$

$$
\matrixx{\dfrac{\partial z}{\partial s}\\\dfrac{\partial z}{\partial t}}=\matrixx{\dfrac{\partial x}{\partial s}&\dfrac{\partial y}{\partial s}\\\dfrac{\partial x}{\partial t}&\dfrac{\partial y}{\partial t}}\matrixx{\dfrac{\partial z}{\partial x}\\\dfrac{\partial z}{\partial y}}=\matrixx{\dfrac{\partial z}{\partial x}\cdot\dfrac{\partial x}{\partial s}+\dfrac{\partial z}{\partial y}\cdot\dfrac{\partial y}{\partial s}\\ \dfrac{\partial z}{\partial x}\cdot\dfrac{\partial x}{\partial t}+\dfrac{\partial z}{\partial y}\cdot\dfrac{\partial y}{\partial t}}

$$

The above matrix is an example of the Jacobian which essentially maps $(x,y)$ to $(s,t)$.

Directional Derivative:
The directional derivative is when the take the rate of change of $f$ is some arbitrary direction $\hat{u}$.
$x(t)=x_0+ta,\ y(t)=y_0+tb$ where $\hat{u}=\brangle{a,b}$
$(D_{\hat{u}}f)(x_0,y_0)=f_x\frac{dx}{dt}+f_y\frac{dy}{dt}=f_x(x_0,y_0)a+f_y(x_0,y_0)b$

$$
(D_{\hat{u}}f)(x_0,y_0)=\brangle{f_x(x_0,y_0),f_y(x_0,y_0)}

$$

This can be simplified by defining the gradient.

$$
\nabla f=\brangle{\dfrac{\partial f}{\partial x},\dfrac{\partial f}{\partial y},\dfrac{\partial f}{\partial z}}

$$

Using this, we can simplify the directional derivative to be.

$$
(D_{\hat{u}}f)(x_0,y_0)=(\nabla f)(x_0,y_0)\cdot \hat{u}

$$

Special note about the gradient: the gradient will always be normal to the surface of the level curve (think a balloon expanding)
## Linear Approximation and Tangent Planes

Recall with linear approximations of one variable, they estimate the function at a point using a tangent line. For a 2 variable function, we use the tangent plane as an approximation.
A trick to finding tangent planes is to treat the function as a function of 3 variables as the gradient can be expressed as the normal vector. So we get,

$$
f_x(x_0,y_0,z_0)(x-x_0)+f_y(x_0,y_0,z_0)(y-y_0)+f_z(x_0,y_0,z_0)(z-z_0)=0

$$

for a function of 3 variables.
For functions of 2 variables, we can write it as a functions of 3 variables as $f(x,y,z)=g(x,y)-z=0$ so $f_z=-1$.
This gives the the equation,

$$
f(x,y)\approx f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)+f(x_0,y_0)

$$

Ex: Given the cosine law, $c^2=a^2+b^2-2ab\cos\theta$, find the linear approximation of $\theta$ at the point $(a_0,b_0,c_0)=(1/2,1,\sqrt{3}/2)$

$$
\begin{aligned}
    &\frac{3}{4}=\frac{1}{4}+1-\cos\theta\\
    &\frac{1}{2}=\cos\theta\Ra \theta=\frac{\pi}{3}\\
    &\frac{\partial}{\partial a}:\ 0=2a-2b\cos\theta+2ab\sin\theta\cdot\theta_a\\
    &\Ra 1-1+\frac{\sqrt{3}}{2}\theta_a\Ra 0=\frac{\sqrt{3}}{2}\theta_a\Ra \theta_a=0\\
    &\frac{\partial}{\partial b}:\ 0=2b-2a\cos\theta+2ab\sin\theta\cdot\theta_b\\
    &0=\frac{3}{2}+\frac{\sqrt{3}}{2}\theta_b\Ra \theta_b=-\sqrt{3}\\
    &\frac{\partial}{\partial c}:\ 2c=2ab\sin\theta\cdot\theta_c\\
    &\sqrt{3}=\frac{\sqrt{3}}{2}\theta_c\Ra \theta_c=2\\
    &\theta\approx\frac{\pi}{3}-\sqrt{3}(b-1)+2\brround{c-\frac{\sqrt{3}}{2}}
\end{aligned}

$$

## Optimization

A critical point of a multivariable function is defined to be where all the partial derivatives equal 0, or more generally, $\nabla f=0$
When we take the critical point of a 3D function, there are 3 different types of points it could have:
1) A local minimum
2) A local maximum
3) A saddle point (neither max or min)
We can also have a degenerate critical point which is when we have a line that acts as a critical point.
To find out which of these three types it is, we can use the 2nd derivative test.
If $(x_0,y_0)$ is a critical point of $f$, we can define a discriminant to be,

$$
D=\detmatrix{f_{xx}&f_{xy}\\f_{yx}&f_{yy}}=f_{xx}f_{yy}-f_{xy}^2

$$


- If $D(x_0,y_0)<0$ and $f_{xx}>0$, then it's a local maximum
- If $D(x_0,y_0)>0$ and $f_{xx}<0$, then it's a local minimum.
- If $D(x_0,y_0)<0$ then it's a saddle point
- If $D(x_0,y_0)=0$ then we can't conclude (degenerate critical point)

Ex: Find and classify the critical points of $f(x,y)=(x^2+y^2-5)(y-1)$

$$
\begin{aligned}
    &\nabla f=\matrixx{2x(y-1)\\2y(y-1)+x^2+y^2-5}=\vec{0}\\
    &x=0:\ 2y(y-1)+y^2-5=0\\
    &3y^2-2y-5=0\Ra (3y-5)(y+1)=0\Ra y=\frac{5}{3},\ -1\\
    &\brround{0,\frac{5}{3}},\ (0,-1)\\
    &y=1:\ x^2+1-5=0\Ra x=\pm2\\
    &(-2,1),\ (2,1)\\
    &f_{xx}=2(y-1)\\
    &f_{yy}=6y-2\\
    &f_{xy}=2x\\
    &D=f_{xx}f_{yy}-f_{xy}^2\\
    &D(2,1)<0\to\text{saddle}\\
    &D(-2,1)<0\to\text{saddle}\\
    &D\brround{0,\frac{5}{3}}>0,\ f_{xx}\brround{0,\frac{5}{3}}>0\to\text{local min}\\
    &D\brround{0,-1}>0,\ f_{xx}(0,-1)<0\to\text{local max}
\end{aligned}

$$

## Lagrange Multipliers

In cases where we want to find the max/min of a function over a closed domain, we can use Lagrange multipliers.
Given some constraint equation $g(x,y,z)=0$, the maximum/minimum value along the boundary will occur where $\nabla f//\nabla g$ or more formally, our critical points will occur where

$$
\eqnsystem{\nabla f=\lambda\nabla g\\g=0}

$$

note that $\lambda$ is some scaling constant.
The case where $\lambda=0$ corresponds the the max/min along the boundary also being a critical point of the function ($\nabla f=0$). So if we also compute the critical points of the function, we can ignore the $\lambda=0$ case.

Ex: The plane $x+y+2z=2$ intersects the paraboloid $z=x^2+y^2$ in an ellipse. Find the points on the ellipse nearest and farthest from the origin.

$$
\begin{aligned}
    &D=\sqrt{x^2+y^2+z^2}\\
    &\text{let }D=D^2=x^2+y^2+z^2\\
    &\text{along region }\brcurly{x+y+2z=2}\cap\brcurly{z=x^2+y^2}\\
    &\Ra g(x,y)=x+y+2(x^2+y^2)-2=0\\
    &f(x,y)=x^2+y^2+(x^2+y^2)\\
    &\eqnsystem{f_x=\lambda g_x\\f_y=\lambda g_y\\g=0}\Ra \eqnsystem{2x+4x(x^2+y^2)=\lambda(1+4x)\\2y+4y(x^2+y^2)=\lambda(1+4y)\\x+y+2(x^2+y^2)=2}\Ra\eqnsystem{2xy+4xy(x^2+y^2)=\lambda y+4\lambda xy\\2xy+4xy(x^2+y^2)=\lambda x+4\lambda xy\\x+y+2(x^2+y^2)=2}\\
    &\Ra \lambda x=\lambda y\\
    &\lambda =0\text{ or }x=y\\
    &\lambda=0\text{ case:}\\
    &\eqnsystem{2x+4x(x^2+y^2)=0\\2y+4y(x^2+y^2)=0}\Ra\eqnsystem{x=0\\y=0}\\
    &\text{if }x=y=0,\ g=x+y+2(x^2+y^2)-2=-2\neq 0\therefore x=y\neq 0\\
    &x=y\text{ case:}\\
    &2y+2(2y^2)=2\Ra 2y^2+y-1=0\Ra(2y-1)(y+1)=0\\
    &x=y=\brcurly{-1,\frac{1}{2}},\ z=x^2+y^2\\
    &\text{gives points }(-1,-1,2),\ \brround{\frac{1}{2},\frac{1}{2},\frac{1}{2}}
\end{aligned}

$$

Ex2: Let $(a,b)$ be a point on the ellipse $x^2+3y^2=3$ and $(c,3-c)$ be a point on the line $x+y=3$. Find the coordinates of the pair of points which are closest to each other.

$$
\begin{aligned}
    &\text{let \ensuremath{D} be the distance squared}\\
    &D=(a-c)^2+(b-3+c)^2\\
    &g=a^2+3b^2-3=0\\
    &\nabla D=\brangle{2(a-c),2(b-3+c),-2(a-c)}\\
    &\nabla g=\brangle{2a,6b,0}\\
    &\eqnsystem{a-c=\lambda a\\b-3+c=3\lambda b\\a-c=b-3+c\\a^2+3b^2=3}\\
    &a-c=3\lambda b\\
    &3\lambda b=\lambda a\Ra \lambda=0\text{ or }3b=a\\
    &\text{if }\lambda=0, a-c=0\Ra a=c\\
    &b-3+c=0\Ra b=3-c\\
    &c^2+3(3-c)^2=4c^2-18c+27=3\Ra 2c^2-9c+12=0\\
    &c=\frac{9\pm\sqrt{81-96}}{4}\to\text{no real solutions}\\
    &\therefore a=3b\\
    &9b^2+3b^2=3\Ra b^2=\frac{1}{4}\Ra b=\pm\frac{1}{2}\Ra a=\pm\frac{3}{2}\\
    &3b-c=b-3+c\Ra 2b+3=2c\Ra c=b+\frac{3}{2}=\pm2\\
    &D\brround{\frac{3}{2},\frac{1}{2},2}=\frac{1}{4}+\frac{1}{4}=\frac{1}{2}\\
    &D\brround{-\frac{3}{2},-\frac{1}{2},-2}=\frac{1}{4}+\frac{169}{4}=\frac{85}{2}\\
    &\therefore \text{ the closest points are }\brround{\frac{3}{2},\frac{1}{2}}\text{ and }(2,1)
\end{aligned}

$$

## Least Squares Interpolation

Given experimental data, $(x_1,y_1),\,(x_2,y_2),\,\ldots(x_i,y_i)$, find the best fit line.
Minimize $D=\sum\limits_{i=1}^n(y_i-(ax_i+b))^2$
We can find the minimum by finding the critical points.

$$
\begin{aligned}
    &\frac{\partial D}{\partial a}=0\Ra\frac{\partial D}{\partial a}=\sum_{i=1}^n2(y_i-(ax_i+b))(-x_i)=0\\
    &\frac{\partial D}{\partial b}=0\Ra\sum_{i=1}^n2(y_i-(ax_i+b))(-1)=0\\
    &\sum_{i=1}^n(x_i^2a+x_ib-x_iy_i)=0\\
    &\sum_{i=1}^n(x_ia+b-y_i)=0\\
    &\left\{\begin{matrix}
    \displaystyle{\left(\sum_{i=1}^nx_i^2\right)a+\left(\sum_{i=1}^nx_i\right)b=\sum_{i=1}^nx_iy_i}\\
    \displaystyle{\left(\sum_{i=1}^nx_i\right)a+nb=\sum_{i=1}^ny_i}
    \end{matrix}\right.\\
    &\to\text{gives a 2x2 linear system}\\
    &\to\text{solve for \ensuremath{a} and b}
\end{aligned}

$$

For interpolating non-linear plots, we can linearize the data.
Ex: $y=ce^{ax}\Ra\ln y=\ln c+ax$
For a polynomial function, we can expand the number of coefficients we have.
Ex: for $y=ax^2+bx+c$, we get:
$D(a,b,c)=\sum\limits_{i=1}^n(y_i-(ax_i^2+bx_i+c))^2$ which gives a 3x3 linear system.
