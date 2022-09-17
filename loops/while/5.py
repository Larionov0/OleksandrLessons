info = '>>'


while True:
    print(info + '\n')
    print('1 - add arrow')
    print('2 - remove arrow')
    print('3 - add n arrows')
    print('4 - remove n arrows')
    print('5 - count arrows')
    print('6 - clear arrows')
    print('7 - exit')

    choice = input("Your choice: ")

    if choice == '1':
        info = info + '>'
    elif choice == '2':
        info = info[0:-1]
    elif choice == '3':
        n = int(input('n = '))
        info = info + n * '>'
    elif choice == '4':
        n = int(input('n = '))
        info = info[:-n]
    elif choice == '5':
        print(len(info))
    elif choice == '6':
        info = ''
    elif choice == '7':
        exit()
    print('\n\n')
