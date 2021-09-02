class Person:
    def setval(self,name,age,hobby):
        self.n=name
        self.a=age
        self.h=hobby
    def printval(self):
        print( self.n,self.a,self.h)

class Child(Person):
    def setvalue(self,name,age,hobby):
        self.n=name
        self.a=age
        self.h=hobby
    def printvalue(self):
        print( self.n,self.a,self.h)
class Student(Child):
    def printv(self):
        print("student is attending exam")
p=Person()
p.setval("anu",12,"readng")
p.printval()
c=Child()
c.setvalue("jukhook",23,'SINGING')
c.printvalue()
c.setval("anu",12,"readng")
c.printval()
s=Student()
s.printv()
s.setvalue("jukhook",23,'SINGING')
s.printvalue()
s.setval("anu",12,"readng")
s.printval()
