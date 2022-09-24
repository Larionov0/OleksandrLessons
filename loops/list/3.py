# Пользователь вводит список оценок студентов в группе за семестр.
# Программа  должна вьівести максимальную оценку, среднюю и минимальную,
# а также посчитать количество отличников (90-100)


marks = []

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


good_students_amount = 0
marks_sum = 0
max_ = 0
min_ = 100

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


print('Good students: ' + str(good_students_amount))
print("Average mark: " + str(marks_sum / len(marks)))
print("Max mark: " + str(max_))
print("Min mark: " + str(min_))
