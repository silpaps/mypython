# class Person():
#     def show(self,num):
#         self.num=num
#         print(self.num)
# class Student(Person):
#     def show(self,num1,num2):
#         self.n1=num1
#         self.n2=num2
#         print(self.n1,self.n2)
# st=Student()
# st.show(3,4)
#st.show(3) calls person method but shows error because python not supporting overloading
class Operators:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
    def num(self,n3,):
        self.n3=n3
        print("inside second method",self.n3)
o=Operators()
o.num(8,2)