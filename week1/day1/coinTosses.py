import random


def coin_tosses(num):
    str_template = 'Attempt #{}: Throwing a coin... It\'s a {}! ... Got {} head(s) so far and {} tail(s) so far'
    tails_heads = ('tails', 'heads')
    results = [0, 0]
    for i in range(1, num + 1):
        toss = int(round(random.random()))
        results[toss] += 1
        print str_template.format(i, tails_heads[toss], results[1], results[0])


coin_tosses(5000)
