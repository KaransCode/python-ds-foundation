# Aggregations, Reshaping & Broadcasting

import numpy as np

matrix = np.array([[10, 20, 30],
                   [40, 50, 60]])

# Aggregations
print("\nSum:", matrix.sum())
print("\nMean:", matrix.mean())
print("\nMax:", matrix.max())
print("\nMin:", matrix.min())
print("\nStandard Deviation:", matrix.std())

# Reshaping
reshaped = matrix.reshape(3, 2)
print("\nReshaped Matrix:\n", reshaped)

# Broadcasting
broadcasted = matrix + 10
print("\nAfter Broadcasting:\n", broadcasted)