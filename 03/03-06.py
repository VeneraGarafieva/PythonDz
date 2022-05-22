a = input()
b = input()
while len(a) < 8:
    print("Короткий")
    a = input()
    b = input()
while "123" in a:
    print("Простой")
    a = input()
    b = input()
while b != a:
    print("Различаются")
    a = input()
    b = input()
else:
    print("OK")
