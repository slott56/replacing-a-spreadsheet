# Regular Tetrahedron

A tetrahedron is a structure with four triangular faces.

Because the tank is flattened at the forward end, we could define a full-sized tetrahedron, and
then truncate a tiny tetrahedron from the front to better estimate the remaining volume.

A symmetric (or regular) Tetrahedron has a volume, $V$, based on the size of the edges, $a$.

$$
V = \frac{a^3}{6\sqrt{2}}
$$

In our case, the actual tank in question has a number of different edge lengths:

-  There are three edges on the aft triangular face. We know the width and height, and can compute the other two edges.

-  Of the three edges on the top triangular face, it shares an edge with the aft face. We know the width and height here, too, and can compute the remaining edges.

-  Finally, the seam along the keel is the sixth and final edge. We can compute this knowing the the top and aft form a right triangle. The hypotenuse of this triangle is the bottom seam.

We have accurate measurements of one edge and two heights. From these we can compute the others.

from myst_nb import glue

The measurements include some heights of isoscoles triangles, from which we need to work out the lengths of the edges.

The aft face, for example is 48 inches across the base, $w$, and 27 tall, $h$. We can divide this into two right triangles, and compute the remaining edge, $e$, length.

$$
e = \sqrt{{\tfrac{w}{2}}^2 + h^2}
$$

## Computing the six edges

We've measured one edge and two heights:

- The the top of the aft section edge is 48 inches.

- The height of the base is 27 inches.

- The height of the top is 46 inces.

From these, we can compute the remaining edges applying the rule $e^2 = {\frac{w}{2}}^2 + h^2$. This works because each isoscolese triangle is two right triangles.

from sympy import *
a_1, a_2, a_3, a_4, a_5, a_6 = symbols('a_1 a_2 a_3 a_4 a_5 a_6')

# The "width" (actually the top) of the aft triangle.
a_1 = 48

# The two sides of the aft triangle, given a height of 27".
a_2 = sqrt((Rational(1, 2)*a_1)**2 + S(27)**2)
a_3 = a_2

If the top were not truncated, it would be a triangle with a base of 48 inches, and height that's a little more than 46 inches. We'll stick with the truncated measurement of 46 inches, rather than estimate the full, untruncated height.

# The two edges of the top, given a height of 46".
a_4 = sqrt((Rational(1, 2)*a_1)**2 + S(46)**2)
a_5 = a_4

The seam along the bottom is the hypotenuse of a 46" by 27" right triangle.

a_6 = sqrt(S(27)**2 + S(46)**2)

We can take the mean of these edges to estimate a regular tetrahedron that has a similar volume.

m = (a_1 + a_2 + a_3 + a_4 + a_5 + a_6)/6

glue("edge", radsimp(m))
glue("edge_f", m.evalf(4))

This suggests an edge length of {glue:}`edge`, 
which is approximately {glue:text}`edge_f:.2f` inches.

The volume needs to be converted from cubic inches to gallons, using the constant $231 \frac{\textbf{cu in}}{\textbf{gal}}$

V_r = m**3 / (6 * sqrt(2)) / 231

var("V")
glue("V_r", Eq(V, radsimp(V_r)))
glue("V_r_f", V_r.evalf(4))

This estimates a volume of {glue:}`V_r`, which is approximately {glue:text}`V_r_f:.2f` gallons. 
    
This is close to the triangular prism estimate, so this is also a useful guage of the space.

## Smallest and Largest

Does it help to bracket this estimate with two other estimates, the least, $l$, and the greatest, $g$? If we split these, it's tolerably close to other estimates.

l = min([a_1, a_2, a_3, a_4, a_5, a_6])
g = max([a_1, a_2, a_3, a_4, a_5, a_6])
V_l = l**3 / (6 * sqrt(2)) / 231
V_g = g**3 / (6 * sqrt(2)) / 231

glue("l", l)
glue("g", g)
glue("V_l", V_l)
glue("V_l_f", V_l.evalf(4))
glue("V_g", V_g)
glue("V_g_f", V_g.evalf(4))
glue("V_lg_f", (V_l.evalf(4)+V_g.evalf(4))/2)

This varies from {glue:}`V_l` to {glue:}`V_g`. 
These extemes are approximately {glue:text}`V_l_f:.2f` gallons to {glue:text}`V_g_f:.2f` gallons. 
The midpoint, {glue:text}`V_lg_f:.2f` gallons, also seems to agree with other estimates.

## Truncation

There's a small 9" tetrahedron we could truncate from this volume to improve accuracy. What's its volume?

V_t = 9**3 / (6 * sqrt(2)) / 231

glue("V_t", V_t)
glue("V_t_f", V_t.evalf(4))

This tiny bit of space is {glue:}`V_t`, which is approximately {glue:text}`V_t_f:.2f` gallons. 
 It's negligible, however, being less than a gallon, and we can safely ignore it.

In the next section, we'll apply some calculus to compute the volume as an infnite some of triangles, each a slightly different shape. We can model the taper from fore to aft, and use this to compute a more accurate volume.

