import random

k = 5
q = 10000
mathWait = k / q
dispersion = mathWait * 1000
successfulExperiment = 0
for i in range(0, 1000):
    kNow = 0
    jNow = 0
    while 1:
        rnd = random.randint(0, 99)
        jNow = jNow + 1
        if rnd in range(0, q):
            kNow = kNow + 1
        if kNow == k:
            break
    dispersion -= jNow
print(mathWait)
print(dispersion / 1000)
print((k+q)/q)
print(k*(1-q)/q)
