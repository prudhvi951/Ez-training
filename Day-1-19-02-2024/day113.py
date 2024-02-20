#discount on tvs on sale 
n = int(input())
'''for i in range(n):
    a,b,c,d = map(int,input().split(" "))
    first = a-c
    second = b-d
    if first>second:
        print("Second")
    elif first<second:
        print("First")
    else:
        print("Any")'''
while n>0:
    a,b,c,d = map(int,input().split(" "))
    first = a-c
    second = b-d
    if first>second:#a-c > b-d
        print("Second")
    elif first<second:#a-c < b-d
        print("First")
    else:
        print("Any")
    n = n-1
    
