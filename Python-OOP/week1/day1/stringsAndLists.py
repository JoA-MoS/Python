words = 'It\'s thanksgiving day. It\'s my birthday,too!'
print words.find('day')
print words.replace('day', 'month')

x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()


x.insert(0, x[0:len(x) / 2])
del x[1:(len(x) / 2)]

print x
