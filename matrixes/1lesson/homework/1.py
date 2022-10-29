matrix = [
    [1, 4, 3],
    [1, 5, 2],
    [3, 2, 4]
]
string = ''
n = int(input('Введите ряд'))
for j in range(len(matrix[0])):
    matrix[n][j] = 0


string = ''
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        string += f"{matrix[i][j]} "
    string = string[:-1] + '\n'
print(string)
