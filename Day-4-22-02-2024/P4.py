#to highest frequency name amoung the 
n = int(input())
k = {}
for i in range(n):
    m = input()
    if m in k:
        k[m] += 1
    else:
        k[m] = 1
h = max(k.values())
p = []
for o in k:
    if k[o] == h:
        p.append(o)
print(max(p),h)
        
        
    
    
