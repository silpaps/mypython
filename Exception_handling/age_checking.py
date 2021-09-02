age=int(input("enter your age"))
if age<=18:
    raise Exception("you are not elligible")
else:
    print("elligible")