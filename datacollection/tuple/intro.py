# tup1=(1,2,3,4,5)
# print(type(tup1))
# print(tup1)
# tup1=1,2,3,4,5
# print(type(tup1))
# print(tup1)
# immutable
# keeps order
# support duplicate data
# hetrogenious
# nesting possible
#tp=(1,2,3,4,5,(1,2,3,4),"hello")
# print(tp)
# for i in tp:
#     print(i)
#
# print(tp[1])
# print(tp[1:5])
# c=tp[3]
# print(c)
# print("max", max(tup1))
# print("min", min(tup1))
# print("len", len(tup1))
#tuple with one element
# a=(2,)#must add comma after one element
# print(type(a))
# tuple_1=()#empty tuple
# print(type(tuple_1))
#>>>>>>>>tuple unpacking
# tp=1,3,"tg"
# a,s,d=tp
# print(a)
# print(s)
# print(d)
#>>>>>>>>>>>>>>>>>>>
# t=(1,2,3,4,5)
# i1,*i2,i3=t
# print(i1)
# print(i3)
# print(i2)
# print(*i2)
#>>>>>>>>>>>>>>
# import  sys
# my_list=[0,1,1,'hello',True]
# my_tuple=(0,1,1,'hello',True)
# print(sys.getsizeof(my_list),"bytes")
# print(sys.getsizeof(my_tuple),"bytes")
#tuple takes less size

#>>>>>>>>>>>>>>>>>>>>>>>>>>
import  timeit
print(timeit.timeit(stmt="[0,1,2,3,4]",number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4)",number=1000000))
#tuple needs lesstime to create