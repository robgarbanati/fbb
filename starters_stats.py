import math
import numpy as np
import pandas as pd
import common

def build_team(rostercsv):
    print(rostercsv)
    roster = pd.read_csv(rostercsv)
    #  print(roster)
    endnum = len(roster.index)

    stats = pd.read_csv("stats.csv", sep='\t')

    team_stats = pd.DataFrame()

    for i in range(0,endnum):
        name = roster.iloc[i,1]
        #  print(name)
        if roster.iloc[i,0] == 'O':
            #  print(name, "is out")
            continue
        playerstats = stats.loc[stats['PLAYER'] == name]
        #  print(playerstats)
        team_stats = team_stats.append(playerstats)

    endnum = len(team_stats.index)
    team_stats = team_stats.sort_values(by='TOTAL', ascending=False)
    indices = [num for num in range(0,endnum)]
    team_stats = team_stats.set_index(pd.Index(indices))
    #  print(team_stats)
    return(team_stats)

def calc_cat_totals(roster):
    endnum = len(roster.index)
    if(endnum > 13):
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
    #  print(team)
    print(team)
    return team

#  def recalc_players_punt(team):

def calc_cost(myteam, theirteam):
    cost = myteam - theirteam
    print(cost)
    return cost.cost

def calc_wins(myteam, theirteam):
    cost = myteam - theirteam
    print(cost)


if __name__ == '__main__':
    total_cost = 0
    print("")
    team = build_team("rob_roster.csv")
    my_cats = calc_cat_totals(team)
    print("")
    team = build_team("kyle_roster.csv")
    cats = calc_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    print("")
    team = build_team("ben_roster.csv")
    cats = calc_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    print("")
    team = build_team("dylan_roster.csv")
    cats = calc_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    print("")
    team = build_team("george_roster.csv")
    cats = calc_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    print("")
    team = build_team("zmo_roster.csv")
    cats = calc_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    print("")
    team = build_team("alex_roster.csv")
    cats = calc_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    print("")
    team = build_team("akbar_roster.csv")
    cats = calc_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    print("")
    team = build_team("brandt_roster.csv")
    cats = calc_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    print("")
    team = build_team("tom_roster.csv")
    cats = calc_cat_totals(team)
    total_cost += calc_cost(my_cats, cats)
    print("total_cost:", total_cost)
    #  my_cats = calc_cat_totals(myteam)
    #  their_cats = calc_cat_totals(theirteam)
    #  calc_cost(my_cats, their_cats)
