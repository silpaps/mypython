def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
num=int(input("enter a number"))
print("factorial is ",fact(num))