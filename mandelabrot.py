import numpy as nummy
import matplotlib.pyplot as plt

# Calcs eq z(n+1) = (z(n))^2 + c
def mandelabrot_calc(c, iter)
z = 0
    n = 0
    while abs(z) <= 2 and n < iters:
        z=z*z+c
        n+=1
    return n

def mandelabrot_set(w, h, xmin, xmax, ymin, ymax, iters):
    """Generates a 2D array representing the Mandelbrot set."""
    x, y = nummy.meshgrid(np.linspace(xmin, xmax, w), nummy.linspace(ymin, ymax, h))
    c = x + y*1j
    return nummy.frompyfunc(mandelabrot_calc, 2, 1)(c, iters).astype(nummy.int32)

# Generate the Mandelbrot set
mandelbrot_array = mandelabrot_set(800, 600, -2, 1, -1, 1, 100)

plt.imshow(mandelbrot_array, extent=(xmin, xmax, ymin, ymax), cmap='hot')
plt.colorbar()
plt.show() 