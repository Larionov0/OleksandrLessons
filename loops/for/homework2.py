lst = 'яблоки как ватрушки'
lst_1 = 'яблуки вам не ватрушки'
i = 0
l1 = len(lst)
l2 = len(lst_1)

if l1 > l2:
    lst_1 += ' ' * (l1 - l2)
else:
    lst += ' ' * (l2 - l1)

while i < max(l1, l2):
    if lst[i] == lst_1[i]:
        print(lst[i] + ' ' + lst_1[i])
    else:
        print(lst[i] + '-' + lst_1[i])
    i += 1
