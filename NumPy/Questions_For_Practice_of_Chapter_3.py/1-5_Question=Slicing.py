'''
Q1 — Basic slicing

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

Extract:
20, 30, 40, 50

Q2 — Start to a position

Extract the first 5 elements.
Expected:
10, 20, 30, 40, 50

Q3 — From a position to the end
Extract:
50, 60, 70, 80

Q4 — Step
Extract every second element:
10, 30, 50, 70

Q5 — Reverse
Reverse the entire array using slicing.
Expected:
80, 70, 60, 50, 40, 30, 20, 10
Don't use np.flip().

'''


import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("----Extracting specifc elements----")
print(arr[1:5])

print("----Extracting an interval----")
print(arr[:5])

print("----Extracting a position to an end----")
print(arr[3:])

print("----Extracting every 2nd element----")
print(arr[::2])

print("----Reversing entire array----")
print(arr[-1::-1])

