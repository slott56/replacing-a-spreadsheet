# Triangular Prism


```{note}
TODO: Subclass fractions.Fraction to create LaTeX rendering
as proper and improper fractions.
```

from myst_nb import glue

from fractions import Fraction
from math import floor

The triangular prism is the area of the triangle, $\frac{1}{2} h \times w$, times the overall length of the prism, $l$.

$$
V = \frac{\frac{1}{2} h \times w \times l}{231 \textbf{ cu in/gal}}
$$

We can state this using sympy to provide a formal definition,.

from sympy import *
h, w, l = symbols('h w l')

V = (Rational(1, 2) * h * w) * l / 231

glue("Vol1", V)

The volume of a triangular prism, converted from cubic inches to gallons.

```{glue:math} Vol1
:label: volume
```

Given a width, $w$, height, $h$, and the overall length, $l$, we know the volume of the space, $V$.

In this case, we'll take the middle of the width and the middle of the height to make a triangular prism.
The overall dimensions are as follows.

(And, yes, these differ slightly from sketches shown elsewhere, these are actual sizes.)

# Forward and aft height of the cross-section triangle, in inches
h_f = 8
h_a = 27

# Forward and aft "width" of the cross-section triangle, in inches.
w_f = 10 + Rational(1, 2)
w_a = 48

# Overall length from forward to aft, in inches.
l_fa = 46

# Midpoint height
h_m = Rational(1, 2)*(h_f + h_a)

# Midpoint width
w_m = Rational(1, 2)*(w_f + w_a)

V_m = Rational(1, 2)*h_m*w_m*l / 231
glue("Vol2", V_m)

glue("Actual", V_m.subs(l, l_fa))
glue("Actual_f", V_m.evalf(subs={l: l_fa}))

Which gets us to this:
    
```{glue:math} Vol2
:label: volume_m
```

Which evaluates to {glue:text}`Actual:.1f`, approximately {glue:text}`Actual_f:.1f` gallons.