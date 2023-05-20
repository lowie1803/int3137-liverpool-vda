import accumulative_pl
import matplotlib.pyplot as plt
import numpy as np

def plotXg(team_name, season):
  x = [team_name]
  y = [
    accumulative_pl.getTeamDataAvg(team_name, season, 'xg')
  ]
  colors = ['red']

  plt.bar(x, y, color=colors)
  plt.xlabel('team')
  plt.ylabel('xG')
  plt.title(f'{team_name} xG vs League avg, season {season}')
  plt.show()

plotXg("team_name", season)