#imports
from data_processing import *


#Main Menu:

def display_mainmenu():
    print('---------------------------------------')
    print('-   SUPER MARIO MAKER! Analytics      -')
    print('---------------------------------------')
    print('MAIN MENU\n')
    print('-----------------------------------------------')
    print('| 1.- Select a Level Difficulty:               |')
    print('-----------------------------------------------')
    print('| (e)asy | (n)ormal | e(x)pert | (s)uperExpert |')
    print('----------------------------------------------\n')
    print('-----------------------------------------------------------')
    print('| 2.- Select a Game Style:                                 |')
    print('-----------------------------------------------------------')
    print('| mario(B)ros | marioBros(3) | mario(W)orld | marioBros(U) |')
    print('-----------------------------------------------------------\n')


def display_submenu_sorts(gameStyle,difficulty):
    print('---------------------------------------')
    print('-   SUPER MARIO MAKER! Analytics      -')
    print('---------------------------------------')
    print('YOU DECIDED TO FILTER BY: {} AND {}\n'.format(DIFFICULTY[difficulty],STYLE[gameStyle]))
    print('------------------------------------------------')
    print('| 1.- Select a sort criteria :                  |')
    print('------------------------------------------------')
    print('|  (L)ikes  | (M)ost Finished | Le(s)s Finished |')
    print('------------------------------------------------\n')
    print('-----------------------------------------------------------')
    print('| 2.- Select a Game Style:                                 |')
    print('-----------------------------------------------------------')
    print('| mario(B)ros | marioBros(3) | mario(W)orld | marioBros(U) |')
    print('-----------------------------------------------------------\n')