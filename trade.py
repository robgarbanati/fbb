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

@click.command()
@click.option('--their-roster', '-o', type=str, default='kyle_roster.csv', help='Specify path to their roster csv.')
def optimize_lineups(their_roster):

    check_if_file_exists(their_roster)
    stats = common.get_stats("zstats.csv")
    ranking_stats = common.get_stats("zstats_rankings.csv")
    ranking_14_stats = common.get_stats("zstats_rankings_14.csv")
    ranking_7_stats = common.get_stats("zstats_rankings_7.csv")
    print(stats)
    print(ranking_stats)
    print(ranking_14_stats)
    print(ranking_7_stats)

    stats = build_team(their_roster, stats)
    ranking_stats = build_team(their_roster, ranking_stats)
    ranking_14_stats = build_team(their_roster, ranking_14_stats)
    ranking_7_stats = build_team(their_roster, ranking_7_stats)
    #  stats = build_team("kyle_roster.csv", stats)
    #  ranking_stats = build_team("kyle_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("kyle_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("kyle_roster.csv", ranking_7_stats)
    #  stats = build_team("brandt_roster.csv", stats)
    #  ranking_stats = build_team("brandt_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("brandt_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("brandt_roster.csv", ranking_7_stats)
    #  stats = build_team("alex_roster.csv", stats)
    #  ranking_stats = build_team("alex_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("alex_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("alex_roster.csv", ranking_7_stats)
    #  stats = build_team("tom_roster.csv", stats)
    #  ranking_stats = build_team("tom_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("tom_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("tom_roster.csv", ranking_7_stats)
    #  stats = build_team("ben_roster.csv", stats)
    #  ranking_stats = build_team("ben_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("ben_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("ben_roster.csv", ranking_7_stats)
    #  stats = build_team("dylan_roster.csv", stats)
    #  ranking_stats = build_team("dylan_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("dylan_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("dylan_roster.csv", ranking_7_stats)
    #  stats = build_team("george_roster.csv", stats)
    #  ranking_stats = build_team("george_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("george_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("george_roster.csv", ranking_7_stats)
    #  stats = build_team("zmo_roster.csv", stats)
    #  ranking_stats = build_team("zmo_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("zmo_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("zmo_roster.csv", ranking_7_stats)
    #  stats = build_team("akbar_roster.csv", stats)
    #  ranking_stats = build_team("akbar_roster.csv", ranking_stats)
    #  ranking_14_stats = build_team("akbar_roster.csv", ranking_14_stats)
    #  ranking_7_stats = build_team("akbar_roster.csv", ranking_7_stats)
    stats = build_team("rob_roster.csv", stats)
    ranking_stats = build_team("rob_roster.csv", ranking_stats)
    ranking_14_stats = build_team("rob_roster.csv", ranking_14_stats)
    ranking_7_stats = build_team("rob_roster.csv", ranking_7_stats)
    
    #  indices = [num for num in range(0,40)]
    #  #  print(stats)
    #  pd.set_option("display.max_rows", 10)
    #  head = stats.head(10)
    #  print(head)
    #  head = ranking_stats.head(10)
    #  print(head)
    #  head = ranking_14_stats.head(10)
    #  print(head)
    #  head = ranking_7_stats.head(10)
    #  print(head)

if __name__ == '__main__':
    optimize_lineups()

