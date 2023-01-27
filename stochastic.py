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