import resources


class Slime:

    def __init__(self):
        self.maxhp = 10
        self.chp = 10
        self.remhp = round(self.chp / self.maxhp * resources.BARS)
        self.losshp = resources.BARS - self.remhp

    def lose_hp(self):
        
