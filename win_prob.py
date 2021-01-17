import click
import math
import numpy as np
import pandas as pd
from os import path
import common

def calc_cat_totals(team):
    i = 0
    total_games = 0
    team_cats = common.team()
    endnum = len(team.index)
    for i in range(0,endnum):
        total_games += team['NumGames'][i]
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
        #  i += 1
    team_cats.ftp = team_cats.ftm/team_cats.fta
    team_cats.fgp = team_cats.fgm/team_cats.fga
    team_cats.calc_stdevs(total_games)
    #  team_cats.calc_variances()
    print(team)
    print(team_cats)
    print(total_games)
    return team_cats

def calc_win_prob(myteam, theirteam, my_stats_csv, their_stats_csv):
    my_stats = pd.read_csv(my_stats_csv)
    their_stats = pd.read_csv(their_stats_csv)
    print(my_stats)
    print(their_stats)
    print("myteam =\n", myteam)
    myteam.pts += my_stats.loc[0, 'PTS']
    myteam.ast += my_stats.loc[0, 'AST']
    myteam.blk += my_stats.loc[0, 'BLK']
    myteam.stl += my_stats.loc[0, 'STL']
    myteam.tpm += my_stats.loc[0, '3PM']
    myteam.to += my_stats.loc[0, 'TO']
    myteam.reb += my_stats.loc[0, 'TREB']
    myteam.fgm += my_stats.loc[0, 'FGM']
    myteam.fga += my_stats.loc[0, 'FGA']
    myteam.ftm += my_stats.loc[0, 'FTM']
    myteam.fta += my_stats.loc[0, 'FTA']
    myteam.ftp = myteam.ftm/myteam.fta
    myteam.fgp = myteam.fgm/myteam.fga
    print("myteam =\n", myteam)
    print("")
    
    print("theirteam =\n", theirteam)
    theirteam.pts += their_stats.loc[0, 'PTS']
    theirteam.ast += their_stats.loc[0, 'AST']
    theirteam.blk += their_stats.loc[0, 'BLK']
    theirteam.stl += their_stats.loc[0, 'STL']
    theirteam.tpm += their_stats.loc[0, '3PM']
    theirteam.to += their_stats.loc[0, 'TO']
    theirteam.reb += their_stats.loc[0, 'TREB']
    theirteam.fgm += their_stats.loc[0, 'FGM']
    theirteam.fga += their_stats.loc[0, 'FGA']
    theirteam.ftm += their_stats.loc[0, 'FTM']
    theirteam.fta += their_stats.loc[0, 'FTA']
    theirteam.ftp = theirteam.ftm/theirteam.fta
    theirteam.fgp = theirteam.fgm/theirteam.fga
    print("theirteam =\n", theirteam)

    cost = myteam - theirteam
    print(cost)

def check_if_file_exists(infile):
    if not path.exists(infile):
        click.echo("Cannot find file at path {f}".format(f=infile))
        sys.exit(1)

@click.command()
@click.option('--my-roster', '-r', type=str, default='rob_roster.csv', help='Specify path to my roster csv.')
@click.option('--their-roster', '-o', type=str, default='brandt_roster.csv', help='Specify path to their roster csv.')
@click.option('--my-stats', '-m', type=str, default='rob_stats.csv', help='Specify path to my stats csv.')
@click.option('--their-stats', '-t', type=str, default='brandt_stats.csv', help='Specify path to their stats csv.')
def optimize_lineups(my_roster, their_roster, my_stats, their_stats):
    check_if_file_exists(my_roster)
    check_if_file_exists(their_roster)
    check_if_file_exists(my_stats)
    check_if_file_exists(their_stats)
    myteam = common.build_team(my_roster)
    theirteam = common.build_team(their_roster)
    my_cats = calc_cat_totals(myteam)
    their_cats = calc_cat_totals(theirteam)
    calc_win_prob(my_cats, their_cats, my_stats, their_stats)

if __name__ == '__main__':
    optimize_lineups()

