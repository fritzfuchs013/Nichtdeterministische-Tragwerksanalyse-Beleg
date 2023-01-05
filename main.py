import numpy as np

from grundloesung import *
class FuzzyTrapez:
    def __init__(self, links, maximuml, maximumr, rechts):
        self.links = links
        self.maximuml = maximuml
        self.maximumr = maximumr
        self.rechts = rechts

    def giveIntervall(self, alphalvl : float) -> (float, float):
        newLinks = self.links + alphalvl * (self.maximuml - self.links)
        newRechts = self.maximumr - alphalvl * (self.rechts - self.maximumr)
        return newLinks, newRechts

a = FuzzyTrapez(1, 4, 4, 5)
x, y = a.giveIntervall(0.1)
print(x,y)

# Eingangsgrößen
L  = 10
b  = 0.2
h1 = FuzzyTrapez(0.65, 0.7, 0.7, 0.75)
h2 = FuzzyTrapez(0.48, 0.5, 0.5, 0.52)
E  = FuzzyTrapez(2.05 * (10 ** 8), 2.10 * (10 ** 8), 2.12 * (10 ** 8), 2.15 * (10 ** 8))
q  = FuzzyTrapez(14.0, 17.0, 18.5, 22.0)
k  = FuzzyTrapez(0.8 * (10 ** 4), 1.0 * (10 ** 4), 1.0 * (10 ** 4), 1.4 * (10 ** 4))
M_max = - np.inf
M_min = + np.inf
#brute force
# alpha lvl Schleife: (0, 0.5, 1)
#Folgend: Schleifen über h1, h2, E, q und k
for alpha in [0, 0.5, 1]:
    h1l, h1r = h1.giveIntervall(alpha)
    h1s = (h1r-h1l)/10
    h1_temp = h1l
    while h1_temp <= h1r:
        h2l, h2r = h2.giveIntervall(alpha)
        h2s = (h2r - h2l) / 10
        h2_temp = h2l
        while h2_temp <= h2r:
            El, Er = E.giveIntervall(alpha)
            Es = (Er - El) / 10
            E_temp = El
            while E_temp <= Er:
                ql, qr = q.giveIntervall(alpha)
                qs = (qr - ql) / 10
                q_temp = ql
                while q_temp <= qr:
                    kl, kr = k.giveIntervall(alpha)
                    ks = (kr - kl) / 10
                    k_temp = kl
                    while k_temp <= kr:
                        #folgende Zeile nur um den Code zu testen, ist dann zu löschen
                        #M= (h1_temp+h2_temp/E_temp) * q_temp / k_temp
                        M = grundloesung(L, b, h1_temp, h2_temp, E_temp, q_temp, k_temp)
                        if M < M_min:
                            M_min = M
                        if M > M_max:
                            M_max = M
                        k_temp = k_temp+ks
                    q_temp = q_temp + qs
                E_temp = E_temp + Es
            h2_temp = h2_temp + h2s
        h1_temp = h1_temp + h1s

print('M_max =', M_max)
print('M_min =', M_min)
