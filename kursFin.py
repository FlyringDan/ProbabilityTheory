import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve

def solve_equation():
    # Определяем функцию, которую нужно интегрировать
    def integrand(z, x):
        return np.exp(-0.9 * z) / (z + x)

    # Определяем функцию уравнения
    def equation(x):
        result, error = quad(integrand, 0, 20, args=(x,))
        return result - 0.1957981 * x

    # Решаем уравнение численно
    solution = fsolve(equation, 1)  # Начальное значение 1 (можно изменить)

    # Вычисляем интеграл для оценки погрешности
    integral, error = quad(integrand, 0, 20, args=(solution[0],))

    # Вычисляем погрешность
    relative_error = abs(integral - 0.1957981 * solution[0]) / abs(0.1957981 * solution[0])

    return solution[0], relative_error

    
# Вызываем функцию и выводим результат
result, error = solve_equation()
print("Решение уравнения: x =", result)
print("Округление: x = ", round(result, 1))
print("Погрешность:", round(result,1) - result)
print("Точное решение l = ", result * 50)
print("округление l  = ", round(result, 1) * 50)
