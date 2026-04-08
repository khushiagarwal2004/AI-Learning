import numpy as np
a1=np.arange(10,dtype=np.int32)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
print(a1)
print(a2)
print(a3)

# ndim : tells dimension of your array 1D,2D,3D
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

# shape : tells order of your array
print(a1.shape)
print(a2.shape)
print(a3.shape)

# size : tells number of items in your array
print(a1.size)
print(a2.size)
print(a3.size)

# itemsize
print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

# dtype
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

# numpy dont change dtype of original array with astype but create new array of it then change it.
# astype : for changing datatype of certain array
a4=a3.astype(np.int32)
print(a4.dtype)