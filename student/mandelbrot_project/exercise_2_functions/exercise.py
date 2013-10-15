"""
Mandelbrot set functions
------------------------

Using the code of exercise 1, create two functions:

1) The first takes bounds over x and y, and the size of the grid,
   and returns the escape times at those coordinates.
   Set the default grid size to 40 .

   For example, a call to this function might look like this:
      escape_times = mandelbrot_grid((-2, 1), (-1.5, 1.5), 40)

2) The second takes a grid of escape times and returns a string
   with the ASCII art representation.

   For example, a call to this function might look like this:
      mandel_ascii = times_to_ascii(escape_times)

3) Use the two functions to print a 50x50 Mandelbrot set using these
   grids:

   x_bounds = (-2, 1)
   y_bounds = (-1.5, 1.5)

   and
   
   x_bounds = (-0.5, 0.3)
   y_bounds = (0.55, 1.35)

"""

def mandelbrot_escape(x, y, n=100):
    """Mandelbrot set escape time algorithm for a given c = x + i*y coordinate.

    Return the number of iterations necessary to escape abouve a fixed threshold
    (4.0) by repeatedly applying the formula:

    z_0 = 0
    z_n = z_{n-1} ^ 2 + c

    If the formula did not escape after `n` iterations, return -1 .

    Parameters
    ----------
    x, y -- float
        Real and imaginary part of the complex number z.

    n -- integer
        Maximum number of iterations.
    """

    z_x = 0
    z_y = 0

    for i in range(n):
        z_x, z_y = z_x**2 - z_y**2 + x,  2*z_x*z_y + y

        # If we are diverging, return the number of iterations.
        if z_x**2 + z_y**2 >= 4.0:
            break
    else:
        i = -1

    return i

def mandelbrot_grid(x_bounds=(-1.0,1.0), y_bounds=(-1.0,1.0), n=40):
    x_min, x_max = x_bounds
    y_min, y_max = y_bounds
    
    x_range = x_max - x_min
    x_step = x_range / (n*1.0 - 1)
    
    y_range = y_max - y_min
    y_step = y_range / (n*1.0 - 1)
    
    current_x = x_min
    current_y = y_max
    grid = []
    for y in range(n):
        grid.append([])
        for x in range(n):
            grid[-1].append(mandelbrot_escape(current_x, current_y))
            current_x += x_step
        current_y -= y_step
        current_x = x_min
    
    return grid

def mandelbrot_ascii(escape_times,multiplier=3):
    translation_table = [' ', '.', ':', 'o', 'O', '0', 'H', 'X', '#']
    mandel_ascii = ''
    for row in escape_times:
        for el in row:
            idx = min(el+1, len(translation_table)-1)
            mandel_ascii += translation_table[idx] * 3
        mandel_ascii += '\n'
    print mandel_ascii

n = 50
x_bounds1 = (-2, 1)
y_bounds1 = (-1.5, 1.5)

x_bounds2 = (-0.5, 0.3)
y_bounds2 = (0.55, 1.35)

escape_times1 = mandelbrot_grid(x_bounds1, y_bounds1, n)
escape_times2 = mandelbrot_grid(x_bounds2, y_bounds2, n)

mandelbrot_ascii(escape_times1,2)
mandelbrot_ascii(escape_times2,2)