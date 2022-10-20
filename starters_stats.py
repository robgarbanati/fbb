from dataclasses import dataclass
import math
import numpy as np
import pandas as pd
import common
import click
import sys

def calc_best_cat_totals(roster):
    #  print(f'{roster=}')
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
    #  print(team)
    return team

#  def recalc_players_punt(team):

@dataclass
class CatErrorMargin:
    pts: float
    ast: float
    blk: float
    stl: float
    tpm: float
    to: float
    reb: float
    fgp: float
    ftp: float
    def __add__(self, other):
        self.pts = self.pts + other.pts
        self.ast = self.ast + other.ast
        self.blk = self.blk + other.blk
        self.stl = self.stl + other.stl
        self.tpm = self.tpm + other.tpm
        self.reb = self.reb + other.reb
        self.ftp = self.ftp + other.ftp
        self.fgp = self.fgp + other.fgp
        self.ftp = self.ftp + other.ftp
        self.to = self.to + other.to

        return self

@dataclass
class WPnErma:
    wp: float
    erma: CatErrorMargin


pts_close_games = 0
ast_close_games = 0
blk_close_games = 0
stl_close_games = 0
tpm_close_games = 0
to_close_games = 0
reb_close_games = 0
fgp_close_games = 0
ftp_close_games = 0

#  def calc_cost(myteam, theirteam, erma):
def calc_cost(myteam, theirteam, wpnerma):
    wp = myteam - theirteam
    print(f"{str(wp)}")
    erma = CatErrorMargin(  pts = 0, ast = 0, blk = 0,
                            stl = 0, tpm = 0, to = 0,
                            reb = 0, fgp = 0, ftp = 0)
    ptserr = 0.5 - wp.pts
    print(f"{ptserr=}")
    erma.pts = ptserr*ptserr
    print(f"{erma.pts=}")
    asterr = 0.5 - wp.ast
    print(f"{asterr=}")
    erma.ast = asterr*asterr
    print(f"{erma.ast=}")
    blkerr = 0.5 - wp.blk
    print(f"{blkerr=}")
    erma.blk = blkerr*blkerr
    print(f"{erma.blk=}")
    stlerr = 0.5 - wp.stl
    print(f"{stlerr=}")
    erma.stl = stlerr*stlerr
    print(f"{erma.stl=}")
    tpmerr = 0.5 - wp.tpm
    print(f"{tpmerr=}")
    erma.tpm = tpmerr*tpmerr
    print(f"{erma.tpm=}")
    toerr = 0.5 - wp.to
    print(f"{toerr=}")
    erma.to = toerr*toerr
    print(f"{erma.to=}")
    reberr = 0.5 - wp.reb
    print(f"{reberr=}")
    erma.reb = reberr*reberr
    print(f"{erma.reb=}")
    fgperr = 0.5 - wp.fgp
    print(f"{fgperr=}")
    erma.fgp = fgperr*fgperr
    print(f"{erma.fgp=}")
    ftperr = 0.5 - wp.ftp
    print(f"{ftperr=}")
    erma.ftp = ftperr*ftperr
    print(f"{erma.ftp=}")
    print(f"{erma=}")
    wpnerma.erma += erma
    #  print(f"{wpnerma=}")

    #  wpnerma.erma.pts += wp.pts*wp.pts
    #  wpnerma.erma.ast += wp.ast*wp.ast
    #  wpnerma.erma.blk += wp.blk*wp.blk
    #  wpnerma.erma.stl += wp.stl*wp.stl
    #  wpnerma.erma.tpm += wp.tpm*wp.tpm
    #  wpnerma.erma.to += wp.to*wp.to
    #  wpnerma.erma.reb += wp.reb*wp.reb
    #  wpnerma.erma.fgp += wp.fgp*wp.fgp
    #  wpnerma.erma.ftp += wp.ftp*wp.ftp
    wpnerma.wp += wp.total_win_prob

    return wpnerma

@click.command()
@click.option('--stats-source', '-s', type=str, default='zstats.csv', help='Specify path to stats csv.')
def calc_win_prob_against_league(stats_source):
    erma = CatErrorMargin(  pts = 0, ast = 0, blk = 0,
                            stl = 0, tpm = 0, to = 0,
                            reb = 0, fgp = 0, ftp = 0)
    wpnerma = WPnErma(wp = 0, erma = erma)
    playoff_wins = 0
    print("")
    print("")
    team = common.build_full_team("rosters/rob_roster.csv", stats_source)
    print(f'{team=}')
    my_cats = calc_best_cat_totals(team)
    print("")
    print("Mark")
    team = common.build_full_team("rosters/mark_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    print(f"{wpnerma=}")
    print(f'after mark: {wpnerma.wp=}')
    print(f'after mark: {wpnerma.erma=}')
    print("")
    print("Lucas")
    team = common.build_full_team("rosters/lucas_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    print(f"{wpnerma=}")
    print("")
    print("Kyle")
    team = common.build_full_team("rosters/kyle_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    print(f"{wpnerma=}")
    print("")
    print("Ben")
    team = common.build_full_team("rosters/ben_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    print(f"{wpnerma=}")
    print("")
    print("Andy")
    team = common.build_full_team("rosters/andy_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    print(f"{wpnerma=}")
    print("")
    print("Alex")
    team = common.build_full_team("rosters/alex_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    print(f"{wpnerma=}")
    print("")
    print("Akbar")
    team = common.build_full_team("rosters/akbar_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    print(f"{wpnerma=}")
    print("")
    print("Tom")
    team = common.build_full_team("rosters/tom_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    print(f"{wpnerma=}")
    print("")
    print("Dylan")
    team = common.build_full_team("rosters/dylan_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    print(f"{wpnerma=}")
    #  playoff_wins += calc_cost(my_cats, cats)
    print("")
    print("Brandt")
    team = common.build_full_team("rosters/brandt_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    print(f"{wpnerma=}")
    #  playoff_wins += calc_cost(my_cats, cats)
    print("")
    print("ZMo")
    team = common.build_full_team("rosters/zmo_roster.csv", stats_source)
    cats = calc_best_cat_totals(team)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    wpnerma = calc_cost(my_cats, cats, wpnerma)
    print(f"{wpnerma=}")
    #  playoff_wins += calc_cost(my_cats, cats)
    print("")
    print("total expected wins:", wpnerma.wp)
    #  print("playoff expected wins:", playoff_wins)

if __name__ == '__main__':
    calc_win_prob_against_league()
