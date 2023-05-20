import accumulative_pl
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 24})

def plotXgComparingAverageOther(team_name, season):
  x = [team_name, 'Other']
  y = [
    accumulative_pl.getTeamDataAvg(team_name, season, 'xg'),
    accumulative_pl.getTeamDataAvgExcludingTeam(team_name, season, 'xg')
  ]
  colors = ['red', 'blue', 'yellow']

  plt.bar(x, y, color=colors)
  plt.xlabel('team')
  plt.ylabel('xGA')
  plt.title(f'{team_name} xG vs League avg, season {season}')
  plt.show()

def calcOpposingPossession(team_name, season):
  return accumulative_pl.getOpposingAvgData(team_name, season, 'possession')

seasons = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

categories = ["Liverpool", "Chelsea", "Man City", "Man United", "Arsenal", "Spurs"]

values = [
  [categories[0], 'red', list(map(lambda x: calcOpposingPossession("Liverpool", x),seasons))],
  [categories[1], '#034694', list(map(lambda x: calcOpposingPossession("Chelsea", x), seasons))],
  [categories[2], '#6CABDD', list(map(lambda x: calcOpposingPossession("Manchester City", x), seasons))],
  [categories[3], 'yellow', list(map(lambda x: calcOpposingPossession("Manchester United", x), seasons))],
  [categories[4], 'pink', list(map(lambda x: calcOpposingPossession("Arsenal", x), seasons))],
  [categories[5], '#132257', list(map(lambda x: calcOpposingPossession("Tottenham Hotspur", x), seasons))],
]

print(values)

x = np.arange(len(seasons))
width = 0.1
multiplier = 0
fig, ax = plt.subplots(layout='constrained')

for equipe in values:
  offset = width * multiplier
  multiplier += 1
  rects = ax.bar(x + offset, equipe[2], width, label=equipe[0], color=[equipe[1]])
  if (equipe[0] == "Liverpool"):
    ax.bar_label(rects, padding=3)

ax.set_ylabel('Average Opposing possession')
ax.set_title("Liverpool's average opposing possession, comparing to the Big Sixes")
ax.set_xticks(x + width, list(map(lambda x: str(x - 1) + '-' + str(x % 2000), seasons)))
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(20, 55)

plt.show()


