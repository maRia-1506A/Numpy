import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr)

arr[1]= np.array([10,10,10])
print("After modification: ")
print(arr)

arr[2,1]= 10
print("After updating arr[2,1]:")
print(arr)