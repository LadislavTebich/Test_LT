import math
maxcislo = int(input('zadej max cislo :'))

for velky in range (1,maxcislo):
    prvocislo = True
    for maly in range (2,round(math.sqrt(velky)+1)):
        if velky % maly == 0:
            prvocislo = False
            break
    if prvocislo == True:
        print("{} je prvocislo".format(velky))


