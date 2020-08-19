slova = ['zelena', 'modra', 'cerna', 'cervena', 'cervena', 'zluta', 'modra', 'seda', 'cerna' , 'cervena', 'zelena']
delky_slov = {}
while slova:
    slovo = slova.pop()
    delka = len(slovo)
    print(slovo, delka)
    delky_slov[delka] = delky_slov.get(delka,0) + 1

print(delky_slov)