import  re
n=input("enter a word")
x="^[A-Z][a-z]+"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
