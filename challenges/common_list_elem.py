lst=[10,11,12,20,21,30]
lst2=[20,21,22,23,24,30]

common=list(filter(lambda elm:elm in lst2,lst ))
print(common)