import numpy as np
a1=np.arange(10)
a2=np.arange(12,dtype=int).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)

# loops
for i in a1:
    print(i)
for i in a2:
    print("\n",i)
for i in a3:
    print("\n",i)

# nditer change your 2d 3d array in 1d while iterating
for i in np.nditer(a3):
    print(i)

# Transpose
print(np.transpose(a2))
print(a2.T) # Syntax 2

# Inverse
A=np.array([[6,1,1],[4,-2,5],[2,8,7]])
print("Inverse is:",np.linalg.inv(A))

# Ravel : change your any dimension array to 1D array
print(np.ravel(a2)) 
print("1D:",a3.ravel())

# Stacking

# Horizontal Stacking
a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)
print(np.hstack((a4,a5,a4,a4)))

# Vertical Stacking
print(np.vstack((a4,a5)))

# Splitting

# Horizontal Splitting
print(np.hsplit(a4,2))
# Vertical Splitting
print(np.vsplit(a4,3))

# Boolean Indexing
a=np.random.randint(1,100,24).reshape(6,4)
print(a)

print(a[a>50])
print(a[(a>50) & (a%2==0)])
print(a[a%7!=0])

# Broadcasting : It tells how numpy treats arrays with different shapes during arithmetic operations.
# The smaller array is broadcasted across larger array so that they have compatible shapes.
a=np.arange(6).reshape(2,3)
b=np.arange(3).reshape(1,3)
print(a,"\n")
print(b,"\n")
c=a+b
print(c,"\n") # Gives sum as : b is added in both rows of a

# Broadcasting Rules
# 1. Make 2 arrays of same dimensions (eg.: if a(3,3) and b(3) then make b as b(1,3))
# 2. Make size of smaller array same as size of array a (eg.: if a(3,3) and b(3) then make b as b(3,3))
# 3. Only strech 1 to make smaller array equal to big one