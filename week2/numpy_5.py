import numpy as np
a1=np.arange(10,dtype=np.int32)
a2=np.arange(12,dtype=int).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

# indexing and slicing
print(a1[-1])

print(a2) # aim is to print 6 nad 11 through indexing or slicing 

print(a2[1,2])
print(a2[2,3])

print(a3) # aim is to print 5 nad 3 through indexing or slicing 

print(a3[1,0,1])
print(a3[0,1,1])

print(a1[2:7:2])
print(a2[0,:]) # for first row in 2d array
print(a2[:,2]) # for third column in 2D array

# practice
print(a2[1:,1:3])
print(a2[::2,::3]) 
print(a2[::2,1::2])
print(a2[1,::3])
print(a2[0:2,1:])

a4=np.arange(27).reshape(3,3,3) 
print("\n\n",a4[1])
print("\n\n",a4[::2])
print("\n\n",a4[0,1])
print("\n\n",a4[1,:,1])
print("\n\n",a4[2,1:,1:])
print("\n\n",a4[::2,0,::2])

# Fancy Indexing
print(a2[2])
