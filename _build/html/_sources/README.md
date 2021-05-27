# Applied math and a spreadsheet-like environment

This is an example of a fairly complex computation that benefits from a spreadsheet-like
capability.

We want to change the measurements, and recompute a very complex estimation.

This use case of "enter data -- see resulting computation" works nicely for spreadsheets
where the computations aren't too tricky. We can examine them for correctness, and trust
they are working.

When the computations become non-trivial, a spreadsheet can be challenging to
validate and debug.
We may not be able to simply examine a computation cell to be sure it's right.

This is where Jupyter Lab can be a dramatic improvement over a spreadsheet.
In these examples we'll do complex symbolic math ("algebra") as well as ordinary
applied math to compute useful values.


# Components Required

You'll need Python, of course. You may want to use Miniconda to help install Python.

    https://docs.conda.io/en/latest/miniconda.html
    
With miniconda, you can build your Python environment.

    conda create --name model python=3.9
    conda activate model

Once you have Python, you can then install the suite of tools for working 
with more advanced symbolic math, Sympy https://docs.sympy.org/latest/index.html

    python -m pip install sympy jupyter-lab

With the Jupyter lab you can launch the `.ipynb` notebooks to 
make changes, and do computations. Like a spreadsheet. But
with real code and real math.

The final publication of a report or book can be done with two additional tools.

Jupyter {Book} https://jupyterbook.org/intro.html

    python -m pip install jupyter-book

Requires MyST{NB} https://myst-nb.readthedocs.io/en/latest/

    python -m pip install myst-nb
    
# Document Production

Run the following:

    jupyter-book build .
    cp _build/html docs

This will create the HTML version. 

To make a PDF, use the following.

    jupyter-book build . --builder pdflatex

(This generally relies on having TeX installed.)

Fair warning: the structure used in this first
release doesn't look very good in a PDF. An
outline that's accetable in HTML can turn out
to be weirdly structured when viewed as a PDF.
