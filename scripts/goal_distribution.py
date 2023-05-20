import accumulative_pl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functools import reduce

from accumulative_pl import data1420

data2021 = pd.read_csv('datasets/pl_20-21.csv')
data2021 = data2021[['Name', 'Goals']]

plt.rcParams.update({'font.size': 22})

players_goals = {}

for i in range(2017, 2021):
  datafilter = data1420[(data1420['team'] == 'Liverpool') & (data1420['season'] == i)][['player_name', 'gf']]
  for row in datafilter.values.tolist():
    if row[0] in players_goals:
      players_goals[row[0]] += row[1]
    elif row[1] > 0:
      players_goals[row[0]] = row[1]


for item in players_goals.items():
  if item[0] == "Danny Ings" or len(data2021[data2021['Name'] == item[0] + ' ']['Goals'].values) == 0:
    continue

  print(data2021[data2021['Name'] == item[0] + ' ']['Goals'].values, item[0])
  players_goals[item[0]] += data2021[data2021['Name'] == item[0] + ' ']['Goals'].values[0]

players_goals = dict(sorted(players_goals.items(), key=lambda x: -x[1]))

players_goals["Other"] = 0
for value in players_goals.values():
  if value < 8:
    players_goals["Other"] += value

players_goals = {key: value for key, value in players_goals.items() if value >= 8}

print(players_goals)

colors = ["#D00027", "#B1AC48", "#00A398", "#D51A3D", "#CAC552", "#D93352", "#E4DD5D", "#80D1CC", "#DE4D68", "#FDF667"]

total = reduce(lambda x, y: x + y, players_goals.values(), 0)

plt.pie(players_goals.values(), labels=players_goals.keys(), autopct='%1.1f%%', startangle=90, colors=colors)
plt.axis('equal')
plt.title(f'Liverpool goal distributions. Total: {total}')
plt.show()
