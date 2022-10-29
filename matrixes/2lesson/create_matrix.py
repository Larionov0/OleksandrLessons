# Создать матрицу с заданньіми параметрами

n = 3
m = 4
symbol = '-'


# create matrix
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(symbol)
    matrix.append(row)

# matrix = [[symbol for j in range(m)] for i in range(n)]


# show matrix
string = ''
for i in range(len(matrix)):
    string += '|'
    for j in range(len(matrix[0])):
        string += f"{matrix[i][j]} "
    string = string[:-1] + '|\n'
print(string)
