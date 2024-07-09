LEVELUP = 20
BORDER = "-" * 50
BARS = 20
REMAINING_HEALTH_SYMBOL = "🟩"
LOST_BAR_SYMBOL = "_"
REMAINING_FOCUS_SYMBOL = "🟦"
fighter_skills = ["SHIELD BASH", "DOUBLE STRIKE", "FORTIFY"]
is_paladin = False
warrior_skills = ["Warcry", "Overhead Slam", "Haymaker"]
is_warrior = False


# Creating the Fighter Class along with advanced Classes
class Fighter:
    # started off the class with fighter specific stats
    def __init__(self):
        self.maxhp = 100
        self.chp = 100
        self.remhp = round(self.chp / self.maxhp * BARS)
        self.losshp = BARS - self.remhp
        self.maxfp = 20
        self.cfp = 20
        self.remfp = round(self.cfp / self.maxfp * BARS)
        self.lossfp = BARS - self.remfp
        self.defense = 20
        self.attack = 10
        self.xp = 0
        self.level = 1
        self.current_skills = ["STRIKE", "BLOCK"]

    # give the player health bar based off of their HP and FP
    def status_bars(self):
        print(f"HEALTH: {self.chp}/{self.maxhp}")
        print(f"|{self.remhp*REMAINING_HEALTH_SYMBOL}{self.losshp*LOST_BAR_SYMBOL}|")
        print(f"FOCUS: {self.cfp}/{self.maxfp}")
        print(f"|{self.remfp*REMAINING_FOCUS_SYMBOL}{self.lossfp*LOST_BAR_SYMBOL}|")

    # def

    # level up player based on current xp
    def lvl_up(self):
        if self.xp == LEVELUP:
            self.level += 1
            print(f"Level Up!\nYou are now Level {self.level}")
            self.xp = 0
            self.chp += 5
            self.maxhp += 5
            self.cfp += 5
            self.maxfp += 5
            self.defense += 10
            self.attack += 5

    def fighter_skill_up(self):
        skill_chosen = False
        while not skill_chosen:
            # used to break the loop if all skills are aquired
            if len(fighter_skills) == 0:
                print("You Have all Fighter Skills!")
                print(f"Current Skills: {self.current_skills}")
                break
            print(fighter_skills)
            skill_choice = input("Choose a Skill: \n").upper()
            # NOTE: the below elif is used to break out of skill choosing
            # loop
            if skill_choice == "QUIT":
                break
            # NOTE: May want to change take off brackets in fighter_skills list
            # looping through every fighter skill to check availability
            for skills in fighter_skills:
                # if valid skill is choosen, accept and store into self.current_skills for know player
                # skills and remove it from the choices of skills
                # NOTE: may need to fix this "if" loop for skill_choice
                if skill_choice == skills:
                    self.current_skills.append(skill_choice)
                    fighter_skills.remove(skill_choice)
                    print(f"You chose {skill_choice}")
                    skill_chosen = True
                else:
                    pass
            if skill_chosen:
                print(BORDER)
                print(f"Current Skills: {self.current_skills}")
            # FIX: -- if the player inputs an invalid input, reprompt them to make a valid input --

    # NOTE: Re-up on class inheritance to possible use this on file for basic classes
    # then create separate class for advance classes to make in depth class structure
