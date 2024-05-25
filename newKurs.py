import numpy as np
from scipy.interpolate import splrep, splev
import matplotlib.pyplot as plt

# Значения P и средних значений y1
P_values = np.array([500, 600, 700, 800, 900, 1000])
average_y1_values = np.array([1.455651e+05, 3.122516e+05, 3.858312e+05, 4.719575e+05, 5.678460e+05, 6.698677e+05])

# Построение сплайна
tck = splrep(P_values, average_y1_values)

# Вычисление значений сплайна в точках исходных данных
y1_spline = splev(P_values, tck)

# Вычисление погрешности сплайна
error = np.abs(y1_spline - average_y1_values)

# Вывод погрешности
#for i in range(len(P_values)):
 #   print(f"Погрешность для P = {P_values[i]}: {error[i]}")


# Создание более плотного набора точек для гладкой кривой
P_smooth = np.linspace(P_values.min(), P_values.max(), 100)
y1_smooth = splev(P_smooth, tck)

#### Значения P и средних значений y1
P_values2 = np.array([500, 600, 700, 800, 900, 1000])
average_y1_values2 = np.array([1.455304e+05, 3.122136e+05, 3.857630e+05,4.718594e+05, 5.677227e+05, 6.697266e+05])

# Построение сплайна
tck2 = splrep(P_values2, average_y1_values2)

# Вычисление значений сплайна в точках исходных данных
y1_spline2 = splev(P_values2, tck2)

# Вычисление погрешности сплайна
error2 = np.abs(y1_spline2 - average_y1_values2)

# Вывод погрешности
#for i in range(len(P_values)):
#    print(f"Погрешность для P = {P_values[i]}: {error[i]}")


# Создание более плотного набора точек для гладкой кривой
P_smooth2 = np.linspace(P_values2.min(), P_values2.max(), 100)
y1_smooth2 = splev(P_smooth2, tck2)

# Визуализация результатов
plt.plot(P_values, average_y1_values, 'bo', label='Исходные данные')
plt.plot(P_smooth, y1_smooth, 'r-', label='Сплайн')
plt.plot(P_values2, average_y1_values2)
plt.plot(P_smooth2, y1_smooth2, 'r-', label='Сплайн')
plt.xlabel('P')
plt.ylabel('y1')
plt.title('Сплайн')
plt.legend()
plt.show()

