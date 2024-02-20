#reverse the given integer using while
n = int(input())
#print(int(n[::-1]))
s = 0
if n>0:
    while n>0:
        k = n%10
        s = (s*10)+k
        n = n//10
    print(s)
else:
    n = -(n)
    while n>0:
        k = n%10
        s = (s*10)+k
        n = n//10
    print(-s)
    

    

