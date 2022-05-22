popitka = ''
count_cats = 0
count = 0
while popitka != 'СТОП':
    text = input()
    if text == 'СТОП':
        break
    if not ("Кот" in text or "кот" in text):
        count += 1    
    if "Кот" in text or "кот" in text:
        count_cats += 1
else:
    print(-1)
if count_cats == 0:
    print(count_cats, -1)