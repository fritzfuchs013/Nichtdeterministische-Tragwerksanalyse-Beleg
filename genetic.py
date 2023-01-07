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

