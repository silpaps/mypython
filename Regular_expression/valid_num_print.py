import re
f=open("numbers","r")
x=x='[+][9][1]\d{10}$'
for i in f:
    number=i.rstrip("\n")#for striping \n from last f line
    match=re.fullmatch(x,number)
    if match!=None:
        print(number)



