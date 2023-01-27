import numpy as np
from scipy.integrate import quad
#from scipy.integrate import simps


def grundloesung_Einspannung(L, b, h_1, h_2, E, q, k):

    def M_0(x):
        return (-q / 2.0) * (x ** 2) + q * L * x - (1 / 2.0) * q * (L ** 2)

    def M_1(x):
        return -x + L

    def h(x):
        return ((h_2 - h_1) / L) * x + h_1

    def I(x):
        return b * (h(x) ** 3) * (1 / 12.0)

    def y(x):
        return (M_0(x) * M_1(x)) / (E * I(x))

    def z(x):
        return (M_1(x) ** 2) / (E * I(x))

    delta_10, err1 = quad(y, 0, L)

    delta_11, err2 = quad(z, 0, L)

    delta_11 = delta_11 + (1.0 / k)

    #print("delta")
    #print(delta_10)
    #print(delta_11)

    X_1 = -(delta_10 / delta_11)

    moment_Einspannung = M_0(0.0) + X_1 * M_1(0.0)

    #print(M_0(0.0))
    #print(M_1(0.0))

    return moment_Einspannung


#m = grundloesung(10, 0.2, 0.7, 0.5, 2.1 * (10 ** 8), 17, 1 * (10 ** 4))

#print(m)



