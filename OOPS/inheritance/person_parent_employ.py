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
class Employ(Person,Parent):
    comp = "ABC corporate"

    def setdetails(self, id, name, salary, age, dept):
        self.id = id
        self.name = name
        self.salary = salary
        self.age = age

        self.dept = dept

    def printdetails(self):
        print("id is", self.id)
        print("name is", self.name)
        print("salary is", self.salary)
        print("age is", self.age)
        print("company name is ", Employ.comp)
        print("department is", self.dept)
e=Employ()
e.setvalue("anu",12,"readng")
e.printvalue()
e.setv("manu",34,"doctor")
e.setdetails(1,"arya",10000,23,"IT DEPT")
e.printdetails()
