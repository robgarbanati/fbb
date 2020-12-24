import math
import numpy as np
import pandas as pd

def build_team(schedcsv):
    schedule = pd.read_csv(schedcsv)
    print(schedule)
    games_played = schedule.iloc[0,2]
    endnum = len(schedule.index)
     
    stats = pd.read_csv("stats.csv", sep='\t')
    #  print(stats)

    #### build team stats
    team_stats = pd.DataFrame()
    i=0
    for i in range(1,endnum):
        name = schedule.iloc[i,1]
        print("name =", name)
        playerstats = stats.loc[stats['PLAYER'] == name]
        #  print(playerstats)
        team_stats = team_stats.append(playerstats)
        team_stats.loc[stats['PLAYER'] == name, 'NumGames'] = schedule.iloc[i, 2]
        i+= 1
    team_stats = team_stats.sort_values(by='TOTAL', ascending=False)
    team_stats = team_stats.set_index(pd.Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    return(team_stats)

class cost():
    pts = 0
    ast = 0
    blk = 0
    stl = 0
    threepm = 0
    to = 0
    reb = 0
    fgm = 0
    fga = 0
    fgp = 0
    ftm = 0
    fta = 0
    ftp = 0
    def __str__(self):
        return """PTS\tAST\tREB\tBLK\tSTL\t3PM\tFG%\tFT%\tTO
{pts:.1f}\t{ast:.1f}\t{reb:.1f}\t{blk:.1f}\t{stl:.1f}\t{tpm:.1f}\t{fgp:.4f}\t{ftp:.4f}\t{to:.1f}
""".format(pts=self.pts, ast=self.ast, reb=self.reb, blk=self.blk, stl=self.stl, tpm=self.threepm, fgp=self.fgp, ftp=self.ftp, to=self.to)

class categories():
    pts = 0
    ast = 0
    blk = 0
    stl = 0
    threepm = 0
    to = 0
    reb = 0
    fgm = 0
    fga = 0
    fgp = 0
    ftm = 0
    fta = 0
    ftp = 0
    def __str__(self):
        return """PTS\tAST\tREB\tBLK\tSTL\t3PM\tFG%\tFT%\tTO
{pts:.1f}\t{ast:.1f}\t{reb:.1f}\t{blk:.1f}\t{stl:.1f}\t{tpm:.1f}\t{fgp:.4f}\t{ftp:.4f}\t{to:.1f}
""".format(pts=self.pts, ast=self.ast, reb=self.reb, blk=self.blk, stl=self.stl, tpm=self.threepm, fgp=self.fgp, ftp=self.ftp, to=self.to)
    def __sub__(self, other):
        print("in sub")
        subcat = cost()
        print(subcat)
        subcat.pts = math.sqrt(2*abs(self.pts - other.pts)/(self.pts + other.pts))
        #  subcat.pts = math.sqrt(abs(self.pts - other.pts))
        print(subcat)
        subcat.ast = math.sqrt(abs(self.ast - other.ast))
        subcat.blk = math.sqrt(abs(self.blk - other.blk))
        subcat.stl = math.sqrt(abs(self.stl - other.stl))
        subcat.threepm = math.sqrt(abs(self.threepm - other.threepm))
        subcat.to = math.sqrt(abs(self.to - other.to))
        subcat.reb = math.sqrt(abs(self.reb - other.reb))
        subcat.fgp = math.sqrt(abs(self.fgp - other.fgp))
        subcat.ftp = math.sqrt(abs(self.ftp - other.ftp))
        return subcat

def calc_cat_totals(team):
    total_games = 24
    i = 0
    team_cats = categories()
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
        team_cats.threepm += team['NumGames'][i] * team['3PM'][i]
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
    print(type(myteam))
    print(type(theirteam))
    cost = myteam - theirteam
    print(cost)


if __name__ == '__main__':
    myteam = build_team("rob.csv")
    print(myteam)
    theirteam = build_team("kyle.csv")
    print(theirteam)
    my_cats = calc_cat_totals(myteam)
    their_cats = calc_cat_totals(theirteam)
    calc_cost(my_cats, their_cats)
