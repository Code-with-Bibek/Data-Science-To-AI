# -----Boolean masking-----> It allows us to filter elements from an arrat based on a specific condition

import numpy as np
arr1 = np.array([1,2,3,4,5,6])
boolean_mask = arr1 > 4
print(boolean_mask)

#-----Boolean Indexing-----> It is a  numpy array comtaining truth values (True/False) that correspond to each elements in the array

arr2 = np.array([10,20,30,40,50])
boolean_indexing = arr2 > 20
result = arr2[boolean_indexing]
print(result)