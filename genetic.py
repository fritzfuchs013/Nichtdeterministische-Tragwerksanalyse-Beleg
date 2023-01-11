import numpy as np
from grundloesung import *


def genetic_algorithm(L, b, h1, h2, E, q, k, alpha):
    #Anzahl der Individuen
    n = 40
    def definegene(fg, alpha):
        low, high = fg.giveintervall(alpha)
        gene = np.random.uniform(low, high)
        return gene

    def definepop(h1, h2, E, q, k, alpha):
        pop = np.array(5)

        for fg in (h1, h2, E, q, k):
            i = 0
            pop[i] = definegene(fg, alpha)

    new_population = np.array((n, 5))
    for i in range(n):
        new_population = np.vstack((new_population, definepop(h1, h2, E, q, k, alpha)))

    return new_population

    def calc_fitness(population, L, b):
        x,y = np.array.size(population)
        M_max_array = [x, 1]
        M_min_array = [x, 1]

        for i in range(x):
            h1 = population[i, 1]
            h2 = population[i, 2]
            E  = population[i, 3]
            q  = population[i, 4]
            k  = population[i, 5]

            M_max, M_min = grundloesung(L, b, h1, h2, E, q, k)
            M_max_array [i, 1] = M_max
            M_min_array [i, 1] = M_min

        population = np.append(population, M_max_array, axis=1)
        population = np.append(population, M_min_array, axis=1)
        return  population

    def crossover(population):
        #neue population mit gecrossten Eigenschaften
        population_cross_1 = np.zeros_like(population)
        population_cross_2 = np.zeros_like(population)
        x, y = np.array.size(population)

        for i in range(x):
            for j in range(y-2):
                population_cross_1 [i,j] = population




    population = definepop(h1, h2, E, q, k, alpha)
    population = calc_fitness(population, L, b)
    #Sortieren nach vorletzter Spalte, d.h. nach M_max
    population = np.argsort(population, axis=-2)
    #Löschen der Schlechtesten Individuen
    x, y = np.array.size(population)

    for i in range(x/2 ?????????):
        population = np.delete(population, 0)

    #Kreuzen der Eigenschaften


