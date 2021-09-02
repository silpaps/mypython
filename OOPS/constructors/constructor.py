#constructor
class Employ:
    def __init__(self,id,name,salary,age,comp_name,dept):#__init__ is used for constructor creation.used initialize instance variables
        self.id=id
        self.name=name
        self.salary=salary
        self.age=age
        self.comp=comp_name
        self.dept=dept
    def printdetails(self):
        print("id is",self.id)
        print("name is",self.name)
        print("salary is",self.salary)
        print("age is",self.age)
        print("company name is ", self.comp)
        print("department is", self.dept)
emp=Employ(1,"arya",10000,23,"abc corporate","IT DEPT")
#by using constructor  we can set values at the time of object creation itself intead of callind seprate method
emp.printdetails()