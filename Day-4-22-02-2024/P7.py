#weighted and directed graph
n = int(input())
k = {}
for i in range(n):
    a,b,c=map(str,input().split())
    c = int(c)
    if a not in k:
        k[a] = [[b,c]]
    else:
        k[a].append([b,c])
print(k)
l = input()
if l in k:
    m = []
    for i in k[l]:
        m.append(i[1])
    print(m)
    mm = min(m)
    for i in k[l]:
        if i[1] == mm:
            print(i[0])
else:
    print("NO ROUTE")

    
