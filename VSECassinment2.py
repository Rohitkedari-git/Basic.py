import numpy as np

#creating 1D Array
arr1 = np.array([100, 200, 300, 400, 500])
print("1D Array:")
print("The 1D Array = ",arr1)

# Using Arange()
arr2 = np.arange(0, 12)
print("\nArray using arange():")
print("The Arange Array = ",arr2)

# Using linspace()
arr3 = np.linspace(31, 33, 7)
print("\nArray using linspace():")
print("The Lenspace = ",arr3)

# 2. Creating a 2D Array
arr2d = np.array([[0, 8, 3],
                  [2, 5, 1],
                  [4, 8, 6]])
print("\n The 2D Array:")

# 3. Indexing
print("\nIndexing:")
print("First element of arr1:", arr1[0])
print("Element at row 2, column 3:", arr2d[1, 2])

# 4. Slicing
print("\nSlicing:")
print("Elements from index 1 to 3:", arr1[1:4])
print("First two rows:\n", arr2d[:2])
print("Second column:", arr2d[:, 1])

# 5. Reshaping
arr4 = np.arange(1, 13)
reshaped = np.reshape(arr4, (3, 4))
print("\nReshaped Array (3x4):")
print(reshaped)

# 6. Mathematical Operations
print("\nMathematical Operations:")
print("Sum =", np.sum(arr1))
print("Mean =", np.mean(arr1))

print("Array + 5 =", arr1 + 5)
print("Array * 2 =", arr1 * 2)
