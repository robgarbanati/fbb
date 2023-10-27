with open('rosters/my_schedule.raw', 'r') as rawfile:
    data = rawfile.readlines()

    #  lines_iter = iter(rawfile)
    clean_data = []
    lines_iter = iter(data[4:])
    prev_line = ""
    players = {}
    doublename = False
    # found_name = False
    name = ""
    move_found = False
    games_left_file = open('rosters/rob_roster.csv'.format(n=name), 'w')
    games_left_file.write("0,1,2\n")
    # skip 5 lines
    for line in lines_iter:
        line = line.replace('\n', '')
        print(f'{line=}')
        # count number of spaces in line
        num_spaces = line.count(' ')
        # state 1: found doublename. Save previous player to file if there was one.
        if num_spaces == 2:
            if name != "":
                print(f"found 2 spaces. Going to write: players[{name}] = {players[name]}")
                games_left_file.write(",{name},{num_games}\n".format(name=name, num_games=players[name]))
            doublename = True
            print(f"found doublename")
            # found_name = False
            name = ""
            move_found = False
            prev_line = line
            continue
        # state 2: found name. Save name.
        if num_spaces == 1 and doublename == True and line in prev_line:
            doublename = False
            # found_name = True
            name = line
            print(f"found player: {name=}")
            players[name] = 0
            continue
        # state 3: found move.
        if line == "MOVE" or line == "O":
            move_found = True
            print(f"move_found")
            if line == "O":
                players[name] = -2
            continue
        # state 4: Increment player's game countfor every line that is not "--"
        if move_found and num_spaces == 0 and line != "--" \
                and name != "" and "SG" not in line and \
                "PG" not in line and "SF" not in line and \
                "PF" not in line and len(line) > 1 and \
                "UTIL" not in line and "Bench" not in line \
                and "Empty" not in line and "IR" not in line:
        # if move_found and num_spaces == 0 and name != "" and len(line) > 2:
            players[name] += 1
            print(f"players[{name}] = {players[name]}")
    print(f"End of loop. Going to write: players[{name}] = {players[name]}")
    games_left_file.write(",{name},{num_games}\n".format(name=name, num_games=players[name]))
