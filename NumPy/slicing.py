import numpy as np

# arr = np.random.randint(1,100,size=(4,4))
arr = np.array([[49, 4, 85, 42],
               [28, 82, 79, 84],
               [5, 35, 21, 47],
               [13, 20, 43,  8]])


print(arr[0:2,0:2])
print(arr[2:,2:])
# print(arr[0:2])

# # Accessing Row
# print(arr[0:4])

# # Accessing Col
# print("Col")
# print(arr[:,0:2])