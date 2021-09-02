class Teacher:
    clgname="ABC COLLEGE"
    def __init__(self,name,sub,dept,tid):
        self.n=name
        self.s=sub
        self.d=dept
        self.t=tid
    def printvalue(self):
        print(self.n ,self.s,self.d,self.t,Teacher.clgname)
obj=Teacher("anu","english","chemistry",112)
obj.printvalue()

