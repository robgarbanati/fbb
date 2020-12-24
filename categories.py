import math
import numpy as np
import pandas as pd

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

class team_cats():
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
        subcat.fgp = 3*math.sqrt(2*abs(self.fgp - other.fgp)/(self.fgp + other.fgp))
        if self.fgp < other.fgp:
            subcat.fgp = -subcat.fgp
        else:
            subcat.wins += 1
        subcat.cost += subcat.fgp
        #  subcat.ftp = math.sqrt(100*abs(self.ftp - other.ftp))
        subcat.ftp = 3*math.sqrt(2*abs(self.ftp - other.ftp)/(self.ftp + other.ftp))
        if self.ftp < other.ftp:
            subcat.ftp = -subcat.ftp
        else:
            subcat.wins += 1
        subcat.cost += subcat.ftp
        return subcat
