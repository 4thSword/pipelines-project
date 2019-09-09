#This script take 7 files from Kaggle dataset and creates the file that is used in our app:

#imports:
import pandas as pd
import numpy as np

#Dataframes acquisition:
#clears = pd.read_csv('input/clears.csv',sep='\t')
course_meta = pd.read_csv('../input/course-meta.csv',sep='\t')
courses = pd.read_csv('../input/courses.csv', sep='\t')
likes = pd.read_csv('../input/likes.csv',sep='\t')
#players = pd.read_csv('input/players.csv', sep='\t')
#plays = pd.read_csv('input/plays.csv',sep='\t')

#Data processing procedure:

def datasets_transformation():
    #likes managing
    likescount = likes.groupby(['id'], as_index=False).agg({'player':'count'})
    likescount.rename(columns={'player':'likes'},inplace=True)
    #merge likes with courses:
    courses_likes = pd.merge(courses, likescount, on='id', how='left')
    #merging with metadatas:
    fulldatacourses = pd.merge(courses_likes, course_meta, on='id', how='left')
    #Grouping to get statistics:
    fullgroupedinfo = fulldatacourses.groupby(['id','difficulty','gameStyle','maker','title','thumbnail','image','creation','likes','firstClear', 'stars',], as_index=False).agg({'players':'sum','clears':'sum','attempts':'sum','clearRate':'mean'})

    return fullgroupedinfo


def app_inputfile_export():
    fullgroupedinfo.to_csv('../input/fullgroupedinfo.csv')


#script execution:
fullgroupedinfo = datasets_transformation()
app_inputfile_export()
