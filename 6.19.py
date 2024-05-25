import random

count = 0
for j in range(1000000):
    firstArea = [1,1,1,1,1,1,1,1,0,0]
    secondArea = [1,1,0,0,0,0,0,0,0,0]
    for i in range(10):
        if (random.choice(firstArea) == 1) or (random.choice(secondArea) == 1):
            if random.randint(1, 10) <= 2:
                count += 1
                break
print(count / 1000000)
print(' ')

for k in range(10):
    print(1 - (0.8 * 0.2**(k)+(1 - 0.8)*0.2**(10 - k)))
