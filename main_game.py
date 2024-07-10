from Fighter import Fighter

# separator for text
BORDER = "-" * 50

game_start = True
player_class = ""

print("Welcome to Dev's Python RPG\n")
choose_class = input(
    "Choose Your Starting Class: \n\nFIGHTER ⚔️// MAGE 🪄//THIEF 🗡️:\n"
).upper()

fighter_player = Fighter()
# mage_player =
# thief_player =
print(BORDER)

if choose_class == "FIGHTER":
    print("Fighter Chosen!!\n")
    player_class = fighter_player
    fighter_player.status_bars()
print(BORDER)


# TODO: make a different "if" loop for each class
# NOTE: Currently working on fighter class hence fighter only path below
while game_start:

    if player_class == fighter_player:

        if fighter_player.xp == 20:
            fighter_player.lvl_up()
            fighter_player.status_bars()
            print(BORDER)

            if fighter_player.level % 3 == 0:
                fighter_player.fighter_skill_up()

        fighter_player.xp += 5

        print("The Traveling Continues...")
        # NOTE: a current loop for testing the lvl up sys. to
        # stop code
        continue_game = input("Continue? (y/n):\n").upper()
        print(BORDER)
        if continue_game == "Y":
            pass
        elif continue_game == "N":
            game_start = False


# TODO: Continue working on fighter class
# TODO: Make an enemy to test out combat functions
# TODO: Make descriptions of class skills in anohter file
# for the player to then pull at the skill selection chooser
