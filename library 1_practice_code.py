
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