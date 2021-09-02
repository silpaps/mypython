# s=input("enter a string")
# for i in s:
#     c=0
#     for d in s:
#         if i==d:
#             c+=1
#     if c>1:
#        print(i)
#        break
#>>>>>>>>>>>>>>>>>alternate
s = input("enter a string")
b=""
for i in s:
    if i not in b:
        b=b+i
    else:
        print("recursive character",i)
        break


