import re
def make_csv_from_raw(raw_file, csv_file):
    #  with open('zstats.raw', 'r') as rawfile, open('zstats.csv', 'w') as csvfile:
    with open(raw_file, 'r') as rawfile, open(csv_file, 'w') as csvfile:
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
        #  for joined_tuple in zip(clean_iter):
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
            #  rx = re.compile(['[1-0]+a-zA-Z]')
            rx = re.compile(' +[0-9]+\t+')
            #  rx = re.compile(' +')
            #  formatted_str = joined_str.replace(' \t', '\t')
            subbed_str = re.sub(rx, '\t', joined_str, 1)
            print(f"{subbed_str=}")
            formatted_str = subbed_str.replace(' \t', '\t')
            print(f"{formatted_str=}")
            formatted_str = formatted_str.replace('\tJr', ' Jr')
            print(f"jr replace: {formatted_str=}")
            formatted_str = formatted_str.replace('(', '\t')
            print(f"{formatted_str=}")
            #  formatted_str = formatted_str.replace(')', '')
            formatted_str = formatted_str.replace(')', '\t')
            print(f"{formatted_str=}")
            formatted_str = formatted_str.replace(u'\xa0', u'')
            print(f"{formatted_str=}")
            formatted_str = formatted_str.replace('/', '\t')
            print(f"{formatted_str=}")
            formatted_str = formatted_str.replace('\t\n', '\n')
            print(f"{formatted_str=}")
            formatted_str = formatted_str.replace('Jr.', 'Jr')
            print(f"{formatted_str=}")
            formatted_str = formatted_str.replace(' III', '')
            print(f"{formatted_str=}")
            formatted_str = formatted_str.replace('P.J.', 'PJ')
            print(f"{formatted_str=}")
            #  formatted_str = '\t'.join(formatted_str.rsplit(' ', 7))
            #  print(f"{formatted_str=}")
            #  index = formatted_str.rfind('\t')
            #  print(f'{index=}')
            #  formatted_str = formatted_str.replace(' ', '')
            #  formatted_str = formatted_str.strip()
            print(f'{formatted_str=}')
            #  print(formatted_str)
            csvfile.write(formatted_str)



make_csv_from_raw('zstats.raw', 'zstats.csv')
make_csv_from_raw('zstats_rankings.raw', 'zstats_rankings.csv')
make_csv_from_raw('zstats_rankings_14.raw', 'zstats_rankings_14.csv')
make_csv_from_raw('zstats_rankings_7.raw', 'zstats_rankings_7.csv')



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
