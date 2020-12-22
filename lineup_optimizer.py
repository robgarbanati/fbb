import numpy as np
import pandas as pd

def build_team(schedcsv):
    schedule = pd.read_csv(schedcsv)
    schedule['Num Games'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i=0
    j=1
    while i<13:
        numgames = 0
        j = 1
        while j<9:
            #  print(schedule.iloc[i,j])
            #  print(type(schedule.iloc[i,j]))
            if type(schedule.iloc[i,j]) == str:
                numgames +=1
            j += 1
        #  print(numgames)
        schedule.iloc[i,9] = numgames
        i+= 1
    print(schedule)
     
    stats = pd.read_csv("stats.csv", sep='\t')
    #  print(stats)

    team_stats = pd.DataFrame()
    i=0
    j=0
    while i<13:
        name = schedule.iloc[i,j]
        #  print(name)
        #  playerstats = pd.DataFrame(stats.loc[name])
        #  print(playerstats)
        #  print(stats['PLAYER'])
        #  print(stats['POS'])
        playerstats = stats.loc[stats['PLAYER'] == name]
        print(playerstats)
        team_stats = team_stats.append(playerstats)
        team_stats.loc[stats['PLAYER'] == name, 'NumGames'] = schedule.iloc[i, 9]
        i+= 1
    team_stats = team_stats.sort_values(by='TOTAL', ascending=False)
    #  indices = pd.series[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    team_stats = team_stats.set_index(pd.Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    return(team_stats)

def calc_cat_totals(team):
    total_games = 24
    i = 0
    print(team['NumGames'][1])
    #  while i<13:
        #  if total_games > team.loc['NumGames']
        #  total_games += team.loc['NumGames']
    total_points = team['PTS'].sum()
    fullsum = team.sum()
    print(total_points)
    print(fullsum)
    print(team['NumGames'])
    print(team['NumGames'][4])


if __name__ == '__main__':
    myteam = build_team("rob.csv")
    print(myteam)
    theirteam = build_team("kyle.csv")
    print(theirteam)
    calc_cat_totals(myteam)
