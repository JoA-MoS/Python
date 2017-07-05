

def draw_stars(a):
    for i in range(0, len(a)):
        cur_type = type(a[i])
        if cur_type is int:
            print '*' * a[i]
        if cur_type is str:
            print a[i][0].lower() * len(a[i])


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
