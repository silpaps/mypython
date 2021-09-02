# def revert_val(func):#div(2,10)
#     def wrapper(no1,no2):#5,10 wrapper is common,can change,no of parametrs must same
#         if no1<no2:
#             (no1,no2)=(no2,no1)
#             return func(no1,no2)
#         else:
#             return func(no1,no2)
#     return wrapper


# @revert_val
# def div(num1,num2):
#     return num1/num2
# print(div(2,10))
# @revert_val
# def div(num1,num2):
#     return num1-num2
# print(div(1,10))

# def admin_required(func):
#     def wrapper(a,b):
#         if a!="admin":
#             raise Exception("you are not allowed")
#         else:
#             return func(a,b)
#     return wrapper
# @admin_required
# def change_pin(user,pin):
#     mypin=pin
#     return mypin
# @admin_required
# def delete_ac(user,accno):
#     return str(accno)+" "+"delete"
#
#
# print(change_pin("admin",1000))
# print(delete_ac('admin',1000))
def check_elligible(func):
    def wrapper(a,b,c):
        if b<18:
            return "not elligible for vaccine"
        else:
            return func(a,b,c)
    return wrapper
@check_elligible
def eligible_vacc(name,age,place):
    n=name
    return n+" "+"you are elligible for vaccine"
print(eligible_vacc("anu",11,"aaaaa"))