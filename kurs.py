import numpy as np
from scipy.integrate import solve_ivp

def differential_equations(x, y, P, l):
    y1, y2, y3, y4 = y

    dM_dx = -P * (l - x)
    I = 5 * (1 + 4 * np.exp(-6 * x / l))
    dI_dx = -20 * np.exp(-6 * x / l) / l

    w = -(dM_dx**2) / (x**2)
    dy1_dx = y2
    dy2_dx = y3
    dy3_dx = y4
    dy4_dx = -(2 / I) * dI_dx * y3 - (1 / I) * (dI_dx**2) * y2 + w / (E * I)

    return [dy1_dx, dy2_dx, dy3_dx, dy4_dx]


# Заданные параметры
l = 100
E = 3 * 10**7

# Начальные условия
x0 = 2

# Значения P для решения
P_values = np.arange(500, 1100, 100)

# Список для хранения средних значений y1
average_y1_values = []

for P in P_values:
    y0 = [0, 0, P * 100 * 10**-7 / 75, P * 3.8 * 10**-7 / 75]
    solution = solve_ivp(lambda x, y: differential_equations(x, y, P, l), [x0, l], y0, method='RK45')
    x = solution.t
    y1, y2, y3, y4 = solution.y

    # Сохраняем последние значения x и y1
    final_x = x[-1]
    final_y1 = y1[-1]

    # Вычисляем среднее значение y1
    average_y1 = np.mean(y1 * -1.0)

    # Добавляем среднее значение в список
    average_y1_values.append(average_y1)

    # Вывод результата

for i, P in enumerate(P_values):
    print("Среднее значение y1 при P = {}: {:.6e}".format(P, average_y1_values[i]))


L = 99.98477586023728
average_y1_values2 = []
for P in P_values:
    y0 = [0, 0, P * 100 * 10**-7 / 75, P * 3.8 * 10**-7 / 75]
    solution2 = solve_ivp(lambda x, y: differential_equations(x, y, P, L), [x0, l], y0, method='RK45')
    x = solution2.t
    y1, y2, y3, y4 = solution2.y

    # Сохраняем последние значения x и y1
    final_x = x[-1]
    final_y1 = y1[-1]

    # Вычисляем среднее значение y1
    average_y12 = np.mean(y1 * -1.0)

    # Добавляем среднее значение в список
    average_y1_values2.append(average_y12)

    # Вывод результата

for i, P in enumerate(P_values):
    print("Среднее значение y1 при P = {}: {:.6e}".format(P, average_y1_values2[i]))
