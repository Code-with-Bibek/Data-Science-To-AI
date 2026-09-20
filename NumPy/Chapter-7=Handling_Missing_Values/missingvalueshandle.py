# Chapter 7 — Handling Missing Values in NumPy

# Covers three functions: np.isnan(), np.isinf(), np.nan_to_num().

# 1. What Is a Missing Value?

# Real-world data is rarely complete.

# python
# marks = np.array([80, 75, 90, ?, 85])   # 4th value is missing

# NumPy represents a missing/invalid numerical value with a special float constant:

# python
# np.nan   # "Not a Number"
# python

import numpy as np

marks = np.array([80, 75, 90, np.nan, 85])

# Value	Meaning
# 80	actual value
# 75	actual value
# 90	actual value
# NaN	missing
# 85	actual value
# 2. Why It's a Problem

# np.nan breaks numerical operations (sums, means, ML models, etc.) if left unhandled.

# DATA → find missing values → handle/replace them → clean DATA → calculations / ML

# Missing values must be detected, then replaced, before the array is safe to use.

# 3. np.isnan() — Detect NaN
# python

import numpy as np

arr = np.array([10, np.nan, 30, np.nan, 50])
result = np.isnan(arr)

print(result)

# [False  True False  True False]

# Value	Is it NaN?
# 10	False
# NaN	True
# 30	False
# NaN	True
# 50	False

# Returns a Boolean array — one True/False per element.

# True means "this value IS NaN" — not "this value is good." False → not NaN   |   True → NaN

# 4. Why Not arr == np.nan?
# python
#  Never do this — NaN never equals anything, not even itself
# arr == np.nan

#  Always use this instead
# np.isnan(arr)
# 5. np.nan_to_num() — Replace NaN

# Detecting isn't enough — you also need to replace the missing values.

# python

import numpy as np

arr = np.array([10, np.nan, 30, np.nan, 50])
result = np.nan_to_num(arr)

print(result)
# [10.  0. 30.  0. 50.]

# Default replacement value is 0.

# Before: [10, NaN, 30, NaN, 50]
#                 ↓ nan_to_num()
# After:  [10,  0,  30,  0,  50]
# Custom replacement value
# python
# result = np.nan_to_num(arr, nan=100)
# # [10, 100, 30, 100, 50]
# 6. Quick Recap — isnan vs nan_to_num
# Function	Job	Mental model
# np.isnan(arr)	Finds NaN : "Where is the missing data?"
# np.nan_to_num(arr)	Replaces NaN:  "Replace it with a number."
# 7. np.isinf() — Detect Infinity

# A second kind of "bad data": infinity.

# python
# np.inf--> positive infinity
# -np.inf-->negative infinity
# python

import numpy as np

arr = np.array([10, np.inf, 30, -np.inf, 50])
result = np.isinf(arr)

print(result)

# [False  True False  True False]
# Value	Infinity?
# 10	False
# +∞	True
# 30	False
# -∞	True
# 50	False

# np.isinf() catches both positive and negative infinity.

# 8. Replacing Infinity

# np.nan_to_num() handles this too, with two extra keyword args:

# python

import numpy as np

arr = np.array([10, np.inf, 30, -np.inf, 50])

result = np.nan_to_num(
    arr,
    posinf=1000,
    neginf=-1000
)

print(result)
# [   10.  1000.    30. -1000.    50.]

import numpy as np

arr = np.array([
    10,
    np.nan,
    30,
    np.inf,
    -np.inf,
    50
])

print("Original array:")
print(arr)
# [   10.    nan    30.    inf   -inf    50.]

print("\nChecking NaN:")
print(np.isnan(arr))
# [False  True False False False False]

print("\nChecking Infinity:")
print(np.isinf(arr))
# [False False False  True  True False]

clean_arr = np.nan_to_num(
    arr,
    nan=0,
    posinf=1000,
    neginf=-1000
)

print("\nCleaned array:")
print(clean_arr)
# [   10.     0.    30.  1000. -1000.    50.]

arr = np.array([10, np.nan, 30, np.nan, 50])

np.mean(arr)     # nan   — poisoned by NaN
np.nanmean(arr)  # 30.0  — ignores NaN, averages the rest

np.sum(arr)      # nan
np.nansum(arr)   # 90.0

np.nanmax(arr)   # 50.0
np.nanmin(arr)   # 10.0