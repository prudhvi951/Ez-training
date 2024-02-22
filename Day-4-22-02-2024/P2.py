#first repeted aplphabet
n = int(input())

for i in range(n):
    m = input()
    k ={}
    for j in m:
        if j not in k:
            k[j] = 1
        else:
            k[j] += 1
    for t in k:
        if k[t] == 2:
            print(t)
            break
        else:
            print(".")

        
