import random
number=random.randint(1,10)
guess=5
while guess>0:
    x=int(input("Guess the number: "))
    guess=guess-1
    if x>number:
        print("Too high")
    elif x<number:
        print("Too Low")
    elif x==number:
        print("You Win!")
        break
if guess==0:
    print("You Lose!")