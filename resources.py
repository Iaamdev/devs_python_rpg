import random

import pandas

# import enemies

LEVELUP = 20
BORDER = "-" * 50
BARS = 35
status_bar_symbol = "█"
lost_bar_symbol = "_"
# TODO: pull and store tier'd enemies inside variables to be chosen
# @ random depending on level of player


# used for roll chance of encountering an enemy
def enemy_enecounter_roll():
    number_chance = [nums for nums in range(0, 100)]
    enemy_encounter_chance = random.choice(number_chance)
    if enemy_encounter_chance > 80:
        print("You have encountered an enemy!!")
        return True
