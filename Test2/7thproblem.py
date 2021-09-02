import re
f=open("file7","r")
f1=open("file8","w")
x=x='[+][9][1]\d{10}$'
for i in f:
    number=i.rstrip("\n")
    match=re.fullmatch(x,number)
    if match!=None:
        f1.write(i)