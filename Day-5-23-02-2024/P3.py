#string having all vowels are not
'''n = input()
m = "aeiouAEIOU"
for i in n:
    if i not in m:
        print("NO")
        break
else:
    print("YES")'''

n = input()
m = "aeiouAEIOU"
c = 0
for i in n:
    if i in m:#not in m
        c+=1
if c == len(n):#if c ==0
    print("YES")
else:
    print("NO")
        
