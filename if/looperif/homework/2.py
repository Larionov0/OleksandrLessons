n1 = input("name 1: ")
n2 = input("name 2: ")
n3 = input("name 3: ")
n4 = input("name 4: ")
n5 = input("name 5: ")
n6 = input("name 6: ")
big = 0
avg = 0
small = 0


if len(n1) >= 10:
    big = big + 1
elif len(n1) >= 5:
    avg = avg + 1
else:
    small = small + 1

if len(n2) >= 10:
    big = big + 1
if 9 <= len(n2) >= 5:
    avg = avg + 1
if len(n2) < 5:
    small = small + 1

if len(n3) >= 10:
    big = big + 1
if 9 <= len(n3) >= 5:
    avg = avg + 1
if len(n3) < 5:
    small = small + 1

if len(n4) >= 10:
    big = big + 1
if 9 <= len(n4) >= 5:
    avg = avg + 1
if len(n4) < 5:
    small = small + 1

if len(n5) >= 10:
    big = big + 1
if 9 <= len(n5) >= 5:
    avg = avg + 1
if len(n5) < 5:
    small = small + 1

if len(n6) >= 10:
    big = big + 1
if 9 <= len(n6) >= 5:
    avg = avg + 1
if len(n6) < 5:
    small = small + 1

print(str(big) + " больших;" + str(avg) + " срених;" + str(small) + " маленьких")
