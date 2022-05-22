popitka = int(input())

for i in range(popitka):
    text = input()
    if "Кот" in text or "кот" in text:
        print("«МЯУ»")
        break
else:
    print("НЕТ")

