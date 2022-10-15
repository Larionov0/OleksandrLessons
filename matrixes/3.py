matrix = [
    [1, 4, 2],
    [5, 6, 1],
    [8, 3, 1],
    [7, 3, 6]
]

# Найти суму всех елементов матрицьі
s = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        s += matrix[i][j]
print(s)
