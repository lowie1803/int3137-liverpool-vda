import accumulative_pl
import matplotlib.pyplot as plt
import numpy as np

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

# plotXgComparingAverageOther('Liverpool', 2020)

seasons = [2016, 2017, 2018, 2019, 2020, 2021, 2022]

categories = ["Liverpool", "Other avg.", "Man City"]

values = [
  [categories[0], 'red', list(map(lambda x: accumulative_pl.getTeamDataAvg('Liverpool', x, 'xg'),seasons))],
  [categories[1], 'blue', list(map(lambda x: accumulative_pl.getTeamDataAvgExcludingTeam("Liverpool", x, 'xg'),seasons))],
  [categories[2], '#6CABDD', list(map(lambda x: accumulative_pl.getTeamDataAvg('Manchester City', x, 'xg'),seasons))]
]

print(values)

# print(values)

x = np.arange(len(seasons))
width = 0.1
multiplier = 0
fig, ax = plt.subplots(layout='constrained')

# colors = ['red', 'gray', 'green', 'blue']

for equipe in values:
  offset = width * multiplier
  multiplier += 1
  rects = ax.bar(x + offset, equipe[2], width, label=equipe[0], color=[equipe[1]])
  if (equipe[0] == "Liverpool"):
    ax.bar_label(rects, padding=3)

ax.set_ylabel('xGoals')
ax.set_title('Liverpool Average expected Goals comparing to average of all other clubs and Man City')
ax.set_xticks(x + width, list(map(lambda x: str(x - 1) + '-' + str(x % 2000), seasons)))
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 3)

plt.show()


