list=[6,5,3,7,2,1,4,5,32,78,12,45,17]
def bsearch():
    list.sort()
    print(list)
    ele=int(input("enter the elemnt to found"))
    flag=0
    low=0
    upp=len(list)-1
    while low<=upp:
        mid=(low+upp)//2
        if ele>list[mid]:
            low=mid+1
        elif ele<list[mid]:
            upp=mid-1
        elif ele==list[mid]:
            flag+=1
            break
    if flag==1:
        print("element found")
    else:
        print("element not found")
bsearch()