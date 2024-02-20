#number of pizza required to fulfill ther appitate
n = int(input())
'''for i in range(n):
    a,b = map(int,input().split())
    if a*b%4==0:
        print(a*b//4)
    else:
        print(a*b//4+1)'''
'''while n>0:
    a,b = map(int,input().split())
    if a*b%4==0:
        print(a*b//4)
    else:
        print(a*b//4+1)
    n = n-1'''
for i in range(n):
    a,b = map(int,input().split())
    ts = a*b
    tp = 0
    while ts>=4:
        ts = ts-4
        tp = tp+1
    if ts == 0:
        print(tp)
    else:
        tp = tp+1
        print(tp)
