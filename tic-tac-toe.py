# Print Board
def printTTT(board):
    if len(board) != 9:
        return "Your list must be 9 numbers long"
    
    rowPos = 0
    for i in range(3):
        print(f"{rowPos}        |{rowPos+1}        |{rowPos+2}        ")
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

def checkwin(borad, turn):
    xoro = xoroturn(turn)
    printTTT(board)
    xwin = None
    owin = None
    if board[2] == 1 and board[4] == 1 and board[6] == 1:
        xwin = True
    elif board[0] == 1 and board[6] == 1 and board[8] == 1:
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
    if board[2] == 1 and board[4] == 1 and board[6] == 1:
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
        if xwin:
            return xwin
        else:
            return False
    if xoroturn(turn) == 2:   
        if owin:
            return owin
        else:
            return False
board = [2,2,1,1,1,2,1,1,0]
move = checkmove(board, 1)
turn = 6
checkturn = xoroturn(turn)
win = checkwin(board, turn)
# printTTT(board)
print(win)