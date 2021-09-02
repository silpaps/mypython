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
class Parent(Person):
    def setv(self, name, age, job):
        self.n = name
        self.a = age
        self.j = job
        print(self.n, self.a, self.j)
class Student(Child):
    def printv(self):
        print("student is attending exam")
p=Person()
p.setval("manu",32,"reading")
p.printval()
c=Child()
c.setvalue("mike",12,"drawing")
c.printvalue()
c.setval("manu",32,"reading")
c.printval()
pa=Parent()
pa.setv("arjun",34,"doctor")
pa.setval("manu",32,"reading")
pa.printval()
st=Student()
st.printv()
st.setvalue("mike",12,"drawing")
st.printvalue()
st.setval("manu",32,"reading")
st.printval()