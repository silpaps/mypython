def calc():
    print("1.addition")
    print("2.subtraction")
    print("3.multipllication")
    print("4.division")
    choice=int(input("enter a chioce"))
    num1=int(input("first number"))
    num2=int(input("second number"))

    if choice==1:
        print(num1+num2)
    elif choice==2:
        print(num1-num2)
    elif choice==3:
        print(num1*num2)
    else:
        print(num1/num2)
calc()


