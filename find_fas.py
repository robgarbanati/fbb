import click
import math
import numpy as np
import pandas as pd
from os import path
import categories

def build_team(schedcsv, stats):
    schedule = pd.read_csv(schedcsv)
    print(schedule)
    endnum = len(schedule.index)
    print(endnum)

    #### build team stats
    team_stats = pd.DataFrame()

    for i in range(1,endnum):
        name = schedule.iloc[i,1]
        print(name)
        playerstats = stats.loc[stats['PLAYER'] == name]
        print(playerstats)
        ind = playerstats.index
        print("ind =", ind)
        stats = stats.drop(ind)
    endnum = len(stats.index)
    print(endnum)
    indices = [num for num in range(0,endnum)]
    stats = stats.set_index(pd.Index(indices))
    print(stats)

    return(stats)

    #  for i in range(1,endnum):
    #      team_stats.loc[stats['PLAYER'] == name, 'NumGames'] = schedule.iloc[i, 2]
    #      games_to_allocate = team_stats['NumGames'][i]
    #      if games_left > games_to_allocate:
    #          games_left -= games_to_allocate
    #      else:
    #          team['NumGames'][i] = total_games
    #          total_games = 0
    #  return(team_stats)

def calc_cat_totals(team):
    i = 0
    team_cats = categories.team()
    print(team['NumGames'][1])
    while i<13:
        if total_games > team['NumGames'][i]:
            total_games -= team['NumGames'][i]
        else:
            team['NumGames'][i] = total_games
            total_games = 0
        team_cats.pts += team['NumGames'][i] * team['PTS'][i]
        team_cats.ast += team['NumGames'][i] * team['AST'][i]
        team_cats.blk += team['NumGames'][i] * team['BLK'][i]
        team_cats.stl += team['NumGames'][i] * team['STL'][i]
        team_cats.tpm += team['NumGames'][i] * team['3PM'][i]
        team_cats.to += team['NumGames'][i] * team['TO'][i]
        team_cats.reb += team['NumGames'][i] * team['TREB'][i]
        team_cats.fgm += team['NumGames'][i] * team['FGM'][i]
        team_cats.fga += team['NumGames'][i] * team['FGA'][i]
        team_cats.ftm += team['NumGames'][i] * team['FTM'][i]
        team_cats.fta += team['NumGames'][i] * team['FTA'][i]
        i += 1
    team_cats.ftp = team_cats.ftm/team_cats.fta
    team_cats.fgp = team_cats.fgm/team_cats.fga
    print(team)
    print(team_cats)
    return team_cats

#  def recalc_players_punt(team):

def calc_cost(myteam, theirteam):
    cost = myteam - theirteam
    print(cost)

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

if __name__ == '__main__':
    optimize_lineups()

