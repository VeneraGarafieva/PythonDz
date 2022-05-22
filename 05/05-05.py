popitka = int(input())
count = 1
for i in range(popitka):
    text = input()
    if not ("Кот" in text or "кот" in text):
        count += 1
    if "Кот" in text or "кот" in text:
        break   
    if text == 'СТОП':
        break
else:
    print(-1)
print(count)