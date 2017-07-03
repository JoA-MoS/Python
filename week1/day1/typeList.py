def typeList(lst):
    # 0 if empty 1 if integers 2 if strings 3 if mixed
    types = 0
    lstSum = 0
    lstStr = ''
    lstType = ''
    for x in lst:
        curType = type(x)
        if curType is int or curType is float:
            lstSum += x
            if types <= 1:
                types = 1
            elif types >= 2:
                types = 3
        if curType is str:
            lstStr += x
            if types == 0 or types == 2:
                types = 2
            elif types == 1 or types == 3:
                types = 3
    if types == 0:
        print 'Empty List'
    if types == 1:
        print 'Integer List'
        print lstSum
    if types == 2:
        print 'String List'
        print lstStr
    if types == 3:
        print 'Mixed List'
        print lstSum
        print lstStr


l = ['magical unicorns', 19, 'hello', 98.98, 'world']
typeList(l)
l = [2, 3, 1, 7, 4, 12]
typeList(l)
l = ['magical', 'unicorns']
typeList(l)
l = []
typeList(l)
