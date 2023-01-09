
from functools import reduce,partial
import numpy as np
import numpy.linalg as linalg
import math
import scipy
from grundloesung import grundloesung
from fuzzy import FuzzyTrapez
# parameterbereich hat n paare an oberen und unteren Grenzen
# 

def und(a,b):
    return a and b

def strukturiertes_absuchen(function, initial_guess, parameterbereich):
    parameter = parameterbereich.shape[0]
    #print(parameter)
    schrittweite = 1.0
    old_point = initial_guess
    old_function_value = math.inf
    new_candidate_point = np.zeros(old_point.shape[0])

    while True:
        #print(old_function_value)
        new_point_found = False
        for i in range(0,old_point.shape[0]):
            delta = np.zeros(old_point.shape[0])
            delta[i] = schrittweite
            #print(delta)
            new_point = old_point + delta
            new_function_value = function(new_point)

            mn, mx = np.array(parameterbereich).T
            is_in_bounds = True
            for para in range(0,parameter):
                is_in_bounds = new_point[i] > mn[i] and new_point[i] < mx[i] and is_in_bounds
            #print(is_in_bounds)

            if is_in_bounds and new_function_value < old_function_value:
                old_function_value = new_function_value
                new_candidate_point = new_point
                new_point_found = True

            # das ganze nochmal in andere raumrichtung
            delta = np.zeros(old_point.shape[0])
            delta[i] = - schrittweite
            #print(delta)
            new_point = old_point + delta
            new_function_value = function(new_point)

            is_in_bounds = True
            for para in range(0,parameter):
                is_in_bounds = new_point[i] > mn[i] and new_point[i] < mx[i] and is_in_bounds
            #print(is_in_bounds)

            if is_in_bounds and new_function_value < old_function_value:
                old_function_value = new_function_value
                new_candidate_point = new_point
                new_point_found = True

        #print(schrittweite, old_point, new_candidate_point)
        

        if new_point_found:
            if abs(linalg.norm(old_point - new_candidate_point)) < 1e-10:
                break
            old_point = new_candidate_point
        else: 
            schrittweite = schrittweite * 0.5

        

    return new_candidate_point

def test_func(werte):
    return (werte[0]-3.5) ** 2 + werte[1] ** 2 + werte[2] ** 2

def modifizierte_grundloesung(laenge, breite, vector):
    return grundloesung(laenge, breite, vector[0], vector[1], vector[2], vector[3], vector[4])

def strukturiertes_absuchen_grundloesung(L, b, h1, h2, Emodul, q, k, alpha):
    # l = konst
    # b = konst
    h1min_max = h1.giveIntervall(alpha)
    h2min_max = h2.giveIntervall(alpha)
    Emin_max = Emodul.giveIntervall(alpha)
    qmin_max = q.giveIntervall(alpha)
    kmin_max = k.giveIntervall(alpha)

    part_func = partial(modifizierte_grundloesung, L, b)

    parameterbereich = np.array([h1min_max, h2min_max, Emin_max, qmin_max, kmin_max])
    initial_guess = np.average(parameterbereich,1)
    print("i=",initial_guess)

    M_min = strukturiertes_absuchen(part_func, initial_guess,parameterbereich)

#strukturiertes_absuchen(test_func, np.array([1,-1.5,-1.5]), np.array([[-1,2],[-2,-1],[-2,-1]]))