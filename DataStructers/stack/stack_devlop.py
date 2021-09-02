# def create(n):
#     s=0
#     while True:
#         global s
#         op=int(input("give the number of option wanted:  1.push  2.pop  3.diplay" ))
#         lis=[]
#         if op==1:
#             while s<n:
#                 elm=int(input("enter the element"))
#                 lis.append(elm)
#                 s=s+1
#                 check=input("do you want to continue -> yes/no")
#                 if check=="no":
#                     break
#         elif op==2:
#             while s>0:
#                 lis.pop()
#                 s=s-1
#                 check = input("do you want to continue -> yes/no")
#                 if check == "no":
#                     break
#
#             else:
#                 print("stack is empty")
#         else:
#             print(lis)
#         check = input("do you want to continue -> yes/no")
#         if check == "no":
#                break
# s=int(input("enter the size of stack"))
# create(s)

#>>>>>>>>>>>>>.....alternate @miss program
stk=[]
size=int(input("enter the size of stack"))
top=0
n=0
def push():
    global top,size
    if (top>size):
        print("stack is full")
    else:
        p=int(input("enter the element you want to push"))
        stk.append(p)
        top+=1
def pop():
    global top,size
    if(top<=0):
        print("stack is esmpty")
    else:
      stk.pop()
    top-=1
def display():
    print(stk)
while(n!=1):
    print("enter the option")
    opt=int(input("1.push, 2.pop, 3.diplay"))
    if(opt==1):
        push()
    elif(opt==2):
        pop()
    else:
        display()
    n=int(input("do you want to continue/press 1 for exit "))