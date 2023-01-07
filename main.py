import time
from bruteforce import *
from genetic import *

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

print('program has started')
#brute force
# alpha lvl Schleife: (0, 0.5, 1)
# Anzahl der Schritte pro Intervall:
n = 1
st = time.time()
for alpha in [0, 0.5, 1]:
    M_max, M_min = bruteforce(L, b, h1, h2, E, q, k, n, alpha, M_max, M_min)
et = time.time()
elapsed_time = et - st

print('M_max =', M_max)
print('M_min =', M_min)
print('benötigte Zeit:', elapsed_time)

n=3
ng = genetic(L, b, h1, h2, E, q, k, n, alpha)
