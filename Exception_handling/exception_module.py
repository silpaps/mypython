lis=[1,2,3,4,5,6]
ind=int(input("give the index if element you want to print"))
try:
    print(lis[ind])
except Exception as e:
    print(e.args)
finally:
    print("inside")