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
        for i in range(52):
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
        return str(len(self.cardlist))+" cards in the deck"
    def drawcard(self):
        return "You drew a "+str(self.cardlist.pop())
    
d=deck()
d.creatdeck()
d.shuffledeck()
d.printdeck()
print(d.getlength())
print(d.drawcard())