profile = {
    'name': 'Justin',
    'age': 34,
    'country_of_birth': 'USA',
    'favorite_language': 'C#',
}


def print_dic(dic, cb):
    for key in dic:
        print cb(key, dic[key])


def key_val_format(k, v):
    return 'My {} is {}'.format(k.replace('_', ' '), str(v))


print_dic(profile, key_val_format)
