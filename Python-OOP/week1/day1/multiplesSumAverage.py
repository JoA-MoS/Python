def odds():
    for i in range(1, 1000, 2):
        print i


def multiples(mult, maxNum):
    x = 1
    r = 0
    while r < maxNum:
        r = x * mult
        print r
        x += 1


def mean(arr):
    return (sum(arr) / (len(arr) + 0.0))


odds()
multiples(5, 100)

a = [1, 2, 5, 10, 255, 6]

print sum(a)
print mean(a)
