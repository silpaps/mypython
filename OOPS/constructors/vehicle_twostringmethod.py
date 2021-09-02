class Vehicle():
    def __init__(self,mod,regno,colour):
        self.m=mod
        self.re=regno
        self.c=colour
    def pval(self):
        print(self.m)
        print(self.re)
        print(self.c)
    def __str__(self):
        return self.m+self.c
ve=Vehicle("ktm",1234456,"black")
ve.pval()
print(ve)