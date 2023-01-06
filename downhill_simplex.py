
import numpy as np

from grundloesung import *

def downhill_simplex(function, parameterbereich: arrayShape):
    parameter = parameterbereich.len()
    points = np.zeros((parameter, parameter+1))
    # numpy.array.argsort
    # points
    # Array of indices that sort a along the specified axis. 
    # If a is one-dimensional, a[index_array] yields a sorted a. 
    # More generally, np.take_along_axis(a, index_array, axis=axis) always yields the sorted a, irrespective of dimensionality.

    # Mitte des Parameterbereichs, + zufällige punkte in jeder richtung als startpunkte

    # Start der Lösung
    print("Downhill Simplex Algorithmus")


main()