spisok = ["Саша", "Игорь", "Яна", "Кукуруз"]
spisok1 = [70, 80, 50, 187]

# i = 0
# while i < len(spisok):
#     spisok2.append(str(spisok1[i]) + " - " + str(spisok[i]))
#     i += 1

# i = 0
# for name in spisok:
#     print(str(spisok1[i]) + '-' + name)
#     i += 1

# for i, name in enumerate(spisok):
#     print(str(spisok1[i]) + '-' + name)

# for i in range(len(spisok)):
#     print(str(spisok1[i]) + '-' + spisok[i])

for name, mass in zip(spisok, spisok1):
    # print(str(mass) + '-' + name + '!')
    print(f'{mass} - {name}!')
