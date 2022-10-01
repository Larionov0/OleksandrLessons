lst = ["Ваня", "Петя", "Маша", "Саша", "Паша", "Даша"]
print(lst)
a = int(input("position of name: "))
b = input("Enter name: ")
lst.pop(a)
lst.insert(a, b)
print(lst)
