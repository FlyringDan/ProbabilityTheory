import numpy as np

num_samples = 1000000

X = np.random.normal(0, 1, num_samples)
Y = np.random.normal(0, 1, num_samples)

prob_a = np.mean(X < Y)
print("Вероятность P(X < Y):", prob_a)

prob_b = np.mean(X > -Y)
print("Вероятность P(X > -Y):", prob_b)
