s=input("enter a string")
v='aeiou'
c=0
for i in s:
    if i in v:
        c=c+1

print(c)