list=[(1,"anu",34,15000),(2,"veena",32,20000),(3,"suresh",33,75000),(4,"karthick",32,570000)]
# t=()
# for i in list:
#         t=i
#         c=len(t)
#         if t[c-1]>50000:
#             print(i)
#>>>>>>>>>>>>>>alternate @ miss solution
for i in list:
    if i[-1]>50000:
        print(i)
