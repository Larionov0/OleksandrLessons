matrix = [
    [1, 4, 2],
    [5, 6, 1],
    [8, 3, 1],
    [7, 3, 6]
]

# вьівести сумму чисел n ряда
i = 1

s = 0
j = 0
while j < len(matrix[0]):
    s += matrix[i][j]
    j += 1


print(s)

