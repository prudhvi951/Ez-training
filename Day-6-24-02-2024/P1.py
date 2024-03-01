def f1(self,x,y):
    return min(x,y)
class C:
    f =f1
    def g(self):
        print("Hello World")
d = C()
d.g()
print(d.f(10,20))
