'''
Syntax = array_name[start:stop:step]  

'''

import numpy as np     # we are working in 1-D array

arr = np.array([10,30,45,67,87,34,45,87])
print(arr[1:7])
print(arr[1:7:2])
print(arr[-7:-2])
print(arr[-2:-7])

print(arr[::])
print(arr[::2 ])
print(arr[::-4])