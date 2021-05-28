# Triangular Prism

A prism is a solid with two triangular faces joined by three rectangular faces. Referring back to the diagram, this is clearly not a good description of the space. The aft and and forward end are triangular, but the remaining three faces are not rectangles; the remaining faces are irregular quadrilaterals.

The volume of a triangular prism is the area of the triangle, $\frac{1}{2} h \times w$, times the overall length of the prism, $l$.

$$
V = \frac{\frac{h \times w}{2} \times l}{231 \textbf{ cu in/gal}}
$$

Our water tank has a large triangle aft and a small triangle forward. If we take the mean between these two extreme sizes, this should describe the space.

from myst_nb import glue

from sympy import *
h, w, l, V = symbols('h w l V')
glue("Vol1", Eq(V, (h * w) / 2 * l / 231, evaluate=False))

Here's a slightly simplified volume of a triangular prism, $V$, including the conversion from cubic inches to gallons.


```{glue:math} Vol1
:label: prism
```

Given a width, $w$, height, $h$, and the overall length, $l$, we know the volume of the space, $V$.

Since the triangles are isoscolese, we've measured their base edge and height. We often call the base edge the "width" of the triangle in the computations that follow.
If necessary, we can compute the other two edges, $e = \sqrt{h^2+{\frac{w}{2}}^2}$. 

## Middling the triangles

For this model of the space, we'll take the middle of the widths and the middle of the heights to describe a regular triangular prism.

The height at the  midpoint, $h_m$, and the width at the midpoint, $w_m$, are as follows:

var("h_f, h_a, w_f, w_a, l_fa")

h_m = Rational(1, 2)*(h_f + h_a)
w_m = Rational(1, 2)*(w_f + w_a)

It can help to see these expressions type set and simplified. Here's what the midpoints look like.

h_m

w_m

## Volume 

The mid-point volume, $V_m$, is computed from the midpoint height and width, $h_m$ and $w_m$, and the overall length, $l_{fa}$. We can expand the midpoint values with the fore-and-aft sizes
to get an overall computation given the five measurements we have.

V_m = ((h_m * w_m)/2 * l_fa) / 231
ratsimp(V_m)

This form, while kind of confusing-looking, has various $h \times w \times l$ terms, giving us confidence that this will be a proper volume computation in cubic inches based on all three dimensions.

## Measurements

The actual dimensions are as follows.
(And, yes, these differ slightly from sketches shown earlier, these are actual sizes.) These are subject to change, so we've collected them in one plce.

measured = {
    # Forward triangle, in inches
    "h_f": 8,
    "w_f": 10 + Rational(1, 2),

    # Aft triangle, in inches
    "h_a": 27,
    "w_a": 48,

    # Overall length from forward to aft, in inches.
    "l_fa": 46,
}

We can substitute the measured values into the volume formula to compute the volume of the space. We'll need to reformulate this slightly, since it's a complex-looking fraction.

V_m.subs(measured)

f"{floor(V_m.subs(measured))} {frac(V_m.subs(measured))} gallons"

We can define a formal equation for volume given the five measurements. This is something we can use to recompute volume as the measurements evolve.

glue("Vol_m", V_m.evalf(3))

Here's a the volume of a triangular prism, including the conversion from cubic inches to gallons.


```{glue:math} Vol_m
:label: prism_mid
```

Given the the following:

- width, $w_f$, and height, $h_f$, of the forward triangle, 
- width, $w_a$, and height, $h_a$, of the aft triangle,
- and the and the overall length, $l$.

Finally, here's the number of gallons as a decimal number.

V_m.evalf(4, measured)

We'll use this as a baseline to compare to the other estimates.  Next, we'll treat the volume as a regular tetrahedron, also. The math is a little more complex: we'll need to deduce the lengths of some edges from the available height and width values.