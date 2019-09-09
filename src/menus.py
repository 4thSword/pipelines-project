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
    #displays menu
    display_submenu_selectrows(sorted_df,gamestyle,difficulty,choice)
    #intriduce in how many level do you want to choose
    max_levels = int( input('How many levels do you want to see?:\n'))
    #filter df and pritn yor choose in terminal
    sorted_df = sorted_df.groupby(['id','difficulty','gameStyle','maker','title','thumbnail','image','creation','likes','firstClear'], as_index=False).agg({'players':'sum','clears':'sum','attempts':'sum','clearRate':'mean'})
    sorted_df.reset_index(inplace=True)
    final_df = sorted_df.head(n=max_levels)
    for index, row in final_df.iterrows():
        print(
        '''     {}-> {}
        ------'''.format(index,row['title']))
    #select a game
    game_index = int(input('Choose a level number:'))    
    game = final_df.iloc[game_index]

    datashowselection(game)


def datashowselection(game):
    clear()
    display_datashowselection(game)
    option = input()
    if option.lower()== 't':
        terminal_data_show(game)
    #elif option.lower() == 'p':
    #   pdf_export(game)
    else:datashowselection(game)

def terminal_data_show(game):
    clear()
    print(game)


