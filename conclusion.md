# Summary and Conclusion

We've looked at a number of alternatives for estimating the volume of the V-berth fuel tank.
Each of these uses some slight simplifications of the geometry to make the math a little simpler.

-   **Regular Triangular Prism**. We picked a mid-point between the two triangular faces and used this to estimate the overall size. The resulting volume was 50.97 gallons.
    
-   **Regular Tetrahedron**. We used two approaches here. 

    - We picked a mid-point among the various edges and used this to estimate the size. The resulting volume was 50.4 gallons.

    - We used the largest and smallest edges to compute two sizes and took the mid-point. The resulting volume was 50.74 gallons.


-   **Irregular Triangular Prism**. The tank is a prism that tapers from aft to forward. We can describe this taper as a function of the distance along the fore-and-aft axis of the tank. The  resulting value was 56.9 gallons.

The simplifying assumption of congruent triangles at each end of the tank is implicit in the initial methods. This is exposed by the irregular prism computation, where we computed areas and volumes with fewer simplifying assumptions.

The use of `sympy` makes it easy to perform the algebraic work and then confirm the formula with measured values.

The use of Jupyter Lab makes it possible to have a spreadsheet-like environment where we can update a measurement and see the resulting computation. We can also confirm that our computations are correct, and even adapt them as we change our assumptions.
