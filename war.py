import random

class card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
    def __str__(self):
        return str(self.value)+" of "+self.suit

class deck:
    def __init__(self):
        self.cardlist=[]
    def creatdeck(self):
        for i in range(1,14):
            self.cardlist.append(card("Hearts",i))
        for i in range(1,14):
            self.cardlist.append(card("Clubs",i))
        for i in range(1,14):
            self.cardlist.append(card("Diamonds",i))
        for i in range(1,14):
            self.cardlist.append(card("Spades",i))
    def printdeck(self):
        for i in range(len(self.cardlist)):
            print(self.cardlist[i])
    def shuffledeck(self):
        for i in range(52):
            x=random.randint(0,len(self.cardlist)-1)
            y=random.randint(0,len(self.cardlist)-1)
            a=self.cardlist[y]
            b=self.cardlist[x]
            self.cardlist[x]=a
            self.cardlist[y]=b
    def getlength(self):
        return len(self.cardlist)
    def drawcard(self):
        return self.cardlist.pop()
    def addcard(self,c):
        self.cardlist.append(c)

maindeck=deck()
maindeck.creatdeck()
maindeck.shuffledeck()
wardeck=deck()
playerdeck=deck()
computerdeck=deck()

for i in range(26):
    playerdeck.addcard(maindeck.drawcard())
    computerdeck.addcard(maindeck.drawcard())

for i in range(10):
    player=playerdeck.drawcard()
    print(player)
    computer=computerdeck.drawcard()
    print(computer)
    if player.value<computer.value:
        print("Computer Won The Round!")
        computerdeck.addcard(player)
        computerdeck.addcard(computer)
    if player.value>computer.value:
        print("Player Won The Round!")
        playerdeck.addcard(player)
        playerdeck.addcard(computer)
    if player.value==computer.value:
        wardeck.addcard(player)
        wardeck.addcard(computer)
        print("WAR!!!")
        for i in range(3):
            player
            wardeck.addcard(playerdeck.drawcard())
            computer
            wardeck.addcard(computerdeck.drawcard())
        playerwar=playerdeck.drawcard()
        wardeck.addcard(playerwar)
        computerwar=computerdeck.drawcard()
        wardeck.addcard(computerwar)
        if playerwar.value<computerwar.value:
            print("Computer Won The War!")
            for i in range(8):
                computerdeck.addcard(wardeck.drawcard())
        if playerwar.value>computerwar.value:
            print("Player Won The War!")
            for i in range(8):
                playerdeck.addcard(wardeck.drawcard())
    print(playerdeck.getlength())
    print(computerdeck.getlength())
    print("------------")