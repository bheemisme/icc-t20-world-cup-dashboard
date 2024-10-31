# 1. Number of matches won by each team irrespective of stage
import matplotlib.pyplot as plt
import seaborn as sns
from analytics.preprocessing import *

def get_win_percent(team):
    team_matches = match[(match['1st Team'] == team) ^ (match['2nd Team'] == team)]
    won_matches = team_matches[team_matches['Winners'] == team]
    return len(won_matches) * 100 / len(team_matches)

win_percents = []
for team in teams:
    win_percents.append(get_win_percent(team))

fig, axs = plt.subplots(nrows=1, constrained_layout=True)
sns.barplot(y=list(teams), x=win_percents, ax=axs)


fig.suptitle("Win Percentage")