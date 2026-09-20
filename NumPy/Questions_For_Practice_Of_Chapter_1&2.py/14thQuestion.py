'''
You have:

marks = np.array([45, 67, 89, 72, 56])

Add 5 marks to every student using NumPy.

Using the same marks array, subtract 10 marks from every student.

Then calculate the new:

minimum
maximum
mean

'''

import numpy as np
marks = np.array([45, 67, 89, 72, 56])
arr_add = marks + 5

print(arr_add) 
print(np.min(arr_add))
print(np.max(arr_add))

arr_sub = marks - 10
print(arr_sub)
print(np.min(arr_sub))
print(np.max(arr_sub))

