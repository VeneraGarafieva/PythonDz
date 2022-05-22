count_cats = 0
popitka = int(input())
for i in range(popitka):
    text = input()
    if "Кот" in text or "кот" in text:
        count_cats += 1
    if "Пёс" in text or "пёс" in text:
        count_cats -= 1
if count_cats <= 0:
    print("НЕТ")
else:
    print("МЯУ")