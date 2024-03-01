"""class parent:
    def fun1(self):
        print("Parent")
class child1(parent):
    def fun2(self):
        print("child1")
class child(child1):
    def fun3(self):
        print("child")
ob = child()
ob.fun3()
ob.fun2()
ob.fun1()
"""
#multi level inheritance 
class vehicle:
    def __init__(self,c):
        self.c = c
    def display3(self):
        print(self.c)
class motor(vehicle):
    def __init__(self,b,c):
        self.b = b
        self.c = c
        super().__init__(c)
    def display2(self):
        print(self.b)
        print(self.c)
class car(motor):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(b,c)
    def display1(self):
        print(self.a)
        print(self.b)
        print(self.c)
ob = car("BMW",3000,"PETROL")
ob.display1()
ob.display2()
ob.display3()
        
    
    
