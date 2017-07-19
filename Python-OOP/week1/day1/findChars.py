def findChars(arr, char):
    out = []
    for w in arr:
        if w.find(char) >= 0:
            out.append(w)
    return out


word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'

print findChars(word_list, char)
