import math
import numpy as np
import pandas as pd
import scipy.stats as st
import itertools 
import functools 
import re


def get_stats(csv_file):
    stats = pd.read_csv(csv_file, sep='\t')
    stats = stats[[c for c in stats if c not in ['TOTAL']]
       + ['TOTAL']]
    endnum = len(stats.index)
    indices = [num for num in range(0,endnum)]
    stats = stats.set_index(pd.Index(indices))
    print(f"{stats=}")
    #  stats.insert(28, 'TheirPuntValue', -1, False)
    stats.insert(28, 'PuntValue', -1, False)
    stats.insert(29, 'PuntDiff', -1, False)
    for index in indices:
        pts = stats.loc[stats.index[index], 'zPTS']
        ast = stats.loc[stats.index[index], 'zAST']
        blk = stats.loc[stats.index[index], 'zBLK']
        reb = stats.loc[stats.index[index], 'zREB']
        ftp = stats.loc[stats.index[index], 'zFT%']
        fgp = stats.loc[stats.index[index], 'zFG%']
        tpm = stats.loc[stats.index[index], 'z3PM']
        stl = stats.loc[stats.index[index], 'zSTL']
        to = stats.loc[stats.index[index], 'zTO']
        total = stats.loc[stats.index[index], 'TOTAL']
        #  print(pts)
        #  print(ast)
        #  print(blk)
        #  print(reb)
        #  print(ftp)
        #  print(fgp)
        #  print(tpm)
        #  print(stl)
        #  print(to)
        #  print(total)
        #  truetotal = pts + ast + blk + reb + ftp + fgp + tpm + stl + to
        #  pv = total - pts - ast - blk - reb - ftp - fgp - stl - to
        pv = stl + tpm + fgp + ftp
        #  pv = total
        punt_diff = pv - total
        stats.loc[stats.index[index], 'PuntValue'] = pv
        stats.loc[stats.index[index], 'PuntDiff'] = punt_diff
        #  stats.loc[stats.index[index], 'TheirPuntValue'] = theirpv
    #  pd.set_option("display.max_rows", 80)
    #  print(stats)
    stats = stats.sort_values(by='PuntValue', ascending=False)
    return stats

def build_full_team(schedcsv, source="projections"):
    #  print(schedcsv)
    schedule = pd.read_csv(schedcsv)
    #  print(schedule)
    endnum = len(schedule.index)
     
    if source == "projections":
        stats = get_stats("zstats.csv")
    else:
        stats = get_stats(source)

    total_z = 0
    
    #### build team stats
    team_stats = pd.DataFrame()
    for i in range(0,endnum):
        name = schedule.iloc[i,1]
        out = schedule.iloc[i,0]
        if out == 'X':
            continue
        playerstats = stats.loc[stats['PLAYER'] == name]
        stats.loc[stats['PLAYER'] == name, 'NumGames'] = schedule.iloc[i,2]
        playerstats = stats.loc[stats['PLAYER'] == name]
        #  print(f'{playerstats=}')
        team_stats = team_stats.append(playerstats)
        z = stats.loc[stats['PLAYER'] == name, 'TOTAL'].values[0]
        #  print(f'{z=}')
        total_z += z
        #  print(f'{total_z=}')
    endnum = len(team_stats.index)
    team_stats = team_stats.sort_values(by='TOTAL', ascending=False)
    indices = [num for num in range(0,endnum)]
    team_stats = team_stats.set_index(pd.Index(indices))

    print(team_stats)
    print(f'{total_z=}')
    return(team_stats)

def build_team(schedcsv, source="projections"):
    #  print(schedcsv)
    schedule = pd.read_csv(schedcsv)
    endnum = len(schedule.index)
     
    if source == "projections":
        stats = get_stats("zstats.csv")
    else:
        stats = get_stats(source)

    #### build team stats
    team_stats = pd.DataFrame()
    total_z = 0
    for i in range(0,endnum):
        name = schedule.iloc[i,1]
        out = schedule.iloc[i,0]
        if out == 'O' or out == 'X':
            continue
        playerstats = stats.loc[stats['PLAYER'] == name]
        stats.loc[stats['PLAYER'] == name, 'NumGames'] = schedule.iloc[i,2]
        playerstats = stats.loc[stats['PLAYER'] == name]
        z = stats.loc[stats['PLAYER'] == name, 'TOTAL']
        total_z += z
        team_stats = team_stats.append(playerstats)
    endnum = len(team_stats.index)
    print(f"{endnum=}")
    team_stats = team_stats.sort_values(by='TOTAL', ascending=False)
    indices = [num for num in range(0,endnum)]
    team_stats = team_stats.set_index(pd.Index(indices))

    print(team_stats)
    print(f'{total_z=}')
    return(team_stats)

def add(a, b):
    return a+b

def mult(a, b):
    return a*b

class winprob():
    pts = 0
    ast = 0
    blk = 0
    stl = 0
    tpm = 0
    to = 0
    reb = 0
    fgm = 0
    fga = 0
    fgp = 0
    ftm = 0
    fta = 0
    ftp = 0
    cost = 0
    wins = 0
    def calc_total_win_prob(self):
        catlist = [self.pts, self.ast, self.blk, self.stl, self.tpm, self.reb, self.to, self.fgp, self.ftp]
        #  catlist = [1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
        #  print(catlist)
        total_prob = 0
        number = 0x1FF
        #  number = 0x1f
        while number >= 0:
            current_prob = 1
            num_ones = bin(number).count("1")
            #  print("number =", number, "num_ones =", num_ones)
            shift_amt = 0
            #  while shift_amt < 9:
            if num_ones < 5:
                number -= 1
                continue
            while shift_amt < 9:
                if number & (1 << shift_amt):
                    #  print("using catlist[{i}] = {f}".format(i=shift_amt, f = catlist[shift_amt]))
                    current_prob *= catlist[shift_amt]
                else:
                    #  print("using 1 - catlist[{i}] = {f}".format(i=shift_amt, f = 1 - catlist[shift_amt]))
                    current_prob *= (1 - catlist[shift_amt])
                shift_amt += 1
                #  print("current_prob =", current_prob)
            total_prob += current_prob
            #  print("total_prob =", total_prob)
            number -= 1
        print("total_prob =", total_prob)
        self.total_win_prob = total_prob
        return
    def __str__(self):
        return """PTS\tAST\tREB\tBLK\tSTL\t3PM\tFG%\tFT%\tTO\tWINS\tCOST
{pts:.3f}\t{ast:.3f}\t{reb:.3f}\t{blk:.3f}\t{stl:.3f}\t{tpm:.3f}\t{fgp:.3f}\t{ftp:.3f}\t{to:.3f}\t{wins:.3f}\t{cost:.3f}""".format(pts=self.pts,
        ast=self.ast, reb=self.reb, blk=self.blk, stl=self.stl, tpm=self.tpm, fgp=self.fgp,
        ftp=self.ftp, to=self.to, wins=self.wins, cost=self.cost)

class team():
    pts = 0
    ast = 0
    blk = 0
    stl = 0
    tpm = 0
    to = 0
    reb = 0
    fgm = 0
    fga = 0
    fgp = 0
    ftm = 0
    fta = 0
    ftp = 0
    pts_stdev = 0
    ast_stdev = 0
    blk_stdev = 0
    stl_stdev = 0
    tpm_stdev = 0
    to_stdev = 0
    reb_stdev = 0
    fgm_stdev = 0
    fga_stdev = 0
    fgp_stdev = 0
    ftm_stdev = 0
    fta_stdev = 0
    ftp_stdev = 0

    pts_variance = 0
    ast_variance = 0
    blk_variance = 0
    stl_variance = 0
    tpm_variance = 0
    to_variance = 0
    reb_variance = 0
    fgm_variance = 0
    fga_variance = 0
    fgp_variance = 0
    ftm_variance = 0
    fta_variance = 0
    ftp_variance = 0

    pts_stdev_mult = 0.062570279
    ast_stdev_mult = 0.089123907
    blk_stdev_mult = 0.160951628
    stl_stdev_mult = 0.163285224
    reb_stdev_mult = 0.066313651
    tpm_stdev_mult = 0.149934668
    fgp_stdev_mult = 0.046979765
    ftp_stdev_mult = 0.044675696
    to_stdev_mult = 0.116600025

    pts_stdev_mult_ten = 0.117058274
    ast_stdev_mult_ten = 0.166735562
    blk_stdev_mult_ten = 0.301112924
    stl_stdev_mult_ten = 0.305478682
    reb_stdev_mult_ten = 0.124061482
    tpm_stdev_mult_ten = 0.28050208
    fgp_stdev_mult_ten = 0.087891092
    ftp_stdev_mult_ten = 0.083580574
    to_stdev_mult_ten = 0.218138673

    def calc_stdevs(self, total_games):
        stdev_ten = self.pts*self.pts_stdev_mult_ten
        variance_ten = math.pow(stdev_ten, 2)
        mult = variance_ten*total_games/10
        if total_games == 0:
            self.pts_stdev = 0
        else:
            self.pts_stdev = math.sqrt(mult)/(total_games/10)

        self.ast_stdev = self.ast*self.ast_stdev_mult_ten
        stdev_ten = self.ast*self.ast_stdev_mult_ten
        variance_ten = math.pow(stdev_ten, 2)
        mult = variance_ten*total_games/10
        if total_games == 0:
            self.ast_stdev = 0
        else:
            self.ast_stdev = math.sqrt(mult)/(total_games/10)

        self.blk_stdev = self.blk*self.blk_stdev_mult
        stdev_ten = self.blk*self.blk_stdev_mult_ten
        variance_ten = math.pow(stdev_ten, 2)
        mult = variance_ten*total_games/10
        if total_games == 0:
            self.blk_stdev = 0
        else:
            self.blk_stdev = math.sqrt(mult)/(total_games/10)

        self.stl_stdev = self.stl*self.stl_stdev_mult
        stdev_ten = self.stl*self.stl_stdev_mult_ten
        variance_ten = math.pow(stdev_ten, 2)
        mult = variance_ten*total_games/10
        if total_games == 0:
            self.stl_stdev = 0
        else:
            self.stl_stdev = math.sqrt(mult)/(total_games/10)

        self.tpm_stdev = self.tpm*self.tpm_stdev_mult
        stdev_ten = self.tpm*self.tpm_stdev_mult_ten
        variance_ten = math.pow(stdev_ten, 2)
        mult = variance_ten*total_games/10
        if total_games == 0:
            self.tpm_stdev = 0
        else:
            self.tpm_stdev = math.sqrt(mult)/(total_games/10)

        self.to_stdev = self.to*self.to_stdev_mult
        stdev_ten = self.to*self.to_stdev_mult_ten
        variance_ten = math.pow(stdev_ten, 2)
        mult = variance_ten*total_games/10
        if total_games == 0:
            self.to_stdev = 0
        else:
            self.to_stdev = math.sqrt(mult)/(total_games/10)

        self.reb_stdev = self.reb*self.reb_stdev_mult
        stdev_ten = self.reb*self.reb_stdev_mult_ten
        variance_ten = math.pow(stdev_ten, 2)
        mult = variance_ten*total_games/10
        if total_games == 0:
            self.reb_stdev = 0
        else:
            self.reb_stdev = math.sqrt(mult)/(total_games/10)

        #  variance = (self.fgp)*(1 - self.fgp)*self.fga
        #  self.fgp_stdev = math.sqrt(variance)
        #  variance = (self.ftp)*(1 - self.ftp)*self.fta
        #  self.ftp_stdev = math.sqrt(variance)

        self.pts_variance = math.pow(self.pts_stdev, 2)
        self.ast_variance = math.pow(self.ast_stdev, 2)
        self.blk_variance = math.pow(self.blk_stdev, 2)
        self.stl_variance = math.pow(self.stl_stdev, 2)
        self.tpm_variance = math.pow(self.tpm_stdev, 2)
        self.to_variance = math.pow(self.to_stdev, 2)
        self.reb_variance = math.pow(self.reb_stdev, 2)

        self.fgm_variance = (self.fgp)*(1 - self.fgp)*self.fga
        self.fgm_stdev = math.sqrt(self.fgm_variance)
        self.fgp_stdev = self.fgm_stdev/self.fga
        self.fgp_variance = self.fgm_variance/self.fga/self.fga
        self.ftm_variance = (self.ftp)*(1 - self.ftp)*self.fta
        self.ftm_stdev = math.sqrt(self.ftm_variance)
        self.ftp_stdev = self.ftm_stdev/self.fta
        self.ftp_variance = self.ftm_variance/self.fta/self.fta
        return

    def __str__(self):
        return """PTS\tAST\tREB\tBLK\tSTL\t3PM\tFG%\tFT%\tTO\n{pts:.1f}\t{ast:.1f}\t{reb:.1f}\t{blk:.1f}\t{stl:.1f}\t{tpm:.1f}\t{fgp:.4f}\t{ftp:.4f}\t{to:.1f}\n{pts_stdev:.1f}\t{ast_stdev:.1f}\t{reb_stdev:.1f}\t{blk_stdev:.1f}\t{stl_stdev:.1f}\t{tpm_stdev:.1f}\t{fgp_stdev:.4f}\t{ftp_stdev:.4f}\t{to_stdev:.1f}\n""".format(
                pts=self.pts, ast=self.ast, reb=self.reb, blk=self.blk, stl=self.stl, tpm=self.tpm,
                fgp=self.fgp, ftp=self.ftp, to=self.to, pts_stdev=self.pts_stdev, 
                ast_stdev=self.ast_stdev, reb_stdev=self.reb_stdev, blk_stdev=self.blk_stdev, 
                stl_stdev=self.stl_stdev, tpm_stdev=self.tpm_stdev, fgp_stdev=self.fgp_stdev,
                ftp_stdev=self.ftp_stdev, to_stdev=self.to_stdev)
    def __sub__(self, other):
        wp = winprob()

        mean = self.pts - other.pts
        variance = self.pts_variance + other.pts_variance
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.pts = st.norm.cdf(zscore)

        mean = self.ast - other.ast
        variance = self.ast_variance + other.ast_variance
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.ast = st.norm.cdf(zscore)

        mean = self.blk - other.blk
        variance = self.blk_variance + other.blk_variance
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.blk = st.norm.cdf(zscore)

        mean = self.stl - other.stl
        variance = self.stl_variance + other.stl_variance
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.stl = st.norm.cdf(zscore)

        mean = self.tpm - other.tpm
        variance = self.tpm_variance + other.tpm_variance
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.tpm = st.norm.cdf(zscore)

        mean = self.reb - other.reb
        variance = self.reb_variance + other.reb_variance
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.reb = st.norm.cdf(zscore)

        mean = self.ftp - other.ftp
        variance = self.ftp_variance + other.ftp_variance
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.ftp = st.norm.cdf(zscore)

        mean = self.fgp - other.fgp
        self.fgp_stdev = self.fgm_stdev/self.fga
        other.fgp_stdev = other.fgm_stdev/other.fga
        variance = math.pow(self.fgp_stdev, 2) + math.pow(other.fgp_stdev, 2)
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.fgp = st.norm.cdf(zscore)

        mean = self.ftp - other.ftp
        self.ftp_stdev = self.ftm_stdev/self.fta
        other.ftp_stdev = other.ftm_stdev/other.fta
        variance = math.pow(self.ftp_stdev, 2) + math.pow(other.ftp_stdev, 2)
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.ftp = st.norm.cdf(zscore)

        mean = self.to - other.to
        variance = self.to_variance + other.to_variance
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.to = st.norm.cdf(-zscore)

        wp.calc_total_win_prob()
        return wp
