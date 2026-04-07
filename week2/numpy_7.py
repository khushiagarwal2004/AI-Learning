# import numpy as np

# sigmoid : Σ(x) = 1 / (1 + e^(-x)) : Convolution me activation function
def sigmoid(array):
    return np.round(1/(1+np.exp(-array)),4)

a=np.arange(10)
print(a)
print(sigmoid(a))

# mean squared error : mean(actual-predicted)^2) : ML mei Loss Function(with what value we inc/dec weights to reduce error) : Linear Regression 
actual=np.random.randint(1,50,25)
predicted=np.random.randint(1,50,25)
print("\n",actual)
print(predicted)

def mean_squared_error(actual,predicted):
    return np.mean((actual-predicted)**2)
print(mean_squared_error(actual,predicted))

# binary cross entropy
actual=np.random.randint(0,2,25)
predicted=np.random.random(25)
def bin_cross_entropy(actual,predicted):
    return -np.mean(actual*np.log(predicted)+(1-actual)*np.log(1-predicted))

print(bin_cross_entropy(actual,predicted))

# isnan
a = np.array([1,2,3,4,5,np.nan,6])
print(a)
print(a[~np.isnan(a)])

# # Graphs
import matplotlib.pyplot as plt
import numpy as np

# y=x
x=np.linspace(-10,10,100)
y=x
plt.plot(x,y)
plt.show()

# y=x^2
x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)
plt.show()

# y=sin(x)
x=np.linspace(-10,10,100)
y=np.sin(x)
plt.plot(x,y)
plt.show()

# y=xlog(x)
x=np.linspace(-10,10,100)
y=x*np.log(x)
plt.plot(x,y)
plt.show()

# sigmoid graph
x=np.linspace(-10,10,100)
y=1/(1+np.exp(-x))
plt.plot(x,y)
plt.show()

# seaborn
import seaborn as sns 
sns.displot([0,1,2,3,4,5])
plt.show()
sns.displot([0,1,2,3,4,5],kind="kde")
plt.show()