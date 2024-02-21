'''n = int(input())
for o in range(n):
    m = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    k = 0
    for i in range(m):
        if (x[i] <= 2* y[i] and y[i] <= 2* x[i]):
            k = k+1
    print(k)'''
    
            
t=int(input())
for i in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    h=0
    for j in range(n):
        if (A[j]<= 2* B[j] and B[j]<= 2* A[j]):
           h=h+1
    print(h)
