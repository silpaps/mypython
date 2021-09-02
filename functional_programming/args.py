# def printval(*args):
#     return args
# print(printval(2,3,4,5,6,7,8))

# def printval(**args):
#     return args
# print(printval(name="anu",age=12,job="teacher"))

def sum(*args):
     s=0
     for i in args:
         s+=i
     return s
print(sum(1,2,3,4))