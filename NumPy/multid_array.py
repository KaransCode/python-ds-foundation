import numpy as np

# 0 dim. Array 
arr0 = np.array("A")
print(arr0)
print(arr0.ndim)

# 1-D Array
arr1 = np.array(["A","B"])
print(arr1)
print(arr1.ndim)

# 2-D Array
arr2 = np.array([["A","B"],
                 ["C","D"],
                 ["E","F"]])
print(arr2)
print(arr2.ndim)

# 3-D Array
arr3 = np.array([[["A","B"], ["C","D"], ["E","F"]], 
                 [["G","H"], ["I","J"], ["K","L"]],
                 [["M","N"], ["O","P"], ["Q","R"]]])
# print(arr3)
print(arr3.shape)
# 3d shape - (depth,row,column)
print(arr3.ndim)