a={1,2,3,4,5,6,7,8,9,10,11,12,13,14}
odd=set()
even=set()
for i in a:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(odd)
print(even)