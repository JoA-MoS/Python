def compareArrays(arr1, arr2):
    if arr1 == arr2:
        return 'The lists are the same.'
    return 'The lists are not the same.'


list_one = [1, 2, 5, 6, 2]
list_two = [1, 2, 5, 6, 2]
print compareArrays(list_one, list_two)
list_one = [1, 2, 5, 6, 5]
list_two = [1, 2, 5, 6, 5, 3]
print compareArrays(list_one, list_two)
list_one = [1, 2, 5, 6, 5, 16]
list_two = [1, 2, 5, 6, 5]
print compareArrays(list_one, list_two)
list_one = ['celery', 'carrots', 'bread', 'milk']
list_two = ['celery', 'carrots', 'bread', 'cream']
print compareArrays(list_one, list_two)
