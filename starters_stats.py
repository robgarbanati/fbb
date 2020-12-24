import math
import numpy as np
import pandas as pd
import categories

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
    if(endnum > 10):
        endnum = 10
    team = categories.team_cats()
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
    #  print(type(myteam))
    #  print(type(theirteam))
    cost = myteam - theirteam
    print(cost)

def calc_wins(myteam, theirteam):
    #  print(type(myteam))
    #  print(type(theirteam))
    cost = myteam - theirteam
    print(cost)


if __name__ == '__main__':
    print("")
    team = build_team("rob.csv")
    my_cats = calc_cat_totals(team)
    print("")
    team = build_team("kyle.csv")
    cats = calc_cat_totals(team)
    calc_cost(my_cats, cats)
    print("")
    team = build_team("ben.csv")
    cats = calc_cat_totals(team)
    calc_cost(my_cats, cats)
    print("")
    team = build_team("dylan.csv")
    cats = calc_cat_totals(team)
    calc_cost(my_cats, cats)
    print("")
    team = build_team("george.csv")
    cats = calc_cat_totals(team)
    calc_cost(my_cats, cats)
    print("")
    team = build_team("zmo.csv")
    cats = calc_cat_totals(team)
    calc_cost(my_cats, cats)
    print("")
    team = build_team("alex.csv")
    cats = calc_cat_totals(team)
    calc_cost(my_cats, cats)
    print("")
    team = build_team("akbar.csv")
    cats = calc_cat_totals(team)
    calc_cost(my_cats, cats)
    print("")
    team = build_team("brandt.csv")
    cats = calc_cat_totals(team)
    calc_cost(my_cats, cats)
    print("")
    team = build_team("tom.csv")
    cats = calc_cat_totals(team)
    calc_cost(my_cats, cats)
    #  my_cats = calc_cat_totals(myteam)
    #  their_cats = calc_cat_totals(theirteam)
    #  calc_cost(my_cats, their_cats)
