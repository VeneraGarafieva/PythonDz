p = int(input())
n = int(input())
owned_set = set()
need_set = set()
for i in range(p):
    owned_set.add(input())
for i in range(n):
    need_set.add(input())
for i in need_set:
    if i in owned_set:
        print("YES")
    else:
        print("NO")