matrix = [
    [1, 4, 2],
    [5, 6, 1],
    [8, 3, 1],
    [7, 3, 6]
]


# вьівести на екран матрицу

string = ''
for i in range(len(matrix)):
    string += '|'
    for j in range(len(matrix[0])):
        string += f"{matrix[i][j]} "
    string = string[:-1] + '|\n'

print(string)
