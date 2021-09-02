# class Student:
#     def setvalue(self,details):
#         self.d=details
#         print(self.d)
# s=Student()
# f=open('student','r')
# for i in f:
#     s.setvalue(i)
class Student:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def pval(self):
        print("name is ",self.n)
        print("age is",self.a)
    def __str__(self):
        return  self.n

f=open('student','r')
for i in f:
    l=i.split(",")
    name=l[0]
    age=l[1]
    s=Student(name,age)
    print(s)
    s.pval()
