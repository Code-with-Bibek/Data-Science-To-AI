'''
Consider:

marks = np.array([
    [80, 75, 90],
    [60, 85, 70],
    [95, 90, 88],
    [72, 65, 78]
])
Find:

shape
size
ndim
dtype

Calculate the average of every value in the entire array.

Find:
highest mark in the entire array
lowest mark in the entire array
total of all marks

Add 5 marks to every mark.

Multiply every mark by 2.

'''

import numpy as np 
marks = np.array([
    [80, 75, 90],
    [60, 85, 70],
    [95, 90, 88],
    [72, 65, 78]   # marks is of 2 dimension
])

print(marks)
print(marks.dtype)
print(marks.shape)
print(marks.size)
print(marks.ndim)


# print(np.max(marks))
# print(np.min(marks))
# print(np.sum(marks))

# print(marks * 2)

