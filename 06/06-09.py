Holodilnik = set()
Ing_rec = set()

for i in range(int(input())):
    p = input()
    Holodilnik.add(p)
for i in range(int(input())):
    recipe = input()
    ingredients = int(input())
    for ingredientes in range(ingredients):
        peremennaya = input()
        Ing_rec.add(peremennaya)
    if Ing_rec <= Holodilnik:
        print(recipe)

