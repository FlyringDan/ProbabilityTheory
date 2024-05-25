import random

count = 0;
for j in range(1000000):
    arr = [1, 1, 1, 1, 1, 1, 1, 0, 0, 1]
    firstPlayer = 0;
    secondPlayer = 0;
    for i in range(10):
        firstRandom = random.choice(arr)
        if firstRandom == 1:
            firstPlayer += 1
            arr.remove(1)
        else:
            count += 1
            break
        secondRandom = random.choice(arr)
        if secondRandom == 1:
            secondPlayer += 1
            arr.remove(1)
        else:
            '''count -= 1'''
            break
print(count / 1000000)

result = 0
for i in range(408):
    result += (2/10)*((8**2)/(10**2))**i
print(result)
    
