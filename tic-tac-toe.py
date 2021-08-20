# Print Board
def printTTT(board):
    if len(board) != 9:
        return "Your list must be 9 numbers long"
    
    rowPos = 0
    for i in range(3):
        print(f"{rowPos+1}        |{rowPos+2}        |{rowPos+3}        ")
        print("    ", end="")
        if board[rowPos] == 1:
            print("x", end="")
        elif board[rowPos] == 2:
            print("o", end="")
        elif board[rowPos] == 0:
            print(" ", end="")
        print("    |", end="")

        print("    ", end="")
        if board[rowPos+1] == 1:
            print("x", end="")
        elif board[rowPos+1] == 2:
            print("o", end="")
        elif board[rowPos+1] == 0:
            print(" ", end="")
        print("    |", end="")

        print("    ", end="")
        if board[rowPos+2] == 1:
            print("x", end="")
        elif board[rowPos+2] == 2:
            print("o", end="")
        elif board[rowPos+2] == 0:
            print(" ", end="")
        print("    ")

        print("         |         |        ")
        print(" ---------------------------")
        rowPos+=3

def checkmove(board, move):
    moveindex = move-1
    if moveindex < 0 or moveindex > 8:
        return False
    elif board[moveindex] == 0:
        return True
    else:
        return False
def xoroturn(turn):
    if (turn % 2) != 0:
        return 1
    else:
        return 2

def checkwin(board, turn):
    xoro = xoroturn(turn)
    xwin = None
    owin = None
    # [1, 0, 1
    #  0, 1, 0
    #  1, 0, 0
    # ]
    if board[2] == 1 and board[4] == 1 and board[6] == 1:
        xwin = True
    elif board[0] == 1 and board[4] == 1 and board[8] == 1:
        xwin = True
    elif board[0] == 1 and board[3] == 1 and board[6] == 1:
        xwin = True
    elif board[1] == 1 and board[4] == 1 and board[7] == 1:
        xwin = True
    elif board[2] == 1 and board[5] == 1 and board[8] == 1:
        xwin = True
    elif board[0] == 1 and board[1] == 1 and board[2] == 1:
        xwin = True
    elif board[3] == 1 and board[4] == 1 and board[5] == 1:
        xwin = True
    elif board[6] == 1 and board[7] == 1 and board[8] == 1:
        xwin = True
    elif board[2] == 2 and board[4] == 2 and board[6] == 2:
        xwin = True
    elif board[0] == 2 and board[6] == 2 and board[8] == 2:
        owin = True
    elif board[0] == 2 and board[3] == 2 and board[6] == 2:
        owin = True
    elif board[1] == 2 and board[4] == 2 and board[7] == 2:
        owin = True
    elif board[2] == 2 and board[5] == 2 and board[8] == 2:
        owin = True
    elif board[0] == 2 and board[1] == 2 and board[2] == 2:
        owin = True
    elif board[3] == 2 and board[4] == 2 and board[5] == 2:
        owin = True
    elif board[6] == 2 and board[7] == 2 and board[8] == 2:
        owin = True
    printTTT(board)
    
    if xoroturn(turn) == 1:   
        if xwin == True:
            return "xwins"
        else:
            return False
    if xoroturn(turn) == 2:   
        if owin:
            return "owins"
        else:
            return False

def makemove(board, pos, turn):
    cBoard = board.copy()
    if checkmove(board, pos):
        move = pos-1
        if xoroturn(turn) == 1:
            cBoard[move] = 1
        else:
            cBoard[move] = 2
        return cBoard
    else:
        print("Not a vaild move")

board = [0,0,0,0,0,0,0,0,0]
turn = 1
def playTTT():
    board = [0,0,0,0,0,0,0,0,0]
    turn = 1
    for i in range(10):
        if turn == 10:
            print("It is a draw!")
            break

        if xoroturn(turn) == 1:
            print("X's Turn")
            Xmove = input("What is you move?")
            while Xmove == "":
                Xmove = input("Sorry, you need to enter a number. What is you move?")
            Xmove = int(Xmove)
            if checkmove(board, Xmove) == False:
                while checkmove(board, Xmove) == False:
                        Xmove = input(f"Sorry square {Xmove} is already filled. What is you move?")
                        Xmove = int(Xmove)
            board = makemove(board, Xmove, turn)
            printTTT(board)    
        else:
            print("O's Turn")
            Omove = input("What is you move?")
            while Xmove == "":
                Xmove = input("Sorry, you need to enter a number. What is you move?")
            Omove = int(Omove)
            if checkmove(board, Omove) == False:
                while checkmove(board, Omove) == False:
                        Omove = input(f"Sorry square {Omove} is already filled. What is you move?")
                        Omove = int(Omove)
            board = makemove(board, Omove, turn)
            printTTT(board)
        win = checkwin(board, turn)
        if checkwin(board, turn) == "xwins":
            print("X has won the game!!!")
            break
        elif checkwin(board, turn) == "owins":
            print("O has won the game!!!")
            break
        turn+=1