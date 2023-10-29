import click
import math
import numpy as np
import pandas as pd
from os import path
import common
import sys

def make_schedule(gm_name: str, source_file: str):
    with open(source_file, 'r') as rawfile:
        data = rawfile.readlines()

        #  lines_iter = iter(rawfile)
        clean_data = []
        lines_iter = iter(data[4:])
        prev_line = ""
        players = {}
        doublename = False
        # found_name = False
        name = ""
        out_text = ""
        counting_games = False
        games_left_file = open(f'rosters/{gm_name}_roster.csv'.format(n=name), 'w')
        games_left_file.write("0,1,2\n")
        # skip 5 lines
        for line in lines_iter:
            line = line.replace('\n', '')
            print(f'{line=}')
            # count number of spaces in line
            num_spaces = line.count(' ')
            # state 1: found doublename. Save previous player to file if there was one.
            if num_spaces == 2:
                doublename = True
                print(f"found doublename")
                # found_name = False
                prev_line = line
                continue
            # state 2: found name. Save name.
            if num_spaces == 1 and doublename == True and line in prev_line and name == "":
                # found_name = True
                name = line
                print(f"found player: {name=}")
                players[name] = 0
                continue
            # state 3 (optional): Found out status
            if line == "O":
                # players[name] = -2
                out_text = "O"
                continue
            # state 4: Found position. Start counting games.
            if counting_games == False and name != "" and \
                    ("SG" in line or \
                    "PG" in line or \
                    "SF" in line or \
                    "PF" in line or \
                    line == "C"):
                counting_games = True
                print(f"counting_games")
                if line == "O":
                    players[name] = -2
                    out_text = "O"
                continue
            # state 6: End of player's schedule. Reset state.
            if counting_games and \
                    (line == "SG" or line == "PG" or line == "SF" or \
                    line == "PF" or line == "C" or line == "UTIL" or \
                    line == "F" or line == "G" or \
                    line == "Bench" or line == "IR"):
                print(f"found positional placement. Going to write: {out_text},{name},{players[name]}")
                # games_left_file.write(",{name},{num_games}\n".format(name=name, num_games=players[name]))
                games_left_file.write(f"{out_text},{name},{players[name]}\n")
                counting_games = False
                name = ""
                out_text = ""
                continue
            # state 5: Increment player's game countfor every line that is not "--"
            if counting_games and line != "--" and num_spaces == 0 and \
                    line != "MOVE" and line != "":
                # assert num_spaces == 0, "unexpected line: {line}".format(line=line)
                players[name] += 1
                print(f"players[{name}] = {players[name]}")

        # print(f"End of loop. Going to write: players[{name}] = {players[name]}")
        # games_left_file.write(f"{out_text},{name},{players[name]}\n")

def check_if_file_exists(infile):
    if not path.exists(infile):
        click.echo("Cannot find file at path {f}".format(f=infile))
        sys.exit(1)

@click.command()
@click.option('--other-team-name', '-o', type=str, default='brandt', help='Specify their name.')
def calc_my_and_their_games_left(other_team_name):
    check_if_file_exists("rosters/my_schedule.raw")
    check_if_file_exists("rosters/their_schedule.raw")

    make_schedule("rob", "rosters/my_schedule.raw")
    make_schedule(other_team_name, "rosters/their_schedule.raw")

if __name__ == '__main__':
    calc_my_and_their_games_left()
