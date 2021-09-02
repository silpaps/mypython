lis=[22,3,4,5,6,7,8,9,10,11,12,13,14,15,16,76]
#error
# min=0
# max=0
# b=[]
# c=0
# for i in lis:
#      c+=1
#     b=lis[c:]
#     for k in b:
#         if k<i:
#             min1=k
#     print(k)
#error
lis.sort()
print("minuimum element",lis[0])
print("maximum element",lis[-1])


