from dataclasses import dataclass

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


