import numpy as np
import pandas as pd

schedule = pd.read_csv("schedule.csv")
print(schedule)
schedule['Num Games'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(schedule)
i=0
j=1
while i<12:
    numgames = 0
    j = 1
    while j<9:
        print(schedule.iloc[i,j])
        print(type(schedule.iloc[i,j]))
        if type(schedule.iloc[i,j]) == str:
            numgames +=1
            print("string")
        j += 1
    print(numgames)
    schedule.iloc[i,9] = numgames
    print(schedule)
    i+= 1
 
stats = pd.read_csv("stats.csv", sep='\t')
print(stats)

their_team = pd.DataFrame()
i=0
j=0
while i<12:
    name = schedule.iloc[i,j]
    print(name)
    #  playerstats = pd.DataFrame(stats.loc[name])
    #  print(playerstats)
    print(stats['PLAYER'])
    print(stats['POS'])
    playerstats = stats.loc[stats['PLAYER'] == name]
    print(playerstats)
    their_team = their_team.append(playerstats)
    their_team.loc[stats['PLAYER'] == name, 'NumGames'] = schedule.iloc[i, 9]
    print(their_team)
    i+= 1

