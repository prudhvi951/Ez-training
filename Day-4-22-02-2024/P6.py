#number of traversing routes to one vertex to anthor vertex
n = int(input())
k = {}
for i in range(n):
    a,b = input().split()
    if a not in k:
        k[a] = [b]
    else:
        k[a] +=[b]

c = input()
if c not in k:
    print("None")
else:
    print(k[c])   
    
