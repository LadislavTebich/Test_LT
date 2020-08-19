# Zadej rozměry šachovnice
size = 10

# Zadej symboly
symbols = ['#',' ']

# Vytvoř šachovnici
desk = []

# Doplň smyčky for, které by měly postupně nahrát celou šachovnice do proměnné 'desk'
for row in range(size):
    line = []

    for cell in range(size):
        i = (row+cell) % len(symbols)
        line.append(symbols[i])

    desk.append(''.join(line))

# Vytiskni šachovnici
print('\n'.join(desk))
