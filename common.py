import math
import numpy as np
import pandas as pd
import scipy.stats as st
import itertools 
import functools 

def get_stats():
    stats = pd.read_csv("zstats.csv", sep='\t')
    stats = stats[[c for c in stats if c not in ['TOTAL']] 
       + ['TOTAL']]
    endnum = len(stats.index)
    indices = [num for num in range(0,endnum)]
    stats = stats.set_index(pd.Index(indices))
    #  stats.insert(28, 'TheirPuntValue', -1, False)
    stats.insert(28, 'PuntValue', -1, False)
    for index in indices:
        ast = stats.loc[stats.index[index], 'zAST']
        blk = stats.loc[stats.index[index], 'zBLK']
        reb = stats.loc[stats.index[index], 'zREB']
        ftp = stats.loc[stats.index[index], 'zFT%']
        fgp = stats.loc[stats.index[index], 'zFG%']
        tpm = stats.loc[stats.index[index], 'z3PM']
        total = stats.loc[stats.index[index], 'TOTAL']
        pv = total - ast - 0.75*blk
        #  pv = total - ast - 0.5*blk - ftp*0.5 - fgp*0.5
        #  theirpv = total - blk - fgp - reb - 0.5*tpm
        stats.loc[stats.index[index], 'PuntValue'] = pv
        #  stats.loc[stats.index[index], 'TheirPuntValue'] = theirpv
    #  print(stats)
    return stats

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
        print(len(catlist))
        print(catlist)
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

    def calc_stdevs(self):
        self.pts_stdev = self.pts*self.pts_stdev_mult
        self.ast_stdev = self.ast*self.ast_stdev_mult
        self.blk_stdev = self.blk*self.blk_stdev_mult
        self.stl_stdev = self.stl*self.stl_stdev_mult
        self.tpm_stdev = self.tpm*self.tpm_stdev_mult
        self.to_stdev = self.to*self.to_stdev_mult
        self.reb_stdev = self.reb*self.reb_stdev_mult
        #  variance = (self.fgp)*(1 - self.fgp)*self.fga
        #  self.fgp_stdev = math.sqrt(variance)
        #  variance = (self.ftp)*(1 - self.ftp)*self.fta
        #  self.ftp_stdev = math.sqrt(variance)

        self.pts_variance = math.pow(self.pts*self.pts_stdev_mult, 2)
        self.ast_variance = math.pow(self.ast*self.ast_stdev_mult, 2)
        self.blk_variance = math.pow(self.blk*self.blk_stdev_mult, 2)
        self.stl_variance = math.pow(self.stl*self.stl_stdev_mult, 2)
        self.tpm_variance = math.pow(self.tpm*self.tpm_stdev_mult, 2)
        self.to_variance = math.pow(self.to*self.to_stdev_mult, 2)
        self.reb_variance = math.pow(self.reb*self.reb_stdev_mult, 2)

        fgm_variance = (self.fgp)*(1 - self.fgp)*self.fga
        fgm_stdev = math.sqrt(fgm_variance)
        self.fgp_stdev = fgm_stdev/self.fga
        self.fgp_variance = fgm_variance/self.fga/self.fga
        print(f'{fgm_variance=}')
        print(f'{fgm_stdev=}')
        print(f'{self.fgp_stdev=}')
        print(f'{self.fga=}')
        print(f'{self.fgm=}')
        print(f'{self.fgp_variance=}')
        ftm_variance = (self.ftp)*(1 - self.ftp)*self.fta
        ftm_stdev = math.sqrt(ftm_variance)
        self.ftp_stdev = ftm_stdev/self.fta
        self.ftp_variance = ftm_variance/self.fta/self.fta
        print(f'{ftm_variance=}')
        print(f'{ftm_stdev=}')
        print(f'{self.ftp_stdev=}')
        print(f'{self.fta=}')
        print(f'{self.ftm=}')
        print(f'{self.ftp_variance=}')
        return

    def __str__(self):
        return """PTS\tAST\tREB\tBLK\tSTL\t3PM\tFG%\tFT%\tTO\n{pts:.1f}\t{ast:.1f}\t{reb:.1f}\t{blk:.1f}\t{stl:.1f}\t{tpm:.1f}\t{fgp:.4f}\t{ftp:.4f}\t{to:.1f}\n{pts_stdev:.1f}\t{ast_stdev:.1f}\t{reb_stdev:.1f}\t{blk_stdev:.1f}\t{stl_stdev:.1f}\t{tpm_stdev:.1f}\t{fgp_stdev:.4f}\t{ftp_stdev:.4f}\t{to_stdev:.1f}\n""".format(
                pts=self.pts, ast=self.ast, reb=self.reb, blk=self.blk, stl=self.stl, tpm=self.tpm,
                fgp=self.fgp, ftp=self.ftp, to=self.to, pts_stdev=self.pts_stdev, 
                ast_stdev=self.ast_stdev, reb_stdev=self.reb_stdev, blk_stdev=self.blk_stdev, 
                stl_stdev=self.stl_stdev, tpm_stdev=self.tpm_stdev, fgp_stdev=self.fgp_stdev,
                ftp_stdev=self.ftp_stdev, to_stdev=self.to_stdev)
    def __sub__(self, other):
        print("in sub")
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
        print(f'{self.ftp=}')
        print(f'{other.ftp=}')
        print(f'{mean=}')
        print(f'{variance=}')
        print(f'{stdev=}')
        print(f'{zscore=}')
        print(f'{wp.ftp=}')

        mean = self.fgp - other.fgp
        variance = self.fgp_variance + other.fgp_variance
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.fgp = st.norm.cdf(zscore)
        print(f'{self.fgp=}')
        print(f'{other.fgp=}')
        print(f'{mean=}')
        print(f'{variance=}')
        print(f'{stdev=}')
        print(f'{zscore=}')
        print(f'{wp.fgp=}')

        mean = self.to - other.to
        variance = self.to_variance + other.to_variance
        stdev = math.sqrt(variance)
        zscore = mean/stdev
        wp.to = st.norm.cdf(-zscore)

        wp.calc_total_win_prob()
        return wp
