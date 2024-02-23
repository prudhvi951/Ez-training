# aabbcc a2b2c2
n = input()
'''m =""
for i in n:
    if i not in m:
        if n.count(i)>1:
            k = n.count(i)
            m = m+i+str(k)
    else:
        m = m+i
print()'''
m = len(n)
k = ""
c = 1
for i in range(1,m):
    if n[i] == n[i-1]:
        c = c+1
    else:
        k = k+n[i-1]+str(c)
        c = 1
k = k+n[len(n)-1]+str(c)
print(k)
        
    
