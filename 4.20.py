import random

count = 0
for i in range(1000000):
    str = ['к', 'а', 'р', 'е', 'т', 'а' ]
    rightArr = ['р', 'а', 'к', 'е', 'т', 'а' ]
    strS = []
    for j in range(6):
        rand = random.choice(str)
        strS.insert(j, rand)
        str.remove(rand)
    if strS == rightArr:
        count = count + 1
print(count / 1000000)

factorial = 1
for i in range(1,7):
    factorial = factorial * i
print(2 / factorial)
