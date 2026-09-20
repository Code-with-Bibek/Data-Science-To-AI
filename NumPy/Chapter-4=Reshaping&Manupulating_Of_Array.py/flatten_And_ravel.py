# Used when multidimensional array need to be convert into 1-D array....

'''
1) array_name.flatten() --> copy
2) array_name.ravel()   --> view

'''

import numpy as np
arr = np.array([[1,2,3,4],
                [6,7,8,9]])

print(arr.flatten())
#                         They both will do the same thing i.e convert into 1D array..
print(arr.ravel())


# But we have some twists to learn so that we dont get confuse later on..

'''
ravel() --> Return only reference/view of the original array
        --> If you modify the array you would notice that the value of the original array also changes.
        --> Ravel is faster than flatten() as it does not occupy any memory.
        --> Ravel is a library-level function. 

flatten() --> Return copy of the original array
          --> If you modify any value of this array value of the original array is not affected.
          --> Flatten() is comparatively slower than ravel() as it occupies memory.
          --> Flatten is a method of an ndarray object.

'''
# Lets look an example :
import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])
ravel_array = arr.ravel()
print(ravel_array)

# If i changed a member of the ravelled array ;

ravel_array[1] = 55
print(ravel_array)
#                    --->> we can see changes in both original and in ravelled...
print(arr)

print("----------------------------------------------------------")

arr = np.array([[1,2,3,4],[5,6,7,8]]) # we again created a new array cuz the previous array was ravelled and has 55 onto the original array also..

flatten_array = arr.flatten()
print(flatten_array)

# If i changed a member of the flattened array ;

flatten_array[3] = 55
print(flatten_array)
print(arr)