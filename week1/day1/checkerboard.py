def checkerboard(x, y):
    for i in range(0, y):
        line = ''
        shift = i % 2
        for j in range(0, x):
            j = j - shift
            # print str(j) + ' - ' + str(j % 2)
            if j % 2:
                line += '*'
            else:
                line += ' '
        print line


checkerboard(12, 12)
