class Chrono:

    def __init__(self, h, m, s):
        self.secondes = s
        self.minutes = m
        self.heures = h

    def augmenter_secondes(self, secondes):
        self.secondes += secondes

        self.minutes += self.secondes // 60
        self.secondes = self.secondes % 60

        self.heures += self.minutes // 60
        self.minutes = self.minutes % 60

    def __str__(self):
        return str(self.heures) + "h " + str(self.minutes) + "min " + str(self.secondes) + "sec"

t = Chrono(21, 24, 55)
print(t)
t.augmenter_secondes(10)
print(t)