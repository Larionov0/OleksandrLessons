from os import system
import msvcrt
import random


n = 14
m = 16

hero_sprite = 'x'

hero_i = 3
hero_j = 5
hero_coins = 0


animals = [
    ['chicken', 10, 7, 7, 'c'],
    ['chicken', 10, 9, 7, 'c'],
    ['chicken', 10, 7, 8, 'c'],
]

turn_number = 0

while True:
    turn_number += 1
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
    print(f'Your coins: {hero_coins}')
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

    i = 0
    while i < len(animals):
        animal = animals[i]
        animal_i, animal_j = animal[2], animal[3]
        if animal_i == hero_i and animal_j == hero_j:
            if animal[0] == 'chicken':
                hero_coins += 3
                animals.pop(i)
                i -= 1
        i += 1

    # alternative

    # alive_animals = []
    # for animal in animals:
    #     animal_i, animal_j = animal[2], animal[3]
    #     if animal_i == hero_i and animal_j == hero_j:
    #         if animal[0] == 'chicken':
    #             hero_coins += 3
    #     else:
    #         alive_animals.append(animal)
    # animals = alive_animals

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

    i = 0
    while i < len(animals):
        animal = animals[i]
        animal_i, animal_j = animal[2], animal[3]
        if animal_i == hero_i and animal_j == hero_j:
            if animal[0] == 'chicken':
                hero_coins += 3
                animals.pop(i)
                i -= 1
        i += 1

    # spawn
    if turn_number % 6 == 0:
        animals.append(['chicken', 10, random.randint(0, n - 1), random.randint(0, m - 1), 'c'])

