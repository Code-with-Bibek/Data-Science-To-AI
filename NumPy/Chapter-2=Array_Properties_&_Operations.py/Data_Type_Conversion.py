# if we wanna convert one data type to another in a array , then 

# syntax --> array_name.astype(type)
        # type--> int , float or str ... or whatever

import numpy as np 
arr = np.array([2,4,6.5,6.89])
print(arr.astype(int))

print(arr.dtype)