import numpy as np


def give_discrete_Value_for_Quantile(my, quantil = 0.9, scale = 0.07):
    federsteifigkeit = - np.log((1 / quantil) - 1) * scale + my

    federsteifigkeit = federsteifigkeit * (10 ** 4) # Korrekte Größe der Federsteifigkeit wird hergestellt

    return federsteifigkeit