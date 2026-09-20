import numpy as np

arr = np.array([10, np.inf, 30, -np.inf, 50])
print(np.nan_to_num(arr,posinf=10,neginf=-9))