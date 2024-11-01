import matplotlib.pyplot as plt
import seaborn as sns
from analytics.preprocessing import *

def get_tos_wins():
    fig, axs = plt.subplots()
    axs.pie(x=match['SameWins'].value_counts().to_numpy(),
             labels = ['Toss & Match Won', 'Opposite'], 
             autopct=lambda x: str(round(x,2))
             )
    return fig


def get_win_method():
    fig, axs = plt.subplots()
    sns.countplot(data=match, y='Winners', hue='Method', ax=axs)
    fig.suptitle("Winners by Method")
    return fig



def get_win_percentage():
    def get_win_percent(team):
        team_matches = match[(match['1st Team'] == team) ^ (match['2nd Team'] == team)]
        won_matches = team_matches[team_matches['Winners'] == team]
        return len(won_matches) * 100 / len(team_matches)

    win_percents = []
    for team in teams:
        win_percents.append(get_win_percent(team))

    fig = plt.figure(figsize=(6,4))
    sns.barplot(y=list(teams), x=win_percents)
    fig.suptitle("Win Percentage")
    return fig


def get_tos_decision():
    fig, axs = plt.subplots()
    sns.barplot(data=match, 
                y='Toss Winning', 
                x= 'SameWins', 
                hue='Toss Decision', 
                errorbar=None, ax=axs)
    fig.suptitle('Chance of Winning by Toss Decision')
    return fig

def get_toss_won():
    # of all the matches won by a country, how many where the country won the toss
    fig = plt.figure()
    sns.countplot(data=match, y='Winners', hue='SameWins')
    plt.title("Number of tosses where team won both match and toss and opposite")
    return fig