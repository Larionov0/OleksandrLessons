lst = [1, 5, 3, 7, 6, 8, 4, 8, 4, 3, 8]


count = 0

# i = 0
# while i < len(lst):
#     print(i, '-', lst[i])
#     i += 1


for el in lst:
    if el < 5:
        count += 1

print(count)
