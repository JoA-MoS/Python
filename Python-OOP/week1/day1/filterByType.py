def isItBig(num):
    if num >= 100:
        return 'That\'s a big number!'
    return 'That\'s a small number'


def isItLong(str):
    if len(str) >= 50:
        return 'long sentence'
    return 'short sentence'


def isItLongList(lst):
    if len(lst) >= 10:
        return 'Big List'
    return 'Short List'


def tester(val):
    t = type(val)
    if t is int:
        return isItBig(val)
    if t is str:
        return isItLong(val)
    if isinstance(val, list):
        return isItLongList(val)
    return 'Unsupported Type'


sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1, 7, 4, 21]
mL = [3, 5, 7, 34, 3, 2, 113, 65, 8, 89]
lL = [4, 34, 22, 68, 9, 13, 3, 5, 7, 9, 2, 12, 45, 923]
eL = []
spL = ['name', 'address', 'phone number', 'social security number']


print tester(sI)
print tester(mI)
print tester(bI)
print tester(eI)
print tester(spI)

print tester(sS)
print tester(mS)
print tester(bS)
print tester(eS)

print tester(aL)
print tester(mL)
print tester(lL)
print tester(eL)
print tester(spL)
