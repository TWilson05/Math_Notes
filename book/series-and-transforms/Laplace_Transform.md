# Laplace Transform

<!-- Source: [Sections/Series_and_Transforms/Laplace_Transform.tex](../../Sections/Series_and_Transforms/Laplace_Transform.tex) -->

## Definition of the Laplace Transform

The Laplace transform maps a function to another function. It effectively maps the frequency and exponential components of a function, converting it from the time domain to the frequency domain. It has some properties that become particularly useful in solving differential equations.
The Laplace transform is defined by

$$
\lap\{f(t)\}=\int_0^\infty f(t)e^{-st}dt

$$

The domain of $\lap\{f(t)\}$ is the set of $s$ where $\lap\{f(t)\}$ converges.
Note that because of the integral, the Laplace operator is linear.

$$
\lap\{c_1f(t)+c_2g(t)\}=c_1\lap\{f\}+c_2\lap\{g\}

$$

However,

$$
\lap\{fg\}\neq\lap\{f\}\cdot\lap\{g\}

$$

Ex: Find the Laplace transform of $1$.

$$
\begin{aligned}
    &\lap\{1\}=\lim_{A\to\infty}\int_0^Ae^{-st}dt=\lim_{A\to\infty}\brsquare{\frac{e^{-st}}{-s}}_0^A=\lim_{A\to\infty}-\frac{1}{s}\brround{e^{-sA}-1}=\frac{1}{s},\ s>0
\end{aligned}

$$

Ex2: Find the Laplace transform of $e^{at}$

$$
\begin{aligned}
    &\lap\{e^{at}\}=\lim_{A\to\infty}\int_0^Ae^{at}\cdot e^{-st}dt\lim_{A\to\infty}\int_0^Ae^{(a-s)t}dt\\
    &=\lim_{A\to\infty}\frac{1}{a-s}\brround{e^{(a-s)A}-1}=\frac{1}{s-a},\ s>-a
\end{aligned}

$$

We can use the result from this example to also compute the Laplace transforms of $\sin(at)$ and $\cos(at)$.

$$
\begin{aligned}
    &\lap\{e^{iat}\}=\frac{1}{s-ia}=\frac{s+ia}{s^2+a^2}\\
    &\lap\{\sin(at)\}=\Re\brcurly{\frac{s+ia}{s^2+a^2}}=\frac{s}{s^2+a^2},\ s>0\\
    &\lap\{\sin(at)\}=\Im\brcurly{\frac{s+ia}{s^2+a^2}}=\frac{a}{s^2+a^2},\ s>0
\end{aligned}

$$

Ex3: Find the Laplace transform of $t^n$

$$
\begin{aligned}
    &\lap\{t^n\}=\int_0^\infty t^ne^{-st}dt\\
    &u=t^n\Ra du=nt^{n-1}dt\\
    &dv=e^{-st}dt\Ra v=-\frac{e^{-st}}{s}\\
    &\lap\{t^n\}=\lim_{A\to\infty}\brround{\brsquare{-\frac{t^n}{s}e^{-st}}_0^A-\int_0^A-\frac{nt^{n-1}}{s}e^{-st}dt}=\lim_{A\to\infty}\frac{n}{s}\int_0^At^{n-1}e^{-st}dt\\
    &\vdots\\
    &\lap\{t^n\}=\frac{n!}{s^n}\int_0^\infty e^{-st}dt=\frac{n!}{s^n}\lap\brcurly{1}=\frac{n!}{s^{n+1}},\ s>0
\end{aligned}

$$

Ex4: Find the Laplace transform of $\ds\int_0^t f(\tau)d\tau$

$$
\begin{aligned}
    &\lap\{\int_0^t f(\tau)d\tau\}=\int_0^\infty\int_0^t f(\tau)d\tau e^{-st}dt\\
    &u=\int_0^t f(\tau)d\tau\Ra du=f(t)dt\\
    &dv=e^{-st}dt\Ra v=-se^{-st}\\
    &\lap\brcurly{\int_0^t f(\tau)d\tau}=\brsquare{\int_0^t f(\tau)d\tau e^{-st}}_0^\infty+\frac{1}{s}\int_0^\infty f(t)e^{-st}dt=\frac{\lap{f(t)}}{s}
\end{aligned}

$$

Ex5: Find the Laplace transform of $f'(t)$

$$
\begin{aligned}
    &\lap\brcurly{f'(t)}=\int_0^\infty f'(t)e^{-st}dt\\
    &u=e^{-st}\Ra du=-\frac{e^{-st}}{s}dt\\
    &dv=f'(t)dt\Ra v=f(t)\\
    &\lap\brcurly{f'(t)}=\brsquare{f(t)e^{-st}}_0^\infty+s\int_0^\infty f(t)e^{-st}dt=s\lap{f(t)}-f(0)
\end{aligned}

$$

This can be defined recursively for multiple derivatives to be

$$
\lap\brcurly{f^{(n)}(t)}=s^n\lap{f(t)}-s^{n-1}f(0)-\cdots-f^{(n-1)}(0)

$$

Ex6: Find the derivative of the Laplace transform

$$
\begin{aligned}
    &\frac{d}{ds}\lap\brcurly{f(t)}=\frac{d}{ds}\int_0^\infty f(t)e^{-st}dt=-t\int_0^{\infty}f(t)e^{-st}dt=-t\lap\brcurly{f(t)}
\end{aligned}

$$

This can also be defined recursively to give the identity

$$
\lap\brcurly{(-t)^nf(t)}=\frac{d^n}{ds^n}\lap\brcurly{f(t)}

$$

Using the Laplace transforms we already have, we can combine them to find the transforms of other non-elementary functions.
Ex7: Find the Laplace tranform of

$$
\begin{aligned}
    &\lap\brcurly{t^2\sin(at)}\\
    &\text{use }\lap\brcurly{(-t)^nf(t)}=\frac{d^n}{ds^n}\lap\brcurly{f(t)}\\
    &(-t)^2=t^2\\
    &\lap\brcurly{t^2\sin(at)}=\frac{d^2}{ds^2}\lap{\sin(at)}=\frac{d^2}{ds^2}\frac{a}{s^2+a^2},\ s>0\\
    &=\frac{d}{ds}\frac{-2as}{(s^2+a^2)^2}=\frac{(s^2+a^2)^2(-2a)-(-2as)(2)(s^2+a^2)(2s)}{(s^2+a^2)^4}=\frac{-2a(s^2+a^2)+8as^2}{(s^2+a^2)^3}\\
    &=\frac{6as^2-2a^3}{(s^2+a^2)^3},\ s>0
\end{aligned}

$$

Ex8: Given that $\lap\brcurly{\sqrt{t}}=\frac{\sqrt{\pi}}{2s^{3/2}}$ find $\lap\brcurly{\frac{1}{\sqrt{t}}}$

$$
\begin{aligned}
    &\frac{d}{dt}\sqrt{t}=\frac{1}{2\sqrt{t}}\Ra \frac{d}{dt}2\sqrt{t}=\frac{1}{\sqrt{t}}\\
    &\lap\brcurly{f'(t)}=s\lap{f(t)}-f(0)\Ra \lap\brcurly{\frac{1}{\sqrt{t}}}=2s\lap\brcurly{\sqrt{t}}-2\sqrt{0}=\frac{2s\sqrt{\pi}}{2s^{3/2}}=\sqrt{\frac{\pi}{s}}\\
    &\text{alternative solution:}\\
    &\lap\brcurly{\sqrt{t}}=\lap\brcurly{\frac{t}{\sqrt{t}}}=-\frac{d}{ds}\lap{\frac{1}{\sqrt{t}}}\\
    &\lap\brcurly{\frac{1}{\sqrt{t}}}=-\int \lap\brcurly{\sqrt{t}}ds=-\int\frac{\sqrt{\pi}}{2s^{3/2}}ds=\sqrt{\frac{\pi}{s}}
\end{aligned}

$$

## Inverse Laplace Transform

Using the table of Laplace transforms becomes particularly useful in finding inverse Laplace transforms. In addition to the functions found, there is also a shifting law such that

$$
\lap\brcurly{e^{at}f(t)}=F(s+a)

$$

where $F(s)$ is the Laplace transform of $f(t)$.
Some common occurrences of this shifting law are

$$
\begin{aligned}
    &e^{-at}\sin(bt)=\frac{b}{(s+a)^2+b^2}\ s>-a\\
    &e^{-at}\cos(bt)=\frac{s+a}{(s+a)^2+b^2},\ s>-a\\
    &e^{-at}t^n=\frac{n!}{(s+a)^{n+1}},\ s>-a
\end{aligned}

$$

Ex:

$$
\begin{aligned}
    &\lap^{-1}\brcurly{\frac{5}{s^2(s+2)}}\\
    &\frac{5}{s^2(s+2)}=\frac{A}{s}+\frac{B}{s^2}+\frac{C}{s+2}\\
    &As(s+2)+B(s+2)+Cs^2=5=As^2+2As+Bs+2B+Cs^2\\
    &A+C=0\\
    &2A+B=0\\
    &2B=5\Ra B=\frac{5}{2}\\
    &2A+\frac{5}{2}\Ra A=-\frac{5}{4}\\
    &-\frac{5}{4}=C\Ra C=\frac{5}{4}\\
    &\lap^{-1}\brcurly{\frac{5}{s^2(s+2)}}=-\frac{5}{4}\lap^{-1}\brcurly{\frac{1}{s}}+\frac{5}{2}\lap^{-1}\brcurly{\frac{1}{s^2}}+\frac{5}{4}\lap^{-1}\brcurly{\frac{1}{s+2}}\\
    &=-\frac{5}{4}u(t)+\frac{5}{2}tu(t)+\frac{5}{4}e^{-2t}u(t)
\end{aligned}

$$

Ex2:

$$
\begin{aligned}
    &\lap^{-1}\brcurly{\frac{se^{-3s}+2}{s^2+2s+2}}\\
    &\frac{se^{-3s}+2}{s^2+2s+2}=\frac{se^{-3s}+e^{-3s}}{(s+1)^2+1}-\frac{e^{-3s}}{(s+1)^2+1}+\frac{2}{(s+1)^2+1}\\
    &\lap^{-1}\brcurly{\frac{se^{-3s}+2}{s^2+2s+2}}=e^{-(t-3)}\cos(t-3)u(t-3)-e^{-(t-3)}\sin(t-3)u(t-3)+2e^{-t}\sin(t)u(t)
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex3: }&\lap^{-1}\brcurly{\frac{8s^2-4s+12}{s(s^2+4)}}\\
    &\frac{8s^2-4s+12}{s(s^2+4)}=\frac{A}{s}+\frac{Bs+C}{s^2+4}\\
    &As^2+4A+Bs^2+Cs=8s^2-4s+12\Ra A=3\\
    &3s^2+12+Bs^2+Cs=8s^2-4s+12\\
    &(3+B)s^2+Cs=8s^2-4s\Ra C=-4\Ra B=5\\
    &\frac{8s^2-4s+12}{s(s^2+4)}=\frac{3}{s}+\frac{5s-4}{s^2+4}=\frac{3}{s}+\frac{5s}{s^2+4}-\frac{4}{s^2+4}\\
    &\lap^{-1}\brcurly{\frac{8s^2-4s+12}{s(s^2+4)}}=3+5\cos(2t)-2\sin(2t)
\end{aligned}

$$

$$
\begin{aligned}
    \text{Ex4: }&\lap^{-1}\brcurly{\frac{s^3-1}{(s^2+1)(s+2)^2}}\\
    &\frac{s^3-1}{(s^2+1)(s+2)^2}=\frac{As+B}{s^2+1}+\frac{C}{s+2}+\frac{D}{(s+2)^2}\\
    &(As+B)(s^2+4s+4)+C(s^2+1)(s+2)+Ds^2+D=s^3-1\\
    &As^3+4As^2+4As+Bs^2+4Bs+4B+Cs^3+2Cs^2+Cs+2C+Ds^2+D=s^3-1\\
    &\eqnsystem{A+C=1\\4A+B+2C+D=0\\4A+4B+C=0\\4B+2C+D=-1}\Ra\augmatrix{1&0&1&0\\4&1&2&1\\4&4&1&0\\0&4&2&1}{1\\0\\0\\-1}\to\augmatrix{1&0&1&0\\0&1&-2&1\\0&4&-3&0\\0&4&2&1}{1\\-4\\-4\\-1}\\
    &\to\augmatrix{1&0&1&0\\0&1&-2&1\\0&0&5&-4\\0&0&10&-3}{1\\-4\\12\\15}\leadsto\augmatrix{1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1}{\frac{1}{25}\\-\frac{7}{25}\\\frac{24}{25}\\-\frac{9}{5}}\Ra\eqnsystem{A=\frac{1}{25}\\B=-\frac{7}{25}\\C=\frac{24}{25}\\D=-\frac{9}{5}}\\
    &\frac{s^3-1}{(s^2+1)(s+2)^2}=\frac{1}{25}\frac{s-7}{s^2+1}+\frac{24/25}{s+2}-\frac{9/5}{(s+2)^2}=\frac{s/25}{s^2+1}-\frac{7/25}{s^2+1}+\frac{24/25}{s+2}-\frac{9/5}{(s+2)^2}\\
    &\lap^{-1}\brcurly{\frac{s^3-1}{(s^2+1)(s+2)^2}}=\frac{1}{25}\cos(t)-\frac{7}{25}\sin(t)+\frac{24}{25}e^{-2t}-\frac{9}{5}\lap\brcurly{\frac{1}{(s+2)^2}}\\
    &\text{use }\lap\brcurly{t^ne^{-at}}=\frac{n!}{(s+a)^{n+1}},\ n=1\\
    &\lap\brcurly{\frac{1}{(s+2)^2}}=te^{-2t}\\
    &\Ra \lap^{-1}\brcurly{\frac{s^3-1}{(s^2+1)(s+2)^2}}=\frac{1}{25}\cos(t)-\frac{7}{25}\sin(t)+\frac{24}{25}e^{-2t}-\frac{9}{5}te^{-2t}
\end{aligned}

$$

Sometimes the inverse Laplace can be difficult to find using conventional methods or even be impossible to express. In this case, we can use the convolution operation.

$$
\lap\brcurly{f(t)*g(t)}=\lap\brcurly{f(t)}\cdot\lap\brcurly{g(t)}

$$

$$
\begin{aligned}
    &\lap\brcurly{f*g}=FG=\brround{\int_0^\infty f(\tau)e^{-s\tau}d\tau}\brround{\int_0^\infty g(\nu)e^{-s\nu}d\nu}=\int_0^\infty\int_0^\infty f(\tau)g(\nu)e^{-s\nu}e^{-s\tau}d\nu d\tau\\
    &\text{let }\nu=t-\tau\\
    &FG=\int_0^\infty\int_\tau^\infty f(\tau) g(t-\tau)e^{-st}dtd\tau=\int_0^\infty\brround{\int_0^t f(\tau) g(t-\tau)d\tau}e^{-st}dt\\
    &\Ra f*g=\int_0^t f(\tau)g(t-\tau)d\tau
\end{aligned}

$$

The Laplace transform can also compute piecewise functions as the Laplace transforms of the delta and step functions are well defined.
The Laplace transform of the delta function can be computed as

$$
\begin{aligned}
    &\lap\{\delta(t-a)\}=\int_0^\infty\delta(t)e^{-st}dt=\lim_{\epsilon\to0}\int_{a-\epsilon}^{a+\epsilon}\delta(t)e^{-st}dt=e^{-at}
\end{aligned}

$$

The Laplace transform of the Heaviside (step) function gives a second shifting law

$$
\begin{aligned}
    &\lap\{u(t-a)f(t-a)\}=\int_0^\infty u(t-a)f(t-a)e^{-st}dt=\int_a^\infty u(t-a)f(t-a)e^{-st}dt\\
    &\text{let }\tau=t-a\Ra d\tau=dt\\
    &t=\tau+a,\ \tau(a)=0,\ \lim_{t\to\infty}\tau=\lim_{A\to\infty}(A-a)=\infty\\
    &\lap\{u(t-a)f(t-a)\}=\int_0^\infty u(\tau)f(\tau)e^{-(\tau+a)s}d\tau=e^{-as}\int_0^\infty f(\tau)d\tau=e^{-as}\lap\brcurly{f(\tau)}\\
    &=e^{-as}\lap\brcurly{f(t)}
\end{aligned}

$$

Ex: Prove $\frac{du(t)}{dt}=\delta(t)$ using the Laplace transform

$$
\begin{aligned}
    &\frac{du(t)}{dt}=\delta(t)\\
    &\lap\brcurly{\frac{du(t)}{dt}}=s\lap\brcurly{u(t)}=s\bfrac{1}{s}=1\\
    &\frac{du(t)}{dt}=\lap^{-1}\brcurly{1}=\delta(t)
\end{aligned}

$$

Ex2:

$$
\begin{aligned}
    &\lap\brcurly{u(t)-u(t-1)}\\
    &=\int_{-\infty}^\infty(u(t)-u(t-1))e^{-st}dt=\int_0^\infty e^{-st}dt-\int_1^\infty e^{-st}dt\\
    &=-\frac{e^{-st}}{s}\eval_0^\infty+\frac{e^{-st}}{s}\eval_1^\infty=\frac{1}{s}-\frac{e^{-s}}{s},\ s>0
\end{aligned}

$$

## Z-Transform

The discrete-time analog to the Laplace transform is called the Z-transform
The Z-transform is defined to be

$$
\boxed{\mathcal{Z}\brcurly{x[n]}=\sum_{n=-\infty}^\infty x[n]z^{-n}}

$$

Ex: find the inverse Z-transform for $\frac{1}{3}<|z|<\frac{1}{2}$

$$
\begin{aligned}
    &F(z)=\frac{z}{z^2+\frac{5}{6}z+\frac{1}{6}}\\
    &\frac{1}{3}<|z|<\frac{1}{2}\\
    &F(z)=\frac{1/z}{1+\frac{5}{6}\frac{1}{z}+\frac{1}{6}\frac{1}{z^2}}=\frac{1/z}{(1+\frac{1}{3z})(1+\frac{1}{2z})}=\frac{A}{1+\frac{1}{3z}}+\frac{B}{1+\frac{1}{2z}}\\
    &A+B=0\Ra A=-B\\
    &\frac{A}{2}+\frac{B}{3}=1\Ra 3A+2B=6\\
    &-B=6\Ra A=6\\
    &F(z)=\frac{6}{1+\frac{1}{3z}}-\frac{6}{1+\frac{1}{2z}}\\
    &f[n]=6\brround{-\frac{1}{3}}^nu[n]+6\brround{-\frac{1}{2}}^nu[-n-1]
\end{aligned}

$$

Ex2: Solve the following difference equation

$$
\begin{aligned}
    &y[k+2]+2y[k+1]+y[k]=2f[k+2]-f[k+1]\\
    &Yz^2+2Yz+Y=2Fz^2-Fz\\
    &Y(z^2+2z+1)=F(2z^2-z)\\
    &H=\frac{Y}{F}=\frac{2z^2-z}{z^2+2z+1}=\frac{2-\frac{1}{z}}{1+\frac{2}{z}+\frac{1}{z^2}}=\frac{2-\frac{1}{z}}{(1+\frac{1}{z})^2}=\frac{2+2/z}{(1+\frac{1}{z})^2}-\frac{3/z}{(1+\frac{1}{z})^2}\\
    &H=\frac{2}{1+\frac{1}{z}}-3\frac{1/z}{(1+\frac{1}{z})^2}\\
    &h[n]=2(-1)^nu[n]+3n(-1)^nu[n]\\
    &h[n]=(2+3n)(-1)^nu[n]
\end{aligned}

$$
