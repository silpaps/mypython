class Person:
    def setv(self,name,age,place):
        self.n=name
        self.a=age
        self.p=place
    def details(self):
        print(self.n,self.a,self.p)
class Parent(Person):
    def setvalue(self,name,age,hobby):
        self.nm=name
        self.ag=age
        self.h=hobby
        print(self.nm,self.ag,self.h)
class Teacher(Parent):
    def setval(self,name,age,subj):
        self.name=name
        self.age=age
        self.s=subj
        print(self.name,self.age,self.s)
t=Teacher()
t.setv("aaaa",12,"bbbbb")
t.details()