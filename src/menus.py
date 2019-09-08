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
        # Go directly to second menu because parameters are introduced as args.
        difficulty = arg1
        game_style = arg2
        subdf = filtercoursesby(game_style,difficulty)
        submenu_sorts(subdf,game_style,difficulty)
        

def submenu_sorts(subdf,gamestyle,difficulty):
    # prints and do the functionalities in submenu_sorts
    clear()
    display_submenu_sorts(gamestyle,difficulty)
    print(subdf.head())
    choice = input("Type sort criteria:")
    sorted_df = sortbycategory(subdf,choice)
    #print(sorted_df.head())
    submenu_selectrows(sorted_df,gamestyle,difficulty,choice)

def submenu_selectrows(sorted_df,gamestyle,difficulty,choice):
    clear()
    display_submenu_selectrows(sorted_df,gamestyle,difficulty,choice)