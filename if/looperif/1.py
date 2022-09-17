n1 = int(input('Number: '))
n2 = int(input('Number: '))
n3 = int(input('Number: '))
n4 = int(input('Number: '))
n5 = int(input('Number: '))


# Count numbers > 5
c = 0

if n1 > 5:
    c = c + 1
if n2 > 5:
    c = c + 1
if n3 > 5:
    c = c + 1
if n4 > 5:
    c = c + 1
if n5 > 5:
    c += 1

print(c)
