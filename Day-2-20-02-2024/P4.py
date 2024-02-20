#factorial of number
'''def fact(n):
    if n==1:
        return 1
    else:
        return n*(fact(n-1))'''
n = int(input())
#m = fact(n)
#print(m)
x = 1
'''for i in range(1,n+1):
    x = x*i'''
#print(x)
while n>0:
    x = x*n
    n=n-1
print(x)
