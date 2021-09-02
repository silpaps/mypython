
employees = [
    {"e_id": 1000, "e_name": "ram", "salary": 25000, "department": "testing", "exp": 1},
    {"e_id": 1001, "e_name": "ravi", "salary": 22000, "department": "ba", "exp": 1},
    {"e_id": 1002, "e_name": "raj", "salary": 20000, "department": "mrkt", "exp": 1},
    {"e_id": 1003, "e_name": "nikil", "salary": 26000, "department": "developer", "exp": 1},
    {"e_id": 1004, "e_name": "nivi", "salary": 28000, "department": "developer", "exp": 2},

]
# for employee in employees:
#     #print(employee["e_name"])
#     print(employee["e_name"].upper())
# e_names=list(map(lambda employee:employee["e_name"],employees))
# print(e_names)
# e_upper=list(map(lambda emp:emp["e_name"].upper(),employees))
# print(e_upper)


#print employ name whos dept is developer
# for employee in employees:
#     if employee["department"]=="developer":
#          #print(employee["e_name"])
#          print(employee["e_name"].upper())
developers=list(filter(lambda emp:emp["department"]=="developer",employees))
dev=list(map(lambda devp:devp["e_name"],developers))
print(dev)
#total salary
# total=0
# for employee in employees:
#     total+=employee["salary"]
# print(total)
salary=sum(list(map(lambda emp:emp["salary"],employees)))
print(salary)
#1case map
#2case filter
#3case reduce
#map function
lst=[1,2,3,4]
# def square(num):
#     return num**2
# squares=list(map(square,lst))
# print(squares)
# cube=list(map(lambda num:num**3,lst))
# print(cube)
#filter
even=list(filter(lambda n:n%2==0,lst))
print(even)
def odd(n):
    if n%2!=0:
        return n
odds=list(filter(odd,lst))
print(odds)
odds=list(filter(lambda n:n%2!=0,lst))
print(odds)
#reduce
from functools import reduce
lst=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,lst)
print(sum)
largets=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(largets)
