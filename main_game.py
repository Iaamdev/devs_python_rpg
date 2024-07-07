from Fighter import Fighter

game_start = True
player_class = ""

print("Welcome to Dev's Python RPG\n")
choose_class = input("Choose Your Starting Class: \n\nFIGHTER//MAGE//THIEF:\n").upper()

fighter_player = Fighter()
# mage_player =
# thief_player =
if choose_class == "FIGHTER":
    player_class = fighter_player

# TODO: make a different "if" loop for each class
# NOTE: Currently working on fighter class hence fighter only path below
while game_start:
    # NOTE: was debugging my fighter_skill_up method
    if player_class == fighter_player:
        if fighter_player.xp == 20:
            fighter_player.lvl_up()
            fighter_player.fighter_skill_up()
            print(fighter_player.current_skills)
            game_start = False
        fighter_player.xp += 20

# TODO: continue working on fighter class
