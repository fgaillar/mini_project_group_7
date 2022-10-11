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
def attack(character, creature):
    if gt.get_character_strength(character) >= gt.get_creature_life(creature):
        ...
    elif gt.get_character_strength(character) < gt.get_creature_life(creature):
        ...
    elif gt.get_creature_strength(creature) >= gt.get_character_life(character):
        ...
    elif gt.get_creature_strength(creature) < gt.get_character_life(character):
        ...


def restart():
    gt.reset_game()
attack('merci', 'Python#611')

