import numpy as np
from scipy.stats import norm
from scipy.stats import logistic
from scipy.stats import lognorm 
from matplotlib import pyplot as plt
from grundloesung_Feld import grundloesung_Feld
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

class LogisticdistributedVariable(StochasticVariable):

  def __init__(self, erwartungswert, standardabweichung):
    self.erwartungswert = erwartungswert
    self.standardabweichung = standardabweichung

  def get_sample(self):
    rv = logistic(self.erwartungswert, self.standardabweichung)
    return rv.rvs()

class ECDF:

  def __init__(self, samples):
    samples.sort()
    self.samples = samples
  # Gibt das q% Quantil der eCDF zurück.
  def quantile(self,q):
    size = len(self.samples)
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

  # Diese Funktion NICHT überschreiben alpha, epsilon, Pf
  def stochastic_analysis(self,level_reliability=0.95,confidence_interval=1e-3,threshold_probability=0.95):
    n_sim = (1.0/(1.0 - level_reliability) * threshold_probability * (1.0 -threshold_probability)/ (confidence_interval**2)) # Formel der Folie
    print("Anzahl der Monte Carlo Samples = ",n_sim)
    erg_samples = [] # ergebnisse
    for i in range(0,int(n_sim)):
      stoch_vars = self.get_stochastic_variables()
      stoch_samples = []
      for j in range(0,len(stoch_vars)):
        stoch_samples += [stoch_vars[j].get_sample()] # ein sample jeder Variable
      erg_samples += [self.basefunction(stoch_samples)]
    eCDF = ECDF(erg_samples)
    return eCDF

# Nutzungsweise von StochasticAnalysis:
# Implementierung der Grundlösung als "Kind" der Klasse
class GrundloesungFeld(StochasticAnalysis):
  # Der Initblock, hier alle deterministischen Ausprägungen aller NICHT stochastischen Variablen implementieren
  def __init__(self, laenge, breite, hoehe1, hoehe2, emodul, qbelast, mu_feder):
    self.laenge = laenge
    self.breite = breite
    self.hoehe1 = hoehe1
    self.hoehe2 = hoehe2
    self.emodul = emodul
    self.qbelast = qbelast
    self.mu_feder = mu_feder
  # Implementierung der Grundlösung, wo nur noch stochastische Variablen dazugegeben werden:
  def basefunction(self,stochastic_args):
    return grundloesung_Feld(self.laenge, self.breite, self.hoehe1, self.hoehe2, self.emodul, self.qbelast, stochastic_args[0])

  # Implementierung der Stochastischen Variablen 
  def get_stochastic_variables(self):
    # return [NormaldistributedVariable(self.mu_feder,100.0)]
    return [LogisticdistributedVariable(self.mu_feder, 0.07)]

# Klassendeklaration Ende
# Abschließend GrundloseungFeld instanziieren (in der Alpha Level Optimierung) und `stochastic_analysis()` ausführen.


grundFeld = GrundloesungFeld(10, 0.2, 0.7, 0.5, 2.1e8, 17.0, 1.0e4)
ecdf = grundFeld.stochastic_analysis(confidence_interval=1e-2)
quantil50 = ecdf.quantile(0.5)
print(quantil50)