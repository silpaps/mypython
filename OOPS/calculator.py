class Calc:
    def add(self,a,b):
        self.a=a
        self.b=b
        res=self.a+self.b
        print(res)
    def sub(self,a,b):
        self.a=a
        self.b=b
        res=self.a-self.b
        print(res)
    def mul(self,a,b):
        self.a=a
        self.b=b
        res=self.a*self.b
        print(res)
    def div(self,a,b):
        self.a=a
        self.b=b
        res=self.a/self.b
        print(res)
ob=Calc()
print("1.addition")
print("2.subtraction")
print("3.multipllication")
print("4.division")
choice=int(input("enter a chioce"))
num1=int(input("first number"))
num2=int(input("second number"))
if choice == 1:
    ob.add(num1,num2)
elif choice == 2:
    ob.sub(num1, num2)
elif choice == 3:
    ob.mul(num1, num2)
else:
    ob.div(num1, num2)