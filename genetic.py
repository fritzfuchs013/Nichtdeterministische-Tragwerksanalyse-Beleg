import numpy as np
from grundloesung import *


def genetic_algorithm(L, b, h1, h2, E, q, k, alpha):
    #Anzahl der Individuen
    n = 40

    def create_gene(fzzy_Gr, alpha):
        low, high = fzzy_Gr.giveintervall(alpha)
        gene = np.random.uniform(low, high)
        return gene

    def create_individuum(h1, h2, E, q, k, alpha):
        individuum = np.array(5)

        i = 0
        for fzzy_Gr in (h1, h2, E, q, k):
            individuum[i] = create_gene(fzzy_Gr, alpha)
            i = i + 1
        return individuum

    def create_population(h1, h2, E, q, k, alpha):
        population = create_individuum(h1, h2, E, q, k, alpha)

        for i in range(n-1):
            population = np.vstack(population, create_individuum(h1, h2, E, q, k, alpha))

        return population

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
        #neue individuum mit gecrossten Eigenschaften
        x, y = np.array.size(population)
        population_cross_child_1 = np.array((x / 2.0), y)
        population_cross_child_2 = np.array((x / 2.0), y)

        for i in range(x/2):
            for j in range(y-2):
                if j <= ((y-2) / 2):
                    population_cross_child_1 [i, j] = population[i, j]
                    population_cross_child_2 [-i, j] = population[-i, j]
                if j > ((y-2) / 2):
                    population_cross_child_1[i, j] = population[-i, j]
                    population_cross_child_2[-i, j] = population[i, j]

        population_crossed = np.vstack(population, population_cross_child_1)
        population_crossed = np.vstack(population_crossed, population_cross_child_2)

        return population_crossed

    population = definepop(h1, h2, E, q, k, alpha)
    population = calc_fitness(population, L, b)
    #Sortieren nach vorletzter Spalte, d.h. nach M_max
    population = np.argsort(population, axis=-2)
    #Löschen der Schlechtesten Individuen
    x, y = np.array.size(population)

    for i in range(x/2 ?????????):
        population = np.delete(population, 0)

    #Kreuzen der Eigenschaften



