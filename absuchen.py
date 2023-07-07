
from functools import reduce,partial
import numpy as np
import numpy.linalg as linalg
import math
import scipy
from grundloesung_Einspannung import grundloesung_Einspannung
from stochastic import GrundloesungFeld
from fuzzy import FuzzyTrapez
# parameterbereich hat n paare an oberen und unteren Grenzen
# 

def und(a,b):
    return a and b

def strukturiertes_absuchen(function, initial_guess, parameterbereich):
    parameter = parameterbereich.shape[0]
    #print(parameter)
    schrittweite = 0.9*np.abs(np.average(parameterbereich,1) - np.array(parameterbereich).T[0])
    #print(schrittweite)
    old_point = initial_guess
    old_function_value = function(initial_guess)
    new_candidate_point = np.zeros(old_point.shape[0])
    max_iter = 1000
    itera = 0

    while itera < max_iter:
        
        #print(old_function_value)
        itera = itera +1
        new_point_found = False
        for i in range(0,old_point.shape[0]):
            #print(itera,schrittweite)
            mn, mx = np.array(parameterbereich).T
            if schrittweite[i] < 1e-15:
                #print(old_function_value)
                continue 
            
            delta = np.zeros(old_point.shape[0])
            delta[i] = schrittweite[i]
            #print(delta)
            new_point = old_point + delta
            
            new_function_value = function(new_point)
            #print(new_point,new_function_value)

            is_in_bounds = True
            for para in range(0,parameter):
                if schrittweite[para] < 1e-15: continue
                is_in_bounds = new_point[para] >= mn[para] and new_point[para] <= mx[para] and is_in_bounds
            #print(is_in_bounds)

            if is_in_bounds and new_function_value > old_function_value:
                old_function_value = new_function_value
                new_candidate_point = new_point
                new_point_found = True

            # das ganze nochmal in andere raumrichtung
            delta = np.zeros(old_point.shape[0])
            delta[i] = - schrittweite[i]
            #print(delta)
            new_point = old_point + delta
            #print(delta, new_point - old_point, new_point)
            new_function_value = function(new_point)

            is_in_bounds = True
            for para in range(0,parameter):
                if schrittweite[para] < 1e-15: continue
                is_in_bounds = new_point[para] >= mn[para] and new_point[para] <= mx[para] and is_in_bounds
            #print(is_in_bounds)

            if is_in_bounds and new_function_value > old_function_value:
                old_function_value = new_function_value
                new_candidate_point = new_point
                new_point_found = True

        #print(schrittweite, old_point, new_candidate_point)
        

        if new_point_found:
            if abs(linalg.norm(old_point - new_candidate_point)) < 1e-10:
                break
            old_point = new_candidate_point
        else: 
            schrittweite = schrittweite * 0.7
    return old_point

def test_func(werte):
    return (werte[0]-3.5) ** 2 + werte[1] ** 2 + werte[2] ** 2

def modifizierte_grundloesung(laenge, breite, vector):
    grundFeld = GrundloesungFeld(laenge, breite, vector[0], vector[1], vector[2], vector[3], vector[4])
    ecdf = grundFeld.stochastic_analysis(confidence_interval=1e-1)
    return ecdf.quantile(0.9)

def modifizierte_grundloesung_max(laenge, breite, vector):
    grundFeld = GrundloesungFeld(laenge, breite, vector[0], vector[1], vector[2], vector[3], vector[4])
    ecdf = grundFeld.stochastic_analysis(confidence_interval=1e-1)
    return -ecdf.quantile(0.9)

def strukturiertes_absuchen_grundloesung(L, b, h1, h2, Emodul, q, k, alpha):
    # l = konst
    # b = konst
    h1min_max = h1.giveIntervall(alpha)
    h2min_max = h2.giveIntervall(alpha)
    Emin_max = Emodul.giveIntervall(alpha)
    qmin_max = q.giveIntervall(alpha)
    kmin_max = k.giveIntervall(alpha)

    part_func = partial(modifizierte_grundloesung, L, b)
    part_func_max = partial(modifizierte_grundloesung_max, L, b)

    parameterbereich = np.array([h1min_max, h2min_max, Emin_max, qmin_max, kmin_max])
    initial_guess = np.average(parameterbereich,1)
    #print("i=",initial_guess)

    M_min = strukturiertes_absuchen(part_func, initial_guess,parameterbereich)
    M_min = part_func(M_min)

    M_max = strukturiertes_absuchen(part_func_max, initial_guess,parameterbereich)
    M_max = part_func(M_max)

    return M_min, M_max

strukturiertes_absuchen(test_func, np.array([-50,-1,-1.5]), np.array([[-100,200],[-1,-1],[-2,-1]]))