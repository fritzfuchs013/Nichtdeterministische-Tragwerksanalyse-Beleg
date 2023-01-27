# Such Algorythmus, Abstand der Punkte im Intervall sind Gauß-Normal Verteilt. d.h. große Abstände in der Mitte, kleine am Rand
from scipy.stats import norm
from grundloesung_Einspannung import *
from scipy.integrate import quad

def gauss_grit (L, b, h_1, h_2, E, q, k, sigma, alpha):
    M_max = - np.inf
    M_min = + np.inf
    n = 0
    # Folgend: Schleifen über h1, h2, E, q und k
    # 1. Festlegung der Grenzen des intervalls der Variable
    h_1_l, h_1_r = h_1.giveIntervall(alpha)
    # 2. Finden der Mitte des Intervalls für die Normalverteilung
    h_1_m = (h_1_r - h_1_l) / 2
    # 3. Festlegung des Start Wertes für Scleife
    h1_temp = h_1_l
    while h1_temp <= h_1_r:
        h_2_l, h_2_r = h_2.giveIntervall(alpha)
        h_2_m = (h_2_r - h_2_l) / 2
        h2_temp = h_2_l
        while h1_temp <= h_1_r:
            E_l, E_r = E.giveIntervall(alpha)
            E_m = (E_r - E_l) / 2
            E_temp = E_l
            while E_temp <= E_r:
                q_l, q_r = q.giveIntervall(alpha)
                q_m = (q_r - q_l) / 2
                q_temp = q_l
                while q_temp <= q_r:
                    k_l, k_r = k.giveIntervall(alpha)
                    k_m = (k_r - k_l) / 2
                    k_temp = k_l
                    while k_temp <= k_r:
                        M = grundloesung(L, b, h1_temp, h2_temp, E_temp, q_temp, k_temp)
                        if M < M_min:
                            M_min = M
                        if M > M_max:
                            M_max = M
                        n=n+1
                        print(M,n)
                    k_temp = k_temp + 100 * stats.norm(k_temp, k_m, sigma)
                q_temp = q_temp + 100 * stats.norm(q_temp, q_m, sigma)
            E_temp = E_temp + 100 * stats.norm(E_temp, E_m, sigma)
        h2_temp = h2_temp + 100 * stats.norm(h_2_temp, h_2_m, sigma)
    h1_temp = h1_temp + 100 *  stats.norm(h_1_temp, h_1_m, sigma)

    return M_max, M_min, n