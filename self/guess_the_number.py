#user guess the number of computer

# import random
# def guess(x):
#     random_number=random.randint(1,x)
#     guess=0
#     while guess!=random_number:
#         guess=int(input(f"give your guess from the range 1 to {x} "))
#         if guess<random_number:
#             print("sorry you guesses a low number")
#         elif guess>random_number:
#             print("sorry you guesses high number")
#     print(f"YAy you guessed correct number{random_number}.Thank yiu for joining the game")
# guess(10)

#computer guess the number of user
import random
def guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low #it canbe high because low==high
        feedback=input(f"Is the {guess} too high then enter (h),if {guess} too low then enter (l),if {guess}correct then (c)")
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
           low =guess+1
    print("yay computer guessed the number correctly ")

guess(100)



