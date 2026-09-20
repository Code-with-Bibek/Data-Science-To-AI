import numpy as np
# ==========================================
# SPLITTING IN NUMPY
# ==========================================

# Splitting means BREAKING an array into
# smaller arrays (parts).


# ------------------------------------------
# 1. np.split()
# ------------------------------------------

# split() divides an array into equal parts.

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.split(arr, 3)

print(result)

# [array([10, 20]),
#  array([30, 40]),
#  array([50, 60])]

# 3 means:
# Divide the array into 3 equal parts.


# ------------------------------------------
# 2. np.vsplit()
# ------------------------------------------

# vsplit = vertical split
# Used with 2D arrays.
# Splits the ROWS.

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])
result = np.vsplit(arr, 2)

print(result)

# [array([[1, 2],
#         [3, 4]]),
#
#  array([[5, 6],
#         [7, 8]])]


# ------------------------------------------
# 3. np.hsplit()
# ------------------------------------------

# hsplit = horizontal split
# Used with 2D arrays.
# Splits the COLUMNS.

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

result = np.hsplit(arr, 2)

print(result)

# [array([[1, 2],
#         [5, 6]]),
#
#  array([[3, 4],
#         [7, 8]])]