'''
Given:

data = np.array([10, 20, 30, 40, 50])

Find:

sum
mean
maximum
minimum
standard deviation
variance

'''

import numpy as np
data = np.array([10, 20, 30, 40, 50])

print("The sum is found to be: ",np.sum(data))
print(np.mean(data))
print(np.max(data))
print(np.min(data))
print(np.std(data))
print(np.var(data))