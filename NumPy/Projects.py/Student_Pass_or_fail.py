'''
Program 3 — Student Pass/Fail

Create a NumPy array containing marks of 10 students.

For example:

[45, 78, 32, 91, 56, 40, 67, 29, 84, 73]

Use Python logic to determine how many students:

passed
failed

Assume:

pass >= 40

Don't worry about fancy NumPy techniques yet. Use the Python knowledge you already have.

'''

import numpy as np

array = np.array([23,35,56,78,12,45,67,90,31,14])

for i in range(10):
    count = 0
    if(array[i] > 40):
        count += 1
    else: pass


print("The number of passed students are : " , count)
        