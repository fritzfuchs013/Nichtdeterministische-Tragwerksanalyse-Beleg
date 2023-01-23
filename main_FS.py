import time
from matplotlib import pyplot as plt
from genetic import *
from fuzzy import *
from grundloesung_Feld import *


# Initiierung Fuzzy-Analyse -----------------------------------------------------------------
# Eingabegrößen aus Aufgabenstellung
L = 10
b = 0.2
h1 = FuzzyTrapez(0.65, 0.7, 0.7, 0.75)
h2 = FuzzyTrapez(0.48, 0.5, 0.5, 0.52)
E = FuzzyTrapez(2.05 * (10 ** 8), 2.10 * (10 ** 8), 2.12 * (10 ** 8), 2.15 * (10 ** 8))
q = FuzzyTrapez(14.0, 17.0, 18.5, 22.0)
k = FuzzyTrapez(0.8 * (10 ** 4), 1.0 * (10 ** 4), 1.0 * (10 ** 4), 1.4 * (10 ** 4))

# Sicherheitsausgabe
print('program has started')

# Testen des Darwin-Algorithmus -----------------------------------------------------------------------
startTime_genetic = time.time()
#M_max_array = np.zeros((7, 5))
n_gen = 50
for alpha in [0.0]:
    M_max, M_min, aufrufe = genetic_algorithm(L, b, h1, h2, E, q, k, alpha, n_gen)
    print('M_max Evolutioniert zuuuuuuu:', M_max)
    print('M_min digitiert zuuuuuuu:', M_min)
    print(aufrufe)
    print('----------------')
    #M_max_array[i, j] = M_max

# Ende Timer und Bildung Differenz
endTime_genetic = time.time()
elapsed_time_genetic = endTime_genetic - startTime_genetic

# Ausgabe der benötigten Zeit
print("---------------------------------------------------------------")
print('benötigte Zeit:', elapsed_time_genetic)
