import numpy as np

n = 1000
X = np.random.rand(n)
Y = X + np.random.randn(n)

correlation = np.corrcoef(X, Y)[0, 1]

print("Корреляция:", correlation)
print(0 / correlation)
print(correlation / correlation)
