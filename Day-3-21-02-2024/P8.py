#even perfect numbers between two ranges
'''n,m = map(int,input().split())
for i in range(n,m+1):
    if i%2==0:
        k = []
        for j in range(1,i):
            if i%j==0:
                k = k+[j]
        s= sum(k)
        if s==i:
            print(i)'''
    
n = int(input())
s = 0
for i in range(2,n+1,2):
    for j in range(1,i):
        if i%j==0:
            s=s+j
    if s==i:
        print(i)
    s=0
                
                
