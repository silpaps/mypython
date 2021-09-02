import  re
n=input("enter a word")
x="^[A-Z]\d\w{3,8}[A-Z]$"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")