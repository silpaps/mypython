#a=int(input("enter a number"))
#if a>0:
#   print("number is positeve")
#elif a==0:
#    print("number is 0")
#else:
#    print("number is negative")

#if condition1:
#    block content
# elif condition 2:
#    block content
# elif cindition 3:
#    block content
# else:
#    block content

#Total_amount =100000
#with_amount=int(input("enter amount required"))
#if with_amount>Total_amount:
#    print("insufficent amount")
#else:
#    print("withdrawl succesfully completed")
#    bal=str(Total_amount-with_amount)
#   print("balance amount is  "+ bal)

#no1=int(input("enter number1"))
#no2=int(input("enter number2"))
#if no1>no2:
#    print(str(no1)+" is greater")
#elif no1==no2:
#    print("equal numbers")
#else:
#    print(str(no2)+" is greater")
no1=int(input("enter number1"))
no2=int(input("enter number2"))
no3=int(input("enter number3"))
if no1>no2:
    if no1>no3:
        print(no1," is greater")
    else:
        print(no3," is greater")
elif no1==no2==no3:
    print("numbers are equal")
else:
    if no2>no3:
        print(no2," is greater")
    else:
        print(no3, "is greater")
