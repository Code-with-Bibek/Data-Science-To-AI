'''
Mixed Challenge 🔥

Use:

data = np.array([
    [45, 72, 91, 38, 65],
    [88, 54, 76, 92, 41],
    [33, 81, 69, 57, 95],
    [74, 46, 89, 63, 52]
])

          Math  Python  Stats  DBMS  DSA

Student 0   45    72     91    38    65
Student 1   88    54     76    92    41
Student 2   33    81     69    57    95
Student 3   74    46     89    63    52 

Do all five:

A. Extract Student 2's complete marks.

B. Extract the Python marks of all students.

C. Extract the first 3 subjects of the last 2 students.

D. Extract all marks greater than 80 using Boolean masking.

E. Extract these specific marks:

Student 0 → Math
Student 1 → DBMS
Student 2 → DSA
Student 3 → Stats

'''

import numpy as np

data = np.array([
    [45, 72, 91, 38, 65],
    [88, 54, 76, 92, 41],
    [33, 81, 69, 57, 95],
    [74, 46, 89, 63, 52]
])

print("----Extracting Student 2's complete marks.----")
print(data[2])

print("------Extracting the Python marks of all students.-----")
print(data[:, [1]])

print("-----Extracting the first 3 subjects of the last 2 students.-----")
print(data[-1:-3:-1 , [0,1,2]][::-1])

print("----Extracting all marks greater than 80 using Boolean masking.------")
result = np.array(data > 80)
new_result = data[result]
print(new_result)

print("------Extracting specific marks.------")
print(data[[0,1,2,3],[0,3,4,2]])     

# Explain of last question.. i.e (E)
# We can use two lists of indices to select specific elements.
#
# Syntax:
# data[[row_indices], [column_indices]]
#
# NumPy pairs the row and column indices position by position.
#
# Example:
# data[[0,1,2,3], [0,3,4,2]]
#
# This means:
# (0,0) → Student 0, Math
# (1,3) → Student 1, DBMS
# (2,4) → Student 2, DSA
# (3,2) → Student 3, Stats
#
# So each row index is paired with the column index
# at the same position.
#
# This is called fancy indexing because we are
# selecting specific/scattered positions rather than
# using a continuous slice.