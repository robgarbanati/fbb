import math
import numpy as np
import pandas as pd
import common

def calc_best_cat_totals(roster):
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
        team.reb += 3.5*roster['TREB'][i]
        team.fgm += 3.5*roster['FGM'][i]
        team.fga += 3.5*roster['FGA'][i]
        team.ftm += 3.5*roster['FTM'][i]
        team.fta += 3.5*roster['FTA'][i]
        #  print(roster['PLAYER'][i])
    team.ftp = team.ftm/team.fta
    team.fgp = team.fgm/team.fga
    team.calc_stdevs(3.5*13)
    #  print(team)
    return team

#  def recalc_players_punt(team):

def calc_cost(theirname, myteam, theirteam):
    wp = myteam - theirteam
    #  print(wp)
    #  print(f'{wp.total_win_prob=}')
    print("win prob vs {n}: {wp}".format(n=theirname, wp=wp.total_win_prob))
    return wp.total_win_prob

def calc_league_win_prob(names, win_sum):
    total_wins = 0
    playoff_wins = 0
    current_player_roster = "{n}_roster.csv".format(n=names[0])
    team = common.build_full_team(current_player_roster)
    current_player_cats = calc_best_cat_totals(team)
    for name in names[1:]:
        #  print(name)
        player_roster = "{n}_roster.csv".format(n=name)
        team = common.build_full_team(player_roster)
        cats = calc_best_cat_totals(team)
        total_wins += calc_cost(name, current_player_cats, cats)
        #  print("")
    print(names[0], "total expected wins:", total_wins)
    win_sum += total_wins
    names = names[1:] + names[:1]
    return [names, win_sum]



if __name__ == '__main__':
    names = ["rob", "kyle", "ben", "dylan",
            "george", "alex", "akbar", "tom",
            "brandt", "zmo"]
    win_sum = 0
    [names, win_sum] = calc_league_win_prob(names, win_sum)
    [names, win_sum] = calc_league_win_prob(names, win_sum)
    [names, win_sum] = calc_league_win_prob(names, win_sum)
    [names, win_sum] = calc_league_win_prob(names, win_sum)
    [names, win_sum] = calc_league_win_prob(names, win_sum)

    [names, win_sum] = calc_league_win_prob(names, win_sum)
    [names, win_sum] = calc_league_win_prob(names, win_sum)
    [names, win_sum] = calc_league_win_prob(names, win_sum)
    [names, win_sum] = calc_league_win_prob(names, win_sum)
    [names, win_sum] = calc_league_win_prob(names, win_sum)
    print(f'{win_sum=}')
