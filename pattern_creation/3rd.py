# 1
# 2 3
# 4 5 6


    num = 1
    for i in range(5):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print("\r")