'''
🟢 Boolean Masking & Indexing

Use: marks = np.array([35, 78, 92, 45, 61, 29, 88, 54])

Q6 — Greater than
Create a Boolean mask that identifies marks greater than 60.
Then use that mask to extract the actual marks.
Expected:
[78, 92, 61, 88]

Q7 — Passing students
Using the same array, extract all marks greater than or equal to 40.
Expected:
[78, 92, 45, 61, 88, 54]

Q8 — Failed students
Extract all marks below 40.
Expected:
[35, 29]

Q9 — High performers
Extract all marks greater than 80.
Expected:
[92, 88]

Q10 — Boolean condition
Extract marks that are:
greater than 50 AND less than 90
Expected:
[78, 61, 88, 54]

'''
import numpy as np
arr = np.array([35, 78, 92, 45, 61, 29, 88, 54])

print("----Greater than 40----")
new_array = arr > 40
result = arr[new_array]
print(result)

print("-----marks greater than or equal to 40 i.e Pass as well as top students-----")
arr = np.array([35, 78, 40, 45, 61, 29, 88, 54])
arr2 = arr >= 40
result = arr[arr2]
print(result)

print("-----marks less than 40 i.e Failed ones-----")
arr = np.array([35, 78, 40, 45, 61, 29, 88,12,3,4,6,89])
arr3 = arr < 40
result = arr[arr3]
print(result)

print("----High performers i.e Greator than 80----")
arr = np.array([35, 78, 40, 45, 61, 29, 88,12,99,89])
arr4 = arr > 80
result = arr[arr4]
print(result)

print("----Marks Extracting----")
arr = np.array([35, 78, 40, 45, 61, 29, 88,12,99,89])
arr5 = ((arr > 50) & (arr < 90))
result = arr[arr5]
print(result)