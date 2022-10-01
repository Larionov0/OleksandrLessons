lst = [6, 1, 2, 7, 7, 1, 6, 4, 6, 5, 9, 4, 6, 5, 3, 5, 4, 4, 9, 3]


# i = 0
# while i < len(lst):
#     lst[i] = lst[i] + 1
#     i += 1

# i = 0
# for number in lst:
#     lst[i] = number + 1
#     i += 1

for i, number in enumerate(lst):
    lst[i] = number + 1

print(lst)
