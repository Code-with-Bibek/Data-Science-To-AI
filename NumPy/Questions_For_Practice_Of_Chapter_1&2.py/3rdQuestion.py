'''
Create a 3D array containing:

[
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

Without manually counting, use NumPy properties to determine:

shape
size
ndim

'''

import numpy as np
array = np.array([[[1,2],[3,4]],
                  [[5,6],[7,8]]])

print(array.shape)
print(array.size)
print(array.ndim)
print(array.dtype)