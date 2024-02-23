'''class classa:
    def factorial(self,n):
        k = 1
        for i in range(1,n+1):
            k = k*i
        print(k)
ob = classa()
ob.factorial(5)'''

'''class classa:
    def __init__(self,n):
        self.n = n
        print(n)
    def fact(self):
        r = 1
        for i in range(1,self.n+1):
            r = r*i
        print(r)
ob = classa(5)
ob.fact()'''
class classa:
    def __init__(self,n):
        self.n = n
    def fact(self):
        print(self.recrfact(self.n))
    def recrfact(self,n):
        if n == 1:
            return 1
        else:
            return n * self.recrfact(n-1)
ob = classa(6)
ob.fact()
        
