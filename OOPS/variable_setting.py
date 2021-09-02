class Person:
    def setvalue(self,name,age):
        self.n=name
        self.a=age
    def printvalue(self):
        print("name",self.n)
        print("age", self.a)
pe=Person()
pe.setvalue("annu",26)
pe.printvalue()
