# -*- coding: utf-8 -*-


def checkerboard(x, y, char='*', delim=' '):

    for i in range(0, y):
        line = ''
        shift = i % 2
        for j in range(0, x):
            j = j - shift
            if j % 2:
                line += char
            else:
                line += delim
        print line


checkerboard(50, 50, u'█')
