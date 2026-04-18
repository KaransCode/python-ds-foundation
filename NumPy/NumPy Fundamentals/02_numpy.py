# Indexing, Slicing & Boolean Masking

import numpy as np

data = np.array([5, 10, 15, 20, 25, 30,35 ,49 ,55])

# Indexing
print("First element:", data[0])
print("\nSecond Last element:", data[-2])

# Slicing
print("\nSlice (3 to 7):", data[3:8])

# Boolean masking
filtered_data = data[data > 15]
print("\nValues greater than 15:", filtered_data)
