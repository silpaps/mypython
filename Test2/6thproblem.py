class Student:
    def __init__(self,name,rlno,dept,mark):
        self.n=name
        self.r=rlno
        self.d=dept
        self.m=mark
    def pval(self):
        print("name is ",self.n)
        print("rolno is",self.r)
        print("dept is",self.d)
        print("mark is",self.m)
    def __str__(self):
        return self.n
gr=0
f=open("file6","r")
for i in f:
    l=i.split(",")
    mark=int(l[3])
    if mark>gr:
        gr=mark
print("higest mark is",gr)
f=open("file6","r")
for k in f:
    l=k.split(",")
    name = l[0]
    rlno = l[1]
    dept = l[2]
    mark=int(l[3])
    if mark==gr:
        s=Student(name,rlno,dept,mark)
        s.pval()
        print(s)

