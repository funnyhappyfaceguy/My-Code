import random
moves=10
board=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
while moves>0:
    if moves==10:
        for i in range(0,3):
            print(board[i])
    # if moves==1:
    #     moves==0
    x=int(input("Which Row: "))
    y=int(input("Which Column: "))
    while board[x][y]=="o" or board[x][y]=="x":
        x=int(input("Which Row: "))
        y=int(input("Which Column: "))
    board[x][y]="x"
    moves=moves-1
    print("Player's Move: ")
    for i in range(0,3):
        print(board[i])
    if board[0][0]=="x" and board[0][1]=="x" and board[0][2]=="x":
        print("Player Wins!")
        break
    if board[1][0]=="x" and board[1][1]=="x" and board[1][2]=="x":
        print("Player Wins!")
        break
    if board[2][0]=="x" and board[2][1]=="x" and board[2][2]=="x":
        print("Player Wins!")
        break
    if board[0][0]=="x" and board[1][0]=="x" and board[2][0]=="x":
        print("Player Wins!")
        break
    if board[0][1]=="x" and board[1][1]=="x" and board[2][1]=="x":
        print("Player Wins!")
        break
    if board[0][2]=="x" and board[1][2]=="x" and board[2][2]=="x":
        print("Player Wins!")
        break
    if board[0][0]=="x" and board[1][1]=="x" and board[2][2]=="x":
        print("Player Wins!")
        break
    if board[0][2]=="x" and board[1][1]=="x" and board[2][0]=="x":
        print("Player Wins!")
        break
    if moves==1:
        print("Tie Game")
        break
    # if moves==1:
    #     moves==0
    a=random.randint(0,2)
    b=random.randint(0,2)
    while board[a][b]=="o" or board[a][b]=="x":
        a=random.randint(0,2)
        b=random.randint(0,2)
    board[a][b]="o"
    moves=moves-1
    print("Computer's Move: ")
    for i in range(0,3):
        print(board[i])
    if board[0][0]=="o" and board[0][1]=="o" and board[0][2]=="o":
        print("Computer Wins!")
        break
    if board[1][0]=="o" and board[1][1]=="o" and board[1][2]=="o":
        print("Computer Wins!")
        break
    if board[2][0]=="o" and board[2][1]=="o" and board[2][2]=="o":
        print("Computer Wins!")
        break
    if board[0][0]=="o" and board[1][0]=="o" and board[2][0]=="o":
        print("Computer Wins!")
        break
    if board[0][1]=="o" and board[1][1]=="o" and board[2][1]=="o":
        print("Computer Wins!")
        break
    if board[0][2]=="o" and board[1][2]=="o" and board[2][2]=="o":
        print("Computer Wins!")
        break
    if board[0][0]=="o" and board[1][1]=="o" and board[2][2]=="o":
        print("Computer Wins!")
        break
    if board[0][2]=="o" and board[1][1]=="o" and board[2][0]=="o":
        print("Computer Wins!")
        break