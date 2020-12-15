from board import *

piece = str

def piecetomove():
    ColourToMove = WHITE
    for row in completeboard:
        for square in row:
            #Find location of white king
            if square[2].get("name") == "k" and square[2].get("pieceColour") == WHITE:
                whitekinglocation = (square[2].get("x"), square[2].get("y"))
                print(whitekinglocation)
            #Finds location of black king
            if square[2].get("name") == "k" and square[2].get("pieceColour") == BLACK:
                blackkinglocation = (square[2].get("x"), square[2].get("y"))
                print(blackkinglocation)
                #Checks whether the colour who is movings king is in check
            if square[2].get("pieceColour") == ColourToMove and square[2].get("check") == True:
                print(f"{ColourToMove} you are in check")
                piece = input("What piece would you like to move?\n")  
            else:
                piece = input(f"{ColourToMove}, what piece would you like to move?\n")  
                checkpiece()

    #Searches board for piece  
    for row in completeboard:
        for square in row:
            piecetype = square[2].get("pieceName")
            x = square[2].get("x")
            y = square[2].get("y")
            if piece == piecetype:
                print(f"Okay, {piecetype} is at {board[x][x]}")

    if ColourToMove == WHITE:
        ColourToMove = BLACK
    else:
        ColourToMove = WHITE

def checkpiece():
    for row in completeboard:
        for square in row:
            if square[2].get("pieceName") == piece:
                pass

def pawnmove():
    for row in completeboard:
        for square in row:
            if square[2].get("name") == "p":
                if square[2].get("moved") == False:
                    if square[2].get("pieceColour") == "White":
                        pass

def checkforcheck():
    pass

def main():
    printannotatedboard()
    print("")
    niceprint(board)
    piecetomove()

main()