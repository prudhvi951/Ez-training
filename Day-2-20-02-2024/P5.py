#adding thress left and right of digit
def threes(n):
    m = n
    l = 0
    while m>0:
        l = l+1
        m=m//10
    n = (3*(10**l))+n
    n = n*10+3
    return n
    
n = int(input())
print(threes(n))
#a = n*10+3
'''r=n
k = 0
while n>0:
    k = k+1
    n=n//10
#print(k)
j = r/(10**k)
#print(j)
j = j+3
#print(j)
j = j*(10**k)
#print(j)
j = j*10+3
print(j)'''


