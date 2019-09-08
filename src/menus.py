#imports:
from display_menus import *
import argparse


#Main Menu:

def main_menu(arg1=None,arg2=None):
    if arg1  == None or arg2 == None:
        #displays menu:
        display_mainmenu()
        #get parameters:
        difficulty = input("Type difficulty code:")
        game_style = input("Type game style code:")
        subdf = filtercoursesby(game_style,difficulty)
        submenu_sorts(subdf,game_style,difficulty)
    else:
        difficulty = arg1
        game_style = arg2
        subdf = filtercoursesby(game_style,difficulty)
        submenu_sorts(subdf,game_style,difficulty)
        

def submenu_sorts(subdf,game_style,difficulty):
