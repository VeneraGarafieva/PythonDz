slovo = input()
while True:
    p = input()
    if slovo[-1] == p[0]:
        slovo = p
        continue
    else:
        print(p)
        break