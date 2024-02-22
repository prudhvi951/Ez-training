#given string is panagram or not
#sets
'''def pana(n):
    m = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    k = set()
    for i in n:
        p = set(i)
        k = k|p
    if len(k) == len(m):
        print("Panagram")
    else:
        print("Not Panagram")
n = input().split()
pana(n)'''
'''def pana2(n):
    #m = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    k = set()
    for i in n:
        p = set(i)
        k = k|p
    if len(k) == 27:
        print("Panagram")
    else:
        print("Not Panagram")
n = input().split()
pana2(n)'''
#dictionary
'''n = input().split()
k = {}
for i in n:
    for j in i:
        if j not in k:
            k[j] = 1
        else:
            k[j]+=1
if len(k) == 26:
    print(k)
    print("PANAGRAM")
else:
    print("NOT PANAGRAM")'''

        
n = input().split()
k = []
for i in n:
    for j in i:
        if j not in k:
            k.append(j)
if len(k)==26:
    print(k)
    print("PANAGRAM")
else:
    print("NOT PANAGRAM")

