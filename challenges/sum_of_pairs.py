"""
lst [1,2,3,4,5]
if 6=>(4,2) #4+2=6
if 7=>(5,2) (4,3) #5+2=7,4+3=7
if we give number output should be  the pairs number from list who's sum is that number
"""
lst=[2,3,4,5]
# n=int(input("give a number"))
# s=0
# c=0
# sa=set()
# for i in lst:
#     c+=1
#     for k in range(c,len(lst)):
#         s=i+lst[k]
#         if n==s:
#             sa.add(i)
#             sa.add(lst[k])
#             print(sa)
#             sa.clear()
#
low=0
upper=len(lst)-1
pair=6
pairs=[]
while(low<upper):
    sum=lst[low]+lst[upper]
    if(sum==pair):
        pairs.append((lst[low],lst[upper]))
        low+=1
    elif (sum>pair):
        upper-=1
    elif(sum<pair):
        low+=1
print(pairs)
