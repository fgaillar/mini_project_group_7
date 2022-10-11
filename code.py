import gaming_tools as gt
import random
def reach_character(variety):
    """
    calcul the reach of the variety of the character.

    Parametres:
    ---------
    reach: reach of the character (int)

    Raises
    ------
    ValueError: if the character does not exist

    """
    if variety == "elf" or variety == "wizard":
        reach = 'long'
    else:
        reach = 'short'
    return reach
def character_life(variety):
    if variety == "dwarf":
        life = random.randint(10,50)
    elif variety == "healer" or 'wizard' or 'necromancer':
        life = random.randint(5,15)
    elif variety == "elf":
        life = random.randint(15,25)
    return life
def character_strength(variety):
        if variety== "dwarf":
            strength = random.randint(10, 50)
        elif variety == "healer" or 'wizard' or 'necromancer':
            strength = random.randint(5, 15)
        elif variety == "elf":
            strength = random.randint(15, 25)
        return strength
def create_new_player(character, variety):
    reach = reach_character(variety)
    life = character_life(variety)
    strength = character_strength(variety)
    gt.add_new_character(character, variety, reach, strength, life)
    print("character is create with name: %s, variety: %s,reach: %d, strength: %d, life: %d" %(character, variety, reach, strength, life))

def team_money(money):
    gt.set_team_money(money)
    return "you earned", money, "coins"

def life_mob():
    nb_mob_slayed = 0
    mob_life = random.randint(1,10)
    mob_life = mob_life * nb_mob_slayed
    return mob_life
def strength_mob():
    mob_strength = random.randint(1, 10)
    mob_strength = mob_strength * mob_strength
    return mob_strength
def reach_mob():
    mob_reach = random.randint(0, 1)
    if mob_reach == 0:
        mob_reach = 'short'
    else:
        mob_reach = 'long'
    return mob_reach
def nb_mob_slayed():
    mob_slayed = gt.get_nb_defeated()
def creature_name():
    mob_name = gt.get_random_creature_name()

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

create_new_creature()

def reset():
    gt.reset_game()

create_new_player('florian', 'necromancer')

reset()