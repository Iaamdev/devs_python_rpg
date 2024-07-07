LEVELUP = 20
fighter_skills = ["SHIELD BASH", "DOUBLE STRIKE", "FORTIFY"]
is_fighter = True
paladin_skills = ["Holy Strike", "Cure", "Divine Blessing", "Smite's Hammer"]
is_paladin = False
warrior_skills = ["Warcry", "Overhead Slam", "Haymaker"]
is_warrior = False


# Creating the Fighter Class along with advanced Classes
class Fighter:
    # started off the class with fighter specific stats
    def __init__(self):
        self.hp = 100
        self.fp = 50
        self.defense = 20
        self.attack = 10
        self.xp = 0
        self.level = 1
        self.current_skills = ["STRIKE", "BLOCK"]

    # level up player based on current xp
    def lvl_up(self):
        if self.xp == LEVELUP:
            self.level += 1
            print(f"Level Up!\nLevel {self.level}")
            self.xp = 0
            self.hp += 20
            self.fp += 10
            self.defense += 10
            self.attack += 5

    def fighter_skill_up(self):
        skill_chosen = False
        print(fighter_skills)
        while not skill_chosen:
            skill_choice = input("Choose a Skill: \n").upper()
            # NOTE: May want to change take off brackets in fighter_skills list
            # looping through every fighter skill to check availability
            for skills in fighter_skills:
                # if valid skill is choosen, accept and store into self.current_skills for know player
                # skills and remove it from the choices of skills
                # NOTE: may need to fix this "if" loop for skill_choice
                if skill_choice == skills:
                    self.current_skills.append(skill_choice)
                    fighter_skills.remove(skill_choice)
                    skill_chosen = True
                else:
                    pass
            # FIX: -- if the player inputs an invalid input, reprompt them to make a valid input --
