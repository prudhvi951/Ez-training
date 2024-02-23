#update string according the string before one
n = int(input())
for i in range(n):
    k = ""
    a,b = input().split()
    for j in b:
        if j not in a:
            k = k+j
    print(k)
