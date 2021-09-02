class Person:
    def setval(self,name,age,hobby):
        self.n=name
        self.a=age
        self.h=hobby
    def printval(self):
        print( self.n,self.a,self.h)


class Parent(Person):#single inheritence
    def setv(self, name, age, job):
        self.n = name
        self.a = age
        self.j = job
        print(self.n, self.a, self.j)


class Teacher(Parent):#multilevel inheritance
    def setvalue(self, name, age, sub):
        self.n = name
        self.a = age
        self.s = sub
        print(self.n)
        print(self.a)
        print(self.s)

class Employ(Teacher,Parent):#multiple inheritence
    comp="ABC corporate"
    def setdetails(self,id,name,salary,age,dept):
        self.id=id
        self.name=name
        self.salary=salary
        self.age=age

        self.dept=dept
    def printdetails(self):
        print("id is",self.id)
        print("name is",self.name)
        print("salary is",self.salary)
        print("age is",self.age)
        print("company name is ", Employ.comp)
        print("department is", self.dept)
#person object
p=Person()
p.setval("aaaa",28,"reading")
p.printval()
#parent object as single inheritence
pa=Parent()
pa.setval("aaaa",28,"reading")
pa.printval()
pa.setv("bbbb",35,"doctor")
#Teacher object as multilevel inheritence
t=Teacher()
t.setval("aaaa",28,"reading")
t.printval()
t.setv("bbbb",35,"doctor")
t.setvalue("cccc",34,"IT")

#Employ as multiple inheritence
e=Employ()
e.setdetails(1,"vvvvvv",100000,56,"IT")
e.printdetails()
e.setvalue("cccc",34,"IT")
e.setv("bbbb",35,"doctor")