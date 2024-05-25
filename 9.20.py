import random
import math

a = 0
b = 0
m = 20
for i in range(1000000):
    sum = 0
    for n in range(10):
        sum += random.randint(1,6)
    if sum == m:
        a += 1
    if sum <= m:
        b += 1
print(a / 1000000)
print(b / 1000000)

print((1 / 6**10) * (math.factorial(19) / (math.factorial(9) * math.factorial(19-9))) - (math.factorial(10) / (math.factorial(1) * math.factorial(10-1))) * math.factorial(13) / (math.factorial(9) * math.factorial(13-9)))
