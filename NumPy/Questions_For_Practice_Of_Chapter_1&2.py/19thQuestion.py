'''
temperature = np.array([
    24, 26, 25, 28, 30,
    29, 27, 31, 32, 30,
    28, 26, 25, 29, 33
])

Find:

a) Basic information :

number of days
shape
dimensions
data type

b) Statistics :

average temperature
highest temperature
lowest temperature
total temperature
variance
standard deviation

c) Further calculations :

Create a new array where every temperature is increased by 2.
Create another array where every temperature is converted to float.
Calculate the new average after adding 2.

'''

import numpy as np
temperature = np.array([
    24, 26, 25, 28, 30,
    29, 27, 31, 32, 30,
    28, 26, 25, 29, 33
])

print("The number of days are : ",temperature.size)
print(temperature.shape)
print(temperature.ndim)
print(temperature.dtype)
    
print("The average temp is : " , np.mean(temperature))
print("The highest temp is : " , np.max(temperature))
print("The lowest temp is : " , np.min(temperature))
print("The total temp is : " , np.sum(temperature))
print("The varience of temp is : " , np.var(temperature))
print("The standard deviation of temp is : " , np.std(temperature))

arr_another_increase = temperature + 2

arr_another = temperature.astype(float)
print(arr_another)

print(arr_another_increase)
print(np.mean(arr_another_increase))