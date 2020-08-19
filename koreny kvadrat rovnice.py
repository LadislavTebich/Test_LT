def ziskej_vstupy():
    acko = int(input('zadej koeficient a: '))
    becko = int(input('zadej koeficient b: '))
    cecko = int(input('zadej koeficient c: '))
    return acko,becko,cecko

def diskriminant(a,b,c):
    return b**2 - 4*a*c

def zjisti_pocet_korenu(D):
    if D > 0 :
        return 2
    elif D == 0:
        return 1
    else:
        return 0

def spocti_koreny(a,b,c,D,nkorenu):
    import math
    if nkorenu == 2:
        x1 = (-b + math.sqrt(D) )/ (2 *a)
        x2 = (-b - math.sqrt(D) )/ (2 *a)
        return x1, x2
    elif nkorenu == 1:
        return -b/(2*a)
    else:
        return None

def main():
    a,b,c = ziskej_vstupy()
    D = diskriminant (a,b,c)
    nkorenu = zjisti_pocet_korenu(D)
    koreny = spocti_koreny(a,b,c,D,nkorenu)
    print(' koreny jsou :',koreny)

if __name__ == "__main__":
    main()