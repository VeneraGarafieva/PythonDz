array1 = set()
array2 = set()
while True:
   a = input()
   if a == "": break
   array1.add(int(a))
while True:
   a = input()
   if a == "": break
   array2.add(int(a))
array3 = array1 & array2
if array3:
   print(*array3, sep="\n")
else:
   print("EMPTY")