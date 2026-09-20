'''
How to check shape , size And Type of an array?

'''
import numpy as np

# shape --> gives the number of rows and columns in an array

arr_shape = np.array([[4,5,6] ,
                     [6,7,4]])
print(arr_shape.shape)

# size --> gives the total number of elememts in an array

arr_size = np.array([[4,5,6] ,
                     [7,7,3]])
print(arr_size.size)

# data type --> tells which type of data type is in the array

arr = np.array([10,28,45,65,56.78])
print(arr.dtype)