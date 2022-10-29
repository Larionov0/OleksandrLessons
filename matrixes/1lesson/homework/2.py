matrix = [
    [0, 1, 4, 2],
    [3, 5, 6, 1],
    [2, 8, 3, 1],
    [8, 7, 3, 6],
]
max_s = float('-inf')
max_i = -1
for i in range(len(matrix)):
    s = 0
    for j in range(len(matrix[0])):
        s += matrix[i][j]
    if s > max_s:
        max_s = s
        max_i = i

for j in range(len(matrix[0])):
    print(matrix[max_i][j])
print(f'Sum: {max_s}\nj: {max_i}')
