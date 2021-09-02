# def sum(n):
#     s=0
#     for i in range(n+1):
#        s=s+i
#     return s
# print(sum(3))
#>>>>>>>>>>>>>>>>>>>fibanocci series>>>>>>>>>>>>>>>>>>>>>

# n1=0
# n2=1
# for i in range(10):
#     print(n1)
#     nth=n1+n2
#     n1=n2
#     n2=nth
# >>>>>>>>>>>>>>prime numbers

# num=int(input("enter a nuber"))
# if num>0:
#     flag=0
#     for i in range(2,num):
#         if num%i==0:
#             flag+=1
#         else:
#             flag+=0
#     if flag==0:
#         print("prime number ")
#     else:
#         print("not a prime")

# >>>>>>>>>>>>>>prime numbers with range
# min=int(input("enter a minimum range"))
# max=int(input("enter a maximum range"))
# for i in range(min,max+1):
#     if i>1:
#         for a in range(2,i):
#             if i%a==0:
#                 break
#         else:
#             print(i)


#>>>>>>>>>>>>>>paliandrome
#malayalam
# a='abdc'
# b=a[::-1]
# print(b)
a=input("enter a string")
b=a[::-1]
print(b)
if a==b:
    print("paliandrome")
else:
    print("not palindrome")


