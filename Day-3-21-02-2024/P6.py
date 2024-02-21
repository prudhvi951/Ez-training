#given is prime or not
n = int(input())
'''for i in range(n):
    m = int(input())
    l = []
    for i in range(1,m+1):
        if m%i == 0:
            l = l+[i]
    if len(l)==2:
        print("PRIME")
    else:
        print("NOT PRIME")
def pr(n):
    for i in range(n):
        m = int(input())
        l = []
        for i in range(1,m+1):
            if m%i == 0:
                l = l+[i]
        if len(l)==2:
            print("PRIME")
        else:
            print("NOT PRIME")'''
    
for i in range(n):
    m = int(input())
    l = []
    for i in range(2,m+1):
        if m%i == 0:
            l = l+[i]
    if len(l)==1:
        print("PRIME")
    else:
        print("NOT PRIME")            
            
