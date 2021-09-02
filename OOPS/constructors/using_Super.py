class Person:
    def __init__(self,name,age,hobby):
        self.n=name
        self.a=age
        self.h=hobby

    def printvalue(self):
        print(self.n, self.a, self.h)
class Student(Person):
    def __init__(self,rlno,mark,name,age,hobby):
        super().__init__(name,age,hobby)
        self.r=rlno
        self.m=mark
    def pval(self):
        print(self.r)
        print(self.m)
        print(self.n)
        print(self.a)
        print(self.h)
s=Student(2,34,"anu",12,"reading")
s.printvalue()
s.pval()
