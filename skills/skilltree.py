import sys

import pandas as pd

# FIX: figure out how to import from different file path
from Devs_PythonRPG.Fighter import Fighter

BORDER = "-" * 50
fighter_data = pd.read_csv("fighter_sd.csv")
mage_data = pd.read_csv("mage_sd.csv")
thief_data = pd.read_csv("thief_sd.csv")
f = Fighter

print(f.warrior_skills)


def skill_check():
    skill_check_complete = False

    # if f.level < 15:
    #     print(f"{fighter_skills}\n")
    # elif f.level > 15 and is_paladin:
    #     print(f"{paladin_skills}\n")
    # elif f.level > 15 and is_warrior:
    #     print(f"{warrior_skills}\n")

    while skill_check_complete:
        # ask for user input on what skill they would like to view
        skill_choice = input("What skill would you like to view?:\n").upper()
        # if their choice is == any skill within their class show
        # the class description
        # if skill_choice == fighter_data.Skill:
        print(fighter_data.Skill)
    # ask the user if they would like to look at another skill
    # if not cancel the loop


# skill_check()

# TODO: USE NEW LIST BELOW TO PULL THE SKILL DESCRIPTION
# BASED ON skill_description_choice
# print(skill_descript)
# print(f"{f.fighter_skills}")
#
# skill_description_choice = input("Type the skill to view skill description: \n").upper()
