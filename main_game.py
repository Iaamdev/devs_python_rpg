import encounter
import resources
import skilltree
from enemy_tiers.enemies import Slime
from Fighter import Fighter

enemy = Slime()
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
elif choose_class == "MAGE":
    print("Mage Chosen!!\n")
    print("The Journey Begins!!\n")
    # player_class = mage_player
    # mage_player.status_bars()

print(resources.BORDER)

# TODO: make a different "if" loop for each class (later)
# NOTE: Currently working on fighter class hence fighter only path below
while game_start:

    if player_class == fighter_player:
        # used currently to roll for enemy encounters
        resources.enemy_enecounter_roll()
        if resources.enemy_enecounter_roll() == True:
            print(enemy.status_bars())
        else:
            pass

        if fighter_player.xp >= resources.LEVELUP:
            fighter_player.lvl_up()
            fighter_player.status_bars()
            print(resources.BORDER)

            if fighter_player.level % 3 == 0:
                fighter_player.fighter_skill_up()

        print("The Traveling Continues...")
        # NOTE: a current loop for testing the lvl up sys. to
        # stop code
        continue_game = input("Continue? (y/n):\n").upper()
        print(resources.BORDER)
        if continue_game == "Y":
            skill_check = input("Would you like to check your skills? (y/n):\n").upper()
            if skill_check == "Y":
                print(resources.BORDER)
                skilltree.skill_check()
                continue
        elif continue_game == "N":
            game_start = False


# TODO: Continue working on fighter class
# TODO: Make an enemy to test out combat functions
# FIX: The health bar does not pop up after "The Traveling Continues"
# like I want it to
