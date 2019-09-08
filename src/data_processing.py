import os
import dotenv
import requests
import pandas as pd
import numpy as np
dotenv.load_dotenv()

#environment variables generation
TOKEN = os.getenv("ID")

#Dataframe load:
clears = pd.read_csv('input/clears.csv')
course_meta = pd.read_csv('input/course-meta.csv')
courses = pd.read_csv('input/courses.csv', sep='\t')
likes = pd.read_csv('input/likes.csv')
players = pd.read_csv('input/players.csv', sep='\t')
plays = pd.read_csv('input/plays.csv')

#global constants:
DIFFICULTY = {
    'e': 'easy'
    'n': 'normal'
    'x': 'expert'
    's': 'superExpert'
}
STYLE={
    'b': 'marioBros',
    '3': 'marioBros3',
    'w': 'marioWorld',
    'u': 'marioBrosU'
}

#Functions to filter an porcess data

def filtercoursesby(s,d):
    # Select a sub Dataframe and filter it by style an difficulty
    
    df = courses[(courses['difficulty']== difficulty[d].value) & (courses['gameStyle'] == style[s].value)]
    return df

