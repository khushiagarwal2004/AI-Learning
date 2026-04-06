# numpy array have fixed size at creation,unlike python list.Changing size of ndarray will create a new array and delete the original. 
# numpy elements are of same datatype
# numpy facilitates advanced mathematical and other types of operations on large number of data.

import numpy as np

# 2D numpy array
a = np.array([1,2,3])
print("2D array is:\n",a)
print("2D array type is:\n",type(a))

# 3D numpy array / Tensor
a = np.array([[[1,2],[2,3]],[[3,4],[4,5]]])
print("3D array is:\n",a)

# dtype
b = np.array([1,2,3],dtype=float)
c = np.array([0,2,3],dtype=bool)
print("array dtype is float:\n",b)
print("array dtype is bool:\n",c)

# arange
c = np.arange(1,11)
d = np.arange(1,11,2)
print("array range is 1-10:\n",c)
print("array range is 1-10 with 2 step:\n",d)

# reshape
e = np.arange(1,11).reshape(2,5)
print("arrange in shape 2X5:\n",e)

# ones and zeros
f = np.ones((3,5),dtype=int)
g = np.zeros((2,2))
print("ones matrix with order 3X5:\n",f)
print("zeros matrix with order 2X2:\n",g)

# random 
h = np.round(np.random.random((3,2)),2)
print("matrix with randome values with order 3X2 and round off till 2 points:\n",h)

# linspace : linearly spaced
# (LowerRange,UpperRange,CountInBetween)
i = np.linspace(-10,10,10)
print("Giving linearly seperable range in between:\n",i)

# identity
j = np.identity(3)
print("Identity Matrix of order 3:\n",j)


