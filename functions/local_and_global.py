# x=5
# def foo():
#     x=3
#     x+=10
#     print("local",x)
# foo()
# print("global",x)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
x=5
def foo():
     #x=3
     global x
     x+=10
     print("local",x)
foo()
print("global",x)


