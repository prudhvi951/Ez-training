class dob:
    def __init__(self,c,d,e):
        self.c =c
        self.d =d
        self.e =e
    def display1(self):
        k = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        print(self.c)
        print(k[self.d-1])
        print(self.e)
        
        
class a(dob):
    def __init__(self,a,b,c,d,e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        super().__init__(c,d,e)
    def display(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)
        print(self.e)
        
ob = a("abc",27,24,8,2001)
ob.display()
ob.display1()
