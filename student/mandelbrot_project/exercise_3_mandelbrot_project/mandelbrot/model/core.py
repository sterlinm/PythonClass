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