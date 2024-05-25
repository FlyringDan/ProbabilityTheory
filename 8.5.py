import random

count = 0
for i in range(1000000):
    firstLamp = random.randint(1,10)
    secondLamp = random.randint(1,10)
    if firstLamp <= 4:
        count += 1
    else:
        if secondLamp <= 4:
            count += 1
print(count / 1000000)

print(0.4 + 0.6*0.4)
