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
    # NOTE: currently debugging my fighter_skill_up method
    if player_class == fighter_player:
        if fighter_player.xp == 20:
            print(BORDER)
            fighter_player.lvl_up()
            fighter_player.status_bars()
            print(BORDER)
            fighter_player.fighter_skill_up()
            print(BORDER)
            # NOTE: a current loop for testing the lvl up sys. to
            # stop code
            continue_game = input("Continue? (y/n):\n").upper()
            if continue_game == "Y":
                pass
            elif continue_game == "N":
                game_start = False
            # game_start = False
        fighter_player.xp += 20

# TODO: continue working on fighter class
