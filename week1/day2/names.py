students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

users = {
    'Students': [
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}


def print_object(obj, formatter):
    o_type = type(obj)
    if o_type is list:
        for i in obj:
            print formatter(i)
    elif o_type is dict:
        for i in obj:
            print i
            print formatter(obj[i])


def name_formatter(user):
    return '{} {}'.format(user['first_name'], user['last_name'])


def part2_formatter(obj):
    counter = 0
    out = ''
    for i in obj:
        # print i
        full_name = name_formatter(i)
        counter += 1
        out += '{} - {} - {}\r\n'.format(counter,
                                         full_name, len(full_name) - 1)
    return out[:-1]


print_object(students, name_formatter)

print_object(users, part2_formatter)
