from board import *

def piece_to_move():
    piece = input("What piece would you like to move?\n")

def pawnmove():
    for row in completeboard:
        for square in row:
            if square[2].get("pieceColour") == WHITE:
                if square[2].get("moved") == False:
                    current_coordinate = square[2].get("coordinates")
                    x_coord = current_coordinate[0]
                    y_coord = current_coordinate[1]
                    #Adds double move to move list
                    square[2].get("moves").append((x_coord + 2, y_coord))
                    print(square[2].get("moves"))

def main():
    pawnmove()

main()