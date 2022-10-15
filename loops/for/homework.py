lst = 'яблоки как ватрушки'
lst_1 = 'яблуки вам не ватрушк и'
i = 0
l1 = len(lst)
l2 = len(lst_1)
while i < max(l1, l2):
    if i < l1:
        letter1 = lst[i]
    else:
        letter1 = ' '

    if i < l2:
        letter2 = lst_1[i]
    else:
        letter2 = ' '

    sign = ' ' if letter1 == letter2 else '-'
    print(letter1 + sign + letter2)
    i += 1
