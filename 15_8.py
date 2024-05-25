import random
import math

def points_on_same_side(num_points):
    count = 0  # счетчик точек, удовлетворяющих условию

    for _ in range(num_points):
        # Генерация случайного радиуса от центра окружности
        radius = random.uniform(0, 1)

        # Генерация случайного угла
        angle = random.uniform(0, 2 * math.pi)

        # Координаты первой точки
        x1 = radius * math.cos(angle)
        y1 = radius * math.sin(angle)

        # Координаты второй точки
        x2 = -x1
        y2 = -y1

        # Проверка условия: обе точки должны находиться по одну сторону от хорды (y >= 0)
        if y1 >= 0 and y2 >= 0:
            count += 1

    probability = count / num_points
    return probability

# Задаем количество генерируемых точек
num_points = 100000000

# Вычисляем вероятность
probability = points_on_same_side(num_points)
print("Вероятность: ", probability)
