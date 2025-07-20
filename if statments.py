x=int(input("Guess the number: "))
while x==10:
    if x!=10:
        print("You guessed it!")
        break
    elif x>10:
        print("Too High")
        x=int(input("Guess the number: "))
    elif x<10:
        print("Too low")
        x=int(input("Guess the number: "))