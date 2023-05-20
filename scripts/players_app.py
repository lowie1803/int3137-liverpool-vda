import accumulative_pl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functools import reduce

from accumulative_pl import data1420

data2021 = pd.read_csv('datasets/pl_20-21.csv')
data2021 = data2021[['Name', 'Goals']]

plt.rcParams.update({'font.size': 22})

names = [
  "Mohamed Salah", "Kevin De Bruyne",
  "Sadio Mané", "Raheem Sterling",
  "Virgil van Dijk", "Kyle Walker",
  "Georginio Wijnaldum", "Bernardo Silva",
  "Roberto Firmino", "Sergio Agüero"
]

players_seasons = {}
players_minutes_per_season = {}

for i in range(2018, 2021):
  datafilter = data1420[data1420['season'] == i][['player_name', 'time']]
  for name in names:
    dataplayer = datafilter[datafilter['player_name'] == name]
    if len(dataplayer['time'].values) == 0:
      continue

    for time in dataplayer['time'].values:
      if name in players_seasons.keys():
        players_seasons[name] += [i]
        players_minutes_per_season[name] += time
      else:
        players_seasons[name] = [i]
        players_minutes_per_season[name] = time

players_minutes_per_season = {key: 1.0 * value / len(np.unique(players_seasons[key])) for key, value in players_minutes_per_season.items()}

print(players_minutes_per_season)
# print(players_seasons)

colors = ["#D00027", "#6CABDD"]

plt.bar(names, players_minutes_per_season.values(), color=colors)
plt.xlabel('Players')
plt.ylabel('Minutes played per season')
plt.title(f'Minutes played per season of top players in Liverpool and Man City (between 2017-2020)')
plt.ylim(1000, 3200)
plt.xticks(rotation=30)
plt.show()

# total = reduce(lambda x, y: x + y, players_goals.values(), 0)

# plt.pie(players_goals.values(), labels=players_goals.keys(), autopct='%1.1f%%', startangle=90, colors=colors)
# plt.axis('equal')
# plt.title(f'Liverpool goal distributions. Total: {total}')
# plt.show()
