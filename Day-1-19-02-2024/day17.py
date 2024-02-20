#traingle validator problem sum of two sides of traingle must be greater than 3 side
n,m,l = map(int,input().split(" "))
if n+m>l and m+l>n and n+1>m:
    print("Yes")
else:
    print("No")
