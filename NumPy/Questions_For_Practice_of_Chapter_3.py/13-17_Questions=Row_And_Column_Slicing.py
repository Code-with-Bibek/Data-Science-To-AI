'''
Row & Column Slicing

Now use this 2D array:

arr2 = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])

Q14 — Row
Extract Row 1.
Expected:
[60, 70, 80, 90, 100]

Q15 — Multiple rows
Extract Rows 1 and 2, including all columns.
Expected:
[[ 60,  70,  80,  90, 100],
 [110, 120, 130, 140, 150]]

Q16 — Column
Extract Column 2.
Expected:
[30, 80, 130, 180]

Q17 — Multiple columns
Extract Columns 1 and 3.
Expected:
[[ 20,  40],
 [ 70,  90],
 [120, 140],
 [170, 190]]

Try to solve this using indexing/fancy indexing.

'''

import numpy as np

arr2 = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])

print("------extracting row 1------")
print(arr2[1])

print("------extracting row 1 & 2-----")
print(arr2[1:3])

print("------extracting column 1st------")
print(arr2[:, 0])

print("------extracting column 1 & 3------")
print(arr2[:, [1,3] ])      # here fancy indexing is applied because we cant simply extract col 1 and 3..
#                             so, we choose which column to extract and that is 1 and 3..(applicable in specific columns)