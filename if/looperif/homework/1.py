a = int(input("Число 1: "))
b = int(input("Число 2: "))
c = int(input("Число 3: "))
d = int(input("Число 4: "))
cnt = 0
if a < 0:
    cnt = cnt + 1
if b < 0:
    cnt = cnt + 1
if c < 0:
    cnt = cnt + 1
if d < 0:
    cnt = cnt + 1
print(cnt)
