import numpy as np

arr = np.array([[1,2,3,4],
                [6,7,8,9],
                [11,12,13,14],
                [16,17,18,19]])
# array_name[start:stop:step]

print(arr[::-2])
print(arr[0:2:1]) 
print(arr[2:4])     # But we are accessing rows only most of the time while learning numpy and thats a big issue...
print(arr[1:])      #  What about columns? Cant we access columns?
print(arr[1::])

print(arr[2,2])  


# TO access column elements :

# Syntax : array_name[:, column_number]

print(arr[:, 0])  # This means , give me column 0th indexed elements from every row i.e. row1->1 row2->6 row3->11 row4->16

print(arr[2, :]) # The whole row 2
print(arr[2, :2]) # The whole row 2 but only include [:2]


print(arr[:, 0:3])  # This will give the first 3 columns elements in a proper matrix form
print(arr[:, ::2])  # This will give column 0th & 2th elements

print(arr[0:2 , 2:])   # This give [[3 4]
#                                   [8 9]]     its like selecting a quadrant

arr[:, 2]       # entire column 2
arr[1, :]       # entire row 1
arr[1:3, :]     # rows 1 and 2
arr[:, 1:3]     # columns 1 and 2
arr[1:3, 1:3]   # rows 1-2 AND columns 1-2