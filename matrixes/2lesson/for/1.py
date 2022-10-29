matrix = [
    [0, 1, 4, 2],
    [3, 5, 6, 1],
    [2, 8, 3, 1],
    [8, 7, 3, 6]
]


max_ = -float('inf')

for row in matrix:
    for num in row:
        if num > max_:
            max_ = num


print(max_)
