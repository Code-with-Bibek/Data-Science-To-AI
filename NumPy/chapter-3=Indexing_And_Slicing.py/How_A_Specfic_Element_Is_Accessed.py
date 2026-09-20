import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[2])   #--> using indexing method and the result is 30 
print(arr[1:3]) #--> using slicing method and the result is [20 30]
print(arr[-1])

'''
Indexing must be given a position...

In 1-D array : we simply do --> array_name[index_no]

But ,

In 2-D array : we do -->  array_name[row,column]

'''
# Numpy follows 0 based indexing..so it counts 0 1 2 3 4 5 and so on

arr1 = np.array([[1,2,3] , [4,5,6] ,
                 [7,8,9] , [10,11,12]])
print(arr1)
print(arr1[2,1])


