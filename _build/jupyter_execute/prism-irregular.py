# Tapered Triangular Prism

A regular prism is a solid with two triangular faces joined by three rectangular faces. 

Referring back to the diagram, this is clearly not a good description of the space. The aft and and forward end are triangular, but the remaining three faces are not rectangles; the remaining faces are irregular quadrilaterals.

One end of the prism, the aft end, or "base", is an isoscolese triangle, 27" by 48".
The other end of the prism, the forward end, is an isoscolese triangle, 8" by 10½".
The overall length is 46".

We can use calculus to sum an infinte sequence of triangles from the small forward end to the large aft end. This will compute the volume of the prism.

from myst_nb import glue
from sympy import *

## Approach

The volume, $V$, of a regular triangular prism is the area of the triangle at either end, $a$, integrated along the length of the prism, $l$.
Since the area is fixed, $a = \frac{h \times w}{2}$, we have this.


$$
V_p = \int_0^l a \text{d}z = \int_{0}^{l} \frac{{h \times w}}{{2}} \text{d}z = \frac{h \times w \times l}{2}
$$

In our case, we don't have the same triangle at each end with a fixed area. Instead, we must define area as a function of the offset from the forward end of the tank, $z$, $a = A(z)$, leading to a slightly more complex integral.

$$
V = \int_0^l A(z) \text{d}z
$$

When we compute the area at any point along the fore-to-aft axis of the tank, we can accurately compute the volume within that infinite sequence of triangles.

As background, here's the regular prism volume computation done with `sympy`. This shows how we can translate the math to Python, and use this confirm our results.

h, w, l, z = symbols("h w l z")

Integral(h*w/2, (z, 0, l))

Integral(h*w/2, (z, 0, l)).doit()

The first step, then, is to compute the area of any triangle from the forward-most $10 \tfrac{1}{2} \times 8$ to the aft-most $48 \times 27$.

## Measurements

Here are the essential measurements. We've defined these as a dictionary so we can substitute them into other equations. This allows us to change the measurements and get results.

var("h_f, h_a, w_f, w_a, l_fa")
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

Here are the essential width as a function of height, $w_h$, and area based on height, $A_h$, given a height of the triangle, $h$. 

h, w_h, l, A, z, A_h, A_z = symbols('h w_h l A z A_h A_z')

glue("wfh", Eq(w_h, factor(w_a/h_a * h), evaluate=False))
w_h = w_a/h_a * h

glue("area_h", Eq(A_h, Rational(1, 2) * h * w_h))

If we assume the fore and aft triangles are congruent, then the width, $w$, of the triangular face of the prism is a function of height, $h$.

```{glue:math} wfh
:label: width_from_height
```

Area, $A = \frac{1}{2} \times w \times h$, can then become a function of height, $h$.

```{glue:math} area_h
:label: area_from_height
```

Height, $h$, depends on the distance along the z-distance, meadured from the front of the tank.
The $z=0$ position is the forward edge, with a measured height of $h_f$. 
The $z=l_{fa}$ position is length from the forward edge to the aft edge; this has a measured height of $h_a$.

$$
h(z) = \frac{\Delta h}{\Delta z} \times z + h_f  = \frac{h_a-h_f}{l_{fa}} \times z + h_f
$$

We're assuming each of the two ends of the prism are congruent. This means we're imposing the aft width and height on the tank as a whole.

Is this a safe assumption? Spoiler alert: it isn't.

## Challenging the Assumption

We've assumed the shape of the forward and aft end of the tank are congruent triangles.
We're treating this as a triangular section that grows in size from a small 8" by 10½" triangle 
to a large 27" by 48" triangle. 

Since $\frac{8}{10 \tfrac{1}{2}} \neq \frac{27}{48}$, we can see the two triangles aren't congruent. This simplifies to $\frac{16}{21} \neq \frac{9}{16}$.

Here are the two triangle area computations based on height. $A_a(h)$ uses the aft height-to-width ratio,
$A_f(h)$ uses the forward height-to-width ratio. The $A(h)$ computations are quite different.

w_a_h = w_a/h_a * h
w_f_h = w_f/h_f * h

A_a_h = Rational(1, 2) * h * w_a_h
A_f_h = Rational(1, 2) * h * w_f_h

A_a_h.subs(measured)

A_a_h.subs(measured).evalf(3)

A_f_h.subs(measured)

A_f_h.subs(measured).evalf(3)

This means a simple $A(h)$ computation using the height, $h$, to compute the area isn't going to be very useful. We have two choices:

- Define area, $A(z)$ based on independent  $h(z)$ and $w(z)$. We can use $A(z) = \frac{h(z) \times w(z)}{2}$.

- Use a midpoint ratio of width to height, $r_m$, to define area. If $w = r_m \times h(z)$, then $A(z) = \frac{h(z) \times w}{2} = \frac{h(z)^2 \times r_m}{2}$.

Using a midpoint ratio is slightly simpler, but suffers from a problem of being inaccurate. The difference between $0.889h^2$ and $0.656h^2$ for small values of $h$ will be significant.

We need to compute the area using independent $h(z)$ and $w(z)$ functions.

## Computing the Area

We can use independent $h(z)$ and $w(z)$ functions to compute the overall area of each triangular section of the tank. 

We'll assume these are linear functions of the form $y = mx + b$. The slope, $m$, for height is $\frac{\Delta h}{\Delta z}$, and the intercept, $b$, is the height at the forward end, $h_f$. The width equation is similar.

This leads to two equations for $h_z$ and $w_z$, which are functions of the distance from the forward end, $z$. 

h_z = (h_a - h_f) / l_fa * z + h_f
glue("hfz", h_z)
w_z = (w_a - w_f) / l_fa * z + w_f
glue("wfz", w_z)

The height, $h(z) =$ {glue:}`hfz`. The width, $w(z) =$ {glue:}`wfz`.

A_z = factor(expand(Rational(1, 2) * h_z * w_z))
glue("area_z", A_z)

From $h(z)$ and $w(z)$, we can compute the area, $A_z$, as a function of the distance along the Z axis, $A(z) = \frac{1}{2} h(z) w(z) = $ {glue:}`area_z`.

This is a bit bulky. We can try to simplify it. First, however, we need to test it to be sure it produces proper area values.

We can evaluate the $h(z)$ and $w(z)$ functions at $z=0$ and $z=l_{fa}$ to be sure we've got them right.  We expect $h(0) = h_f$, $h(l_{fa}) = h_a$, $w(0) = w_f$, and $w(l_{fa}) = w_a$. We can also substitute the actual measurements to compute values for the fore and aft triangles to be sure they match the original measurements.

h_z.subs({z: 0}).evalf()

w_z.subs({z: 0}).evalf()

h_z.subs({z: l_fa}).evalf()

w_z.subs({z: l_fa}).evalf()

glue("h_f", h_z.subs(measured).subs({z: 0}).evalf())

glue("w_f", w_z.subs(measured).subs({z: 0}).evalf())

glue("h_a", h_z.subs(measured).subs({z: measured['l_fa']}).evalf())

glue("w_a", w_z.subs(measured).subs({z: measured['l_fa']}).evalf())

To confirm that we've done this right so far, let's check the model against reality.

At the forward end of the tank, this model predicts a triangle {glue:text}`w_f:.1f` across the top,
    with a height of {glue:text}`h_f:.1f`. This matches the $10.5 \times 8$ actual.
    
At the aft end of the tank, this model predicts a triangle {glue:text}`w_a:.1f` across the top,
    with a height of {glue:text}`h_a:.1f`. This matches the $48 \times 27$ actual, also.
    
Now that we can compute the shape of the triangle at each end of the space, we can compute the area, $A(z) = \frac{h(z) w(z)}{2}$. From this, we can then compute the volume.

## Volume based on overall length

The volume is the integral of the areas, $A(z)$ where $z$ varies from zero to the length of the prism, $l_fa$.

$$
V = \int_{0}^{l_{fa}} A(z) \text{d}z
$$

For a regular prism this is the $V_p = \frac{h l w}{2}$ formula. Our area is not simply $\frac{hw}{2}$, it's $A(z) = $ {glue:}`area_z`.

var("V")
glue("V", Eq(V, Integral(A_z, (z, 0, l_fa))))

The volume is computed with 

```{glue:math} V
:label: volume
```

We can substitute our measurements to get the volume. We'll apply the magical 231 cubic inch per gallon factor to get the volume in gallons of fresh water.

V = Integral(A_z.subs(measured), (z, 0, measured['l_fa']))
V_r = (V.doit()/231).limit_denominator(100)
f"{floor(V_r)} {frac(V_r)} gallons"

V_r.evalf(3)

## Simplified form

We can create decimal approximations for the fractions, and work with a direct computation that avoids integration. It's not clear that this is simpler. The generic `simplify()` is a poor choice.

var("l")
simplify(Integral((A_z/231).evalf(3), (z, 0, l_fa)))

This variation collects the various factors together, giving a closed form that's kind of workable. It involves terms based on $l_{fa}$, $l_{fa}^2$, and $l_{fa}^3$ which seems about right. This has a single constant term out front for the conversion from cubic inches to gallons.

(Using cubic centimeters and liters would avoid the magical 231 cubic inches per gallon.)


We can try and factor the polynomial , which leads to a much simpler-looking computation of volume.

V_c = factor(simplify(Integral((A_z/231).evalf(3), (z, 0, l_fa))))
V_c

This seems to be an elegant closed-form equatio for computing volume from the given measurements. We can recompute the volume as our measurements improve.

V_c.subs(measured)

## Matrices

Note that in the closed form volume equation, each term has some combination of $h_a$, $w_a$, $h_f$, and $w_f$, and unavoidable source of complexity. This "sum-of-combinations" suggests there may is a matrix expression to summarize this complexity. 

The following nonsense shows that we can reproduce the volume formula. The following nonsense lacks a clear interpretation. Because it happens to work, it's likely related to the proper scalar triple product (or box product). 

M_h = Matrix([h_a, h_f])
M_w = Matrix([w_a, w_f])

V_m = l_fa*(M_h*M_w.transpose()).vec().dot(Matrix([S(1)/3, S(1)/6, S(1)/6, S(1)/3]))/(2*231)
V_m

V_m.subs(measured).evalf(3)

We've left this in as a placeholder for future learning. This seems to be part of the parallelepiped dot product computation.