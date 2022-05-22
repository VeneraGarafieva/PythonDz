popitka = ''
count = 1
while popitka != 'СТОП':
    text = input()
    if not ("Кот" in text or "кот" in text):
        count += 1
    if "Кот" in text or "кот" in text:
        print(count)
else:
    print(-1)
