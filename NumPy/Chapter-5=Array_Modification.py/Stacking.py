'''
syntax_for_2d_array = np.vstack((arr1, arr2))

'''

# ==========================================
# STACKING IN NUMPY
# ==========================================

# Stacking means JOINING arrays together.


# ------------------------------------------
# 1. vstack() → Vertical Stacking
# ------------------------------------------

# vstack = vertical stack
# It joins arrays from TOP to BOTTOM.
# Rows increase.

import numpy as np 

# Example:

arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

result = np.vstack((arr1, arr2))

print(result)

# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]


# ------------------------------------------
# 2. hstack() → Horizontal Stacking
# ------------------------------------------

# hstack = horizontal stack
# It joins arrays from LEFT to RIGHT.
# Columns increase.

result = np.hstack((arr1, arr2))

print(result)

# [[1 2 5 6]
#  [3 4 7 8]]


# ------------------------------------------
# MEMORY TRICK
# ------------------------------------------

# vstack → V → Vertical → ↓
#
# hstack → H → Horizontal → →
