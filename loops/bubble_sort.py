lst = [6, 1, 2, 7, 7, 1, 6, 4, 6, 5, 9, 4, 6, 5, 3, 5, 4, 4, 9, 3]


ogr = len(lst) - 1
while ogr > 0:
    i = 0
    while i < ogr:
        if lst[i + 1] < lst[i]:
            # temp = lst[i]
            # lst[i] = lst[i + 1]
            # lst[i + 1] = temp
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
        i += 1
    ogr -= 1


print(lst)
