# stk=[]
# size=int(input("enter the size of queue"))
# top=0
# n=0
# def nqueue():
#     global top,size
#     if (top>=size):
#         print("queue is fill")
#     else:
#         elm=int(input("enter the elemnet to add into queue"))
#         stk.append(elm)
#         top=top+1
# def dqueue():
#     global top,size
#     if (top<=0):
#         print("queue is empty")
#     else:
#         elm=stk[0]
#         stk.remove(elm)
#         top=top-1
# def display():
#     print(stk)
# while(n!=1):
#     print("enter the option")
#     opt=int(input("1.nqueue, 2.dqueue, 3.diplay"))
#     if(opt==1):
#         nqueue()
#     elif(opt==2):
#         dqueue()
#     else:
#         display()
#     n=int(input("do you want to continue/press 1 for exit "))
que=[]
front=0
rear=0
size=int(input("enter the size of queue"))
n=0
def insert():
    global front,rear,size,que
    if(rear>=size):
        print("queue is fill")
    else:
        p=int(input("enter the element want to insert"))
        que.insert(rear,p)
        rear+=1
    for i in range(front,rear):
        print(que[i])
def delete():
    global front, rear, size, que
    if (front==rear):
        print("queue is empty")
    else:
        front+=1
        for i in range(front,rear):
            print(que[i])
while(n!=1):
    print("enter the option")
    opt=int(input("1.insert, 2.delete"))
    if(opt==1):
        insert()
    elif(opt==2):
        delete()
    n=int(input("do you want to continue/press 1 for exit "))

