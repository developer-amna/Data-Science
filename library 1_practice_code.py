
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