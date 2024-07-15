import pandas

import Fighter as f

BORDER = "-" * 50
data = pandas.read_csv("skill_descriptions.csv")
# skill_list = data.Skill.to_list()
# skill_descript = data.Description.to_dict()
skill_list = data.to_dict()

new_skills_list = pandas.DataFrame(skill_list)
# TODO: USE NEW LIST BELOW TO PULL THE SKILL DESCRIPTION
# BASED ON skill_description_choice
new_skills_list.to_csv("new_skills_list_test.csv")
# print(skill_descript)
# print(f"{f.fighter_skills}")
#
# skill_description_choice = input("Type the skill to view skill description: \n").upper()
