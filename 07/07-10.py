step = int(input())
text = input()
result = ''
p = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
for char in list(text.lower()):
    if char in p:
        pos = p.find(char) + step
        if pos >= len(p):
            pos -= len(p)
        result += p[pos]
    else:
        result += char
print(result)