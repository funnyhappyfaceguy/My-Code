import random
number=random.randint(1,10)
print(number)
x=int(input("Guess the number: "))
guess=4

while guess>0:
    if x>number:
        print("Too high")
        x=int(input("Guess the number: "))
        guess=guess-1
    elif x<number:
        print("Too Low")
        x=int(input("Guess the number: "))
        guess=guess-1
    elif x==number:
        print("You Win!")
        break
print("You Lose!")