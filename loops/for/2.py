names = ['alex', 'bob', 'anna', 'katia', 'vasya']

# посчитать количество имен, последняя буква которьіх входит в множество a, x, g, d, f

letters = ['a', 'x', 'g', 'd', 'f']
# letters = 'axgdf'
c = 0
for name in names:
    if name[-1] in letters:
        c += 1


print(c)
