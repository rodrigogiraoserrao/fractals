"""
Creates a black and white basic rendering of the Mandelbrot set.
c.f. https://mathspp.com/blog/creating-mandelbrot-set-animation
"""

import numpy as np
import PIL.Image

def is_mandelbrot(z, max_iterations=15):
    """Approximately determine if z is in the Mandelbrot set."""

    i = 0
    f = lambda w: w*w + z
    x = 0
    while i < max_iterations and abs(x) <= 2:
        i += 1
        x = f(x)
    return abs(x) <= 2

if __name__ == "__main__":
    pixel_width, pixel_height = 640, 480
    width = 3.2
    height = width*pixel_height/pixel_width
    centre = -0.5 + 0j
    cx, cy = centre.real, centre.imag
    left, right = cx - width/2, cx + width/2
    bot, top = cy - height/2, cy + height/2
    print(left, right, bot, top)

    array = 255*np.array([[
        is_mandelbrot(
            complex(left + x*width/pixel_width, top - y*height/pixel_height)
        ) for x in range(pixel_width)] for y in range(pixel_height)
    ], dtype=np.uint8)
    PIL.Image.fromarray(array).save("imgs/bwmandelbrot3.png")
