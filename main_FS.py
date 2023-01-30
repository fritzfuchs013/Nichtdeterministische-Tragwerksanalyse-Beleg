import time
from matplotlib import pyplot as plt
from genetic import *
from fuzzy import *
from genetic_FS import genetic_algorithm_FS


# Initiierung Fuzzy-Analyse -----------------------------------------------------------------
# Eingabegrößen aus Aufgabenstellung
L = 10
b = 0.2
h1 = FuzzyTrapez(0.65, 0.7, 0.7, 0.75)
h2 = FuzzyTrapez(0.48, 0.5, 0.5, 0.52)
E = FuzzyTrapez(2.05 * (10 ** 8), 2.10 * (10 ** 8), 2.12 * (10 ** 8), 2.15 * (10 ** 8))
q = FuzzyTrapez(14.0, 17.0, 18.5, 22.0)
my = FuzzyTrapez(0.9, 0.95, 0.95, 1.1)

# Sicherheitsausgabe
print('program has started')

# Testen des Darwin-Algorithmus -----------------------------------------------------------------------
startTime_genetic = time.time()
n_gen = 25

for alpha in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99]:
    M_max, M_min, aufrufe = genetic_algorithm_FS(L, b, h1, h2, E, q, my, alpha, n_gen)
    x_coordinates = [M_min, M_max]
    y_coordinates = [alpha, alpha]
    plt.plot(x_coordinates, y_coordinates, color="navy")
    print('M_max Evolutioniert zuuuuuuu:', M_max)
    print('M_min digitiert zuuuuuuu:', M_min)
    print(aufrufe)
    print('----------------')
plt.savefig("Fuzzy_stochastisch_Feld_05_quantil.png")
# Ende Timer und Bildung Differenz
endTime_genetic = time.time()
elapsed_time_genetic = endTime_genetic - startTime_genetic

# Ausgabe der benötigten Zeit
print("---------------------------------------------------------------")
print('benötigte Zeit:', elapsed_time_genetic)
