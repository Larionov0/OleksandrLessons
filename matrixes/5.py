matrix = [
    [0, 1, 4, 2],
    [3, 5, 6, 1],
    [2, 8, 3, 1],
    [8, 7, 3, 6]
]


# вьівести столбец,  сумма чисел которого максимальная
max_s = float('-inf')  # минус бесконечность
max_j = -1
for j in range(len(matrix[0])):
    s = 0
    for i in range(len(matrix)):
        s += matrix[i][j]

    if s > max_s:
        max_s = s
        max_j = j


for i in range(len(matrix)):
    print(matrix[i][max_j])
print(f'Sum: {max_s}\nj: {max_j}')
