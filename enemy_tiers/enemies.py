import sys

sys.path.insert(1, "../")

import colors
import resources


class Slime:

    def __init__(self):
        self.maxhp = 10
        self.chp = 10
        self.remhp = round(self.chp / self.maxhp * resources.BARS)
        self.losshp = resources.BARS - self.remhp
        self.attack = 1
        self.defense = 5

    def status_bars(self):
        print(f"HEALTH: {self.chp}/{self.maxhp}")
        print(
            f"|{colors.color_green2}{self.remhp*resources.status_bar_symbol}{self.losshp*resources.lost_bar_symbol}{colors.color_default}|"
        )

    # def fight(self):
