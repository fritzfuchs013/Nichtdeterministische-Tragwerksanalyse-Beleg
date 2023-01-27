import numpy as np
from scipy.stats import norm 
from scipy.stats import lognorm 
from matplotlib import pyplot as plt
import math

class StochasticVariable:
  def get_sample(self):
    return 0.0

class NormaldistributedVariable(StochasticVariable):
  
  def __init__(self, erwartungswert, standardabweichung):
    self.erwartungswert = erwartungswert
    self.standardabweichung = standardabweichung

  def get_sample(self):
    rv = norm(self.erwartungswert, self.standardabweichung)
    return rv.rvs()

# Überlegung für LogNormalVerteilung https://www.desmos.com/calculator/zjm58uxrkj

class ECDF:

  def __init__(self, samples):
    samples.sort()
    self.samples = samples
  # Gibt das q% Quantil der eCDF zurück.
  def quantile(self,q):
    size = samples.len()
    index = int(q / size)
    return self.samples[index]
  # Hier können noch mehr Funktionen implementiert werden.

class StochasticAnalysis:
  # Ein Kind der Stochastischen Analyse muss 2 Funktionen implementieren
  def basefunction(self,stochastic_args):
    print("Hier sollte die Funktion aufgerufen werden, für die die Stochastische Analyse durchgeführt werden soll!")
    return 0.0

  # Hier wird ein Array stochastischer Variablen zurückgegeben.
  def get_stochastic_variables(self):
    print("Diese Funktion sollte alle Stochastischen Variablen zurückgeben")
    return []

  # Diese Funktion NICHT überschreiben
  def stochastic_analysis(self,level_reliability,confidence_interval,threshold_probability):
    n_sim = (1.0/(1.0 - level_reliability) * threshold_probability * (1.0 -threshold_probability)/ (confidence_interval**2)) # Formel der Folie
    erg_samples = [] # ergebnisse
    for i in range(0,int(n_sim)):
      stoch_vars = self.get_stochastic_variables()
      stoch_samples = []
      for j in range(0,stoch_vars.len()):
        stoch_samples += [stoch_vars[j].get_sample()] # ein sample jeder Variable
      erg_samples += [self.basefunction(stoch_samples)]
    eCDF = ECDF(erg_samples)
    return eCDF

#fck scipy.lognormal!
#emodul = NormaldistributedVariable(21.0e4,100.0)
#federsteif = LogDistributedVariable(21.0,100.0)

#indezes = []
#emodulsample = []
#federsteifsample = []
#for i in range(0,1000):
#  emodulsample += [emodul.get_sample()]
#  federsteifsample += [federsteif.get_sample()]
#  indezes += [i*1/1000]

#emodulsample.sort()
#federsteifsample.sort()

#plt.plot(federsteifsample, indezes, color="navy")
#plt.plot(federsteifsample, indezes, color="navy")
#plt.show()