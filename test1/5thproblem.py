def add(a,b):
    print("sum is ",a+b)
def sub(a,b):
    print("difference is ", a - b)
def mul(a,b):
    print("product is ", a * b)
def div(a,b):
    print("quotient is", a / b)
def floor(a,b):
    print("quotient is",a//b)
def exp(a,b):
    c=1
    for i in range(b):
        c=c*a
    print(c)
print(" 1  addition ")
print( "2 subtraction")
print(" 3 multiplication")
print(" 4 division")
print(" 5 floor division")
print(" 6 exponent")
op=int(input("select one above operation"))
if op==1:
    a = int(input("give the first number"))
    b = int(input("give the second number"))
    add(a,b)
elif op==2:
    a = int(input("give the first number"))
    b = int(input("give the second number"))
    sub(a,b)
elif op==3:
    a = int(input("give the first number"))
    b = int(input("give the second number"))
    mul(a,b)
elif op==4:
    a = int(input("give the first number"))
    b = int(input("give the second number"))
    div(a,b)
elif op==5:
    a = int(input("give the first number"))
    b = int(input("give the second number"))
    floor(a,b)
else:
    a = int(input("give the  number"))
    b = int(input("give the exponent"))
    exp(a,b)


