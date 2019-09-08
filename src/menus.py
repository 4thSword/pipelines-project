#imports:
from ./display_menus.py import *
import argparse

#Main Menu:

def main_menu(arg1=None,arg2=None):
    if arg1  == None or arg2 == None:
        #displays menu:
        display_mainmenu()
        #get parameters:
        difficulty = input("Type difficulty code:")
        game_style = input("Type difficulty code:")
        
       
    else:
        submenu_sorts(arg1,arg2)


