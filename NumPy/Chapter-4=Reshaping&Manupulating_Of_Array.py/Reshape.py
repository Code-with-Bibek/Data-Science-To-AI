'''
syntax --> array_name.reshape(row,column)    means , what is going to be the new row and column ..

dimensions can be only reshaped iff dimensions match

'''

import numpy as np

arr = np.array([1,2,4,5,6,7,8,9])
print(arr.reshape(2,4))