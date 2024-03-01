from abc import ABC,abstractmethod#abstraction class
class shape:
    def __init__(self):
        pass
    @abstractmethod#abstraction of method
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print(self.l*self.b)
class square(shape):
    def __init__(self,s):
        self.s =s
    def area(self):
        print(self.s**2)
ob = square(4)
ob.area()
