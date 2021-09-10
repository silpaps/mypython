import random
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"give your guess from the range 1 to {x} "))
        if guess<random_number:
            print("sorry you guesses a low number")
        elif guess>random_number:
            print("sorry you guesses high number")
    print(f"YAy you guessed correct number{random_number}.Thank yiu for joining the game")
guess(10)
