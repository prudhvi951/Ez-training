#to incrent the ascii values according to the user
#approch 1
n = int(input())
k = ""
for i in range(n):
    m,n= input().split()
    n = int(n)
    for j in m:
        p = ord(j)+n
        if p > 122:
            p = 96 + (p-122)
            k = k + chr(p)
        else:
            k = k + chr(p)
    print(k)
#approch 2
n = int(input())
m = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
for i in range(n):
    a,b = input().split()
    b = int(b)
    p = ""
    for j in a:
        k = m.index(j)+b
        if k>26:
            k = k%26
        p = p+m[k]
    print(p)
