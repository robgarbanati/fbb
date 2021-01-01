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
    stats.insert(28, 'PuntValue', -1, False)
    stats.insert(28, 'TheirPuntValue', -1, False)
    for index in indices:
        ast = stats.loc[stats.index[index], 'zAST']
        blk = stats.loc[stats.index[index], 'zBLK']
        reb = stats.loc[stats.index[index], 'zREB']
        ftp = stats.loc[stats.index[index], 'zFT%']
        fgp = stats.loc[stats.index[index], 'zFG%']
        tpm = stats.loc[stats.index[index], 'z3PM']
        total = stats.loc[stats.index[index], 'TOTAL']
        pv = total - ast - blk - ftp*0.5 - fgp*0.5
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
    def __str__(self):
        return """PTS\tAST\tREB\tBLK\tSTL\t3PM\tFG%\tFT%\tTO
{pts:.1f}\t{ast:.1f}\t{reb:.1f}\t{blk:.1f}\t{stl:.1f}\t{tpm:.1f}\t{fgp:.4f}\t{ftp:.4f}\t{to:.1f}""".format(pts=self.pts, ast=self.ast, reb=self.reb, blk=self.blk, stl=self.stl, tpm=self.tpm, fgp=self.fgp, ftp=self.ftp, to=self.to)
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
