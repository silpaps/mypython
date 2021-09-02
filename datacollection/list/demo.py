# lst=[1,2,3,4,5]
# print(lst)
#1follow order
# s=[1,1,2,2]
# print(s)
#2allow dulicate data
#print(type(s))
#3 hetrogenous
# c=[1,3,"true",True,False]
# print(c)
# list1=[1,2,3,4,5,6]
# for i in list1:
#     print(i)
# list1=[]
# list1.append(1)
# list1.append(2)
# print(list1)

# lim=int(input("enter the limit"))
# lis=[]
# for i in range(lim):
#     c=input("enter the item")
#     lis.append(c)
# print(lis)

#nesting possible
# lis=[1,1,8,[4,5,7,[68,9,5],14]]
# print(lis)
#list is mutable

# lis=[1,2,3]
# lis.remove(2)
# print(lis)
# lis.clear
# del lis
# print(lis)
#list slicing
lis=[1,2,3,4,5,6,7,8,9,10,11,12]
print(lis[1:4])
print(lis[1:])
print(lis[:4])
print(lis[1:4:2])# index 1 to  index 4 with increment 2
print(lis[::-1])
print(lis[:])

#>>>>>>>extend

# lis=[1,2,3,4,5]
# a=['a','b','c']
# lis.extend(a)
# print(lis)
# lis.append(a)#whwn using append list 'a' is added as another element into list 'lis', but when using extend 'lis'
# # is extended with elements in 'a'
#print(lis)

#>>>>>>>>>>> spliting
# a="hello , world"
# b=a.split(",")
# print(b)
# for i in b:
#     print(i)
#
# list.pop()# delete last element
# list.insert(1,5)#(insert(position,value)