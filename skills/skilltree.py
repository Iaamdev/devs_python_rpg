import sys

import pandas as pd

sys.path.insert(1, "../")

import resources
from Fighter import (
    Fighter,
    fighter_skills,
    is_paladin,
    is_warrior,
    paladin_skills,
    warrior_skills,
)

BORDER = "-" * 50
fighter_data = pd.read_csv("fighter_sd.csv")
mage_data = pd.read_csv("mage_sd.csv")
thief_data = pd.read_csv("thief_sd.csv")
f = Fighter()


def skill_check():
    skill_check_complete = False

    # FIX: create a loop for displaying skill descriptions
    while not skill_check_complete:

        if f.level < 15:
            print(f"{fighter_skills}\n")
        elif f.level > 15 and is_paladin:
            print(f"{fighter_skills + paladin_skills}\n")
        elif f.level > 15 and is_warrior:
            print(f"{fighter_skills + warrior_skills}\n")

        # ask for user input on what skill they would like to view
        skill_choice = input("What skill would you like to view?:\n").upper()
        print(resources.BORDER)

        # run through the class row to check choice and display description
        for key, row in fighter_data.iterrows():
            if skill_choice == row.Skill[0:]:
                print(f"Description: {row.Description}")
                print(f"Stat Effects: {row.Stats}")
                print(resources.BORDER)

        # ask the user if they would like to look at another skill if not cancel the loop
        skill_choice = input(
            "Would you like to look at another skill? (y/n):\n"
        ).upper()
        if skill_choice == "Y":
            print(resources.BORDER)
            pass
        elif skill_choice == "N":
            skill_check_complete = True


skill_check()
