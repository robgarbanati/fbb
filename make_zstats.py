with open('zstats.raw', 'r') as rawfile, open('zstats.csv', 'w') as csvfile:
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
    csvfile.write("""PLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\tFGM\tFGA\tFT%\tFTM\tFTA\t3PM\tPTS\tTREB\tAST\tSTL\tBLK\tTO\tTOTAL\tzFG%\tzFT%\tz3PM\tzPTS\tzREB\tzAST\tzSTL\tzBLK\tzTO\n""")
    clean_iter = iter(clean_data)
    for joined_tuple in zip(clean_iter, clean_iter):
        print(joined_tuple)
        joined_list = list(joined_tuple)
        joined_list[0] = joined_list[0].strip()
        joined_list.append(joined_list[1].strip())
        joined_list[1] = "\t"
        joined_list.append("\n")
        joined_str = "".join(joined_list)
        formatted_str = joined_str.replace(' \t', '\t')
        formatted_str = formatted_str.replace('(', '\t')
        formatted_str = formatted_str.replace(')', '')
        formatted_str = formatted_str.replace(u'\xa0', u'')
        formatted_str = formatted_str.replace('/', '\t')
        print(formatted_str)
        csvfile.write(formatted_str)

        # now change the 2nd line, note that you have to add a newline
        #  data[1] = 'Mage\n'
        #  print(data)
        #  csvfile.writelines(data)

