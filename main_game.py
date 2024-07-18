import resources
from Fighter import Fighter
from skills import skilltree as st

# separator for text

game_start = True
player_class = ""

print("Welcome to Dev's Python RPG\n")
choose_class = input(
    "Choose Your Starting Class: \n\nFIGHTER ⚔️// MAGE 🪄//THIEF 🗡️:\n"
).upper()

fighter_player = Fighter()
# mage_player =
# thief_player =
print(resources.BORDER)

if choose_class == "FIGHTER":
    print("Fighter Chosen!!\n")
    print("The Journey Begins!!\n")
    player_class = fighter_player
    fighter_player.status_bars()
print(resources.BORDER)


# TODO: make a different "if" loop for each class (later)
# NOTE: Currently working on fighter class hence fighter only path below
while game_start:

    if player_class == fighter_player:
        # used currently to roll for enemy encounters
        resources.enemy_enecounter_roll()

        if fighter_player.xp >= resources.LEVELUP:
            fighter_player.lvl_up()
            fighter_player.status_bars()
            print(resources.BORDER)

            if fighter_player.level % 3 == 0:
                fighter_player.fighter_skill_up()

        print("The Traveling Continues...")
        # NOTE: a current loop for testing the lvl up sys. to
        # stop code
        continue_game = input("Continue Skill check? (y/n):\n").upper()
        print(resources.BORDER)
        if continue_game == "Y":
            skill_check = input("Would you like to check your skills? (y/n):\n").upper()
            if skill_check == "Y":
                st.skill_check()
                continue
        elif continue_game == "N":
            game_start = False


# TODO: Continue working on fighter class
# TODO: Make an enemy to test out combat functions
