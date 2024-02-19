# B-small,large or equal
n = input().split(" ")
#a,b = map(int,input().split())
a = int(n[0])
b = int(n[1])
if a>b:
    print("a > b")
    #print(str(a)+">"+str(b))
elif b>a:
    print("a < b")
    #print(str(b)+">"+str(a))
else:
    print("a == b")
    #print(str(a)+"=="+str(b))
