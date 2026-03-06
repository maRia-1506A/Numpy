import numpy as np

arr1 = np.array([1, 3, 6])
arr2 = np.array([2, 6, 0])

# merge array
merged = np.concatenate((arr1, arr2))
print("Merged array: ", merged)

# Row add
original_arr = np.array([[1, 2, 3], [4, 6, 8]])
new_row = np.array([[4, 6, 0]])

updated_new_row = np.vstack((original_arr, new_row)) # vertically row added (vstack)

print("\nOriginal Array:\n", original_arr)
print("Updated with new row:\n", updated_new_row)

# Column add
new_col= np.array([[2],[7]])

updated_new_col= np.hstack((original_arr, new_col)) # horizontally column added (hstack)

print("\nOriginal Array:\n", original_arr)
print("Updated with new column:\n", updated_new_col)
