#quality of the products and return its cost
k = int(input())
for i in range(k):
    n,q = map(int,input().split(" "))
    x = input().split(" ")
    y = input().split(" ")
    c = 0
    for i in range(len(x)):
        if int(x[i]) >= q:
            p = x.index(x[i])
            c = c + int(y[p])
    print(c)
            
#2
t = int(input())
for i in range(t):
    n,x = map(int,input().split(" "))
    a = list(map(int,input().split(" ")))
    b = list(map(int,input().split(" ")))
    c = 0
    for j in range(n):
        if a[j]>=x:
            c =c +b[j]
    print(c)
            
