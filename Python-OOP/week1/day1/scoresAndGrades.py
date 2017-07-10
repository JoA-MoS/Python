import random


def grades(criteria):
    print 'Scores and Grades'
    for i in range(10):
        print criteria(random.randint(60, 100))
    print 'End of the program Bye!'


def testCriteria(score):
    respTemp = 'Score: {}; Your grade is {}'
    grade = ''
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    return respTemp.format(grade, score)


grades(testCriteria)
