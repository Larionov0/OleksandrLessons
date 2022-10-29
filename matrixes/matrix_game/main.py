from os import system
import msvcrt
import random


n = 14
m = 16

hero_sprite = 'x'

hero_i = 3
hero_j = 5


animals = [
    ['chicken', 10, 7, 7, 'c'],
    ['chicken', 10, 9, 7, 'c'],
    ['chicken', 10, 7, 8, 'c'],
]


while True:
    # create matrix
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append('-')
        matrix.append(row)

    matrix[hero_i][hero_j] = hero_sprite

    for animal in animals:
        i = animal[2]
        j = animal[3]
        sprite = animal[4]

        matrix[i][j] = sprite

    # clear screen
    system('cls')

    # show matrix
    string = ''
    for i in range(len(matrix)):
        string += '|'
        for j in range(len(matrix[0])):
            string += f"{matrix[i][j]} "
        string = string[:-1] + '|\n'
    print(string)

    print('WASD: ')
    choice = msvcrt.getch().decode()
    if choice == 'w':
        if hero_i != 0:
            hero_i -= 1
    elif choice == 'a':
        if hero_j != 0:
            hero_j -= 1
    elif choice == 's':
        if hero_i != n - 1:
            hero_i += 1
    elif choice == 'd':
        if hero_j != m - 1:
            hero_j += 1

    for animal in animals:
        if animal[0] == 'chicken':
            dir = random.choice(['w', 'a', 's', 'd'])
            if dir == 'w':
                if animal[2] != 0:
                    animal[2] -= 1
            elif dir == 'a':
                if animal[3] != 0:
                    animal[3] -= 1
            elif dir == 's':
                if animal[2] != n - 1:
                    animal[2] += 1
            elif dir == 'd':
                if animal[3] != m - 1:
                    animal[3] += 1
