import numpy as np

rng = np.random.default_rng()

n = rng.integers(low=1, high=1001)
# n = rng.integers(low=1, high=1001, size=(2,2))
print(n)

floating_num = np.random.uniform(low=-10 , high=1 , size=3)
print(floating_num)

# Shuffle

arr = np.array([1,2,3,4,5])
rng.shuffle(arr)
print(arr)

# Choice

fruits = np.array(["apple","banana","Pineapple","Mango"])
fruit = rng.choice(fruits,size=2)
print(fruits)
print(fruit)