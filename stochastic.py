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

class LogDistributedVariable(StochasticVariable):

  def __init__(self, erwartungswert, standardabweichung):
    self.erwartungswert = erwartungswert
    self.standardabweichung = standardabweichung

  # Aufpassen: Damit sich die Werte "Erwartungswert" und "Standardabweichung" so verhalten wie sich sich verhalten sollen,
  # sind die Werte so hier transformiert, siehe: https://stackoverflow.com/questions/8870982/how-do-i-get-a-lognormal-distribution-in-python-with-mu-and-sigma?rq=1 !
  def get_sample(self):
    mu = self.erwartungswert     # target mean
    sigma = np.sqrt(self.standardabweichung)  # target varianz

    a = 1 + (sigma / mu) ** 2
    s = np.sqrt(np.log(a))
    scale = mu / np.sqrt(a)
    di = lognorm(s=s, scale=scale)
    return di.rvs()

class ECDF:

  def __init__(self, samples):
    samples.sort()
    self.samples = samples

  def quantile(self,q):
    size = samples.len()
    index = math.floor(q / size)
    return self.samples[index]


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