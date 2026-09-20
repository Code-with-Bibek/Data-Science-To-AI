'''
To remove an element from a certain index , we use delete..

syntax_for_1D_array = np.delete(array_name , index_no)
syntax_for_2D_array = np.delete(array_name , index_no , axis = 0/1/none)

'''

import numpy as np


# ==============================
# 1. DELETE FROM A 1D ARRAY
# ==============================

arr = np.array([10, 20, 30, 40, 50])

result = np.delete(arr, 2)

print(result)

# [10 20 40 50]

# index 2 was:
# [10, 20, 30, 40, 50]
#          ↑
#        index 2
#
# So 30 is removed.


# ==============================
# 2. DELETE MULTIPLE ELEMENTS
# ==============================

result = np.delete(arr, [1, 3])

print(result)

# [10 30 50]

# index 1 → 20 removed
# index 3 → 40 removed


# ==============================
# 3. DELETE A ROW → axis=0
# ==============================

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

result = np.delete(arr2, 1, axis=0)

print(result)

# [[1 2 3]
#  [7 8 9]]

# axis=0 means ROW
#
# row index 1:
# [4 5 6]
#    ↑
# removed


# ==============================
# 4. DELETE A COLUMN → axis=1
# ==============================

result = np.delete(arr2, 1, axis=1)

print(result)

# [[1 3]
#  [4 6]
#  [7 9]]

# axis=1 means COLUMN
#
# column index 1:
#
# 2
# 5
# 8
#
# is removed.


# ==============================
# 5. DELETE MULTIPLE ROWS
# ==============================

result = np.delete(arr2, [0, 2], axis=0)

print(result)

# [[4 5 6]]

# row 0 → removed
# row 2 → removed


# ==============================
# 6. DELETE MULTIPLE COLUMNS
# ==============================

result = np.delete(arr2, [0, 2], axis=1)

print(result)

# [[2]
#  [5]
#  [8]]

# column 0 → removed
# column 2 → removed


# ==============================
# 7. DELETE WITHOUT axis
# ==============================

result = np.delete(arr2, 2)

print(result)

# [1 2 3 4 6 7 8 9]

# Without axis:
# NumPy treats the 2D array as 1D
# and deletes from the flattened array.


# ==============================
# 8. ORIGINAL ARRAY DOES NOT CHANGE
# ==============================

arr = np.array([10, 20, 30])

result = np.delete(arr, 1)

print(arr)

# [10 20 30]

print(result)

# [10 30]


# ==============================
# SYNTAX
# ==============================

# np.delete(array, index, axis=None)
#
# array → original array
# index → index/indices to remove
# axis=None → flatten and delete
# axis=0 → delete rows
# axis=1 → delete columns
