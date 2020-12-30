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

    csvfile.write("""R\tPLAYER\tPOS\tTEAM\tGP\tMPG\tFG%\FGM\ttFGA\tFT%\tFTM\tFTA\t3PM\tPTS\tTREB\tAST\tSTL\tBLK\tTO\tTOTAL\tzFG%\tzFT%\tz3PM\tzPTS\tzREB\tzAST\tzSTL\tzBLK\tzTO\n""")
    clean_iter = iter(clean_data)
    for joined_tuple in zip(clean_iter, clean_iter):
        joined_list = list(joined_tuple)
        joined_list.append("\n")
        joined_str = "\t".join(joined_list)
        formatted_str = joined_str.replace(' \t', '\t')
        formatted_str = formatted_str.replace('(', '\t')
        formatted_str = formatted_str.replace(')', '')
        formatted_str = formatted_str.replace('/', '\t')
        print(formatted_str)
        csvfile.write(formatted_str)

        # now change the 2nd line, note that you have to add a newline
        #  data[1] = 'Mage\n'
        #  print(data)
        #  csvfile.writelines(data)

