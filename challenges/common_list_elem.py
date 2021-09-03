lst=[10,11,12,20,21,30]
lst2=[20,21,22,23,24,30]

# common=list(filter(lambda elm:elm in lst2,lst ))
# print(common)
pos1=0
pos2=1
if lst[pos1]==lst2[pos2]:
    print(lst[pos1])
    pos1+=1
    pos2+=1
elif lst[pos1]<lst2[pos2]:
     pos1+=1
else:
     pos2+=1

