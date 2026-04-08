import numpy as np

# Linear Regression
weights=np.array([0.5,1.2,-0.3])
features=np.array([2.0,3.0,1.0])
bias = 0.8
prediction=np.dot(weights,features)+bias
print(f"Prediction: {prediction:.2f}")

# Similarity check
user_a = np.array([5, 3, 0, 1])   # ratings for 4 movies
user_b = np.array([4, 0, 4, 1])
similarity = np.dot(user_a, user_b)
print(f"Raw similarity: {similarity}")

# Normalization 
# L0 norm : return count of non-zeros term
# Manhattan Norm L1 norm : ||v||₁ = |v₁| + |v₂| + ... + |vₙ|
v = np.array([3, -4, 0, 2])
l1 = np.linalg.norm(v, ord=1) 
print(l1)

# Euclidean Norm L2 norm : ||v||₂ = √(v₁² + v₂² + ... + vₙ²)
# By default L2 is ord=2

# Max Norm : L∞ Norm : ||v||∞ = max(|v₁|, |v₂|, ..., |vₙ|)
v = np.array([3, -7, 2])
linf = np.linalg.norm(v, ord=np.inf)
print(linf)


