'''
Syntax_For_Insert = np.insert(array_name , index_no , value , axis = none)

HERE , 
index_no = where we want to insert our new value
value = actual value
axis = 0 ; if it is for 2-D arrray

'''

import numpy as np

arr2_d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print("----------Inserting-------------")
print(np.insert(arr2_d,2,[10,11,12],axis=0))
print(np.insert(arr2_d,2,[13,14,15],axis=1))

# AI generated note--->


import numpy as np


# ==============================
# 1. INSERT INTO A 1D ARRAY
# ==============================

arr = np.array([10, 20, 30, 40])

result = np.insert(arr, 2, 99)

print(result)
# [10 20 99 30 40]

# index 2 means:
# insert 99 BEFORE the element currently at index 2
#
# Index:
#          0   1   2   3
# Original [10, 20, 30, 40]
#
# Insert 99 at index 2:
#          0   1   2   3   4
# Result   [10, 20, 99, 30, 40]


# ==============================
# 2. INSERT MULTIPLE VALUES
# ==============================

result = np.insert(arr, 2, [99, 100])

print(result)
# [10 20 99 100 30 40]


# ==============================
# 3. INSERT INTO A 2D ARRAY
# ==============================

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# ------------------------------
# INSERT A ROW → axis=0
# ------------------------------

new_row = [10, 11, 12]

result = np.insert(arr2, 1, new_row, axis=0)

print(result)

# [[ 1  2  3]
#  [10 11 12]
#  [ 4  5  6]
#  [ 7  8  9]]

# index 1 means:
# insert the new row BEFORE row index 1.


# ------------------------------
# INSERT A COLUMN → axis=1
# ------------------------------

new_column = [10, 11, 12]

result = np.insert(arr2, 1, new_column, axis=1)

print(result)

# [[ 1 10  2  3]
#  [ 4 11  5  6]
#  [ 7 12  8  9]]

# index 1 means:
# insert the new column BEFORE column index 1.


# ==============================
# 4. INSERT WITHOUT axis
# ==============================

result = np.insert(arr2, 2, 99)

print(result)

# [ 1  2 99  3  4  5  6  7  8  9 ]

# Without axis:
# NumPy treats the array as 1D
# and inserts into the flattened array.


# ==============================
# 5. ORIGINAL ARRAY DOES NOT CHANGE
# ==============================

arr = np.array([10, 20, 30])

result = np.insert(arr, 1, 99)

print(arr)
# [10 20 30]

print(result)
# [10 99 20 30]


# ==============================
# IMPORTANT SHAPE RULE
# ==============================

# Suppose the original array is:
#
# shape = (3, 3)


# axis=0 → inserting a ROW
#
# The new row needs 3 values:
#
# [10, 11, 12]


# axis=1 → inserting a COLUMN
#
# The new column needs 3 values:
#
# [10, 11, 12]


# ==============================
# SYNTAX
# ==============================

# np.insert(array, index, values, axis=None)
#
# array  → original array
# index  → position where data is inserted
# values → data you want to insert
# axis=None → treat array as 1D
# axis=0 → insert rows
# axis=1 → insert columns

