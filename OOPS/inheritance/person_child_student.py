#multiple inheritence
class Person:
    def setvalue(self,name,age,hobby):
        self.n=name
        self.a=age
        self.h=hobby
    def printvalue(self):
        print( self.n,self.a,self.h)

class Child:
    def setvalue(self,name,age,hobby):
        self.n=name
        self.a=age
        self.h=hobby
    def printvalue(self):
        print( self.n,self.a,self.h)
class Student(Person,Child):
    def printv(self):
        print("student is attending exam")
s=Student()
s.setvalue("anu",12,"readng")
s.printvalue()
s.setvalue("jukhook",23,'SINGING')
s.printvalue()
s.printv()
#here person ,child is parent class