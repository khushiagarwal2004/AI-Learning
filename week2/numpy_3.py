import numpy as np

a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)
print(a1,"\n\n",a2,"\n")

# scalar operations

# arithmetic
print(a1*2,"\n")
print(a1**2,"\n")
 
# relational
print(a1>5)
print(a2==15)

# vector operations : shapes must be same for it to perform

# arithmetic
print(a1+a2)
print(a2**a1)

