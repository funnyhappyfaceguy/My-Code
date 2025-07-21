import random
moves=9
board=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
while moves>0:
    for i in range(0,3):
        print(board[i])
    x=int(input("Which Row: "))
    y=int(input("Which Column: "))
    while board[x][y]=="o" or board[x][y]=="x":
        x=int(input("Which Row: "))
        y=int(input("Which Column: "))
    board[x][y]="x"
    a=random.randint(0,2)
    b=random.randint(0,2)
    while board[a][b]=="o" or board[a][b]=="x":
        a=random.randint(0,2)
        b=random.randint(0,2)
    board[a][b]="o"
