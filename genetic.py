import numpy as np
from grundloesung import *


def genetic_algorithm(L, b, h1, h2, E, q, k, alpha):
    #Anzahl der Individuen
    n = 4

    def create_gene(fzzy_Gr, alpha):
        low, high = fzzy_Gr.giveIntervall(alpha)
        gene = np.random.uniform(low, high)
        return gene

    def create_individuum(h1, h2, E, q, k, alpha):
        individuum = np.empty((5))

        i = 0
        for fzzy_Gr in (h1, h2, E, q, k):
            individuum[i] = create_gene(fzzy_Gr, alpha)
            i = i + 1

        return individuum

    def create_population(h1, h2, E, q, k, alpha):
        population = create_individuum(h1, h2, E, q, k, alpha)

        for i in range(n-1):
            population = np.vstack((population, create_individuum(h1, h2, E, q, k, alpha)))

        return population


    def calc_fitness(population, L, b):
        rows = population.shape[0]
        fitness_array = np.empty((rows))

        for i in range(rows):
            h1 = population[i, 0]
            h2 = population[i, 1]
            E  = population[i, 2]
            q  = population[i, 3]
            k  = population[i, 4]

            fitness = grundloesung(L, b, h1, h2, E, q, k)
            fitness_array[i] = fitness

        fitness_array_trans = fitness_array.reshape((rows, 1))
        population = np.append(population, fitness_array_trans, axis=1)
        return  population


    def crossover(population):
        #neue individuum mit gecrossten Eigenschaften
        print(population)
        x, y = population.shape
        #x = population.shape[0]
        #y = population.shape[1]
        population_cross_child_1 = np.zeros((int(x / 2), y))
        population_cross_child_2 = np.zeros((int(x / 2), y))

        for i in range(int(x / 2)):
            for j in range(y-1):
                if j <= ((y-1.0) / 2):
                    population_cross_child_1 [i, j] = population[i, j]
                    population_cross_child_2 [-i, j] = population[-i, j]
                if j > ((y-1.0) / 2):
                    population_cross_child_1[i, j] = population[-i, j]
                    population_cross_child_2[-i, j] = population[i, j]

        population_crossed = np.vstack((population, population_cross_child_1))
        population_crossed = np.vstack((population_crossed, population_cross_child_2))

        return population_crossed

    def mutation(population, h1, h2, E, q, k, alpha):
        rows = population.shape[0]

        for i in range(rows):
            j = 0
            for fzzy_Gr in (h1, h2, E, q, k):
                low, high = fzzy_Gr.giveIntervall(alpha)
                if population [i, j] > low and population [i, j] < high:
                    delta = 0.01 * np.random.uniform(low, high) * np.random.choice((-1, 1))
                    population [i,j] = population[i, j] + delta
                    if  population [i, j] < low:
                        population [i, j] = low
                    if  population[i, j] > high:
                        population[i, j] = high
                j = j+1
        return population


    population = create_population(h1, h2, E, q, k, alpha)
    print(population)
    for i in range(10):
        population = calc_fitness(population, L, b)
        population = np.argsort(population, axis=-1)
        # Aussortieren der Schlechtesten Indiviuuen
        rows = population.shape[0]
        for i in range(int(rows / 2)):
            # index "0" löscht die schlechteste fitness, mit "-1" lscht man die beste (je nachdem ob man nach Max or Min optimiert
            population = np.delete(population, 0, axis=0)

        population = crossover(population)
        population = mutation(population, h1, h2, E, q, k, alpha)

    M_max = population[0, 5]

    return M_max
        
"""    
#test
    population = definepop(h1, h2, E, q, k, alpha)
    population = calc_fitness(population, L, b)
    #Sortieren nach vorletzter Spalte, d.h. nach M_max
    population = np.argsort(population, axis=-2)
    #Löschen der Schlechtesten Individuen
    x, y = np.array.size(population)

    for i in range(x/2 ?????????):
        population = np.delete(population, 0)

    #Kreuzen der Eigenschaften

"""

