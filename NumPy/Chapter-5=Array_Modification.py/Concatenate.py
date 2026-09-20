'''
syntax_For_1D_Array = np.concatenate((arr1, arr2))

Syntax_For_2D_Array = np.concatenate((arr1, arr2), axis=0/1/none)

'''
import numpy as np

arr1 = np.array([1,2,3])                
arr2 = np.array([4,5,6])     
print(np.concatenate((arr1 , arr2)))

arr3 = np.array([[1,2,3],
                 [4,5,6]])
arr4 = np.array([[7,8,9],
                 [10,11,12]])

#axis=0 → joining rows
#         columns must match

#axis=1 → joining columns
#        rows must match

print(np.concatenate((arr3,arr4),axis = 0))
print(np.concatenate((arr3,arr4),axis = 1))