import click
import math
import numpy as np
import pandas as pd
from os import path
import categories

def build_team(schedcsv, stats):
    schedule = pd.read_csv(schedcsv)
    #  print(schedule)
    endnum = len(schedule.index)
    #  print(endnum)

    #### build team stats
    team_stats = pd.DataFrame()

    for i in range(1,endnum):
        name = schedule.iloc[i,1]
        #  print(name)
        playerstats = stats.loc[stats['PLAYER'] == name]
        #  print(playerstats)
        ind = playerstats.index
        #  print("ind =", ind)
        stats = stats.drop(ind)
    endnum = len(stats.index)
    #  print(endnum)
    indices = [num for num in range(0,endnum)]
    stats = stats.set_index(pd.Index(indices))
    #  print(stats)

    return(stats)

def check_if_file_exists(infile):
    if not path.exists(infile):
        click.echo("Cannot find file at path {f}".format(f=infile))
        sys.exit(1)

def optimize_lineups():

    stats = pd.read_csv("stats.csv", sep='\t')
    print(stats)

    stats = build_team("rob_roster.csv", stats)
    stats = build_team("kyle_roster.csv", stats)
    stats = build_team("brandt_roster.csv", stats)
    stats = build_team("alex_roster.csv", stats)
    stats = build_team("tom_roster.csv", stats)
    stats = build_team("ben_roster.csv", stats)
    stats = build_team("dylan_roster.csv", stats)
    stats = build_team("george_roster.csv", stats)
    stats = build_team("zmo_roster.csv", stats)
    stats = build_team("akbar_roster.csv", stats)
    
    indices = [num for num in range(0,40)]
    head = stats.head(80)
    head.insert(17, 'PuntValue', -1, False)
    pd.set_option("display.max_rows", 80)
    #  for index in indices:
    print(head)

if __name__ == '__main__':
    optimize_lineups()

