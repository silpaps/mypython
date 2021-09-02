# a=int(input("emter first elememt"))
# b=int(input("emter second elememt"))
# if b!=0:
#  print(a/b)
# else:
#  print("division by zero is not possible")

#>>>>>>>>>>>>>>>>>>>>>
# a=int(input("emter first elememt"))
# b=int(input("emter second elememt"))
# try:
#     res=a/b
#     print(res)
# except:
#     print("exception occured /zero division")
#>>>>>>>>>>>>>>>>>>>
a=int(input("emter first elememt"))
b=int(input("emter second elememt"))
try:
    res=a/b
    print(res)
except Exception as e:
    print(e.args)
finally:
    print("inside")

