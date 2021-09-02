#function without arguments
# def add():
#     num1=int(input("enter num1"))
#     num2=int(input("enter num2"))
#     add =num1+num2
#     print(add)
# add()

#function with arguments
# def add(num1,num2):
#     print(num1+num2)
# add(3,5)
#function with arguments and return type
# def add(num1,num2):
#     add=num1+num2
#     return add
# print(add(3,5))
#function without argument using odd cheking
# def odd():
#     num=int(input("enter a number"))
#     if num%2==1:
#         print(num,"is odd nuber")
#     else:
#         print("even number")
# odd()
#using function with argument  factorial
def fact(num):
    if num > 0:
       fact=1
       for i in range(1,num+1):
           fact=fact*i
       print(fact)
    elif num==0:
       print("1")
    else:
       print("factorial doesn't exist for negative numbers")
fact(5)





