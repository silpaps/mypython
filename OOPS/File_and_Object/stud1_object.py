class Student:
    def __init__(self,name,id,dept,mark):
        self.n=name
        self.id=id
        self.d=dept
        self.m=mark
    def pval(self):
        print("name is ",self.n)
        print("id is",self.id)
        print("dept is",self.d)
        print("mark is",self.m)
    def __str__(self):
        return  self.n
f=open('stud1','r')
for i in f:
    l=i.split(",")
    name=l[0]
    id=l[1]
    dept=l[2]
    mark=l[3]
    s=Student(name,id,dept,mark)
    print(s)
    s.pval()
