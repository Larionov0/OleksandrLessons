names = ['alex', 'bob', 'anna', 'innokentiy', 'katia', 'vasya']


max_name = ''
max_count = 0


for name in names:
    if len(name) > max_count:
        max_count = len(name)
        max_name = name

print(max_count, max_name)
