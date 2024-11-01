import random

import pandas as pd

# import enemies

LEVELUP = 20
BORDER = "-" * 50
BARS = 35
status_bar_symbol = "█"
lost_bar_symbol = "_"

# TODO: pull and store tier'd enemies inside variables to be chosen
# @ random depending on level of player
# ----------------- completed for low tier enemies


low_tier_enemies_data = pd.read_csv("low_tier_enemies.csv")
# low_tier_enemies = low_tier_enemies_data.to_dict()
low_tier_enemies = low_tier_enemies_data["enemy"]
lte_list = low_tier_enemies.to_list()


# used for roll chance of encountering an enemy
def enemy_enecounter_roll():
    number_chance = [nums for nums in range(0, 100)]
    enemy_encounter_chance = random.choice(number_chance)
    enemy_choice = random.choice(lte_list)
    # FIX: continue roll for rand enemy choice
    if enemy_encounter_chance > 80:

        print("You have encountered an enemy!!")
        return True
