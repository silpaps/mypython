s={1,2,3,4,5,6,7,8,9,10,11,12,13,15,17,34,37,97}
#s={2,5,7,8,10}
prime=set()
nonprime=set()
for i in s:
    if i>1:
        for k in range(2,i):
            if i%k==0:
                nonprime.add(i)
                break
        else:
            prime.add(i)
print("prime_set",prime)
print("nonprime_set",nonprime)
