'''
Create:

[10, 20, 30, 40, 50]

Convert the array from integer to:

float
str

Check the dtype after each conversion.

'''

import numpy as np
array = np.array([10, 20, 30, 40, 50])

arr_float = array.astype(float)
print(arr_float.dtype)

arr_string = array.astype(str)
print(arr_string.dtype)

'''
we will get output like this from string --> <U2
It simply means :   
                Unicode string with a maximum length of 2 characters.

                
if we got something like this : [10, 20, 30, 40, 5000] --> output will be : <U4
'''