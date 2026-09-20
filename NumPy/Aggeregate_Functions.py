# Aggregate function = summarize data and typically returns a single value

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,5,4,22,45,78,97])

print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))
print(np.argmin(arr)) # This will give the index 0f the min number location
print(np.argmax(arr)) # This will give the index of the max number location

arr2 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])

print(np.mean(arr2))
print(np.min(arr2))
print(np.max(arr2))
print(np.std(arr2))
print(np.var(arr2))
print(np.argmin(arr2)) # This will give the index 0f the min number location
print(np.argmax(arr2)) # This will give the index of the max number location

print(np.sum(arr2,axis=0)) # This will give the sum of each columns 
print(np.sum(arr2,axis=1)) # This will give the sum of each rows
