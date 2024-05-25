import numpy as np
import matplotlib.pyplot as plt

# параметры распределения
p = 0.3
r = 50
a = r * (1 - p)

# генерация выборки отрицательно биномиального распределения
sample_nb = np.random.negative_binomial(r, p, size=10000)

# гистограмма выборки
plt.hist(sample_nb, bins=range(max(sample_nb)+2), density=True, alpha=0.5, label='Negative Binomial')

# расчет и график плотности распределения Пуассона
lambda_ = a * p / (1 - p)
x = np.arange(0, max(sample_nb)+1)
index = x[0] # or any other element in the array
y = np.exp(-lambda_) * lambda_**index / np.math.factorial(index)
plt.plot(x, y, 'r-', label='Poisson')

plt.legend()
plt.show()
