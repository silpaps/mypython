list1=[1,2,33,2,13,12,22,19]
# list1.sort()
# print(list1)
new_list=[]
while list1:
    min=list1[0]
    for i in list1:
        if i < min:
            min=i
    new_list.append(min)
    list1.remove(min)

print(new_list)

