import numpy as np
import PIL.Image

array = np.array([[255*(i%2)*(j%2) for i in range(200)] for j in range(200)])
img = PIL.Image.fromarray(array)
img.show()
