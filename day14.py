#second largest amoung 3
n = int(input())
m = int(input())
l = int(input())
if n>m and n>l:
    n=0
elif m>n and m>l:#m>l
    m=0
else:
    l=0
if n>m and n>l:
    print(n)
elif m>n and m>l:#m>l
    print(m)
else:
    print(l)
