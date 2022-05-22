a = int(input())
cities = []
for i in range(a):
    cities.append(str(input()))
new_city = input()
if new_city in set(cities):
    print("TRY ANOTHER")
else: 
    print("OK")