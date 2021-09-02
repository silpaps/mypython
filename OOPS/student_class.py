# class Student:
#     def setvalue(self,rlno,name,schname):
#         self.rln=rlno
#         self.n=name
#         self.sn=schname
#     def printvalue(self):
#         print("rollno is",self.rln)
#         print("name is", self.n)
#         print("school name is", self.sn)
# st=Student()
# st.setvalue(1,"rahul","ABC School")
# st.printvalue()


class Student:
    sn='ABC school'#static variable
    def setvalue(self,rlno,name):
        self.rln=rlno
        self.n=name
    def printvalue(self):
        print("rollno is",self.rln)
        print("name is", self.n)
        print("school name is",Student.sn)

st=Student()
st.setvalue(1,"rahul")
st.printvalue()


