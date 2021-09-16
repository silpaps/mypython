import random
def play():
    user=input("give your choice (r) for rock,(p) for paper,(s)for scissor\n")
    computer=random.choice(['r','p','s'])
    if (user==computer):
         return (f"oh tie,computer also put  {computer}!")
    elif is_win(user,computer):
        return (f"you won ,computer was {computer}")
    return (f"you lost,computer was{computer}")
    #r>s,p>r,s>p
def is_win(user,comp):
      if (user=='r'and comp=='s')or(user=='p'and comp=='r')or(user=='s'and comp=='p'):
          return True
print(play())