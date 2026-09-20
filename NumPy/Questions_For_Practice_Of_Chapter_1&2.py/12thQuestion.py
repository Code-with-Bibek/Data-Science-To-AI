'''
Create an array containing:

10, 20, 30, 40

Convert it to floating-point numbers and then calculate its mean.

'''

import numpy as np
array = np.array([10,20,30,40])
print(array.astype(float))

print(np.mean(array))