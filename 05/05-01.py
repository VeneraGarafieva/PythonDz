a = int(input("Введите первое число "))
b = int(input("Введите второе число "))

if a < b:
    for i in range(a,b+1):
        if not i % 3 and not i % 5:
            print("FizzBuzz")
        elif not i % 3:
            print("Fizz")
        elif not i % 5:
            print("Buzz")
        else:
            print(i)
else:
    print("Error")

