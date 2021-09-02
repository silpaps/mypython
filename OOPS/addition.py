class Add:
    def takevalue(self,a,b):
        self.a=a
        self.b=b
    def printres(self):
        self.c=self.a+self.b
        print(self.c)
res=Add()
res.takevalue(3,5)
res.printres()
