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
        print(f"{i=}")
        print(f"{name=}")
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

    stats = common.get_stats("zstats.csv")
    #  ranking_stats = common.get_stats("zstats_rankings.csv")
    #  ranking_14_stats = common.get_stats("zstats_rankings_14.csv")
    #  ranking_7_stats = common.get_stats("zstats_rankings_7.csv")
    print(stats)
    #  print(ranking_stats)
    #  print(ranking_14_stats)
    #  print(ranking_7_stats)

    stats = build_team("rosters/lucas_roster.csv", stats)
    stats = build_team("rosters/andy_roster.csv", stats)
    stats = build_team("rosters/kyle_roster.csv", stats)
    #  ranking_stats = build_team("rosters/kyle_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("rosters/kyle_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("rosters/kyle_roster.csv", ranking_7_stats)
    stats = build_team("rosters/brandt_roster.csv", stats)
    #  ranking_stats = build_team("rosters/brandt_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("rosters/brandt_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("rosters/brandt_roster.csv", ranking_7_stats)
    stats = build_team("rosters/alex_roster.csv", stats)
    #  ranking_stats = build_team("rosters/alex_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("rosters/alex_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("rosters/alex_roster.csv", ranking_7_stats)
    stats = build_team("rosters/tom_roster.csv", stats)
    #  ranking_stats = build_team("rosters/tom_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("rosters/tom_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("rosters/tom_roster.csv", ranking_7_stats)
    stats = build_team("rosters/ben_roster.csv", stats)
    #  ranking_stats = build_team("rosters/ben_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("rosters/ben_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("rosters/ben_roster.csv", ranking_7_stats)
    stats = build_team("rosters/dylan_roster.csv", stats)
    #  ranking_stats = build_team("rosters/dylan_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("rosters/dylan_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("rosters/dylan_roster.csv", ranking_7_stats)
    stats = build_team("rosters/mark_roster.csv", stats)
    #  ranking_stats = build_team("rosters/george_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("rosters/george_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("rosters/george_roster.csv", ranking_7_stats)
    stats = build_team("rosters/zmo_roster.csv", stats)
    #  ranking_stats = build_team("rosters/zmo_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("rosters/zmo_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("rosters/zmo_roster.csv", ranking_7_stats)
    stats = build_team("rosters/akbar_roster.csv", stats)
    #  ranking_stats = build_team("rosters/akbar_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("rosters/akbar_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("rosters/akbar_roster.csv", ranking_7_stats)
    stats = build_team("rosters/rob_roster.csv", stats)
    #  ranking_stats = build_team("rosters/rob_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("rosters/rob_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("rosters/rob_roster.csv", ranking_7_stats)
    
    pd.set_option("display.max_rows", 80)
    head = stats.head(80)
    print(head)
    #  head = ranking_stats.head(80)
    #  print(head)
    #  head = ranking_14_stats.head(80)
    #  print(head)
    #  head = ranking_7_stats.head(40)
    #  print(head)

if __name__ == '__main__':
    optimize_lineups()

