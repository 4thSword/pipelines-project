#imports:
from display_menus import *
import argparse
from os import system, name

#Auxiliary functions:
 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



#Main Menu:

def main_menu(arg1=None,arg2=None):
    clear()
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
        

def submenu_sorts(subdf,gamestyle,difficulty):
    clear()
    display_submenu_sorts(gamestyle,difficulty)
    print(subdf.head())
    sorted_df = False
    while True: # not sorted_df: # (sorted_df == False):
        choice = input("Type sort criteria:")
        sorted_df = sortbycategory(subdf,choice)
        if sorted_df:
            break
    
