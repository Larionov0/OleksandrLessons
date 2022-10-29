matrix = [
    [0, 1, 4, 2],
    [3, 5, 6, 1],
    [2, 8, 3, 1],
    [8, 7, 3, 6]
]


# max_j = 0
# max_s = 0
#
# for j in range(len(matrix[0])):
#     s = 0
#     for row in matrix:
#         s += row[j]
#
#     if s > max_s:
#         max_s = s
#         max_j = j
#
#
# for row in matrix:
#     print(row[max_j])


max_row = []
max_s = 0
for row in matrix:
    s = 0
    for num in row:
        s += num

    if s > max_s:
        max_s = s
        max_row = row

print(max_row)
