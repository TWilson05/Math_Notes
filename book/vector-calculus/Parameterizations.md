# Parameterizations of Curves and Surfaces

<!-- Source: [Sections/Vector_Calculus/Parameterizations.tex](../../Sections/Vector_Calculus/Parameterizations.tex) -->

## Parametric Equations of Curves

We have often seen equations in the form of $y=f(x)$. We can express both $x$ and $y$ in terms of a common variable $t$ in order to create a vector form of the function and show how the function changes over time.
A parametric equation will be in the form of $\vec{r}(t)=\brangle{\vec{x}(t),\vec{y}(t),\vec{z}(t)}$
Ex: What curve is represented by $x=\cos t$ and $y=\sin t$ for $t\in[0,2\pi]$

$$
\begin{aligned}
    &\sin^2t+\cos^2t=1\\
    &y^2+x^2=1
\end{aligned}

$$

This is the equation of the unit circle. By plugging in points, we can see that it starts at $(1,0)$ and rotates counterclockwise.
Ex2: What curve is represented by $x=t$ and $y=t^2$
$y=x^2$
The function is an upward opening parabola.
We can also define slightly more complicated functions through parametrics such as a cycloid:
$\vec{r}(\theta)=\brangle{a\theta-a\sin\theta,a-a\cos\theta}$ where $a$ is the radius.
Ex3: Find a parameterization of the curve given by the intersection of $\{z=\sqrt{x^2+y^2}\}\cap\{z=1+y\}$

$$
\begin{aligned}
    &\text{try }x=t\\
    &z=\sqrt{t^2+y^2},\ z=1+y\\
    &1+y=\sqrt{t^2+y^2}\\
    &(1+y)^2=t^2+y^2\Ra 1+2y+y^2=t^2+y^2\\
    &y=\frac{1}{2}(t^2-1)\\
    &z=1+\frac{1}{2}(t^2-1)=\frac{1}{2}(t^2+1)\\
    &\vec{r}(t)=\brangle{t,\frac{1}{2}(t^2-1),\frac{1}{2}(t^2+1)}
\end{aligned}

$$

**Derivatives of Parametric Curves**
When taking the derivative of a parametric equation, we can either analyze the time derivatives of each component or we can use the chain rule to compare components to each other as we would normally do.

$$
\frac{dy}{dx}=\frac{dy/dt}{dx/dt}

$$

For the example of the cycloid, we have $\dfrac{d\vec{r}}{d\theta}=\brangle{a-a\cos\theta,a\sin\theta}$.
We can also get $\dfrac{dy}{dx}=\dfrac{a\sin\theta}{a-a\cos\theta}$
Ex: If $x=2t^2+3$ and $y=t^4$, find $\frac{dy}{dx}$

$$
\begin{aligned}
    &\frac{dy}{dt}=4t^3\\
    &\frac{dx}{dt}=4t\\
    &\frac{dy}{dx}=\frac{4t^3}{4t}=t^2\\
    &x=2t^2+3\Ra t^2=\frac{x-3}{2}\\
    &\frac{dy}{dx}=\frac{x-3}{2}
\end{aligned}

$$

We can also define higher order derivatives using the same method:

$$
\frac{d^2y}{dx^2}=\frac{dy'/dt}{dx/dt}

$$

The derivatives for linear operations follow naturally from the product rule:

$$
\frac{d}{dt}(f(t)\vec{r}(t))=f'(t)\vec{r}(t)+f(t)\vec{r}'(t)

$$

$$
\frac{d}{dt}(\vec{u}(t)\cdot\vec{v}(t))=\vec{u}'\cdot\vec{v}+\vec{u}\cdot\vec{v}'

$$

$$
\frac{d}{dt}(\vec{u}(t)\times\vec{v}(t))=\vec{u}'\times\vec{v}+\vec{u}\times\vec{v}'

$$

Motion:
$\vec{r}$ is the position vector, $s$ is the arc length (distance travelled along trajectory), $\vec{v}$ is the velocity, $\|\vec{v}\|$ is the speed, and $\vec{a}$ is the acceleration.
Note that $\vec{v}$ is always the direction tangent to the path of motion.

$$
\begin{aligned}
    &\vec{v}=\frac{d\vec{r}}{dt}\\
    &\vec{a}=\frac{d\vec{v}}{dt}\\
    &\|\vec{v}\|=\frac{ds}{dt}\\
    &\vec{v}=\hat{T}\|\vec{v}\|=\hat{T}\frac{ds}{dt}\\
    &s=\int_{t_0}^{t_1}\|\vec{r}'(t)\|dt
\end{aligned}

$$

Ex: Find the speed of an object travelling around the unit circle.

$$
\begin{aligned}
    &\vec{r}=\brangle{\cos t,\sin t}\\
    &(\Delta s)^2=(\Delta x)^2+(\Delta y)^2\\
    &\brround{\frac{\Delta s}{\Delta t}}^2=\brround{\frac{\Delta x}{\Delta t}}^2+\brround{\frac{\Delta y}{\Delta t}}^2\\
    &\frac{ds}{dt}=\sqrt{\brround{\frac{dx}{dt}}^2+\brround{\frac{dy}{dt}}^2}\\
    &\|\vec{v}\|=\sqrt{\sin^2 t+\cos^2 t}=1
\end{aligned}

$$

Ex2: Find the circumference of a circle of radius $a$

$$
\begin{aligned}
    &\vec{r}=\brangle{a\cos t,a\sin t}\\
    &ds=\sqrt{a^2\sin^2t+a^2\cos^2t}dt=adt\\
    &s=\int_0^{2\pi}adt=at\eval_0^{2\pi}=2\pi a
\end{aligned}

$$

Kepler's Law:
states that for a planet in an elliptical orbit, the area swept out over time is always constant.
$\|\vec{r}\times\vec{v}\|=\text{constant}$
With this we can prove that $\vec{a}_\parallel\vec{r}$

$$
\begin{aligned}
    &\frac{d}{dt}(\vec{r}\times\vec{v})=0\\
    &\frac{d\vec{r}}{dt}\times\vec{v}+\vec{r}\times\frac{d\vec{v}}{dt}=0\\
    &\vec{v}\times\vec{v}+\vec{r}\times\vec{a}=0\\
    &\vec{r}\times\vec{a}=0\\
    &\therefore\vec{a}_\parallel\vec{r}
\end{aligned}

$$

## Curvature

Curvature is defined to be how "curvy" a curve is. This is done by using a tangent circle to approximate the curve (similar to how a tangent line works).
The circle which best approximates the curve near a point is called the *circle of curvature*.
The radius of this circle is called the *radius of curvature* (represented by $\rho$) and the center of the circle is called the *center of curvature*.
The value of curvature itself is defined to be

$$
\kappa=\frac{1}{\rho}

$$

Note as $\kappa\to\infty$ the curve is *very* curvy and as $\kappa\to0$ the curve is linear.
The equation for curvature is given by

$$
\kappa=\brvertical{\frac{\vec{v}(t)\times\vec{a}(t)}{\brround{\frac{ds}{dt}}^3}}

$$

which, expressed in cartesian coordinates can simplify to

$$
\kappa=\frac{\brvertical{\frac{d^2y}{dx^2}}}{\brround{1+\brround{\frac{dy}{dx}}^2}^{3/2}}

$$

Additionally, the radius of curvature is given by

$$
\rho(t)=\frac{1}{\kappa(t)}

$$

and the center of curvature is given by

$$
\vec{r}(t)+\rho(t)\hat{N}(t)

$$

## Parametric Equations of Surfaces

Similar to lines, we can represent a surface with a parameterization $\vec{r}(u,v)$.
There are often many different ways to parameterize a surface but some will result in simpler forms than others.
If your surface has spherical symmetry, try an analog to spherical coordinates where one variable is taken to be a constant (usually $\rho$).
If your surface has circular symmetry about an axis, try cylindrical coordinates where one variable is taken to be a constant (usually $r$).
Otherwise, a good option may be to use Cartesian where you set your two variables to $x$ and $y$ and set the z-position to be a function of $x$ and $y$.
Ex: Parameterize the hemisphere of radius 5 that lies above the xy-plane using 3 different parameterizations

$$
\begin{aligned}
    &S=\brcurly{x^2+y^2+z^2=25,\ z\geq0}\\
    &\vec{r}(x,y)=\brangle{x,y,\sqrt{25-x^2-y^2}}\\
    &\vec{r}(r,\theta)=\brangle{r\cos\theta,r\sin\theta,\sqrt{25-r^2}}\\
    &\vec{r}(\theta,\phi)=\brangle{5\cos\theta\sin\phi,5\sin\theta\sin\phi,5\cos\phi}
\end{aligned}

$$

Ex2: Find a parameterization of a torus with larger radius $A$ (from the origin) smaller radius $a$ (internal radius)

$$
\begin{aligned}
    &\text{circular symmetry so try polar}\\
    &\text{let \ensuremath{\theta} be the revolution around the central z-axis}\\
    &\text{let \ensuremath{\varphi} be the revolution about the inside of the torus}\\
    &(r(\varphi),z(\varphi))=(A+a\sin\varphi,a\cos\varphi)\\
    &x(\theta,\varphi)=r(\varphi)\cos\theta\\
    &y(\theta,\varphi)=r(\varphi)\sin\theta\\
    &z(\theta,\varphi)=z(\varphi)\\
    &\vec{r}(\theta,\varphi)=\brangle{(A+a\sin\varphi)\cos\theta,(A+a\sin\varphi)\sin\theta,a\cos\varphi}
\end{aligned}

$$
