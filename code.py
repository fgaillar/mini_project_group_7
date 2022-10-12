import gaming_tools as gt
import random

def create_new_player(character, variety):
    if variety == "wizard" or variety == "elf":
        reach = "long"
    elif variety == "dwarf" or variety == "necromancer" or variety == "healer":
        reach = "short"
    if variety == "dwarf":
        strength = random.randint(10, 50)
        life = random.randint(10, 50)
    elif variety == "elf":
        strength = random.randint(15, 25)
        life = random.randint(15, 25)
    elif variety == "necromancer" or "wizard" or "healer":
        life = random.randint(5, 15)
        strength = random.randint(5, 15)
    gt.add_new_character(character, variety, reach, strength, life)
    print("The character %s appeared! a hero %s with %s reach, %d strength and %d life " % (character, variety, reach, strength, life))
def team_money():
    money = gt.get_team_money()
    print('Team actualy have %d money' % (money))
def create_new_creature():
    creature = gt.get_random_creature_name()
    randreach = random.randint(1, 2)
    if randreach == 1:
        reach = "short"
    else:
        reach = "long"
    life = (random.randint(1, 10))*(1 + gt.get_nb_defeated())
    strength = (random.randint(1, 10))*(1 + gt.get_nb_defeated())
    gt.add_creature(creature, reach, strength, life)
    print('the creature %s has appeared! it has %s reach, %d life, %d strength' % (creature, reach, life, strength))
def fight(character, creature):
    if gt.get_character_life(character) > 0:
        if (gt.get_character_reach(character) == 'long') or (gt.get_character_reach(character) == 'short' and gt.get_creature_reach(creature) == 'short'):
            if gt.creature_exists(creature):
                 if gt.get_character_strength(character) < gt.get_creature_life(creature):
                        gt.set_creature_life(creature, (gt.get_creature_life(creature) - gt.get_character_strength(character)))
                        if gt.get_creature_strength(creature) < gt.get_character_life(character):
                            gt.set_character_life(character, (gt.get_character_life(character) - gt.get_creature_strength(creature)))
                            print('The character %s has been hurt by %d from %s, now he have %d HP.' % (character, gt.get_creature_strength(creature), creature, gt.get_character_life(character)))
                        if gt.get_character_strength(character) >= gt.get_character_life(character):
                            gt.set_character_life(character, 0)
                            print('%s character have died' % (character))
                 elif gt.get_character_strength(character) >= gt.get_creature_life(creature):
                        if gt.get_creature_strength(creature) < gt.get_character_life(character):
                            gt.set_character_life(character, (gt.get_character_life(character) - gt.get_creature_strength(creature)))
                            print('The character %s has been hurt by %d from %s, now he has %d HP.' % (character, gt.get_creature_strength(creature), creature, gt.get_character_life(character)))
                        elif gt.get_creature_strength(creature) >= gt.get_character_life(character):
                            gt.set_character_life(character, 0)
                            print('%s character have died' % (character))
                        print('The creature %s is now dead by taking %d damage from %s' % (creature, gt.get_character_strength(character), character))
                        gt.set_team_money(gt.get_team_money() + 50)
                        print('You earn 50 coins, current balance: %d' % (gt.get_team_money()))
                        gt.remove_creature(creature)
                        gt.set_nb_defeated((gt.get_nb_defeated() + 1))
                        print('Creature killed: %d' % (gt.get_nb_defeated()))
            else:
                print('This creature doesn\'t exist')
        else:
            print('Character doesn\'t have the reach')
    else:
        print("This character is dead")
def divide_hp(character1, creature):
    if gt.character_exists(character1):
        if gt.get_character_variety(character1) == "wizard":
            if gt.get_team_money() >= 20:
                if gt.creature_exists(creature):
                    gt.set_creature_life(creature, (gt.get_creature_life(creature)//2))
                    gt.set_team_money((gt.get_team_money() - 20))
                    print('%s has now %d HP' % (creature, gt.get_creature_life(creature)))
                    print('Current balance is at: %d' % (gt.get_team_money()))
                else:
                    print("%s doesn\'t exist" %(creature))
            else:
                print("Your team is too poor, try again when you have earned more money!")
        else:
            print('%s hasn\'t such power.' %(character1))
    else:
        print("%s doesn\'t exist." % (character1))
def heal(character1, character2):
    if gt.character_exists(character1):
        if gt.get_character_variety(character1) == "healer":
            if gt.get_team_money() >= 5:
                if gt.character_exists(character2):
                    gt.set_character_life(character2, (gt.get_character_life(character2) + 10))
                    gt.set_team_money((gt.get_team_money()-5))
                    print("%s has recover 10 hp and is now at : %d life" % (character2, gt.get_character_life(character2)))
                    print("Current balance is at: %d" % (gt.get_team_money()))
                else:
                    print('%s doesn\'t exist' %(character2))
            else:
                print("Your team is too poor, try again when you have earned more money!")
        else:
            print('%s hasn\'t such power.' %(character1))
    else:
        print("%s doesn\'t exist." %(character1))

def revive(character1,character2):
    if gt.character_exists(character1):
        if gt.get_character_variety(character1) == "necromancer":
            if gt.get_team_money() >= 75:
                if gt.character_exists(character2):
                    if gt.get_character_life(character2) == 0:
                        gt.set_character_life(character2, (gt.get_character_life(character2) + 10))
                        print("%s come back from the death and has now: %d hp" % (character2, gt.get_character_life(character2)))
                        print("Current balance is at: %d" % (gt.get_team_money()))
                    else:
                        print("%s is still alive" % (character2))
                else:
                    print('%s doesn\'t exist' % (character2))
            else:
                print("Your team is too poor, try again when you have earned more money")
        else:
            print('%s hasn\'t such power' %(character1))
    else:
        print("%s doesn\'t exist" %(character1))

def restart():
    gt.reset_game()
    gt.set_team_money(50)

restart()