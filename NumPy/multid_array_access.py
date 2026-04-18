import numpy as np

# 0 dim. Array 
# arr0 = np.array("A")
# print(arr0)

# 1-D Array
arr1 = np.array(["A","B"])
print(arr1[1])

# 2-D Array
arr2 = np.array([["A","B"],
                 ["C","D"],
                 ["E","F"]])
print(arr2[1][0])

# 3-D Array
arr3 = np.array([[["A","B"], ["C","D"], ["E","F"]], 
                 [["G","H"], ["I","J"], ["K","L"]],
                 [["M","N"], ["O","P"], ["Q","R"]]])
print(arr3[1][2][0])
word = arr3[2,1,0] + arr3[2,1,1]
print(word)