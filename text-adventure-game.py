

#BLACK MAGIC ACROPOLIS

#Text-Based Adventure Game
#by c-l90
#------------------------------------------------------------#



import random
import math 

def scenario_selection():
    scenario_list = ['Dark Temple', 'Occultist\'s Library', 'Sorcerer\'s Trial']
    random_scenario = random.choice(scenario_list)
    def selection_process():
        scenario_choice = input('\nChoose a scenario:\n- Dark Temple (D)\n- Occultist\'s Library (O)\n- Sorcerer\'s Trial (S)\n- Random (R)\n>> ').upper()
        if scenario_choice == 'D':
            print('You have chosen the Dark Temple episode')
        elif scenario_choice == 'O':
            print('You have chosen the Occultist\'s Library episode')
        elif scenario_choice == 'S':
            print('You have chosen the Sorcerer\'s Trial episode')
        elif scenario_choice == 'R':
            print(f'You are playing the {random_scenario} episode\n')
        else:
            print('Invalid selection. Please try again.')
            selection_process()
    selection_process()

def character_selection():
    character_list = ['Occultist', 'Hunter', 'Emissary']
    random_choice = random.choice(character_list)
    def choice_process():
        player_choice = input('\nSelect your character:\n- Occultist (O)\n- Hunter (H)\n- Emissary (E)\n- Random (R)\n>> ').upper()
        if player_choice == 'O':
            print('You have chosen the role of the Occultist')
        elif player_choice == 'H':
            print('You have chosen the role of the Hunter')
        elif player_choice == 'E':
            print('You have chosen the role of the Emissary')
        elif player_choice == 'R':
            print(f'You are the {random_choice}\n')
        else:
            print('Invalid selection. Please try again.')
            choice_process()
    choice_process()



def battle():

    #Setup
    enemy_list = ['Prophet', 'Mercenary', 'Practitioner', 'Demon', 'Foot Soldier', 'Wild Boar']
    random_enemy = random.choice(enemy_list)
    global enemy_health
    enemy_health = 100
    print(f'\nYou have encountered the {random_enemy}.\n')

    #Attack Sequence
    def attack_sequence():
        global enemy_health
        while enemy_health > 0:
            initial_player_choice = input('Choose an attack:\n- Spirit Ambush (S)\n- Dark Incantation (D)\n- Morningstar Attack (M)\n- Poisoned Arrow (P)\n>> ').upper()
            if initial_player_choice == 'S' or initial_player_choice == 'D' or initial_player_choice == 'M' or initial_player_choice == 'P':
                enemy_health -= random.randint(1, 100)
                print(f'Enemy health now at {enemy_health}\n')
            else:
                print('Invalid choice.\n')
                attack_sequence()

    attack_sequence()
    print(f'The {random_enemy} has been defeated.\n')



def story_one():
    print('You have been banished by the King, cast out on charges of black magic. You leave the City Gates and travel along the lonely path. You must reach safety, for evil things come out at night.\nYou come across a split in the road.\n')
    def first_choice():
        story_one_choice = input('Do you go left (L) or right (R)?\n >> ').upper()
        if story_one_choice == 'L':
            print('\nYou have chosen the Left Path, which leads to the Mountain.')
        elif story_one_choice == 'R':
            print('\nYou have chosen the Right Path, which leads to the Valley.')
        else:
            print('Invalid choice.')
            first_choice()
    first_choice()

def gameplay():

    #Introduction
    print('\n******BLACK MAGIC ACROPOLIS******\n\nWelcome to the beginning of your journey. You will have to utilize your wits to survive this land. Enemy forces lurk around every corner, within the shadows, and will be unforgiving. Do you have what it takes?\n')
    print('This is a text-based adventure game. Select the appropriate options when prompted to continue through each action.')

    #Choose Character and Scenario
    scenario_selection()
    character_selection()

    #Gameplay
    story_one()
    print('\nYou hear something in the distance--a terrible sound. It approaches.\n')
    battle()

gameplay()


