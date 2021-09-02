#>>>>>>common element in two strings
# a="afgh"
# b="cdfk"
# for i in a:
#     for a in b:
#         if i==a:
#             print(i)
#alternate
# a="afdh"
# b="cdfk"
# for i in a:
#     if i not in b:
#         print(i)

# storing  one string to another
# a="luminar"
# b=""
# for i in a:
#     b=b+i
# print(b)
#>>>>>>>>>>>>element checking
# a="selected"
# b=input("enter charecter")
# for i in a:
#     flag=0
#     if i==b:
#         break
#     else:
#         flag+=1
# if flag==0:
#     print("present")
# else:
#     print("not present")

#>>>>to count
# a="malaylam"
# b=input("enter charecter")
# c=0
# for i in a:
#     if i==b:
#        c=c+1
# print(c)
#>>>>>>>>symbol removing
sym="~!@#$%^&*()_+-={}[];:<,>./?|"
string="hellohai12@#$%^&67"
c=""
for i in string:
    if i not in sym:
         c=c+i

print(c)





