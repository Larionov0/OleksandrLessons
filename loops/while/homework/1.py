a = int(input())
b = int(input())

action = 1 if b > a else -1

while action * (b - a) > 0:
    print(a)
    a += action
