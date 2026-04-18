import numpy as np

arr = np.array([12,11,14,21])

# Scalar Arithematic Operation on Np.array
# print(arr + 2)
# print(arr - 2)
# print(arr * 2)
# print(arr / 2)
# print(arr + arr)
# print(arr ** 2)

# Vectorized arithematic
arr1 = np.array([1.213, 2.4231 , 5.698])
# print(np.sqrt(arr))
# print(np.round(arr1))
# print(np.floor(arr1))
# print(np.ceil(arr1))

# print(np.pi)

# Element-wise operations

arr1 = np.array([12,31,41,50,60])
arr2 = np.array([21,10,71,86,76])

sum = arr1 + arr2
min = arr2 - arr1
# print(sum)
# print(min)

# Comparison Operator

scores = np.array([45,48,65,67,76,78])
high = scores >= 50
scores[scores < 50] = -1
print(high)
print(scores)