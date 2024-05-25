import random

count = 0
for i in range(10000000):
    if (random.randint(0,999)^2) % 10 == 1:
        count += 1
print(count / 1000000)
