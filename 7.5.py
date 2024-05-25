import random

noBrokenIn100 = 0
noBrokenIn1000 = 0
areThereBroken = False
for i in range(10000):
    bulbs = 1000
    brokenBulbs = random.randint(0,6)
    setOfUsedBulbs = []
    for j in range(100):
        rnd = random.randint(0, bulbs)
        while (rnd in setOfUsedBulbs):
            rnd = random.randint(0, bulbs)
        setOfUsedBulbs.append(rnd)
        if (brokenBulbs != 0) and (rnd < brokenBulbs):
            areThereBroken = True
            break
    if (areThereBroken == False):
        noBrokenIn100 = noBrokenIn100 + 1
    if (brokenBulbs == 0):
        noBrokenIn1000 = noBrokenIn1000 + 1
    areThereBroken = False
print(noBrokenIn1000 / noBrokenIn100)
