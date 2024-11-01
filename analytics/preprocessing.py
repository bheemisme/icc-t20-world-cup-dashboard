import pandas as pd
import numpy as np

batting = pd.read_csv('./data/Batting summaries for every match.csv')
bowling = pd.read_csv('./data/Bowling summaries for every match.csv')
match = pd.read_csv('./data/Match Summary.csv')
player = pd.read_csv('./data/Player_Info T20 WC 2024.csv')

match.dropna(inplace=True)
player = player[~player['batting_style'].isna()]

players = set(player['name'].unique())
teams = set(match['1st Team']).union(set(match['2nd Team']))
match['Match Date'] = pd.to_datetime(match['Match Date'])


def preprocess_age(age):
    a = age.split(' ')

    years = int(a[0][:-1])
    days = 0
    if len(a) > 1:
        days = int(a[1][:-1])/365
    

    return years+round(days, 2)

batting['SR'] =batting['SR'].replace('-', np.nan)
batting['SR']=  pd.to_numeric(batting['SR'])

player['age'] = player['age'].apply(preprocess_age)
match['SameWins'] = match.apply(lambda x: 1 if x['Winners'] == x['Toss Winning'] else 0, axis=1)
