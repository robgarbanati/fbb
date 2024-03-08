with open('rosters/rosters.raw', 'r') as rawfile:
    data = rawfile.readlines()
    for line in data:
        line = line.strip()
        line = line.replace(' \t', '\t')
        print(line)

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
        if line == "Sweet Home Wembanyama":
            found_gm = True
            gm = "tom"
        elif line == "Hali Bomaye":
            found_gm = True
            gm = "brandt"
        elif line == "Back-To-Back Man Gets Paid":
            found_gm = True
            gm = "rob"
        elif line == "Choi Boys":
            found_gm = True
            gm = "dylan"
        elif line == "Finding Melo":
            found_gm = True
            gm = "akbar"
        elif line == "MasterbAyton To Her Only Franz":
            found_gm = True
            gm = "ben"
        elif line == "SHAQTIN A POOLE":
            found_gm = True
            gm = "kyle"
        elif line == "Wham-Bam Thankyou Ma'am":
            found_gm = True
            gm = "lucas"
        elif line == "Weed Use And Work Ethic":
            found_gm = True
            gm = "zmo"
        elif line == "Telos B.C.":
            found_gm = True
            gm = "jake"
        elif line == "Uncle Steve's Mets":
            found_gm = True
            gm = "mark"
        elif line == "King Slayer":
            found_gm = True
            gm = "andy"
        else:
            found_gm = False

        if found_gm:
            teams[gm] = []
            rosterfile = open('rosters/{n}_roster.csv'.format(n=gm), 'w')
            #  rosterfile.write("{gm}\n".format(gm=gm))
            rosterfile.write("0,1,2\n")
        elif line in prev_line and line != '' and line != 'F' and line != 'C' and line != 'O':
            line = line.replace('Nic ', 'Nicolas ')
            line = line.replace('P.J. ', 'PJ ')
            line = line.replace('O.G. ', 'OG ')
            # line = line.replace('Jr.', 'Jr')
            line = line.replace(' III', '')
            line = line.replace('Alperen Sengun', 'Alperen Sengün')
            print(f'{line=}')
            print(f'{teams=}')
            teams[gm].append(line)
            rosterfile.write(",{line},3.5\n".format(line=line))
        prev_line = line
    print(f'{teams=}')
    print(f'{teams["tom"]=}')
    print(f'{teams["brandt"]=}')
    print(f'{teams["rob"]=}')
    print(f'{teams["dylan"]=}')
    print(f'{teams["akbar"]=}')
    print(f'{teams["ben"]=}')
    print(f'{teams["kyle"]=}')
    print(f'{teams["lucas"]=}')
    print(f'{teams["zmo"]=}')
    print(f'{teams["jake"]=}')
    print(f'{teams["mark"]=}')
    print(f'{teams["andy"]=}')
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
        formatted_str = formatted_str.replace('Nic ', 'Nicolas ')
        formatted_str = formatted_str.replace('P.J. ', 'PJ ')
        formatted_str = formatted_str.replace('O.G. ', 'OG ')
        formatted_str = formatted_str.replace('Jr.', 'Jr')
        #  index = formatted_str.rfind('\t')
        #  print(f'{index=}')
        #  formatted_str = formatted_str.replace(' ', '')
        #  formatted_str = formatted_str.strip()
        print(f'{formatted_str=}')
        #  print(formatted_str)
        csvfile.write(formatted_str)

#  with open('zstats_rankings.raw', 'r') as rawfile, open('zstats_rankings.csv', 'w') as csvfile:
#      data = rawfile.readlines()
#      #  for line in data:
#          #  line = line.strip()
#          #  line = line.replace(' \t', '\t')
#          #  print(line)
#
#      #  lines_iter = iter(rawfile)
#      clean_data = []
#      lines_iter = iter(data)
#      for line in lines_iter:
#          if line[0] != 'R':
#              clean_data.append(line.strip())
#
#      #  csvfile.write("""0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23\t24\t25\t26\t27\t28\n""")
#      csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tzFG%\tFT%\tFTM\tFTA\tzFT%\t3PM\tz3PM\tPTS\tzPTS\tREB\tzREB\tAST\tzAST\tSTL\tzSTL\tBLK\tzBLK\tTO\tzTO\tTOTAL\n""")
#      #  csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tFT%\tFTM\tFTA\t3PM\tPTS\tTREB\tAST\tSTL\tBLK\tTO\tTOTAL\tzFG%\tzFT%\tz3PM\tzPTS\tzREB\tzAST\tzSTL\tzBLK\tzTO\n""")
#      clean_iter = iter(clean_data)
#      for joined_tuple in zip(clean_iter, clean_iter, clean_iter, clean_iter, clean_iter,
#                              clean_iter, clean_iter, clean_iter, clean_iter, clean_iter):
#          print(f'{joined_tuple=}')
#          joined_list = list(joined_tuple)
#          #  print(f'{joined_list=}')
#          #  joined_list[0] = joined_list[0].strip()
#          #  joined_list.append(joined_list[1].strip())
#          #  joined_list[1] = "\t"
#          joined_list.append("\n")
#          print(f'{joined_list=}')
#          joined_str = "\t".join(joined_list)
#          print(f'{joined_str=}')
#          formatted_str = joined_str.replace(' \t', '\t')
#          formatted_str = formatted_str.replace('(', '\t')
#          formatted_str = formatted_str.replace(')', '')
#          formatted_str = formatted_str.replace(u'\xa0', u'')
#          formatted_str = formatted_str.replace('/', '\t')
#          formatted_str = formatted_str.replace('\t\n', '\n')
#          print(f'{formatted_str=}')
#          #  print(formatted_str)
#          csvfile.write(formatted_str)
#
#  with open('zstats_rankings_14.raw', 'r') as rawfile, open('zstats_rankings_14.csv', 'w') as csvfile:
#      data = rawfile.readlines()
#      #  for line in data:
#          #  line = line.strip()
#          #  line = line.replace(' \t', '\t')
#          #  print(line)
#
#      #  lines_iter = iter(rawfile)
#      clean_data = []
#      lines_iter = iter(data)
#      for line in lines_iter:
#          if line[0] != 'R':
#              clean_data.append(line.strip())
#
#      #  csvfile.write("""0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23\t24\t25\t26\t27\t28\n""")
#      csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tzFG%\tFT%\tFTM\tFTA\tzFT%\t3PM\tz3PM\tPTS\tzPTS\tREB\tzREB\tAST\tzAST\tSTL\tzSTL\tBLK\tzBLK\tTO\tzTO\tTOTAL\n""")
#      #  csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tFT%\tFTM\tFTA\t3PM\tPTS\tTREB\tAST\tSTL\tBLK\tTO\tTOTAL\tzFG%\tzFT%\tz3PM\tzPTS\tzREB\tzAST\tzSTL\tzBLK\tzTO\n""")
#      clean_iter = iter(clean_data)
#      for joined_tuple in zip(clean_iter, clean_iter, clean_iter, clean_iter, clean_iter,
#                              clean_iter, clean_iter, clean_iter, clean_iter, clean_iter):
#          print(f'{joined_tuple=}')
#          joined_list = list(joined_tuple)
#          #  print(f'{joined_list=}')
#          #  joined_list[0] = joined_list[0].strip()
#          #  joined_list.append(joined_list[1].strip())
#          #  joined_list[1] = "\t"
#          joined_list.append("\n")
#          print(f'{joined_list=}')
#          joined_str = "\t".join(joined_list)
#          print(f'{joined_str=}')
#          formatted_str = joined_str.replace(' \t', '\t')
#          formatted_str = formatted_str.replace('(', '\t')
#          formatted_str = formatted_str.replace(')', '')
#          formatted_str = formatted_str.replace(u'\xa0', u'')
#          formatted_str = formatted_str.replace('/', '\t')
#          formatted_str = formatted_str.replace('\t\n', '\n')
#          print(f'{formatted_str=}')
#          #  print(formatted_str)
#          csvfile.write(formatted_str)
#
#  with open('zstats_rankings_7.raw', 'r') as rawfile, open('zstats_rankings_7.csv', 'w') as csvfile:
#      data = rawfile.readlines()
#      #  for line in data:
#          #  line = line.strip()
#          #  line = line.replace(' \t', '\t')
#          #  print(line)
#
#      #  lines_iter = iter(rawfile)
#      clean_data = []
#      lines_iter = iter(data)
#      for line in lines_iter:
#          if line[0] != 'R':
#              clean_data.append(line.strip())
#
#      #  csvfile.write("""0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23\t24\t25\t26\t27\t28\n""")
#      csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tzFG%\tFT%\tFTM\tFTA\tzFT%\t3PM\tz3PM\tPTS\tzPTS\tREB\tzREB\tAST\tzAST\tSTL\tzSTL\tBLK\tzBLK\tTO\tzTO\tTOTAL\n""")
#      #  csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tFT%\tFTM\tFTA\t3PM\tPTS\tTREB\tAST\tSTL\tBLK\tTO\tTOTAL\tzFG%\tzFT%\tz3PM\tzPTS\tzREB\tzAST\tzSTL\tzBLK\tzTO\n""")
#      clean_iter = iter(clean_data)
#      for joined_tuple in zip(clean_iter, clean_iter, clean_iter, clean_iter, clean_iter,
#                              clean_iter, clean_iter, clean_iter, clean_iter, clean_iter):
#          print(f'{joined_tuple=}')
#          joined_list = list(joined_tuple)
#          #  print(f'{joined_list=}')
#          #  joined_list[0] = joined_list[0].strip()
#          #  joined_list.append(joined_list[1].strip())
#          #  joined_list[1] = "\t"
#          joined_list.append("\n")
#          print(f'{joined_list=}')
#          joined_str = "\t".join(joined_list)
#          print(f'{joined_str=}')
#          formatted_str = joined_str.replace(' \t', '\t')
#          formatted_str = formatted_str.replace('(', '\t')
#          formatted_str = formatted_str.replace(')', '')
#          formatted_str = formatted_str.replace(u'\xa0', u'')
#          formatted_str = formatted_str.replace('/', '\t')
#          formatted_str = formatted_str.replace('\t\n', '\n')
#          print(f'{formatted_str=}')
#          #  print(formatted_str)
#          csvfile.write(formatted_str)
