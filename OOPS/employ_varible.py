# class Employ:
#     def setdetails(self,id,name,salary,age,comp_name,dept):
#         self.id=id
#         self.name=name
#         self.salary=salary
#         self.age=age
#         self.comp=comp_name
#         self.dept=dept
#     def printdetails(self):
#         print("id is",self.id)
#         print("name is",self.name)
#         print("salary is",self.salary)
#         print("age is",self.age)
#         print("company name is ", self.comp)
#         print("department is", self.dept)
# emp=Employ()
# emp.setdetails(1,"arya",10000,23,"abc corporate","IT DEPT")
# emp.printdetails()

class Employ:
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
emp=Employ()
emp.setdetails(1,"arya",10000,23,"IT DEPT")
emp.printdetails()
emp1=Employ()
emp1.setdetails(2,"sayesha",10011,25,"IT DEPT")
emp1.printdetails()



