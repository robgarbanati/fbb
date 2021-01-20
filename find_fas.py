import click
import math
import numpy as np
import pandas as pd
from os import path
import common

def build_team(schedcsv, stats):
    print(schedcsv)
    schedule = pd.read_csv(schedcsv)
    endnum = len(schedule.index)


    #### build team stats
    team_stats = pd.DataFrame()

    for i in range(0,endnum):
        name = schedule.iloc[i,1]
        playerstats = stats.loc[stats['PLAYER'] == name]
        team_stats = team_stats.append(playerstats)
        ind = playerstats.index
        stats = stats.drop(ind)

    endnum = len(team_stats.index)
    indices = [num for num in range(0,endnum)]
    team_stats = team_stats.set_index(pd.Index(indices))
    print(team_stats)

    return(stats)

def check_if_file_exists(infile):
    if not path.exists(infile):
        click.echo("Cannot find file at path {f}".format(f=infile))
        sys.exit(1)

def optimize_lineups():

    stats = common.get_stats()
    #  total_stats = common.get_total_stats()
    print(stats)
    #  print(total_stats)

    stats = build_team("kyle_roster.csv", stats)
    #  total_stats = build_team("kyle_roster.csv", total_stats)
    stats = build_team("brandt_roster.csv", stats)
    #  total_stats = build_team("brandt_roster.csv", total_stats)
    stats = build_team("alex_roster.csv", stats)
    #  total_stats = build_team("alex_roster.csv", total_stats)
    stats = build_team("tom_roster.csv", stats)
    #  total_stats = build_team("tom_roster.csv", total_stats)
    stats = build_team("ben_roster.csv", stats)
    #  total_stats = build_team("ben_roster.csv", total_stats)
    stats = build_team("dylan_roster.csv", stats)
    #  total_stats = build_team("dylan_roster.csv", total_stats)
    stats = build_team("george_roster.csv", stats)
    #  total_stats = build_team("george_roster.csv", total_stats)
    stats = build_team("zmo_roster.csv", stats)
    #  total_stats = build_team("zmo_roster.csv", total_stats)
    stats = build_team("akbar_roster.csv", stats)
    #  total_stats = build_team("akbar_roster.csv", total_stats)
    stats = build_team("rob_roster.csv", stats)
    #  total_stats = build_team("rob_roster.csv", total_stats)
    
    indices = [num for num in range(0,40)]
    #  print(stats)
    pd.set_option("display.max_rows", 40)
    head = stats.head(40)
    print(head)
    #  total_head = total_stats.head(40)
    #  print(total_head)

if __name__ == '__main__':
    optimize_lineups()

