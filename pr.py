
def fact(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact

an = 0
for i in range(5):
    an = (-1)**i / fact(i)
print((1/fact(10) * an))
