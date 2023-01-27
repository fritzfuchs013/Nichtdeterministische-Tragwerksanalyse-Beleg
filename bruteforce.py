from grundloesung_Einspannung import *
from scipy.integrate import quad


def bruteforce(L, b, h1, h2, E, q, k, n, alpha):
    M_max = - np.inf
    M_min = + np.inf
    # Folgend: Schleifen über h1, h2, E, q und k
    h1l, h1r = h1.giveIntervall(alpha)
    h1s = (h1r - h1l) / n
    if h1s == 0:
        h1s = 1
    h1_temp = h1l
    while h1_temp <= h1r:
        h2l, h2r = h2.giveIntervall(alpha)
        h2s = (h2r - h2l) / n
        if h2s == 0:
            h2s = 1
        h2_temp = h2l
        while h2_temp <= h2r:
            El, Er = E.giveIntervall(alpha)
            Es = (Er - El) / n
            E_temp = El
            while E_temp <= Er:
                ql, qr = q.giveIntervall(alpha)
                qs = (qr - ql) / n
                if qs == 0:
                    qs = 1
                q_temp = ql
                while q_temp <= qr:
                    kl, kr = k.giveIntervall(alpha)
                    ks = (kr - kl) / n
                    if ks == 0:
                        ks = 1
                    k_temp = kl
                    while k_temp <= kr:
                        M = grundloesung(L, b, h1_temp, h2_temp, E_temp, q_temp, k_temp)
                        if M < M_min:
                            M_min = M
                        if M > M_max:
                            M_max = M
                        k_temp = k_temp + ks
                    q_temp = q_temp + qs
                E_temp = E_temp + Es
            h2_temp = h2_temp + h2s
        h1_temp = h1_temp + h1s
    return M_max, M_min
