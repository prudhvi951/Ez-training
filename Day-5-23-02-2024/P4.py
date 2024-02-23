#check is numeric or not
#1
n = input()
m = "0123456789"
c = 0
for i in n:
    if i in m:
        c +=1
if c == len(n):
    print("YES")
else:
    print("NO")
#2
n = input()
m = "0123456789"
c = 0
for i in n:
    if i not in m:
        c +=1
if c == 0:
    print("YES")
else:
    print("NO")
#3
n = input()
m = "0123456789"
for i in n:
    if i not in m:
        print("NO")
        break
else:
    print("YES")
#4
n = input()
if n.isdigit():
    print("YES")
else:
    print("NO")

    
