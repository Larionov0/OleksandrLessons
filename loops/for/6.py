lst = [6, 1, 2, 7, 7, 1, 6, 4, 6, 5, 9, 4, 6, 5, 3, 5, 4, 4, 9, 3]


for i, number in enumerate(lst):
    if i % 3 == 2:
        lst[i] = 0
        print(number)


print(lst)
