age = int(input('Your age: '))

# if age >= 18:
#     print('You are old')
#     print(':)')
#     if age > 80:
#         print('You are too old')
# else:
#     print('You are small!')


if 80 > age >= 18:
    print('You are old')
elif age >= 80:
    print('You are too old')
else:
    print('You are small!')
