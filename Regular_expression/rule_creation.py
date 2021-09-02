# import re
#
# n="hello"
# x='[a-z]+'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

# import re
#
# n="56KG"
# x='[0-9A-Z]+'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

# import re
#
# n="56KG"
# x='[0-9]{2}[A-Z]{2}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

# import re
#
# n=(input("give mobile number"))
# x='\d{10}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


# import re
#
# n="+919633577785"
# x='\W{1}[0-9]{2}[0-9]{10}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

# import re
#
# n="+919633577785"
# x='[+][9][1]\d{10}$'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

# import re
#
# n="KL12TE1234"
# x='[A-Z0-9]+'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

# import re
#
# n="KL12TE1234"
# x='[A-Z]{2}\d{2}[A-Z]{2}\d{4}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")


#combination of uppercase and lowercase ending with number
# import re
#
# n="aabb6"
# x='[a-zA-Z]+\d$'
#
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

#mailvalidation
# import  re
# n=input("enter gmail")
# x='[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")
#starting with a and ending with b
# import  re
# n=input("enter a word")
# x="^a[a-zA-Z0-9\W]*b$"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")
#minimum length 8 and maximum lenth 15 and except numbers
# import  re
# n=input("enter a word")
# x="[a-zA-Z\W]{8,15}"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

# import  re
# n=input("enter a word")
# x="[\D]{8,15}"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")
#starting with uppercase and
#then lowercase letters,symbol ,digits
import  re
n=input("enter a word")
x="^[A-Z][a-zA-Z\d\W]*"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
