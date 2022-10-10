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
    return character, variety, reach, life, strength

def create_monster(monter_name,):