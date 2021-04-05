import math
import numpy as np
import pandas as pd
import common
import click

def calc_best_cat_totals(roster):
    print(f'{roster=}')
    endnum = len(roster.index)
    if endnum > 13:
        endnum = 13
    team = common.team()
    for i in range(0, endnum):
        team.pts += 3.5*roster['PTS'][i]
        team.ast += 3.5*roster['AST'][i]
        team.blk += 3.5*roster['BLK'][i]
        team.stl += 3.5*roster['STL'][i]
        team.tpm += 3.5*roster['3PM'][i]
        team.to += 3.5*roster['TO'][i]
        team.reb += 3.5*roster['REB'][i]
        team.fgm += 3.5*roster['FGM'][i]
        team.fga += 3.5*roster['FGA'][i]
        team.ftm += 3.5*roster['FTM'][i]
        team.fta += 3.5*roster['FTA'][i]
        #  print(roster['PLAYER'][i])
    team.ftp = team.ftm/team.fta
    team.fgp = team.fgm/team.fga
    team.calc_stdevs(3.5*13)
    print(team)
    return team

#  def recalc_players_punt(team):

def calc_cost(myteam, theirteam):
    wp = myteam - theirteam
    print(wp)
    print(f'{wp.total_win_prob=}')
    return wp.total_win_prob

def calc_wins(myteam, theirteam):
    cost = myteam - theirteam
    print(cost)


@click.command()
@click.option('--stats-source', '-s', type=str, default='zstats.csv', help='Specify path to stats csv.')
def calc_win_prob_against_league(stats_source):
    playoff_wins = 0
    total_cost = 0
    print("")
    print("")
    team = common.build_full_team("rob_roster.csv", stats_source)
    #  print(f'{team=}')
    my_cats = calc_best_cat_totals(team)
    #  print("")
    #  print("Kyle")
    #  team = common.build_full_team("kyle_roster.csv", stats_source)
    #  cats = calc_best_cat_totals(team)
    #  total_cost += calc_cost(my_cats, cats)
    #  print("")
    #  print("Ben")
    #  team = common.build_full_team("ben_roster.csv", stats_source)
    #  cats = calc_best_cat_totals(team)
    #  total_cost += calc_cost(my_cats, cats)
    #  print("")
    #  print("George")
    #  team = common.build_full_team("george_roster.csv", stats_source)
    #  cats = calc_best_cat_totals(team)
    #  total_cost += calc_cost(my_cats, cats)
    #  print("")
    #  print("Alex")
    #  team = common.build_full_team("alex_roster.csv", stats_source)
    #  cats = calc_best_cat_totals(team)
    #  total_cost += calc_cost(my_cats, cats)
    print("")
    print("Akbar")
    team = common.build_full_team("akbar_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    #  print("")
    #  print("Tom")
    #  team = common.build_full_team("tom_roster.csv", stats_source)
    #  cats = calc_best_cat_totals(team)
    #  total_cost += calc_cost(my_cats, cats)
    print("")
    print("Dylan")
    team = common.build_full_team("dylan_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    #  total_cost += calc_cost(my_cats, cats)
    playoff_wins += calc_cost(my_cats, cats)
    print("")
    print("Brandt")
    team = common.build_full_team("brandt_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    playoff_wins += calc_cost(my_cats, cats)
    print("")
    print("ZMo")
    team = common.build_full_team("zmo_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    playoff_wins += calc_cost(my_cats, cats)
    print("")
    print("total expected wins:", total_cost)
    print("playoff expected wins:", playoff_wins)

if __name__ == '__main__':
    calc_win_prob_against_league()
