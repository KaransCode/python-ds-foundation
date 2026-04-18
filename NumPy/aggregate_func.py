import numpy as np

# Aggregate functions = summarize data and typically
# return a single value

arr = np.random.randint(1,100,size=(3,3))
print(arr)
print(np.sum(arr))

print(np.sum(arr, axis=0)) # Column-wise |
print(np.sum(arr, axis=1)) # Row-wise   ---

print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))