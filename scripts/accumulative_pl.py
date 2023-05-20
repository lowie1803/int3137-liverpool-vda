import numpy as np
import pandas as pd
from functools import reduce

databasic1021 = pd.read_csv('datasets/1021-basic.csv')
data1420 = pd.read_csv('datasets/1420-players-in-season.csv')
data2023 = pd.read_csv('datasets/2023-matches-in-season.csv')

def seasonParticipatedTeams2(season):
  data = data2023[['team', 'season']] if season >= 2020 else newdata1420[['team', 'season']]
  data = data[data['season'] == season]
  return np.unique(data['team'].values)

def getTeamDataSum(team_name, season, quantifiable_data):
  data = data2023[['team', 'season', quantifiable_data]] if season >= 2021 else data1420[['team', 'season', quantifiable_data]]
  filtered_data = data[data['team'] == team_name]
  filtered_data = filtered_data[filtered_data['season'] == season]
  values = filtered_data[quantifiable_data].values
  res = reduce(lambda x, y: x + y, values, 0.0)
  return res

def getTeamDataAvg(team_name, season, quantifiable_data):
  return getTeamDataSum(team_name, season, quantifiable_data) / 38.0

def getTeamDataSumExcludingTeam(team_name, season, quantifiable_data):
  data = data2023[['team', 'season', quantifiable_data]] if season >= 2021 else data1420[['team', 'season', quantifiable_data]]
  filtered_data = data[data['team'] != team_name]
  filtered_data = filtered_data[filtered_data['season'] == season]
  values = filtered_data[quantifiable_data].values
  res = reduce(lambda x, y: x + y, values, 0.0)
  return res

def getTeamDataAvgExcludingTeam(team_name, season, quantifiable_data):
  return getTeamDataSumExcludingTeam(team_name, season, quantifiable_data) / (38 * 19.0)

def getOpposingAvgData(team_name, season, field):
  if season <= 2021:
    datafilter = databasic1021[databasic1021['season'] == season]
    datafilterAway = datafilter[datafilter['away_team'] == team_name]
    datafilterHome = datafilter[datafilter['home_team'] == team_name]

    opposingHomeClearances = datafilterAway[f'home_{field}'].values
    opposingAwayClearances = datafilterHome[f'away_{field}'].values

    return (reduce(lambda x, y: x + y, opposingHomeClearances, 0.0) + reduce(lambda x, y: x + y, opposingAwayClearances, 0.0)) / 38.0
  else:
    datafilter = data2023[data2023['opponent'] == team_name]
    datafilter = datafilter[datafilter['season'] == season]
    values = datafilter[field].values
    return reduce(lambda x, y: x + y, values, 0.0) / 38.0

def countMatches(team_name, season, field):
  if season <= 2021:
    datafilter = databasic1021[databasic1021['season'] == season]
    datafilterAway = datafilter[datafilter['away_team'] == team_name]
    datafilterHome = datafilter[datafilter['home_team'] == team_name]

    opposingHomeClearances = datafilterAway[datafilterAway[f'away_{field}'] >= 3]
    opposingAwayClearances = datafilterHome[datafilterHome[f'home_{field}'] >= 3]

    return len(opposingHomeClearances) + len(opposingAwayClearances)
  else:
    datafilter = data2023[data2023['team'] == team_name]
    datafilter = datafilter[datafilter['season'] == season]
    return len(datafilter[datafilter[field] >= 3])

