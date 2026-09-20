'''
Create a 2D array:

1  2  3
4  5  6

Find:

shape
size
number of dimensions
data type

'''

import numpy as np
array = np.array([[1,2,3],
                  [4,5,6]])

print(array.shape)
print(array.size)
print(array.ndim)
print(array.dtype)