def prime(min,max):
    sum=0
    for i in range(min, max + 1):
        if i>1:
            for a in range(2,i):
                if i%a==0:
                    break
            
            else:
                sum+=i
    return sum
# a=int(input("give minimum range"))
# b=int(input("give maximum range"))
print(prime(1,10))

