#number of packets of candy required to give each child 1 quan
n = int(input())
for i in range(n):
    o,p = map(int,input().split(" "))
    if p<o:
        if (o-p)%4==0:
            print((o-p)//4)
        else:
            print((o-p)//4+1)
    else:
        print(0)
'''while n>0:
    o,p = map(int,input().split(" "))
    if p<o:
        if (o-p)%4==0:
            print((o-p)//4)
        else:
            print((o-p)//4+1)
    else:
        print(0)
    n = n-1'''
    
        
