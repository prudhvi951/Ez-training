#finding if team is eligible for partcipate contest by knowing divisors of number of participants
'''n = int(input())
for j in range(n):
    m = int(input())
    k = 0
    l = 0
    for i in range(1,m+1):
        if m%i == 0:
            if i%2 == 0:
                k = k+1
            else:
                l = l+1
    if k== l:
        print(1)
    else:
        print(0)'''

'''n = int(input())
for j in range(n):
    m = int(input())
    k = []
    l = []
    for i in range(1,m+1):
        if m%i == 0:
            if i%2 == 0:
                k = k+[i]
            else:
                l = l+[i]
    if len(k)== len(l):
        print(k)
        print(l)
    else:
        print(0)'''
        
def contest(n):
    for j in range(n):
        m = int(input())
        k = []
        l = []
        for i in range(1,m+1):
            if m%i == 0:
                if i%2 == 0:
                    k = k+[i]
                else:
                    l = l+[i]
        if len(k)== len(l):
            print(k)
            print(l)
        else:
            print(0)
    
n = int(input())
contest(n)
    
