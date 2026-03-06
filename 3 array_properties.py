import numpy as np

c = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Shape:", c.shape)
print("Size:", c.size)
print("Dimension:", c.ndim)

# compatibility
a1 = np.array([1, 4, 7])
a2 = np.array([2, 5, 9, 6])
a3 = np.array([3, 6, 5])
print("\nCompatibility shapes: ", a1.shape == a2.shape) 
print("Compatibility shapes: ", a1.shape == a3.shape) 