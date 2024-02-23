#count of given charcter in gien string
'''s = input()
c = input()
f = 0
for i in range(len(s)):#in s
    if s[i] == c:#i == c
        f = f+1
print(c,f)'''

s = input()
c = input()
f = 0
for i in range(len(s)):
    if s[i] == c and i%2==0:
        f = f+1
print(c,f)

'''s = input()
c = input()
print(s.count(c))'''
