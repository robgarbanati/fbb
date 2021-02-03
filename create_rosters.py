with open('rosters.raw', 'r') as rawfile, :
    data = rawfile.readlines()
    #  for line in data:
        #  line = line.strip()
        #  line = line.replace(' \t', '\t')
        #  print(line)

    #  lines_iter = iter(rawfile)
    clean_data = []
    lines_iter = iter(data)
    prev_line = ""
    teams = {}
    gm = ""
    rosterfile = None
    for line in lines_iter:
        line = line.replace('\n', '')
        print(f'{line=}')
        if line == "CarMelo Ball" or line == "Weed Use And Work Ethic" or \
        line == "Rain City Bitch Pigeons" or line == "A Tingus In My Pingus" or \
        line == "Choi Boys" or line == "LaVar Ball 4 Prez" or line == "LaVar Ball 4 Prez" or \
        line == "Inbred Intangibles" or line == "Titties Over Titles" or line == "Team De'Ath":
            gm = line
            teams[gm] = []
            rosterfile = open('{n}_roster.csv'.format(n=gm), 'w')
            rosterfile.write(gm)
        elif line in prev_line and line != '' and line != 'F' and line != 'O':
            print(f'{teams=}')
            teams[gm].append(line)
            rosterfile.write(line)
        prev_line = line
    print(f'{teams=}')
    print(f'{teams["CarMelo Ball"]=}')
    exit(0)

    #  csvfile.write("""0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23\t24\t25\t26\t27\t28\n""")
    csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tzFG%\tFT%\tFTM\tFTA\tzFT%\t3PM\tz3PM\tPTS\tzPTS\tREB\tzREB\tAST\tzAST\tSTL\tzSTL\tBLK\tzBLK\tTO\tzTO\tTOTAL\n""")
    #  csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tFT%\tFTM\tFTA\t3PM\tPTS\tTREB\tAST\tSTL\tBLK\tTO\tTOTAL\tzFG%\tzFT%\tz3PM\tzPTS\tzREB\tzAST\tzSTL\tzBLK\tzTO\n""")
    clean_iter = iter(clean_data)
    for joined_tuple in zip(clean_iter, clean_iter, clean_iter, clean_iter, clean_iter,
                            clean_iter, clean_iter, clean_iter, clean_iter, clean_iter):
        print(f'{joined_tuple=}')
        joined_list = list(joined_tuple)
        #  print(f'{joined_list=}')
        #  joined_list[0] = joined_list[0].strip()
        #  joined_list.append(joined_list[1].strip())
        #  joined_list[1] = "\t"
        joined_list.append("\n")
        print(f'{joined_list=}')
        joined_str = "\t".join(joined_list)
        print(f'{joined_str=}')
        formatted_str = joined_str.replace(' \t', '\t')
        formatted_str = formatted_str.replace('(', '\t')
        formatted_str = formatted_str.replace(')', '')
        formatted_str = formatted_str.replace(u'\xa0', u'')
        formatted_str = formatted_str.replace('/', '\t')
        formatted_str = formatted_str.replace('\t\n', '\n')
        #  index = formatted_str.rfind('\t')
        #  print(f'{index=}')
        #  formatted_str = formatted_str.replace(' ', '')
        #  formatted_str = formatted_str.strip()
        print(f'{formatted_str=}')
        #  print(formatted_str)
        csvfile.write(formatted_str)

with open('zstats_rankings.raw', 'r') as rawfile, open('zstats_rankings.csv', 'w') as csvfile:
    data = rawfile.readlines()
    #  for line in data:
        #  line = line.strip()
        #  line = line.replace(' \t', '\t')
        #  print(line)

    #  lines_iter = iter(rawfile)
    clean_data = []
    lines_iter = iter(data)
    for line in lines_iter:
        if line[0] != 'R':
            clean_data.append(line.strip())

    #  csvfile.write("""0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23\t24\t25\t26\t27\t28\n""")
    csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tzFG%\tFT%\tFTM\tFTA\tzFT%\t3PM\tz3PM\tPTS\tzPTS\tREB\tzREB\tAST\tzAST\tSTL\tzSTL\tBLK\tzBLK\tTO\tzTO\tTOTAL\n""")
    #  csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tFT%\tFTM\tFTA\t3PM\tPTS\tTREB\tAST\tSTL\tBLK\tTO\tTOTAL\tzFG%\tzFT%\tz3PM\tzPTS\tzREB\tzAST\tzSTL\tzBLK\tzTO\n""")
    clean_iter = iter(clean_data)
    for joined_tuple in zip(clean_iter, clean_iter, clean_iter, clean_iter, clean_iter,
                            clean_iter, clean_iter, clean_iter, clean_iter, clean_iter):
        print(f'{joined_tuple=}')
        joined_list = list(joined_tuple)
        #  print(f'{joined_list=}')
        #  joined_list[0] = joined_list[0].strip()
        #  joined_list.append(joined_list[1].strip())
        #  joined_list[1] = "\t"
        joined_list.append("\n")
        print(f'{joined_list=}')
        joined_str = "\t".join(joined_list)
        print(f'{joined_str=}')
        formatted_str = joined_str.replace(' \t', '\t')
        formatted_str = formatted_str.replace('(', '\t')
        formatted_str = formatted_str.replace(')', '')
        formatted_str = formatted_str.replace(u'\xa0', u'')
        formatted_str = formatted_str.replace('/', '\t')
        formatted_str = formatted_str.replace('\t\n', '\n')
        print(f'{formatted_str=}')
        #  print(formatted_str)
        csvfile.write(formatted_str)

with open('zstats_rankings_14.raw', 'r') as rawfile, open('zstats_rankings_14.csv', 'w') as csvfile:
    data = rawfile.readlines()
    #  for line in data:
        #  line = line.strip()
        #  line = line.replace(' \t', '\t')
        #  print(line)

    #  lines_iter = iter(rawfile)
    clean_data = []
    lines_iter = iter(data)
    for line in lines_iter:
        if line[0] != 'R':
            clean_data.append(line.strip())

    #  csvfile.write("""0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23\t24\t25\t26\t27\t28\n""")
    csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tzFG%\tFT%\tFTM\tFTA\tzFT%\t3PM\tz3PM\tPTS\tzPTS\tREB\tzREB\tAST\tzAST\tSTL\tzSTL\tBLK\tzBLK\tTO\tzTO\tTOTAL\n""")
    #  csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tFT%\tFTM\tFTA\t3PM\tPTS\tTREB\tAST\tSTL\tBLK\tTO\tTOTAL\tzFG%\tzFT%\tz3PM\tzPTS\tzREB\tzAST\tzSTL\tzBLK\tzTO\n""")
    clean_iter = iter(clean_data)
    for joined_tuple in zip(clean_iter, clean_iter, clean_iter, clean_iter, clean_iter,
                            clean_iter, clean_iter, clean_iter, clean_iter, clean_iter):
        print(f'{joined_tuple=}')
        joined_list = list(joined_tuple)
        #  print(f'{joined_list=}')
        #  joined_list[0] = joined_list[0].strip()
        #  joined_list.append(joined_list[1].strip())
        #  joined_list[1] = "\t"
        joined_list.append("\n")
        print(f'{joined_list=}')
        joined_str = "\t".join(joined_list)
        print(f'{joined_str=}')
        formatted_str = joined_str.replace(' \t', '\t')
        formatted_str = formatted_str.replace('(', '\t')
        formatted_str = formatted_str.replace(')', '')
        formatted_str = formatted_str.replace(u'\xa0', u'')
        formatted_str = formatted_str.replace('/', '\t')
        formatted_str = formatted_str.replace('\t\n', '\n')
        print(f'{formatted_str=}')
        #  print(formatted_str)
        csvfile.write(formatted_str)

with open('zstats_rankings_7.raw', 'r') as rawfile, open('zstats_rankings_7.csv', 'w') as csvfile:
    data = rawfile.readlines()
    #  for line in data:
        #  line = line.strip()
        #  line = line.replace(' \t', '\t')
        #  print(line)

    #  lines_iter = iter(rawfile)
    clean_data = []
    lines_iter = iter(data)
    for line in lines_iter:
        if line[0] != 'R':
            clean_data.append(line.strip())

    #  csvfile.write("""0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23\t24\t25\t26\t27\t28\n""")
    csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tzFG%\tFT%\tFTM\tFTA\tzFT%\t3PM\tz3PM\tPTS\tzPTS\tREB\tzREB\tAST\tzAST\tSTL\tzSTL\tBLK\tzBLK\tTO\tzTO\tTOTAL\n""")
    #  csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tFT%\tFTM\tFTA\t3PM\tPTS\tTREB\tAST\tSTL\tBLK\tTO\tTOTAL\tzFG%\tzFT%\tz3PM\tzPTS\tzREB\tzAST\tzSTL\tzBLK\tzTO\n""")
    clean_iter = iter(clean_data)
    for joined_tuple in zip(clean_iter, clean_iter, clean_iter, clean_iter, clean_iter,
                            clean_iter, clean_iter, clean_iter, clean_iter, clean_iter):
        print(f'{joined_tuple=}')
        joined_list = list(joined_tuple)
        #  print(f'{joined_list=}')
        #  joined_list[0] = joined_list[0].strip()
        #  joined_list.append(joined_list[1].strip())
        #  joined_list[1] = "\t"
        joined_list.append("\n")
        print(f'{joined_list=}')
        joined_str = "\t".join(joined_list)
        print(f'{joined_str=}')
        formatted_str = joined_str.replace(' \t', '\t')
        formatted_str = formatted_str.replace('(', '\t')
        formatted_str = formatted_str.replace(')', '')
        formatted_str = formatted_str.replace(u'\xa0', u'')
        formatted_str = formatted_str.replace('/', '\t')
        formatted_str = formatted_str.replace('\t\n', '\n')
        print(f'{formatted_str=}')
        #  print(formatted_str)
        csvfile.write(formatted_str)
