
# To install numpy first run this command in the terminal :
# pip install numpy

# After Installing numpy import it using import command:

import numpy as np

# Creating NumPy arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.zeros(5)
arr3 = np.ones(5)
arr4 = np.arange(1, 11, 2)
arr5 = np.random.randint(0,100,6)

print("Array:", arr1)
print("Zeros:", arr2)
print("Ones:", arr3)
print("Arange:", arr4)
print("Array with Random Integers :", arr5)

# Array properties
print("Shape:", arr1.shape)
print("Size:", arr1.size)
print("Data Type:", arr1.dtype)
