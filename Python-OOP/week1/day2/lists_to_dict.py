name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider",
                   "giraffe", "ticks", "dolphins", "llamas", "goats"]


def make_dict(arr1, arr2):
    new_dict = {}
    long_arr = arr1
    short_arr = arr2
    if arr1 <= arr2:
        long_arr = arr2
        short_arr = arr1
    for i in range(len(long_arr)):
        if i < len(short_arr):
            new_dict[long_arr[i]] = short_arr[i]
        else:
            new_dict[long_arr[i]] = None

    return new_dict


print make_dict(name, favorite_animal)
