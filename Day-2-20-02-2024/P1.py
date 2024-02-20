#remaining profit of a sugur cane seller 70%
def test_case(k):
    if k>0:
        p = int(input())
        l = alice_profit(p)
        print(l)
    else:
        return
    test_case(k-1)

def alice_profit(n):
    t = n*50
    p = t*(30/100)
    return int(p)

n = int(input())
test_case(n)

'''for i in range(n):
    m = int(input())
    alice_profit(m)'''
'''while n>0:
    o = int(input())
    alice_profit(o)
    n = n-1'''
