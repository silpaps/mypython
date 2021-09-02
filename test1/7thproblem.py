c=input("enter a string")
a="aeiou"
b=" "
for i in c:
    if i not in a:
        b=b+i
print(b)
