a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = str(input("Введите оператор(+,-,*,-)"))

if c == "/":
    if a == 0 or b == 0:
        print("88888")
    else:
        print(a/b)
elif c == "*":
    print(a*b)
elif c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
else:
    print("88888")
