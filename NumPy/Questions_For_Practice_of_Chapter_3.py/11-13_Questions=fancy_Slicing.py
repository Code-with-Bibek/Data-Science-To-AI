'''
 Fancy Indexing

Use:

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

Q11
Extract elements at indexes:[0, 3, 6]
Expected:
[10, 40, 70]

Q12
Extract elements at indexes:[1, 4, 7]
Expected:
[20, 50, 80]

Q13
Extract elements in this order:[7, 2, 5, 0]
Expected:
[80, 30, 60, 10]

Important: Notice that the requested indexes aren't in increasing order.

'''

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

result = arr[[0,3,6]]
print(result)

result = arr[[1,4,7]]
print(result)

result = arr[[7,2,5,0]]
print(result)

