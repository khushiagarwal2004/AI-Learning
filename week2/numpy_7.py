import numpy as np

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

