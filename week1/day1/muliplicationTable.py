def multiplicationTable(start, end):
    for i in range(start, end):
        if i == start:
            line = 'x\t'
            for j in range(start, end):
                line += str(j) + '\t'
            print line

        line = str(i) + '\t'
        for j in range(start, end):
            line += str(i * j) + '\t'
        print line


multiplicationTable(5, 10)
