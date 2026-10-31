# Functions of Multiple Variables

<!-- Source: [Sections/Multivariable_Calculus/Functions_of_Multiple_Variables.tex](../../Sections/Multivariable_Calculus/Functions_of_Multiple_Variables.tex) -->

## Classification of 3D Surfaces

So far, we have only been working in the 2D plane with functions of 2 variables: $y=f(x)$. We can extend the same ideas to higher dimensions: A function $z=f(x,y)$ will form a surface in 3 dimensions and a function $w=f(x,y,z)$ will span 4 dimensions. While we are still able to analyze the behaviors of higher dimensional systems, we will often stick to functions of 3 variables for the sake of visualization.

As with 2D, there are a few common functions that you should recognize and be able to plot.

- Planes
    These are of the form $z=ax+by+c$ (as seen in a previous section)
```{figure} ../figures/original/Math217Pictures/planeGraph.png
:name: fig-differential-planegraph
:alt: Existing mathematics notes figure (planeGraph). Review provenance before publication.
:width: 85%

Existing source figure: `Images/Math217Pictures/planeGraph.png`. It is preserved for review and is not assumed publication-cleared.
```

- Spheres
    These are of the form $x^2+y^2+z^2=r^2$ (similar to a circle in 2D)
```{figure} ../figures/original/Math217Pictures/sphereGraph.png
:name: fig-differential-spheregraph
:alt: Existing mathematics notes figure (sphereGraph). Review provenance before publication.
:width: 85%

Existing source figure: `Images/Math217Pictures/sphereGraph.png`. It is preserved for review and is not assumed publication-cleared.
```

- Cylinders
    These are of the form $x^2+y^2=1$. Note that this is a function defined in terms of only $x$ and $y$ so it will be the same for all $z$.
```{figure} ../figures/original/Math217Pictures/cylinderGraph.png
:name: fig-differential-cylindergraph
:alt: Existing mathematics notes figure (cylinderGraph). Review provenance before publication.
:width: 85%

Existing source figure: `Images/Math217Pictures/cylinderGraph.png`. It is preserved for review and is not assumed publication-cleared.
```

- Cones
    These are of the form $z=\sqrt{x^2+y^2}$ for a one-sided cone and $z^2=x^2+y^2$ for a two-sided cone.
```{figure} ../figures/original/Math217Pictures/coneGraph.png
:name: fig-differential-conegraph
:alt: Existing mathematics notes figure (coneGraph). Review provenance before publication.
:width: 85%

Existing source figure: `Images/Math217Pictures/coneGraph.png`. It is preserved for review and is not assumed publication-cleared.
```

- Paraboloids
    These are of the form $z=x^2+y^2$
```{figure} ../figures/original/Math217Pictures/parabaloidGraph.png
:name: fig-differential-parabaloidgraph
:alt: Existing mathematics notes figure (parabaloidGraph). Review provenance before publication.
:width: 85%

Existing source figure: `Images/Math217Pictures/parabaloidGraph.png`. It is preserved for review and is not assumed publication-cleared.
```

- Saddles
    These are of the form $z=x^2-y^2$
```{figure} ../figures/original/Math217Pictures/saddleGraph.png
:name: fig-differential-saddlegraph
:alt: Existing mathematics notes figure (saddleGraph). Review provenance before publication.
:width: 85%

Existing source figure: `Images/Math217Pictures/saddleGraph.png`. It is preserved for review and is not assumed publication-cleared.
```


There are many more functions not mentioned such as ellipsoids, hyperboloids, and parabolic cylinders but this should be enough to begin to get an idea of what 3D functions look like.

## Sketching Surfaces

Sketching surfaces in 3D is often trickier than in 2D but there are a few useful tricks to get an idea what the surface looks like.
One of the most useful ones is level curves. This is where if we have a function $z=f(x,y)$, we set $z$ to be a constant and draw the curve on the xy-plane for varying $z$ (in 2D these are called contour plots).
In short, a contour plot is an overlay of lines of $f(x,y)=k$ plotted on the xy-plane. The rate of greatest change (the gradient) is always perpundicular to the contour lines.
Similarly, a level surface is the overlay of surfaces of $f(x,y,z)=k$ plotted in 3-space (or higher).
Ex: $z=x^2+4y^2-2x+2$
```{figure} ../figures/original/Math217Pictures/contourPlot.png
:name: fig-differential-contourplot
:alt: Existing mathematics notes figure (contourPlot). Review provenance before publication.
:width: 85%

Existing source figure: `Images/Math217Pictures/contourPlot.png`. It is preserved for review and is not assumed publication-cleared.
```

This becomes increasingly useful for visualizing functions in 4 dimensions as we can define their level curves as 3D functions.
Ex: $F=x^2+y^2+z^2$
```{figure} ../figures/original/Math217Pictures/levelCurves.png
:name: fig-differential-levelcurves
:alt: Existing mathematics notes figure (levelCurves). Review provenance before publication.
:width: 85%

Existing source figure: `Images/Math217Pictures/levelCurves.png`. It is preserved for review and is not assumed publication-cleared.
```

Sometimes it can be useful to sketch contour plots in multiple planes as it may be easier or give different perspectives.
Other useful tricks in sketching curves that will be seen later may be to take the gradient (as it gives a vector field normal to the level curves at all points) or to find the critical points of the function.
