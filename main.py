import time
from matplotlib import pyplot as plt
from bruteforce import *
from gausgrit import *
from genetic import *

from fuzzy import * 

a = FuzzyTrapez(1, 4, 4, 5)
x, y = a.giveIntervall(1)
print(x,y)
# Eingangsgrößen
L  = 10
b  = 0.2
h1 = FuzzyTrapez(0.65, 0.7, 0.7, 0.75)
h2 = FuzzyTrapez(0.48, 0.5, 0.5, 0.52)
E  = FuzzyTrapez(2.05 * (10 ** 8), 2.10 * (10 ** 8), 2.12 * (10 ** 8), 2.15 * (10 ** 8))
q  = FuzzyTrapez(14.0, 17.0, 18.5, 22.0)
k  = FuzzyTrapez(0.8 * (10 ** 4), 1.0 * (10 ** 4), 1.0 * (10 ** 4), 1.4 * (10 ** 4))

print('program has started')
#brute force
# alpha lvl Schleife: (0, 0.5, 1)
# Anzahl der Schritte pro Intervall:
n = 1
st_bruteforce = time.time()

for alpha in [0.0, 0.5, 1.0]:
    M_max, M_min = bruteforce(L, b, h1, h2, E, q, k, n, alpha)
    print(M_max, M_min)

    x_coordinates = [M_min, M_max]
    y_coordinates = [alpha, alpha]
    plt.plot(x_coordinates, y_coordinates, color="navy")

et_bruteforce = time.time()
elapsed_time_bruteforce = et_bruteforce - st_bruteforce

print('M_max =', M_max)
print('M_min =', M_min)
print('benötigte Zeit:', elapsed_time_bruteforce)

plt.show()
plt.savefig("out.png")

n=3
ng = genetic(L, b, h1, h2, E, q, k, n, alpha)

#t_gauss = time.time()
#for alpha in [0, 0.5, 1]:
 #   M_max, M_min, n = gauss_grit(L, b, h1, h2, E, q, k, 3, alpha)
 #   print(M_max, M_min, n)

#et_bruteforce = time.time()
#elapsed_time_gauss = et_gauss - st_gauss
#print('M_max =', M_max)
#print('M_min =', M_min)
#print('benötigte Zeit:', elapsed_time_gauss)