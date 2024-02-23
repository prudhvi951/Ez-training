#to find vowel count and consonants count
#1
'''n = input()
m = "AEIOUaeiou"
c = 0
v = 0
for i in n:
    if i not in m:
        c +=1
    else:
        v = v+1
print(v,c)'''
#2
'''n = input()
m = "AEIOUaeiou"
c = 0
v = 0
for i in n:
    if i in m:
        v +=1
    else:
        c = c+1
print(v,c)'''
#3
'''n = input()
m = "AEIOUaeiou"
z = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
c = 0
v = 0
for i in n:
    if i in m:
        v +=1
    elif i in z:
        c = c+1
print(v,c)'''
#4
n = input()
m = "AEIOUaeiou"
c = 0
v = 0
for i in n:
    if i in m:
        v +=1
    elif i.isalpha():
        c = c+1
print(v,c)
