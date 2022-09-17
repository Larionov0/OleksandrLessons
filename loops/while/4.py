age = 10

while True:
    print('You are ' + str(age))
    print('1 - grow up')
    print('2 - try to enter')
    print('3 - go out')

    c = input('Your choice: ')
    if c == '1':
        age += 1
        print('You grew up for 1 year')
    elif c == '2':
        if age >= 18:
            print('You are welcome')
            break
        else:
            print('You are young')
    elif c == '3':
        print('You went out')
        break
    else:
        print('Wrong choice')
