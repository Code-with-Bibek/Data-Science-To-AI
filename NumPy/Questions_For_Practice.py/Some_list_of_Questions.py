# ==========================================================
# 13. PRACTICE QUESTION 1
# ==========================================================

# Create an array:
# [10, 20, 30, 40, 50]
#
# Add 10 to every element.
#
# Do NOT use a loop.


# ==========================================================
# 14. PRACTICE QUESTION 2
# ==========================================================

# Create:
#
# prices = [100, 200, 300, 400]
#
# Apply a 20% discount to every price.
#
# Do NOT use a loop.


# ==========================================================
# 15. PRACTICE QUESTION 3
# ==========================================================

# Create:
#
# marks = [
#     [50, 60, 70],
#     [65, 75, 85],
#     [80, 90, 95]
# ]
#
# Add:
#
# [5, 10, 15]
#
# to every row using broadcasting.


# ==========================================================
# 16. PRACTICE QUESTION 4
# ==========================================================

# Create:
#
# temperatures = [
#     [25, 26, 27],
#     [30, 31, 32],
#     [35, 36, 37]
# ]
#
# Subtract 5 from every temperature.
#
# Use broadcasting.


# ==========================================================
# 17. PRACTICE QUESTION 5
# ==========================================================

# Create:
#
# prices = [
#     [100, 200, 300],
#     [400, 500, 600]
# ]
#
# Add tax:
#
# [10, 20, 30]
#
# to every row.


# ==========================================================
# 18. PRACTICE QUESTION 6
# ==========================================================

# Create:
#
# students = [
#     [70, 80, 90],
#     [60, 75, 85],
#     [90, 95, 88]
# ]
#
# Add the following bonus to each student:
#
# Student 1 → 5
# Student 2 → 10
# Student 3 → 2
#
# Use broadcasting.


# ==========================================================
# 19. FINAL CHALLENGE
# ==========================================================

# You have the following prices:
#
# prices = [
#     [100, 200, 300],
#     [400, 500, 600],
#     [700, 800, 900]
# ]
#
# Apply different discounts to each column:
#
# First column  → 10%
# Second column → 20%
# Third column  → 30%
#
# Use broadcasting.
#
# Do NOT use a loop.
#
# Expected idea:
#
# [100, 200, 300]  → discounts [10%, 20%, 30%]
# [400, 500, 600]  → discounts [10%, 20%, 30%]
# [700, 800, 900]  → discounts [10%, 20%, 30%]


# ==========================================================
# IMPORTANT MEMORY
# ==========================================================

# VECTORIZATION
# = Apply an operation to many elements
#   without explicitly writing a Python loop.
#
# Example:
#
# arr * 2


# BROADCASTING
# = Allows compatible arrays of different shapes
#   to work together.
#
# Example:
#
# matrix + vector


# BROADCASTING RULE
#
# NumPy compares shapes from RIGHT → LEFT.
#
# Dimensions are compatible when:
#
# 1. They are equal
# OR
# 2. One of them is 1
#
#
# Example:
#
# (2, 3)
# (3,)
#
# Compatible ✓
#
#
# Example:
#
# (3, 3)
# (2,)
#
# Not compatible ✗


# ==========================================================
# GOLDEN LINE
# ==========================================================
#
# Vectorization = HOW NumPy applies the operation
#
# Broadcasting = HOW NumPy makes different shapes
#                compatible
#
# ==========================================================