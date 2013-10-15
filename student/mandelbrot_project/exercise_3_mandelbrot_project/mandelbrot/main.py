from mandelbrot.model.core import mandelbrot_grid
from mandelbrot.ui.ascii import mandelbrot_ascii

n = 50
x_bounds1 = (-2, 1)
y_bounds1 = (-1.5, 1.5)

x_bounds2 = (-0.5, 0.3)
y_bounds2 = (0.55, 1.35)

escape_times1 = mandelbrot_grid(x_bounds1, y_bounds1, n)
escape_times2 = mandelbrot_grid(x_bounds2, y_bounds2, n)

mandelbrot_ascii(escape_times1,2)
mandelbrot_ascii(escape_times2,2)