""" 
Calculate Derivative
--------------------

Topics: NumPy array indexing and array math.

Use array slicing and math operations to calculate the
numerical derivative of ``sin`` from 0 to ``2*pi``.  There is no
need to use a 'for' loop for this.

Plot the resulting values and compare to ``cos``.

Bonus
~~~~~

Implement integration of the same function using Riemann sums or the
trapezoidal rule.

See :ref:`calc-derivative-solution`.
"""
from numpy import linspace, pi, sin, cos, cumsum
from matplotlib.pyplot import plot, show, subplot, legend, title, draw

# calculate the sin() function on evenly spaced data.
x = linspace(0,2*pi,101)
y = sin(x)

subplot(3,1,1)
plot(x,y)

dy = y[1:]-y[:-1]
dx = x[1:]-x[:-1]

deriv_sin = dy / dx
subplot(3,1,2)
plot(x[:-1],deriv_sin)
subplot(3,1,3)
plot(x,cos(x))
draw()
show()