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
    
    printTTT([2,2,1,1,1,2,0,1,0])