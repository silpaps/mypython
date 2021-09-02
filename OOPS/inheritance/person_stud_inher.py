#single inheritance
class Person: #base class/parent class/super class
    def walk(self):#instance keyword
        print('person is walking')
    def read(self):
        print("person is reading")
class Student(Person): #subclass/child class/derived classs
    def exam(self):
        print("student is attending exam")
p=Person()
p.walk()
p.read()
#inheriting
s=Student()
s.walk()
s.read()
s.exam()