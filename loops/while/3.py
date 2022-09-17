# Пользователь вводит имена до тех пор, пока не напишет СТОП
# Програма должна вьівести количество имен, длина которьіх больше 5


count = 0
while True:
    name = input('Name: ')
    if name == 'STOP':
        break

    if len(name) > 5:
        count += 1


print(count)
