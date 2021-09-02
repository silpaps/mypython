class Vehicle:
    def __init__(self,model,regno,company,milage):
        self.m=model
        self.r=regno
        self.c=company
        self.mil=milage
    def printval(self):
        print("vehicle is",self.m,self.r,self.c,self.mil)
class Bus(Vehicle):
    def __init__(self,model,regno,company,milage,color,tyre):
        super().__init__(model,regno,company,milage)
        self.col=color
        self.ty=tyre
    def pval(self):
        print("bus is",self.m,self.r,self.c,self.mil,self.col,self.ty)
    def __str__(self):
        return self.m+" "+self.r
b=Bus("bus","KL14AR1300","TATA","3.63Kmpl","blue",4)
b.pval()
b.printval()
print(b)