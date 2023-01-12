import numpy as np
from grundloesung import *


def genetic_algorithm(L, b, h1, h2, E, q, k, alpha, n_gen):
    #Anzahl der Individuen (Muss eine Gerade Zahl sein)
    n = 100

    def create_gene(fzzy_Gr, alpha):
        low, high = fzzy_Gr.giveIntervall(alpha)
        gene = np.random.uniform(low, high)
        return gene

    def create_individuum(h1, h2, E, q, k, alpha):
        individuum = np.zeros((6))

        i = 0
        for fzzy_Gr in (h1, h2, E, q, k):
            individuum[i] = create_gene(fzzy_Gr, alpha)
            i = i + 1

        return individuum

    def create_population(h1, h2, E, q, k, alpha,n):
        population = create_individuum(h1, h2, E, q, k, alpha)

        for i in range(n-1):
            population = np.vstack((population, create_individuum(h1, h2, E, q, k, alpha)))

        return population


    def calc_fitness(population, L, b):
        rows = population.shape[0]

        for i in range(rows):
            h1 = population[i, 0]
            h2 = population[i, 1]
            E  = population[i, 2]
            q  = population[i, 3]
            k  = population[i, 4]

            population[i, 5] = grundloesung(L, b, h1, h2, E, q, k)
        return  population


    def crossover(population):
        #neue individuum mit gecrossten Eigenschaften
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
        mutation_rate = 0.0005
        #diff_rel = (population[-int((rows / 2) + 1), 5] - population[0, 5]) / population[-int((rows / 2) + 1), 5]
        #if diff_rel < mutation_rate:
        #    mutation_rate = diff_rel

        for i in range(rows):
            j = 0

            for fzzy_Gr in (h1, h2, E, q, k):
                low, high = fzzy_Gr.giveIntervall(alpha)
                delta = mutation_rate * np.random.uniform(low, high) * np.random.choice((-1, 1))
                population [i,j] = population[i, j] + delta

                if  population [i, j] < low:
                    population [i, j] = low

                if  population[i, j] > high:
                    population[i, j] = high

                j = j+1
        return population

# optimierung nach M_max: ---------------------------------------------------------
    population = create_population(h1, h2, E, q, k, alpha, n)
    population = calc_fitness(population, L, b)
    population = population[np.argsort(population[:, -1])]
    for j in range(int(n / 5)):
        # index für "obj=0" löscht die schlechteste fitness, mit "obj=-1" löscht man die beste (je nachdem ob man nach Max or Min optimiert
        population = np.delete(population, obj=0, axis=0)

    for i in range(n_gen):
        population = calc_fitness(population, L, b)
        population = population[np.argsort(population[:, -1])]

        # Aussortieren der Schlechtesten Indiviuuen
        rows = population.shape[0]
        for j in range(int(rows / 2)):
            # index für "obj=0" löscht die schlechteste fitness, mit "obj=-1" löscht man die beste (je nachdem ob man nach Max or Min optimiert
            population = np.delete(population, obj=0, axis=0)

        population = crossover(population)
        population = mutation(population, h1, h2, E, q, k, alpha)

    population = calc_fitness(population, L, b)
    M_max = population[-0, 5]

# optimierung nach M_min: ---------------------------------------------------------
    population = create_population(h1, h2, E, q, k, alpha, n)
    population = calc_fitness(population, L, b)
    population = population[np.argsort(population[:, -1])]
    for j in range(int(n / 5)):
        # index für "obj=0" löscht die schlechteste fitness, mit "obj=-1" löscht man die beste (je nachdem ob man nach Max or Min optimiert
        population = np.delete(population, obj=-1, axis=0)

    for i in range(n_gen):
        population = calc_fitness(population, L, b)
        population = population[np.argsort(population[:, -1])]

        # Aussortieren der Schlechtesten Indiviuuen
        rows = population.shape[0]
        for j in range(int(rows / 2)):
            # index für "obj=0" löscht die schlechteste fitness, mit "obj=-0" löscht man die beste (je nachdem ob man nach Max or Min optimiert
            population = np.delete(population, obj=-1, axis=0)

        population = crossover(population)
        population = mutation(population, h1, h2, E, q, k, alpha)

    population = calc_fitness(population, L, b)
    M_min = population[0, 5]


    return M_max, M_min

#Hurensohn