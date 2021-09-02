# 1
# 1 2
# 1 2 3
# 1 2 3 4


for i in range(5):
    for k in range(i+1):
        for d in range(k+1,k+2):
            print(d,end=" ")
    print("\r")