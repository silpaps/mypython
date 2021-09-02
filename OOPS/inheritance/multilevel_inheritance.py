class A:
    def printa(self):
        print("inside A")
class B(A):
    def printb(self):
        print("inside B")
class C(B):
    def printc(self):
        print("inside C")
a=A()
a.printa()
b=B()
b.printb()
b.printa()
c=C()
c.printc()
c.printb()
c.printa()


