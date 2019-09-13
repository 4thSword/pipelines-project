# Pipelines Project

## Overview:

In this project It is requested to find a Dataset in Kaggle and get conclusions about its data and enriching it using an API or Web Scraping.

## SUPER MARIO MAKER! Analytics

I would like to introduce my SUPER MARIO MAKER Analytics. 

Using 3 .csv files from the 7 publiseh in [SMMnet](https://www.kaggle.com/leomauro/smmnet), leaning it and creatng only 1 files with data about Super mario maker levels and the users statistics.

The API used to enrich data is the Twitch API and its use is implemented durind the app execution.


## First step, data cleaning

Before starting to use the app, it is necessary to download from the [dataset page](https://www.kaggle.com/leomauro/smmnet) the files files called:

* couuses.csv
* course_meta.csv
* likes.csv

After download it is necessary to place them into a folder called __input__ in the root directory of the repository and run the script __datacleaning.py__ with the python engine. It must create in the folder __input__ a new file called __fullgroupedinfo.csv__.\
Now it is time to launch __main.py__ and start to use our app.

### Main Menu

It lets you to do a first filtering of data about the game diffculty and the game style in which the level is builted.


### Sorting Menu
It shows the filters applied and let you sort by number of Likes, the most completed levels or the less completed levels.


### Levels selection menu

Not it is shown how many leves do we have and lets the user select hoy many will be listed.
Afterwars it is possible to select one of them.

### Data Visualization selection:

Let the user choose if want to get the info printed in terminal o exported to a pdf file. (PDF export si not implemented yet.)

### Game stats:

Show all the game stats and check if the level maker and the first player in accomplish the level have Twitch account and shows their Twitch ID if exists.
