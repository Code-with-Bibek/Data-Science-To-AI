
import numpy as np

# ==============================
# 1. APPEND TO A 1D ARRAY
# ==============================

arr = np.array([10, 20, 30, 40])

result = np.append(arr, 50)

print(result)
# [10 20 30 40 50]


# ==============================
# 2. APPEND MULTIPLE VALUES
# ==============================

result = np.append(arr, [50, 60, 70])

print(result)
# [10 20 30 40 50 60 70]


# ==============================
# 3. APPEND TO A 2D ARRAY
# ==============================

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# ------------------------------
# Add a ROW → axis=0
# ------------------------------

new_row = [[10, 11, 12]]

result = np.append(arr2, new_row, axis=0)

print(result)

# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]


# ------------------------------
# Add a COLUMN → axis=1
# ------------------------------

new_column = [[10],
              [11],
              [12]]

result = np.append(arr2, new_column, axis=1)

print(result)

# [[ 1  2  3 10]
#  [ 4  5  6 11]
#  [ 7  8  9 12]]


# ==============================
# 4. WITHOUT axis
# ==============================

result = np.append(arr2, [10, 11, 12])

print(result)

# [ 1  2  3  4  5  6  7  8  9 10 11 12 ]

# Without axis, NumPy treats the array as 1D
# (it effectively flattens it).


# ==============================
# 5. ORIGINAL ARRAY DOES NOT CHANGE
# ==============================

arr = np.array([10, 20, 30])

result = np.append(arr, 40)

print(arr)
# [10 20 30]

print(result)
# [10 20 30 40]


# ==============================
# IMPORTANT SHAPE RULE
# ==============================

# If axis=0 → adding ROW
#
# Original:
# shape = (3, 3)
#
# New row must have 3 columns:
# [[10, 11, 12]]


# If axis=1 → adding COLUMN
#
# Original:
# shape = (3, 3)
#
# New column must have 3 rows:
# [[10],
#  [11],
#  [12]]


# ==============================
# SYNTAX
# ==============================

# np.append(array, values, axis=None)
#
# array → original array
# values → data you want to add
# axis=None → flatten and append
# axis=0 → append rows
# axis=1 → append columns

print("---------------Appending-----------------")

arr2_d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(np.append(arr2_d,[[13,14,15]],axis=0))
print(np.append(arr2_d, [[13],[14],[15]], axis=1))