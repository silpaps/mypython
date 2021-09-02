list=[[1,2,3],
      [4,5,6],
      [7,8,9]
      ]
#print(len(list))
# for row in range(3):
#     for col in range(3):
#         print(list[row][col])
# for row in list:
#     for col in row:
#         print(col)
# s='AEIOUaeiou'
# txt=input("enter a word")
# t=""
# for i in txt:
#     if i in s:
#         t=t+"g"
#     else:
#         t=t+i
# print("translated word is",t)
# '''
# this is simple program to translate vowels
# '''
# try:
#     num=int(input("enter number"))
#     res=num/0
#     print(res)
# except ZeroDivisionError:
#     print("divide with zero is not possible")
# except ValueError:
#     print("invalid input")
a=set()
# a.add(1)
# a.add(2)
# a.add(3)
print(a)
k={1,2,3,4,5}
for i in k:
    c=i*i
    a.add(c)
    c=0
print(a)