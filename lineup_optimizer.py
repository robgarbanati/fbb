import click
import math
import numpy as np
import pandas as pd
from os import path
import categories

def build_team(schedcsv):
    games_left = 24
    schedule = pd.read_csv(schedcsv)
    print(schedule)
    games_played = schedule.iloc[0,2]
    print(games_played)
    games_left -= games_played
    endnum = len(schedule.index)
    print(endnum)
     
    stats = pd.read_csv("stats.csv", sep='\t')
    #  print(stats)

    #### build team stats
    team_stats = pd.DataFrame()
    for i in range(1,endnum):
        name = schedule.iloc[i,1]
        playerstats = stats.loc[stats['PLAYER'] == name]
        print(playerstats)
        team_stats = team_stats.append(playerstats)
    team_stats = team_stats.sort_values(by='TOTAL', ascending=False)
    indices = [num for num in range(1,endnum)]
    team_stats = team_stats.set_index(pd.Index(indices))
    #  team_stats = team_stats.set_index(pd.Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

    for i in range(1,endnum):
        name = schedule.iloc[i,1]
        numgames = schedule.iloc[i,2]
        print("name =", name, " numgames =", numgames)
        player = team_stats.loc[team_stats['PLAYER'] == name]
        team_stats.loc[team_stats['PLAYER'] == name, 'NumGames'] = numgames
        print(team_stats)
        #  games_to_allocate = team_stats['NumGames'][i]
        #  if games_left > games_to_allocate:
        #      games_left -= games_to_allocate
        #  else:
        #      team_stats['NumGames'][i] = games_left
        #      games_left = 0
    return(team_stats)




        #  print("player =", player)
        #  player['NumGames'] = numgames
        #  print("player with numgames =", player)
        #  print("numgames =", player['NumGames'])

def calc_cat_totals(team):
    i = 0
    team_cats = categories.team()
    #  print(team['NumGames'][1])
    endnum = len(schedule.index)
    print(endnum)
    for i in range(1,endnum):
    #      if total_games > team['NumGames'][i]:
    #          total_games -= team['NumGames'][i]
    #      else:
    #          team['NumGames'][i] = total_games
    #          total_games = 0
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

@click.command()
@click.option('--my-roster', '-r', type=str, default='rob_roster.csv', help='Specify path to my roster csv.')
@click.option('--their-roster', '-o', type=str, default='kyle_roster.csv', help='Specify path to their roster csv.')
@click.option('--my-stats', '-m', type=str, default='rob_stats.csv', help='Specify path to my stats csv.')
@click.option('--their-stats', '-t', type=str, default='kyle_stats.csv', help='Specify path to their stats csv.')
def optimize_lineups(my_roster, their_roster, my_stats, their_stats):
    check_if_file_exists(my_roster)
    check_if_file_exists(their_roster)
    check_if_file_exists(my_stats)
    check_if_file_exists(their_stats)
    myteam = build_team(my_roster)
    print(myteam)
    theirteam = build_team(their_roster)
    print(theirteam)
    #  my_cats = calc_cat_totals(myteam)
    #  their_cats = calc_cat_totals(theirteam)
    #  calc_cost(my_cats, their_cats)

if __name__ == '__main__':
    optimize_lineups()

