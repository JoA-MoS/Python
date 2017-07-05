def odd_even(start, end, cb):
    for i in range(start, end + 1):
        cb(i)


def printOddEven(i):
    outStr = 'Number is {}.  This is an {} number.'
    if i % 2:
        print outStr.format(i, 'odd')
    else:
        print outStr.format(i, 'even')


def map(arr, cb):
    mapped = []
    for i in range(0, len(arr)):
        mapped.append(cb(arr[i]))
    return mapped


def multiply(v):
    return v * 5


def layered(v):
    return [1] * v


odd_even(1, 2000, printOddEven)

a = [2, 4, 10, 16]

print map(a, multiply)
print map(a, layered)
