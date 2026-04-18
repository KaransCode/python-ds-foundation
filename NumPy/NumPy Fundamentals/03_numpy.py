# Vectorized Operations & Mathematical Functions
import numpy as np

values = np.array([2, 4, 6, 8, 10])

# Vectorized operations
squared = values ** 2
added = values + 5
subtract = values - 1
multiply = values * 3

print("\nOriginal:", values)
print("\nSquared:", squared)
print("\nAfter Addition + 5:", added)
print("\nAfter Subtraction - 1:", subtract)
print("\nAfter Multiplying by 3:", multiply)

# Mathematical functions
print("\nSquare Root:", np.sqrt(values))
print("\nLog Values:", np.log(values))