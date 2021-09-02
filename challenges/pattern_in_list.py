#lst[2,4,6]=>[10,8,6]
#lst[3,5,7]=>[12,10,8]
#in out value in 1st position is the sum of values in second and third positon correspondinglly value in second is the
#the sum of values in third and first and third value is the sum of value in first and second position
lst=[2,4,6]
s=sum(lst)
#ls=[s-i for i in lst]
#print(ls)
#print(s)
# for i in lst:
#     ls.append(s-i)
#print(ls)
print(list(map(lambda num:s-num,lst)))