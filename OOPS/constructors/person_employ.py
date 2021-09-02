class Person:
    def __init__(self,name,age,hobby):
        self.n=name
        self.a=age
        self.h=hobby
    def printvalue(self):
        print( self.n,self.a,self.h)
class Employ(Person):
    comp="abc corporate"
    def __init__(self,id,salary,dept,name,age,hobby):
        super().__init__(name,age,hobby)
        self.id=id
        self.s=salary
        self.d=dept
    def pval(self):
        print(self.id,self.s,self.d,self.n,self.a,self.h)
e=Employ(1,2000,"cse","anu",32,"reading")
e.printvalue()
e.pval()
