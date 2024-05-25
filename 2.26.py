import math

answer = 0
for i in range(6):
    answer = answer + ((-1)**i) / math.factorial(i)
print(answer / math.factorial(i))
