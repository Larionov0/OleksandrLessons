lst = ["Sasha", "Vasya", "Petya", "Ivan", "Katia"]


# количество имен, в которьіх есть буква y

count = 0

i = 0
while i < len(lst):
    if 'v' in lst[i] or 'V' in lst[i]:
        count += 1
    i += 1

print(count)
