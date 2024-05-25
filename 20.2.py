import numpy as np
import matplotlib.pyplot as plt

def f_X(x):
    return 1 / (x * np.log(10))

X = np.random.exponential(scale=1, size=10000)

Y = np.log(X)

def f_Y(y):
    return f_X(np.exp(y)) * np.exp(y)

plt.hist(Y, bins=50, density=True, label='Y')
plt.xlabel('Y')
plt.ylabel('Probability Density')
plt.title('Probability Density of Y')
plt.legend()
plt.show()
