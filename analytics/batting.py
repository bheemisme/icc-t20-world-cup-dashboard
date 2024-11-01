import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from scipy.stats import trim_mean
from analytics.preprocessing import *

def get_batting_style_counts():
    fig, axs = plt.subplots()
    axs.pie(
        x=player['batting_style'].value_counts(), 
        labels=['Right Hand Batsman', 'Left Hand Batsman'], 
        autopct=lambda x: str(round(x, 2))
    )
    fig.suptitle('Percentage of Batsmen per Batting Style')
    return fig


def get_avg_strike_rate_per_batting_style():
    def get_avg_strike_rate(batting_style):
        rhb = player[player['batting_style'] == batting_style]['name']
        sr = 0
        n = 0
        for batsman in rhb:
            n += len(batting[batting['batsmanName'] ==batsman]['SR'])
            sr = sr + np.sum(batting[batting['batsmanName'] ==batsman]['SR'])

        sr = sr/n
        return sr

    batting_style_scores = {}
    for bt in player['batting_style'].unique():
        batting_style_scores[bt] = get_avg_strike_rate(bt)
    
    fig,axs = plt.subplots(1)
    
    sns.barplot(
        x=['Right hand Batting', 'Left Hand Batting'],
        y=[batting_style_scores['Right hand Bat'], batting_style_scores['Left hand Bat']],
        width=0.1,
        ax=axs
    )

    fig.suptitle('Average strike rate for batting style')
    return fig


def get_top_5_batsmen_on_strike_rate():
    fig = plt.figure()

    top_5_batsmen = batting.groupby(by='batsmanName')['SR'].mean().sort_values(ascending=False)[:5]
    sns.barplot(x=top_5_batsmen.values, y=top_5_batsmen.index)
    plt.ylabel('batsman')
    plt.xlabel('avg strike rate')
    plt.title('Top 5 performing batsman')
    return fig


def get_batsmen_with_most_half_centuries():
    fig = plt.figure()
    top_5 = batting[batting['runs'] >= 50]['batsmanName'].value_counts()\
    .sort_values(ascending=False)[:5]
    sns.barplot(y=top_5.index, x=top_5.values)
    plt.ylabel('batsman')
    plt.xlabel('Number of half centuries')
    plt.title('Top 5 batsman with most half centuries')
    return fig





def get_batsman_metrics(name: str):

    fig, axs = plt.subplots(ncols=3, figsize=(12,3))
    batsman= batting[batting['batsmanName'] == name]
    
    sns.barplot(
                x=['avg runs', 'avg strike rate'], 
                y=[trim_mean(batsman['runs'], proportiontocut=0.25), 
                   trim_mean(batsman['SR'], proportiontocut=0.25)
                ], ax=axs[0],
                width=0.5
            )
    sns.barplot(
                y=[batsman['4s'].sum(), batsman['6s'].sum()], 
                x=['4s', '6s'],
                ax=axs[1], 
                width=0.5
            )
    sns.countplot(data=batsman, x='out/not_out', ax=axs[2], width=0.5)
    fig.suptitle(f'name = {name}, team = {batsman['teamInnings'].unique()[0]}')
    return fig


def get_batsman_trend(name: str):
    fig = plt.figure(figsize=(10,2))
    h = batting[batting['batsmanName'] == name]
    sns.lineplot(data=h, x='match',  y='runs')
    plt.xticks(rotation=90)
    plt.title(f'name = {name}')
    return fig

