s={2,3,4,5,6,7,8}
d={1,4,6,18,11,13}
common=set()
for i in s:
    if i in d:
        common.add(i)
print(common)