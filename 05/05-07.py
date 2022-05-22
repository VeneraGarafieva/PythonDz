decrees = int(input())
in_war = 'Евразия'
in_peace = 'Остазия'
for i in range(decrees):
    command = input()
    if command == 'С кем война?':
        print(in_war)
    if command == 'С кем мир?':
        print(in_peace)
    if command == 'Меняем':
        in_war, in_peace = in_peace, in_war
