
import numpy as np
import time

arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print(arr.ndim)
print(arr.dtype)

py_list  = list(range(1_000_000))
py_result = []
start_time = time.time()
for i in py_list:
    py_result.append(i+5)
end_time = time.time()
print("Python List time:",end_time - start_time)

np_array = np.arange(1_000_000)
start_time = time.time()
np_result = np_array + 5
end_time = time.time()
print("Numpy Array Time:", end_time - start_time)
# Creating Arrays in numpy
arr = np.array([1,2,3])
print (arr)

print(np.zeros((2,3)))
print(np.ones((2,3)))
print(np.full((2,3),7))

print(np.arange(0,10,2))
print(np.linspace(0,1,5))

print(np.eye(3))
print(np.diag([1,2,3]))
np.array([1,2,3],dtype = float)
arr = np.array([1.5,2.7,3.9])
print(arr.astype(int))

# Numpy Indexing, Slicing & Strides

arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])
print(arr[0,1])
print(arr[2,2])
print(arr[-1,-2])
print(arr[-3,-3])

print(arr[0:2,1:3])
print(arr[::2,::2])

slice_arr = arr[0,:2]
slice_arr[0] = 999
print(arr[0])

copy_arr = arr[1].copy()
copy_arr[1] = 555
print(arr[1])

# numpy random numbers, Reproducebility & Performance Tips

rng = np.random.default_rng()
flips = rng.integers(0,2,size = 100000)
prob_heads = np.mean(flips)
print("Estimated Probability of heads: ",prob_heads)

import time 
start = time.time()
squares = [i**2 for i in range (1000000)]
end = time.time()
print("loop time:",end - start)

# Numpy vectorized
start = time.time()
arr = np.arange(1000000)
squares_np = arr**2
end = time.time()
print("Vectorized time: ",end - start)