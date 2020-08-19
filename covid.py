N = 1000 # pocet obyvatel
S = N - 1 # nakazitelni = zdravi
I = 1 # nakazeno
ndays = 30 # behem 30 dni

beta = 0.4 # jak se to prenasi
gama = 0.035 # jak dobre se to leci

for iday in range(ndays):
    dS = -beta*S*I/N + gama*I # to se odecte z mnoziny zdravyvc + ti,co se vylecili
    dI = - dS
    S += dS
    I += dI
    print("den :{} S: {}, I: {}".format(iday+1, S, I))