# class Person():
#     def show(self,num,a):
#         self.num=num
#         self.a=a
#         print(self.num,self.a)
# class Student(Person):
#     def show(self,num1,num2):
#         self.n1=num1
#         self.n2=num2
#         self.c=self.n1+self.n2
#         print(self.n1,self.n2,self.c)
# st=Student()
# st.show(3,4)
# class Parent:
#     def printval(self,num):
#         self.num=num
#         print("inside parent class",self.num)
# class Child:
#     def printval(self,num1):
#         self.num1=num1
#         print("inside child class ",self.num1)
# c=Child()
# c.printval(2)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>child class overrides parent class

class Operators:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
    def num(self,n3,n4):
        self.n3=n3
        self.n4=n4
        print("inside second method",self.n3,self.n4)
o=Operators()
o.num(8,4)