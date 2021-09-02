a=int(input("emter first elememt"))
b=int(input("emter second elememt"))
try:
    res=a/b
    print(res)
except:
    print("exception occured /zero division")
finally:
    print("inside")