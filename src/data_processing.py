import os
import dotenv
import requests
import pandas as pd
import numpy as np
dotenv.load_dotenv()

#environment variables generation
TOKEN = os.getenv("ID")

#Dataframe load:
#clears = pd.read_csv('../input/clears.csv')
#course_meta = pd.read_csv('../input/course-meta.csv')
#courses = pd.read_csv('../input/courses.csv', sep='\t')
#likes = pd.read_csv('../input/likes.csv')
#players = pd.read_csv('../input/players.csv', sep='\t')
#plays = pd.read_csv('../input/plays.csv')
fullinfo = pd.read_csv('../input/fullgroupedinfo.csv')


#global constants:
DIFFICULTY = {
    'e': 'easy',
    'n': 'normal',
    'x': 'expert',
    's': 'superExpert'
}
STYLE={
    'b': 'marioBros',
    '3': 'marioBros3',
    'w': 'marioWorld',
    'u': 'marioBrosU'
}
SORT ={
    'l':'likes',
    'm': 'Most Finished',
    's': 'Less Finished'
}

#Functions to filter an porcess data

def filtercoursesby(st,d):
    # Select a sub Dataframe and filter it by style an difficulty
    df = fullinfo[(fullinfo['difficulty']== DIFFICULTY[d]) & (fullinfo['gameStyle'] == STYLE[st])]
    return df

def sortbycategory(df,choice):
    choice = choice.lower()
    if choice == 'm':
        return df.sort_values(by=['clears'],ascending=False)
    elif choice == 's':
        return df.sort_values(by=['clears'])
    elif choice == 'l':
        return df.sort_values(by=['likes'],ascending=False)
    else:
        return False