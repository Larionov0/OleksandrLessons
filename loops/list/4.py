marks = []


while True:
    good_students_amount = 0
    marks_sum = 0
    max_ = 0
    min_ = 101

    i = 0
    while i < len(marks):
        if marks[i] >= 90:
            good_students_amount += 1

        marks_sum = marks_sum + marks[i]

        if marks[i] > max_:
            max_ = marks[i]

        if marks[i] < min_:
            min_ = marks[i]

        i += 1

    print('\n\n\nMain menu\n'
          'Good students: ' + str(good_students_amount))
    print("Average mark: " + str((marks_sum / len(marks)) if len(marks) > 0 else 0))
    print("Max mark: " + str(max_))
    print("Min mark: " + str(min_ if min_ != 101 else 0))

    print(marks)
    print('1 - add numbers')
    print('2 - delete marks')
    print('3 - clear marks')
    print('4 - exit')

    choice = input('Your choice: ')
    if choice == '1':
        while True:
            print(marks)
            mark = input('Input mark: ')
            if mark == 'stop' or mark == 'STOP':
                break
            else:
                if mark.isdigit():
                    if 0 < int(mark) <= 100:
                        marks.append(int(mark))
                    else:
                        print('MARK MUST BE BETWEEN 1 AND 100!')
                else:
                    print('NOT INTEGER!')
    elif choice == '2':
        cursor_i = 0
        while True:
            if len(marks) == 0:
                break

            print('\n\n')
            print(marks)
            sym_sum = 0
            i = 0
            while i < cursor_i:
                sym_sum += 2 + len(str(marks[i]))
                i += 1
            print(' ' * (1 + sym_sum) + '^')

            print('a - left')
            print('d - right')
            print('s - delete')
            print('b - back')
            choice = input('Choice: ')
            if choice == 'a':
                if cursor_i != 0:
                    cursor_i -= 1
            elif choice == 'd':
                if cursor_i != len(marks) - 1:
                    cursor_i += 1
            elif choice == 's':
                marks.pop(cursor_i)
                if cursor_i == len(marks):
                    cursor_i -= 1
            elif choice == 'b':
                break

    elif choice == '3':
        marks.clear()
    elif choice == '4':
        exit()
    else:
        pass
