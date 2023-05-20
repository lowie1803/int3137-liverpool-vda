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

def calcDataGFMinusXG(team_name, season):
  return accumulative_pl.getTeamDataAvg(team_name, season, 'xg')


# plotXgComparingAverageOther('Liverpool', 2020)

teams = ['Liverpool', 'Other teams Avg.']

categories = []

values = [
  [categories[0], 'red', list(map(lambda x: calcDataGFMinusXG("Liverpool", x),seasons))],
  [categories[1], '#034694', list(map(lambda x: calcDataGFMinusXG("Chelsea", x), seasons))],
  [categories[2], '#6CABDD', list(map(lambda x: calcDataGFMinusXG("Manchester City", x), seasons))],
  [categories[3], 'yellow', list(map(lambda x: calcDataGFMinusXG("Manchester United", x), seasons))],
  [categories[4], 'pink', list(map(lambda x: calcDataGFMinusXG("Arsenal", x), seasons))],
  [categories[5], '#132257', list(map(lambda x: calcDataGFMinusXG("Tottenham Hotspur", x), seasons))],
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

ax.set_ylabel('Clearances, Fouls, Shots, Passes')
ax.set_title("Liverpool's xG per match comparing to other Big Sixes")
ax.set_xticks(x + width, list(map(lambda x: str(x - 1) + '-' + str(x % 2000), seasons)))
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 15)

# ax2 = ax.twinx()

# ax2.set_ylabel('Points gained', color="brown")
# ax2.plot(x, [60, 76, 75, 97, 99, 69, 92], color="brown")
# ax2.tick_params(axis='y', labelcolor="brown")
# ax2.set_ylim(0, 120)

# fig.tight_layout()

plt.show()


