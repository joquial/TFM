import numpy as np
list2 = [[1, 2, 3, 4],[3, 4, 5.5, 6], [5, 6, 7, 8]]
arr2 = np.array(list2, float)
list1 = [[1, 2, 3],[4, 5.5, 6], [7, 8, 9],[ 1, 2.89, 3.123]]
arr1 = np.array(list1, float)
# shape
print('Shape: ', arr2.shape)

# dtype
print('Datatype: ', arr2.dtype)

# size
print('Size: ', arr2.size)

# ndim
print('Num Dimensions: ', arr2.ndim)
print('Matrix: ', arr2)
print(arr2*arr2)
print(arr2.dot(arr1))
