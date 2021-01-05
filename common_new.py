import math
import numpy as np
import pandas as pd

def get_stats():
    stats = pd.read_csv("zstats.csv", sep='\t')
    stats = stats[[c for c in stats if c not in ['TOTAL']] 
       + ['TOTAL']]
    endnum = len(stats.index)
    indices = [num for num in range(0,endnum)]
    stats = stats.set_index(pd.Index(indices))
    stats.insert(28, 'TheirPuntValue', -1, False)
    stats.insert(28, 'PuntValue', -1, False)
    for index in indices:
        ast = stats.loc[stats.index[index], 'zAST']
        blk = stats.loc[stats.index[index], 'zBLK']
        reb = stats.loc[stats.index[index], 'zREB']
        ftp = stats.loc[stats.index[index], 'zFT%']
        fgp = stats.loc[stats.index[index], 'zFG%']
        tpm = stats.loc[stats.index[index], 'z3PM']
        total = stats.loc[stats.index[index], 'TOTAL']
        pv = total - ast - 0.5*blk - ftp*0.5 - fgp*0.5
        theirpv = total - blk - fgp - reb - 0.5*tpm
        stats.loc[stats.index[index], 'PuntValue'] = pv
        stats.loc[stats.index[index], 'TheirPuntValue'] = theirpv
    print(stats)
    return stats

class cost():
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
    def __str__(self):
        return """PTS\tAST\tREB\tBLK\tSTL\t3PM\tFG%\tFT%\tTO\tWINS\tCOST
{pts:.1f}\t{ast:.1f}\t{reb:.1f}\t{blk:.1f}\t{stl:.1f}\t{tpm:.1f}\t{fgp:.4f}\t{ftp:.4f}\t{to:.1f}\t{wins:.1f}\t{cost:.1f}""".format(pts=self.pts,
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
    pts_stdev_mult = 0
    ast_stdev_mult = 0
    blk_stdev_mult = 0.8
    stl_stdev_mult = 0
    tpm_stdev_mult = 0
    to_stdev_mult = 0
    reb_stdev_mult = 0
    fgm_stdev_mult = 0
    fga_stdev_mult = 0
    fgp_stdev_mult = 0
    ftm_stdev_mult = 0
    fta_stdev_mult = 0
    ftp_stdev_mult = 0
    def calc_stdevs():
        pts_stdev = pts*pts_stdev_mult;
        ast_stdev = ast*ast_stdev_mult;
        blk_stdev = blk*blk_stdev_mult;
        stl_stdev = stl*stl_stdev_mult;
        tpm_stdev = tpm*tpm_stdev_mult;
        to_stdev = to*to_stdev_mult;
        reb_stdev = reb*reb_stdev_mult;
        fgm_stdev = fgm*fgm_stdev_mult;
        fga_stdev = fga*fga_stdev_mult;
        fgp_stdev = fgp*fgp_stdev_mult;
        ftm_stdev = ftm*ftm_stdev_mult;
        fta_stdev = fta*fta_stdev_mult;
        ftp_stdev = ftp*ftp_stdev_mult;

    def __str__(self):
        return """PTS\tAST\tREB\tBLK\tSTL\t3PM\tFG%\tFT%\tTO\n{pts:.1f}\t{ast:.1f}\t{reb:.1f}\t{blk:.1f}\t{stl:.1f}\t{tpm:.1f}\t{fgp:.4f}\t{ftp:.4f}\t{to:.1f}\n{pts_stdev:.1f}\t{ast_stdev:.1f}\t{reb_stdev:.1f}\t{blk_stdev:.1f}\t{stl_stdev:.1f}\t{tpm_stdev:.1f}\t{fgp_stdev:.4f}\t{ftp_stdev:.4f}\t{to_stdev:.1f}\n""".format(
                pts=self.pts, ast=self.ast, reb=self.reb, blk=self.blk, stl=self.stl, tpm=self.tpm,
                fgp=self.fgp, ftp=self.ftp,pts_stdev=self.pts_stdev, ast_stdev=self.ast_stdev,
                reb_stdev=self.reb_stdev, blk_stdev=self.blk_stdev, stl_stdev=self.stl_stdev,
                tpm_stdev=self.tpm_stdev, fgp_stdev=self.fgp_stdev, ftp_stdev=self.ftp_stdev,
                to_stdev=self.to_stdev)
    def __sub__(self, other):
        #  print("in sub")
        subcat = cost()
        subcat.pts = math.sqrt(2*abs(self.pts - other.pts)/(self.pts + other.pts))
        if self.pts < other.pts:
            subcat.pts = -subcat.pts
        else:
            subcat.wins += 1
        subcat.cost += subcat.pts
        #  subcat.pts = math.sqrt(abs(self.pts - other.pts))
        #  subcat.ast = math.sqrt(abs(self.ast - other.ast))
        subcat.ast = math.sqrt(2*abs(self.ast - other.ast)/(self.ast + other.ast))
        if self.ast < other.ast:
            subcat.ast = -subcat.ast
        else:
            subcat.wins += 1
        subcat.cost += subcat.ast
        #  subcat.blk = math.sqrt(abs(self.blk - other.blk))
        subcat.blk = math.sqrt(2*abs(self.blk - other.blk)/(self.blk + other.blk))
        if self.blk < other.blk:
            subcat.blk = -subcat.blk
        else:
            subcat.wins += 1
        subcat.cost += subcat.blk
        #  subcat.stl = math.sqrt(abs(self.stl - other.stl))
        subcat.stl = math.sqrt(2*abs(self.stl - other.stl)/(self.stl + other.stl))
        if self.stl < other.stl:
            subcat.stl = -subcat.stl
        else:
            subcat.wins += 1
        subcat.cost += subcat.stl
        #  subcat.tpm = math.sqrt(abs(self.tpm - other.tpm))
        subcat.tpm = math.sqrt(2*abs(self.tpm - other.tpm)/(self.tpm + other.tpm))
        if self.tpm < other.tpm:
            subcat.tpm = -subcat.tpm
        else:
            subcat.wins += 1
        subcat.cost += subcat.tpm
        #  subcat.to = math.sqrt(abs(self.to - other.to))
        subcat.to = math.sqrt(2*abs(self.to - other.to)/(self.to + other.to))
        if self.to > other.to:
            subcat.to = -subcat.to
        else:
            subcat.wins += 1
        subcat.cost += subcat.to
        #  subcat.reb = math.sqrt(abs(self.reb - other.reb))
        subcat.reb = math.sqrt(2*abs(self.reb - other.reb)/(self.reb + other.reb))
        if self.reb < other.reb:
            subcat.reb = -subcat.reb
        else:
            subcat.wins += 1
        subcat.cost += subcat.reb
        #  subcat.fgp = math.sqrt(100*abs(self.fgp - other.fgp))
        subcat.fgp = 1.5*math.sqrt(2*abs(self.fgp - other.fgp)/(self.fgp + other.fgp))
        if self.fgp < other.fgp:
            subcat.fgp = -subcat.fgp
        else:
            subcat.wins += 1
        subcat.cost += subcat.fgp
        #  subcat.ftp = math.sqrt(100*abs(self.ftp - other.ftp))
        subcat.ftp = 1.5*math.sqrt(2*abs(self.ftp - other.ftp)/(self.ftp + other.ftp))
        if self.ftp < other.ftp:
            subcat.ftp = -subcat.ftp
        else:
            subcat.wins += 1
        subcat.cost += subcat.ftp
        return subcat
