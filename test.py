import gaming_tools as gt
import random
def fight(character, creature):
    if  not gt.get_creature_reach(creature) == 'short' and gt.get_character_reach(character) == 'long' :
        if gt.get_character_life(character) > 0:
            if gt.get_character_strength(character) < gt.get_creature_life(creature):
                gt.set_creature_life(creature, (gt.get_creature_life(creature) - gt.get_character_strength(character)))
            if gt.get_character_strength(character) >= gt.get_creature_life(creature):
                gt.set_creature_life(creature, 0)
                print('The creature %s is now dead by taking %d damage from %s' % (creature, gt.get_character_strength(character), character))
        else:
            print('This character is dead')
    else:
        print('You don\'t have the good reach')

    if not gt.get_creature_reach(creature) == 'short' and gt.get_character_reach(character) == 'long':
        if gt.get_character_life(character) > 0:
            if gt.get_creature_strength(creature) < gt.get_character_life(character):
                gt.set_character_life(character, (gt.get_character_life(character) - gt.get_creature_strength(creature)))
                print('The character %s has been hurt by %d from %s' % (character, gt.get_creature_strength(creature), creature))
            if gt.get_character_strength(creature) >= gt.get_character_life(character):
                gt.set_character_life(character, 0)

def attack(character, creature):
    if gt.get_character_reach(character) == gt.get_creature_reach(creature):
       if gt.get_character_strength(character) < gt.get_creature_life(creature):
           gt.set_creature_life(creature, (gt.get_creature_life(creature)-(gt.get_character_strength(character))))
           if gt.get_creature_strength(creature) > gt.get_character_life(character):
                gt.remove_characater(character)
                print(character, 'is dead')
       else:
           if gt.get_character_strength(character) >= gt.get_creature_life(creature) and gt.get_creature_strength(creature) >= gt.get_character_life(character):
                gt.remove_characater(character)
                gt.remove_creature(creature)
                print(creature, 'is dead')
                print(character, 'is dead')
           else:
               if gt.get_character_strength(character) >= gt.get_creature_life(creature):
                   gt.set_creature_life((gt.get_creature_life(creature))-(gt.get_character_strength(character)))
                   gt.remove_creature(creature)
                   print(creature, 'is dead')
    else:
        print('there is impossible to attack')