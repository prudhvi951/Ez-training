#isprime
class classn:
    def __init__(self,n):
        self.n = n
    def isprime(self):
        c = 0
        for i in range(1,self.n+1):
             if self.n%i == 0:
                    c = c + 1
        if c == 2:
            return "Yes"
        else:
            return "No"
ob1 = classn(20)
ob2 = classn(13)
print(ob1.isprime())
print(ob2.isprime())
