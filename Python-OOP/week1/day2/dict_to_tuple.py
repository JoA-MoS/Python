def dict_to_tuple(dic):
    lst_tup = []
    for i in dic:
        lst_tup.append((i, dic[i]))
    return lst_tup


my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}

print dict_to_tuple(my_dict)
