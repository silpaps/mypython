#       *
#      * *
#     * * *
#    * * * *
s=6
for i in range(5):
    for d in range(s):
             print(end=" ")
    s=s-1
    for k in range(i + 1):
            print("*",end=" ")
    print("\r")

