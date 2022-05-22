a = int(input())
b = int(input())
a += b
class1 = set()
class2 = set()
for i in range(a):
    student = input()
    if student in class1:
        class1.remove(student)
        class2.add(student)
    else:
        class1.add(student)
if len(class1) <=0:
    print("NO")
else:
    print(len(class1))
