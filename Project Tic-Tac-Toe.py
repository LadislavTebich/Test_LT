# vygenerovat herni pole
# umet zadat o/x
# stridani hracu
# vyhodnoceni hry (vitezstvi/remiza)
# drobnosti
# vykreslit hru do konzole
# qt graficke rozhranni, vx, grafika pygame

def vygeneruj_matici(nradku, nsloupcu):
    matrix = [[0]*nsloupcu for i in range(nradku)]
    return matrix

def vykresli_matici(matice):

    for radek in matice:
        text = ""
        for symbol in radek:
            if symbol == 0:
                text +=" |"
            elif symbol == 1:
                text +="o|"
            elif symbol == 2:
                text +="+|"
            else:
                text +="?|"
        print(text[:-1])
        print("--"*len(matice))

def vitezstvi_sloupce(matice,hrac):
    nradku = len(matice)
    nsloupcu = len(matice[0])
    for jsloupec in range(nsloupcu):
        vitezstvi = True
        for iradek in range(nradku):
            if matice[iradek] [jsloupec] != hrac:
                vitezstvi = False
        if vitezstvi:
            return True
    return False

def vitezstvi_radku(matice,hrac):
    for radek in matice:
        vitezstvi = True
        for symbol in radek:
            if symbol != hrac:
                vitezstvi = False
        if vitezstvi:
            return True
    return False

def remiza(matice):
    #kdyz nebude v matici ani jedna nula
    #cistsi kod pocitanim tahu
    return True

def vitezstvi_diagonaly(matice, hrac):

    vitezstvi = True
    nradku = len(matice[0])
    for diagonala in range(nradku):
        if matice[diagonala] [diagonala] != hrac:
            vitezstvi = False
    if vitezstvi:
        return True
    return False
def preved_na_pozici(cislo,nsloupcu):
    cislo -=1
    radek = cislo //nsloupcu
    sloupec = cislo % nsloupcu
    return (radek, sloupec)

def main():
    rozmer = int(input("Zadej rozmer hrany pole :"))
    piskvorky = vygeneruj_matici(rozmer, rozmer)
    game_on = True
    tah = 1
    while game_on:
        symbol = 2 if tah % 2 == 0 else 1
        if symbol == 2:
            print('Hraje krizek')
        else:
            print('Hraje kolecko')
        cislo = int(input("zadej pozici 1-9: "))
        radek, sloupec = preved_na_pozici(cislo,rozmer)

        if piskvorky[radek][sloupec] == 0:
            piskvorky[radek][sloupec] = symbol
            tah +=1
        else:
            print ('Jiz obsazene pole')
        vykresli_matici(piskvorky)
        if vitezstvi_radku(piskvorky, symbol) or vitezstvi_sloupce(piskvorky,symbol) or vitezstvi_diagonaly(piskvorky,symbol):
            print('Vitezstvi !')
            game_on = False


if __name__ == "__main__":
    main()
