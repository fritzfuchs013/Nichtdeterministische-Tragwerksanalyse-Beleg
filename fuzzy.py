class FuzzyTrapez:
    def __init__(self, links, maximuml, maximumr, rechts):
        self.links = links
        self.maximuml = maximuml
        self.maximumr = maximumr
        self.rechts = rechts

    def giveIntervall(self, alphalvl : float) -> (float, float):
        newLinks = self.links + alphalvl * (self.maximuml - self.links)
        newRechts = self.maximumr - alphalvl * (self.rechts - self.maximumr)
        return newLinks, newRechts