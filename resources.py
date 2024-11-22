import random

import pandas as pd

import enemy_tiers.enemies

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
    # used to roll enemy if greater than 80
    if enemy_encounter_chance > 70:
        print("You have encountered", enemy_choice.upper(), "!!")
        if enemy_choice == "SLIME":
            enemy_tiers.enemies.Slime.status_bars()
        # FIX: add way to show status bars for slime
        # return True
    else:
        pass


enemy_enecounter_roll()
