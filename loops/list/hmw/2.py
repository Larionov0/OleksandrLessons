list_1 = [1, 4, 3, 3, 2, 5, 6, 6]
list_2 = []
i = 0
while i < len(list_1):
    if i % 2 == 0:
        list_2.append(0)
    else:
        list_2.append(list_1[i] * 2)
    i += 1
print(list_2)
