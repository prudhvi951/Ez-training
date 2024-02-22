#to store contacts and retrive the contact number by name
n = int(input())
k = {}
for i in range(n):
    a,b = input().split()
    k[a] = b
def fun(l):
    if l in k:
        print(l,"=",k[l])
    else:
        print("Not Found")
while True:
    l = input()
    fun(l)
    
