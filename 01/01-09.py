print("Введите ваш логин:")
a = input()
print("Введите ваш резервный email:")
b = input()
if "@" in a and not "@" in b:
    print("Вы ввели некоретный логин и email!")
elif not "@" in b:
    print("Вы ввели некорректный email!")
elif "@" in a:
    print("Вы ввели некорректный логин!")
else:
    print("OK")
