class Person:
    def setvalue(self,name,age,hobby):
        self.n=name
        self.a=age
        self.h=hobby
    def printvalue(self):
        print(self.n,self.a,self.h)
class Parent:
     def setv(self,name,age,job):
         self.n=name
         self.a=age
         self.j=job
         print(self.n,self.a,self.j)
class Teacher(Person,Parent):
    def setval(self,name,age,sub):
        self.n=name
        self.a=age
        self.s=sub
        print(self.n)
        print(self.a)
        print(self.j)
t=Teacher()
t.setvalue("anu",12,"reading")
t.printvalue()
t.setv("manu",38,"doctor")
