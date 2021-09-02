class Student:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def printv(self):
        print(self.n,self.a)
student=[Student("kookie",23),
         Student("jin",29),
         Student("jimin",25)]
def run(student):
    for s in student:
        s.printv()
run(student)