#print number of words
#approch 1
'''n = int(input())
k = "AEIOUaeiou"
for i in range(n):
    m =input()
    v = 0
    c = 0
    w = m.strip()
    p = len(w.split())
    for j in m:
        if j in k:
            v = v+1
        elif j.isalpha():
            c = c+1
    print(p,v,c)'''
#approch 2
t = int(input())
d = "AEIOUaeiou"
for i in range(t):
    s = list(input().split())
    v = 0
    c = 0
    w = len(s)
    for j in s:
        for k in j:
            if k.isalpha():
                if k in d:
                    v = v+1
                else:
                    c = c+1
    print(w,v,c)
            
    
