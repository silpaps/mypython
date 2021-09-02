class Animal:
    def __init__(self,name,breed,color):
        self.n=name
        self.b=breed
        self.c=color
    def animalis(self):
        print("animal is",self.n,self.b,self.c)
class Dog(Animal):
    def __init__(self,name,breed,color,age,food):
        super().__init__(name,breed,color)
        self.a=age
        self.f=food
    def dogis(self):
        print(self.n,self.b,self.c,self.a,self.f)
    def __str__(self):
        return self.n+" "+self.b

d=Dog("tomy","labrador","black",3,"chiken")
d.dogis()
d.animalis()
print(d)