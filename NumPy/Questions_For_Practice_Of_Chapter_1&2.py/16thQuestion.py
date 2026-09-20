'''
Given:

temperatures = np.array([25, 27, 31, 29, 22, 30, 28])

Find:

Average temperature
Highest temperature
Lowest temperature
Temperature variance
Temperature standard deviation

'''

import numpy as np
temperatures = np.array([[25, 27, 31, 29, 22, 30, 28]])

print("The average temp is : " , np.mean(temperatures))
print("The highest temp is :" , np.max(temperatures))
print("The lowest temp is :" , np.min(temperatures))
print("The temp variance is :" , np.var(temperatures))
print("The Temp standard deviation is :" , np.std(temperatures))