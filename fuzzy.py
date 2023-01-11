class FuzzyTrapez:
    def __init__(self, links, maximuml, maximumr, rechts):
        self.links = links
        self.maximuml = maximuml
        self.maximumr = maximumr
        self.rechts = rechts

    def giveIntervall(self, alphalvl : float) -> (float, float):
        m_links  = 1.0 / (self.maximuml - self.links)
        m_rechts = 1.0 / (self.maximumr - self.rechts)

        new_links  = self.links + (alphalvl / m_links)
        new_rechts = self.maximumr + ((alphalvl -1 ) / m_rechts)
        return new_links, new_rechts