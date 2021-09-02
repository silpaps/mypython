# * * * * * *
#  * * * * * *
#   * * * * * *
#    * * * * * *
d=1
for i in range(5):
    for k in range(d):
        print(end=" ")
    d+=1
    for j in range(5,0,-1):
        print("*",end=" ")
    print("\r")