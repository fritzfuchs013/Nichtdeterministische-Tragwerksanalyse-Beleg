class FuzzyDreieck:
    def __init__(self, links, maximuml, maximumr, rechts):
        self.links = links
        self.maximuml = maximuml
        self.maximumr = maximumr
        self.rechts = rechts

    def giveIntervall(self, alphalvl : float) -> (float, float):
        newLinks = self.links + alphalvl * (self.maximuml - self.links)
        newRechts = self.maximumr - alphalvl * (self.rechts - self.maximumr)
        return newLinks, newRechts

a = FuzzyDreieck(1, 4, 4, 5)
x, y = a.giveIntervall(0.1)
print(x,y)

# Eingangsgrößen

h1 = FuzzyDreieck(0.65, 0.7, 0.7, 0.75)
h2 = FuzzyDreieck(0.48, 0.5, 0.5, 0.52)

