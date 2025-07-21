import random
games=3
c=0
p=0
while games>0:
    comp=random.randint(1,3)
    x=int(input("Rock paper scissors. 1 is rock, 2 is paper and 3 is scissors: "))
    games=games-1
    if (x==1 and comp==2) or (x==2 and comp==3) or (x==3 and comp==1):
        print("Computer Wins the Round!")
        c=c+1
    elif (comp==1 and x==2) or (comp==2 and x==3) or (comp==3 and x==1):
        print("Player Wins the Round!")
        p=p+1
    else:
        print("Tie")
if c>p:
    print("Computer Wins the Game!")
elif p>c:
    print("Player Wins the Game!")
elif p==c:
    print("Tie Game")