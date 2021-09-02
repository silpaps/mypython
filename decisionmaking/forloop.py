#for (variable) in range(number)
# block content
# for i in range(2,8):
#     print(i)
#for i in range(2,10,2):
#   print(i)
#min=int(input("enter minimum range "))
#max=int(input("enter maxmum range "))

#for i in range(min,max+1):
#    print(i)

#........Multiplication table..........
no=int(input("give the number"))
if no>0:
    print("multiplication table of ", no)
    for i in range(1,11):
        mul=i*no
        print(i,"*",no,"=",mul)
else:
    print("multiplication table cannot generate")
