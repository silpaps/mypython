def linsearch(p):
    list1 = [1, 2, 3, 4, 5, 6, 7, 12, 23, 14, 45, 56, 44, 56]
    flag=0
    for i in list1:
        if i==p:
            flag=1
            break
    if flag==1:
        print("presnet")
    else:
        print("not present")


find=int(input("entert the number to find"))
linsearch(find)

