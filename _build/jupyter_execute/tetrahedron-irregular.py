# Irregular Tetrahedron

A tetrahedron is a structure with four triangular faces.

In our case, we have some irregularity.

The "base" is an isoscolese triangle, 27 by 48.
The "top" of the space is isoscolese triangle, 46 by 48.

We can assume the shape from top to base is consistent, allowing us to work out a volume computation based on 
the distance from top to base.  There's a triangular section that grows in size from a small 10.5 x 8 triangle 
to a large 27 x 48 triangle.


from myst_nb import glue
from sympy import *

# Forward and aft height of the cross-section triangle, in inches
h_f = S(8)
h_a = S(27)

# Forward and aft "width" of the cross-section triangle, in inches.
w_f = S(10.5)
w_a = S(48)

# Overall length from forward to aft, in inches.
l_fa = S(46)

h, w, l, A, z, A_h, A_z = symbols('h w l A z A_h A_z')
w = w_a/h_a * h
glue("wfh", w)

A_h = Rational(1, 2) * h * w 
glue("area_h", A_h)

Width, $w$, is a function of height, $h$.

```{glue:math} wfh
:label: width_from_height
```

Area, $A = \frac{1}{2} \times w \times h$, can then become a function of height, $h$.

```{glue:math} area_h
:label: area_from_height
```

Height, $h$, is a function of the z-distance from the front of the tank.
The $z=0$ position is the forward edge, with a height of $h_f$. 
The $z=l_{fa}$ position is the aft edge, with a height of $h_a$.

$$
h(z) = \frac{\Delta h}{\Delta z} \times z + h_f
$$ 

$$
h(z) = \frac{h_a-h_f}{l_{fa}} \times z + h_f
$$

h_z = (h_a - h_f) / l_fa * z + h_f
glue("hfz", h_z)
w_z = w_a/h_a * h_z
glue("wfz", w_z)
A_z = expand(Rational(1, 2) * h_z * w_z)
glue("area_z", A_z)


This means area is a function of the distance along the Z axis.

The height, $h(z) =$ {glue:}`hfz`. The width, $w(z) =$ {glue:}`wfz`.

The area, $A(z) =$ {glue:}`area_z`.

glue("h_f", h_z.subs({z: 0}).evalf())
glue("w_f", w_z.subs({z: 0}).evalf())
glue("h_a", h_z.subs({z: l_fa}).evalf())
glue("w_a", w_z.subs({z: l_fa}).evalf())


To confirm that we've done this right so far, let's check the model against reality.

At the forward end of the tank, this model predicts a triangle {glue:text}`w_f:.1f` across the top,
    with a height of {glue:text}`h_f:.1f`. This is a close fit against the 10.5 x 8.
    
At the aft end of the tank, this model predicts a triangle {glue:text}`w_a:.1f` across the top,
    with a height of {glue:text}`h_a:.1f`. This is the exact size of the aft end.


The volume is the integral of the areas along the length of the prism.

$$
V_p = \int_{0}^{l} \frac{{h \times w}}{{2}} z dz
$$

For a regular prism this is the $A = \frac{1}{2}h w \times l$ formula. Our area is not, however, simply $\frac{1}{2}  h w$, it's $A(z) = $ {glue:}`area_z`.

Our volume, in cubic inches, is defined as a definite integral of $A(z)$ from $z = 0$ to $z = 46$.

V = Integral(A_z, (z, 0, l_fa))

glue("V", V)

The volume is computed with 

```{glue:math} V
:label: volume
```


V_r = (V.doit()/231).limit_denominator(100)
f"{floor(V_r)} {frac(V_r)} gallons"

V_r.evalf(3)

