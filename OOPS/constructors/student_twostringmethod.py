class Student():
    college="SNGCE"
    def __init__(self,name,rlno,dept):
        self.n=name
        self.r=rlno
        self.d=dept

    def pval(self):
        print(self.n,self.r,self.d,Student.college)
    def __str__(self):
        return self.n +self.d
s=Student("anu",12,"cse")
s.pval()
print(s)
