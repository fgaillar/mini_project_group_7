import gaming_tools as gt
def create_player(name, type):
    """Create a character/player

    Parameters :
    ------------
    name: name of player (str)
    type: role of caracter (str)
    """
    correct_type = True
    money = gt.get_team_money()

    if gt.is_there_a_creature() or gt.get_nb_defeated() > 0:
        print('You can\'t create another player during the game')
    else:
        if type == 'dwarf':
            gt.add_new_character(name, type, 'short', randint(10, 50), randint(10, 50))
        elif type == 'elf':
            gt.add_new_character(name, type, 'long', randint(15, 25), randint(15, 25))
        elif type == 'healer':
            gt.add_new_character(name, type, 'short', randint(5, 15), randint(5, 15))
        elif type == 'necromancer':
            gt.add_new_character(name, type, 'short', randint(5, 15), randint(5, 15))
        elif type == 'wizard':
            gt.add_new_character(name, type, 'long', randint(5, 15), randint(5, 15))
        else:
            print('Please enter a valid type !')
            correct_type = False

        if correct_type:
            print('Player %s created with %d strength, %d life and %s reach. You got 50 coins' % (name, gt.get_character_strength(name), gt.get_character_life(name), gt.get_character_reach(name)))
            gt.set_team_money(money + 50)

create_player('florian','elf')