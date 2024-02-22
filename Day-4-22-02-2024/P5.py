#to know the database is whether corrupted or not
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    k = {}
    for j in range(b):
        x,y = map(int,input().split())
        if y not in k:
            k[y] = [x]
        else:
            k[y] += [x]#can use append
    for o in k:
        if len(k[o])>a:
            print("CORRUPTED")
            break
        else:
            print("NOT CORRUPTED")
            break
        
    
