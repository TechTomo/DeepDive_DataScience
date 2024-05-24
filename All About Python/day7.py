#Numpy Arrays

import numpy as np

arr = np.array([1, 2, 3])
print(arr)
print(type(arr))
print(arr.shape)

lst1=[1,2,3,4,5]
lst2=[2,3,4,5,6]
lst3=[3,4,5,6,7]

lst5=np.array([lst1,lst2,lst3])
print(lst5)
print(lst5.shape)

print(arr[1:])
print(lst5[1:,3:])

print(lst5.reshape(5,3))
print(np.zeros((2,2)))
print(np.ones((2,2)))
print(np.random.randint(10,100,6))
print(np.random.rand(2,2))
print(np.random.random_sample((2,2)))