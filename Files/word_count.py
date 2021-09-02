d={}
f=open('word','r')
for i in f:
    l=i.split(" ")
    for k in l:
        if k not in d:
            d.update({k:1})
    else:
        val=int(d[k])
        d.update({i: val + 1})
print(d)
# count={}
# f=open('word','r')
# for



