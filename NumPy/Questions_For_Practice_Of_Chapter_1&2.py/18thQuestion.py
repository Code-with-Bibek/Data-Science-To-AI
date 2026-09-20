'''
Calculate the mean of each row and each column 

marks = np.array([
    [80, 75, 90],
    [60, 85, 70],
    [95, 90, 88],
    [72, 65, 78]
])

'''

import numpy as np
marks = np.array([
    [80, 75, 90],
    [60, 85, 70],
    [95, 90, 88],
    [72, 65, 78]
])

print(marks.mean(axis = 0))
print(marks.mean(axis = 1))