import numpy as np

# ==========================================================
# 1. VECTORIZATION
# ==========================================================

arr = np.array([10, 20, 30, 40, 50])

result = arr * 2

print("Original array:", arr)
print("After multiplying by 2:", result)


# ==========================================================
# 2. SCALAR BROADCASTING
# ==========================================================

arr = np.array([10, 20, 30, 40, 50])

result = arr + 5

print("\nOriginal array:", arr)
print("After adding 5:", result)


# ==========================================================
# 3. SUBTRACTION
# ==========================================================

temperatures = np.array([25, 28, 30, 32, 35])

result = temperatures - 2

print("\nTemperatures:", temperatures)
print("After subtracting 2:", result)


# ==========================================================
# 4. MULTIPLICATION
# ==========================================================

prices = np.array([100, 200, 300, 400])

result = prices * 2

print("\nPrices:", prices)
print("Doubled prices:", result)


# ==========================================================
# 5. DISCOUNT USING VECTORIZATION + BROADCASTING
# ==========================================================

prices = np.array([100, 200, 300, 400])
discount = 10

discount_amount = prices * discount / 100
final_prices = prices - discount_amount

print("\nOriginal prices:", prices)
print("Discount amount:", discount_amount)
print("Final prices:", final_prices)


# ==========================================================
# 6. 2D BROADCASTING
# ==========================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

result = matrix + vector

print("\nMatrix:")
print(matrix)

print("Vector:")
print(vector)

print("Matrix + Vector:")
print(result)


# ==========================================================
# 7. BROADCASTING WITH SUBTRACTION
# ==========================================================

matrix = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

discount = np.array([10, 20, 30])

result = matrix - discount

print("\nMatrix:")
print(matrix)

print("Discount:")
print(discount)

print("After discount:")
print(result)


# ==========================================================
# 8. ROW-WISE BROADCASTING
# ==========================================================

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 88]
])

bonus = np.array([5, 10, 2])

result = marks + bonus

print("\nMarks:")
print(marks)

print("Bonus:")
print(bonus)

print("Marks after bonus:")
print(result)


# ==========================================================
# 9. BROADCASTING WITH A COLUMN
# ==========================================================

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 88]
])

bonus = np.array([
    [5],
    [10],
    [2]
])

result = marks + bonus

print("\nMarks:")
print(marks)

print("Bonus:")
print(bonus)

print("Marks after bonus:")
print(result)


# ==========================================================
# 10. CHECKING SHAPES
# ==========================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

print("\nMatrix shape:", matrix.shape)
print("Vector shape:", vector.shape)

result = matrix + vector

print("Result:")
print(result)


# ==========================================================
# 11. BROADCASTING RULE EXAMPLE
# ==========================================================

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = np.array([10, 20, 30])

print("\narr1 shape:", arr1.shape)
print("arr2 shape:", arr2.shape)

result = arr1 + arr2

print("Result:")
print(result)


# ==========================================================
# 12. INCOMPATIBLE SHAPES
# ==========================================================

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr2 = np.array([10, 20])

print("\narr1 shape:", arr1.shape)
print("arr2 shape:", arr2.shape)

# The following line will give an error
# because the shapes are not broadcast-compatible.

# result = arr1 + arr2


