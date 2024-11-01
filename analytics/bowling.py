from analytics.preprocessing import *

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import trim_mean

def get_bowler_metrics(name: str):
    bowler = bowling[bowling['bowlerName'] == name]
    average_econ_rate = trim_mean(bowler['economy'], 0.25)
    average_dot_balls = bowler['dotBalls'].mean()
    avg_4s_concede = bowler['4s_Conceded'].mean()
    avg_6s_concede = bowler['6s_Conceded'].mean()
    avg_maiden = bowler['maiden'].mean()
    total_wickets = bowler['wickets'].sum()
    total_wides = bowler['wides'].sum()
    total_nos = bowler['noBalls'].sum()
    team = bowler['bowlingTeam'].iloc[0]
    
    return pd.DataFrame({
        "metrics": ['avg econ rate', 
                    'avg dot balls', 
                    'avg 4s conceded', 
                    'avg 6s conceded',
                    'avg maiden overs',
                    'total wickets',
                    'total wides',
                    'total noballs'],
        'values': [average_econ_rate, average_dot_balls, 
                   avg_4s_concede, 
                   avg_6s_concede, 
                   avg_maiden, total_wickets ,total_wides, total_nos]
    }), team


def get_top_5_bowlers():
    top_5 = bowling.groupby(by=['bowlerName', 'bowlingTeam'])['economy'].apply(lambda x: trim_mean(x, 0.25)).sort_values(ascending=True)[:5]
    fig = plt.figure(figsize=(6,4))
    sns.barplot(y=top_5.index.map(lambda x: x[0] + "-" + x[1]), x=top_5.values)
    plt.ylabel('bowler')
    plt.xlabel('economy rate')
    plt.title('Top 5 bowlers as per economy rate')
    return fig

def get_bowler_trend(name: str):
    bowler = bowling[bowling['bowlerName'] == name]
    team = bowler['bowlingTeam'].iloc[0]
    fig = plt.figure(figsize=(12,2))
    sns.lineplot(x=bowler['match'],y=bowler['runsConceded'])
    plt.xticks(rotation=90)
    plt.ylabel('runs conceded')
    plt.xlabel('match')
    fig.suptitle(f'Bowler Name = {name}, Team = {team}')
    return fig


def get_top_5_bowling_styles():
    bowling['name'] = bowling['bowlerName']
    mergeddf = pd.merge(player, bowling,on = 'name', how='inner')
    top_5_bowling_styles = mergeddf.groupby(by='bowling_style')['runsConceded'].apply(lambda x: trim_mean(x, 0.25)).sort_values(ascending=False)[:5]
    fig = plt.figure()
    sns.barplot(y=top_5_bowling_styles.index, x=top_5_bowling_styles.values)
    plt.ylabel('Bowling Styles')
    plt.xlabel('Average Runs Conceded')
    fig.suptitle('Top 5 Bowling Styles By Runs Conceded')
    return fig
