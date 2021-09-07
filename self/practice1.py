# friends=["jungkook","RM","jimin","jin","tea","jhope","suga"]
# for i in range(len(friends)):
#     print(friends[i])
# def raise_pow(base_num,pow_num):
#     result=1
#     for i in range(pow_num):
#         result=result*base_num
#     return result
# print(raise_pow(2,3))
# q=[1,2,3,4,5,6,7]
# def squ(s):
#     for i in s:
#         print(i**2)
# squ(q)
# s="asdfg"
# for i in s:
#     s.index(i)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>string formatting
# input=incredible
#output=in... in... incredible?


# def stutter(word):
# 		return '{0}... {0}... {1}?'.format(word[:2], word)
# word=stutter("incredible")
# print(word)
#in... in... incredible?

# def stutter(word):
# 	return (2*(word[:2]+'... '))+word+'?'
# word=stutter("incredible")
# print(word)
#in... in... incredible?

# def stutter(word):
# 	return word[0:2] + '... ' + word[0:2] + '... ' + word + '?'

#stutter = lambda w: '{}... {}... {}?'.format(w[:2], w[:2], w)
# s='{0}{1}{2}'.format("a","b","c")
# print(s)

def calculator(num1, op, num2):
    if op=="+":
             re=num1+num2
             return re
    elif op=="-":
             re=num1-num2
             return re
    elif op=="*":
             re=num1*num2
             return re
    else:
         if num2==0:
                 return "cant divide with zero"

         else:
                 re = num1 / num2
                 return re

res=calculator(10,"/",0)
print(res)