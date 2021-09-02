s="hello world hello hello"
b=s.split(" ")
c={}

for i in b:
    if i not in c:
        c.update({i:1})
    else:
        val=int(c[i])
        c.update({i:val+1})
print(c)