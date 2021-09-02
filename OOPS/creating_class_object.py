#class
class Person:
    def walk(self):#instance keyword
        print('person is walking')
    def read(self):
        print("person is reading")
#object creation->Person(),reference pe1
pe1=Person()
pe1.walk()
pe1.read()
#object2
pe2=Person()
pe2.walk()
pe2.read()