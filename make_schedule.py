import click
import math
import numpy as np
import pandas as pd
from os import path
import common
import sys

def make_schedule(gm_name: str, source_file: str, last_day: str = "NOV 5"):
    with open(source_file, 'r') as rawfile:
        data = rawfile.readlines()
        lines_iter = iter(data[4:])
        prev_line = ""
        players = {}
        found_doublename = False
        found_name = False
        name = ""
        out_text = ""
        num_days = 0
        counting_games = False
        last_day_found = False
        days_counted_for_this_player = 0
        games_left_file = open(f'rosters/{gm_name}_roster.csv'.format(n=name), 'w')
        games_left_file.write("0,1,2\n")
        for line in lines_iter:
            # state 1: Ignore first few useless lines
            if line == "SLOT" or line == "PLAYER" or line == "OPP" \
                    or line == "STATUS" or line == "ACTION":
                continue
            # state 2: Count each date line until last_day
            if line.startswith("OCT") or line.startswith("NOV") or line.startswith("DEC") or \
                    line.startswith("JAN") or line.startswith("FEB") or line.startswith("MAR") or \
                    line.startswith("APR"):
                if  last_day_found:
                    continue
                num_days += 1
                print(f"{num_days=}")
            if line == last_day:
                last_day_found = True
                print(f"{num_days=}")
                continue
            line = line.replace('\n', '')
            print(f'{line=}')
            # count number of spaces in line
            num_spaces = line.count(' ')
            # state 3: done with dates. find doublename.
            if num_spaces >= 2 and found_doublename == False:
                found_doublename = True
                print(f"found doublename")
                prev_line = line
                continue
            # state 4: find name. Save name.
            if num_spaces >= 1 and found_doublename == True and found_name == False and line in prev_line and name == "":
                found_name = True
                name = line
                print(f"found player: {name=}")
                players[name] = 0
                continue
            # state 5: (optional): Find out status
            if line == "O":
                # players[name] = -2
                out_text = "O"
                continue
            # state 6: Find position. Start counting games.
            if counting_games == False and name != "" and \
                    ("SG" in line or \
                    "PG" in line or \
                    "SF" in line or \
                    "PF" in line or \
                    line == "C"):
                counting_games = True
                days_counted_for_this_player = 0
                print(f"counting_games")
                if line == "O":
                    # players[name] = -2
                    out_text = "O"
                continue
            # state 8: End of player's schedule. Reset state.
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
                found_doublename = False
                found_name = False
                continue
            # state 7: Increment player's game countfor every line that is not "--"
            # if counting_games and line != "--" and num_spaces == 0 and \
            #         line != "MOVE" and line != "":
            if counting_games:
                if num_spaces == 0 and line != "MOVE" and line != "":
                    days_counted_for_this_player += 1
                    print(f"{days_counted_for_this_player=}")
                    if line != "--" and days_counted_for_this_player <= num_days:
                        players[name] += 1
                        print(f"players[{name}] = {players[name]}")

        print(f"End of loop. Going to write: players[{name}] = {players[name]}")
        games_left_file.write(f"{out_text},{name},{players[name]}\n")

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
