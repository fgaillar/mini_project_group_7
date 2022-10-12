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


def restart():
    gt.reset_game()
    gt.set_team_money(50)

restart()