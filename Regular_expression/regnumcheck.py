import re
f1=open('regnum','r')
f2=open('pyregnum','a')
x='[A-Z]{3}\d{2}[P][Y]\d{4}'
for i in f1:
    reg=i.rstrip("\n")
    match=re.fullmatch(x,reg)
    if match!=None:
      f2.write(reg)
      f2.write("\n")

