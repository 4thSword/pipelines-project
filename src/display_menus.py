#imports
from data_processing import *


#Main Menu:

def display_mainmenu():

    print(
    '''
    ---------------------------------------
    -   SUPER MARIO MAKER! Analytics      -
    ---------------------------------------
    
    MAIN MENU

    ------------------------------------------------
    | 1.- Select a Level Difficulty:               |
    ------------------------------------------------
    | (e)asy | (n)ormal | e(x)pert | (s)uperExpert |
    ------------------------------------------------

    ------------------------------------------------------------
    | 2.- Select a Game Style:                                 |
    ------------------------------------------------------------
    | mario(B)ros | marioBros(3) | mario(W)orld | marioBros(U) |
    ------------------------------------------------------------
    '''
    )

def display_submenu_sorts(gameStyle,difficulty):
    print('''
    ---------------------------------------
    -   SUPER MARIO MAKER! Analytics      -
    ---------------------------------------
    
     YOU DECIDED TO FILTER BY: {} AND {}

    -------------------------------------------------
    | 1.- Select a sort criteria :                  |
    -------------------------------------------------
    |  (L)ikes  | (M)ost Finished | Le(s)s Finished |
    -------------------------------------------------
    '''.format(DIFFICULTY[difficulty],STYLE[gameStyle]))


def display_submenu_selectrows(df,gamestyle,difficulty,choice):
    print(
    '''
    ---------------------------------------
    -   SUPER MARIO MAKER! Analytics      -
    ---------------------------------------
    
     YOU DECIDED TO FILTER BY: {} AND {}
     AND SORT BY: {}

    -------------------------------------------------
    | 1.- There is {} levels with this criteria  |
    -------------------------------------------------
    
    -------------------------------------------------
    '''.format(DIFFICULTY[difficulty],STYLE[gamestyle],SORT[choice],len(df)))

def display_datashowselection(game):
    print(
    '''
    ---------------------------------------
    -   SUPER MARIO MAKER! Analytics      -
    ---------------------------------------
    
     YOU DECIDED TO SEE THE ANALYTICS OF: 

      {} 
     
    -------------------------------------------------
    | 1.- How do you want to get information?       |
    -------------------------------------------------
    |       (T)rerminal       |        (P)df        |
    -------------------------------------------------
    '''.format(game['title']))

