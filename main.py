import time
from matplotlib import pyplot as plt
from bruteforce import *
from gausgrit import *
from genetic import *
from absuchen import *
from fuzzy import * 


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


# brute force --------------------------------------------------------------------------------
# Beginn Timer
startTime_bruteforce = time.time()

# Anzahl der Schritte pro Intervall:
n = 1

# Initiierung Algorithmus über alle alpha level in der Schleife: (0, 0.5, 1)
for alpha in [0.0, 0.5, 1.0]:
    M_max, M_min = bruteforce(L, b, h1, h2, E, q, k, n, alpha)

    # Kontrolle der einzelnen errechneten Intervalle in der Konsolenausgabe
    print("-------------------------------------------------------")
    print('M_max =', M_max)
    print('M_min =', M_min)

    # Erstellung Plot des jeweiligen alpha-lvl Intervalls
    x_coordinates = [M_min, M_max]
    y_coordinates = [alpha, alpha]
    plt.plot(x_coordinates, y_coordinates, color="navy")

# Ende Timer und Bildung Differenz
endTime_bruteforce = time.time()
elapsed_time_bruteforce = endTime_bruteforce - startTime_bruteforce

# Ausgabe der benötigten Zeit
print("---------------------------------------------------------------")
print('benötigte Zeit:', elapsed_time_bruteforce)

# Ausgabe Plot
#plt.show()
plt.savefig("plot_BruteForce.png")


# Testen des Darwin-Algorithmus -----------------------------------------------------------------------
startTime_genetic = time.time()
#M_max_array = np.zeros((7, 5))
n_gen = 50
for alpha in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
    M_max, M_min = genetic_algorithm(L, b, h1, h2, E, q, k, alpha, n_gen)
    print('M_max Evolutioniert zuuuuuuu:', M_max)
    print('M_min digitiert zuuuuuuu:', M_min)
    print('----------------')
    #M_max_array[i, j] = M_max

    # Erstellung Plot des jeweiligen alpha-lvl Intervalls
    x_coordinates = [M_min, M_max]
    y_coordinates = [alpha, alpha]
    plt.plot(x_coordinates, y_coordinates, color="navy")

    # Erstellen Plot von Streuung zu Nummer von Generationen


# Ende Timer und Bildung Differenz
endTime_genetic = time.time()
elapsed_time_genetic = endTime_genetic - startTime_genetic

# Ausgabe der benötigten Zeit
print("---------------------------------------------------------------")
print('benötigte Zeit:', elapsed_time_genetic)

# Ausgabe Plot
#plt.show()
plt.label("Brute Force Optimierung")
plt.savefig("plot_genetic.png")

# Noch nicht aufgeräumter Test-Krams ------------------------------------------------------------------
"""

start_time = time.time()

for alpha in [0.0, 0.5, 1.0]:
    M_min, M_max = strukturiertes_absuchen_grundloesung(L, b, h1, h2, E, q, k, alpha)
    print(alpha, M_min, M_max)

end_time = time.time()
elapsed_time = end_time - start_time

print('M_max =', M_max)
print('M_min =', M_min)
print('benötigte Zeit:', elapsed_time)

#t_gauss = time.time()
#for alpha in [0, 0.5, 1]:
 #   M_max, M_min, n = gauss_grit(L, b, h1, h2, E, q, k, 3, alpha)
 #   print(M_max, M_min, n)

#et_bruteforce = time.time()
#elapsed_time_gauss = et_gauss - st_gauss
#print('M_max =', M_max)
#print('M_min =', M_min)
#print('benötigte Zeit:', elapsed_time_gauss)

"""