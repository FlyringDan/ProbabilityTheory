import random

count = 0;
for j in range(1000000):
    rand = random.randint(1, 10)
    if (3 <= rand) and (rand <= 7):
        count += 1
print(count/ 1000000)

print((60*60-2*40*40/2)/(60*60))
