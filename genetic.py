import numpy as np


def genetic_algorithm(L, b, h1, h2, E, q, k, alpha, n):
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

    def calc_fitness (population, L, b):
        x,y = np.array.size(population)
        M_max_array = [x,1]
        M_min_array = [x,1]
        for i in range(x):
            h1 = population[i,1]
            h2 = population[i,2]
            E  = population[i,3]
            q  = population[i,4]
            k  = population[i,5]
            M_max, M_min = grundloesung(L, b, h1, h2, E, q, k)
            M_max_array [i,1] = M_max
            M_min_array [i,1] = M_min

        population = np.vstack(population, M_max_array)
        population = np.vstack(population, M_min_array)


