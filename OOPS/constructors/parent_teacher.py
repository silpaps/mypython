class Parent():
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def printval(self):
        print(self.n,self.a)
class Teacher(Parent):
    def __init__(self,id,subject,name,age):
        super().__init__(name,age)
        self.id=id
        self.sub=subject
    def pval(self):
        print(self.id,self.n,self.a,self.sub)
    def __str__(self):
        return self.n+" " + str(self.id)
t=Teacher(1,"english","anu",32)
t.pval()
print(t)