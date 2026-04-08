import numpy as np
a1=np.random.random((3,3))
a1=np.round(a1*100)
print(a1)

# max/min/sum/prod
print(np.max(a1))
print(np.min(a1))
print(np.sum(a1))
print(np.prod(a1))

# axis=0 : column wise
# axis=1 : row wise
print(np.max(a1,axis=1))

# mean/median/std/var
print(np.mean(a1))
print(np.median(a1,axis=0).astype(int))
print(np.std(a1).astype(int))
print(np.var(a1,axis=1).astype(int))

# trignometric
print(np.sin(a1))

# dot product
a2=np.arange(6).reshape(2,3)
a3=np.arange(6,15).reshape(3,3)
print("Dot product")
print(np.dot(a2,a3))
print(a2@a3)

# log and exponents
print(np.log(a1))
print(np.exp(a1))

# round/floor/ceil
print(np.round(np.random.random((2,3))*100))
print(np.floor(np.random.random((2,3))*100))
print(np.ceil(np.random.random((2,3))*100))