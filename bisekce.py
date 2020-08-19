def najdi_prostredek (a,b):
    return (a+b)/2

def tisk_korene (koren, presnost):
    print ('nasel jsem s presnosti :{} koren :{}'.format(presnost, koren))

def kontrola_korene(potenc_koren, presnost):
    if (abs(f(potenc_koren)) <= presnost):
        return True
    else:
        return False

def f(x):
    return 5*x - 4

def main ():
    presnost = 0.000001
    a = 0
    b = 1
    c = najdi_prostredek(a,b)
    while not kontrola_korene(c, presnost):
        print('aktualni typ: ',c)
        if f(a)*f(c) < 0:
            b = c
        else :
            a = c
        c = najdi_prostredek(a,b)
    tisk_korene (c, presnost)

if __name__ == '__main__':
    main()