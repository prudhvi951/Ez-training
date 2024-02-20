#number of 4 digits in the given integer
def test_case(n):
    if n>0:
        m = int(input())
        p = digi(m)
        print(p)
    else:
        return
    test_case(n-1)
def digi(m):
    f = 0
    while m>0:
        if m%10 == 4:
            f = f+1
        m = m//10
    return f



n = int(input())
test_case(n)
'''while n>0:
    m = int(input())
    f = 0
    while m>0:
        if m%10 == 4:
            f = f+1
        m = m//10
    print(f)
    n=n-1'''

