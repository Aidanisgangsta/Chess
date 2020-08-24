import moves

BOARDSIZE = 8
WHITE = "White"
BLACK = "Black"
BLANK = "."
ANNOBLANK = ". "

board = []
completeboard = []

def printrow(lst):
    for row in lst:
        print(row)

def niceprint(lst):
    for row in lst:
        for square in row:
            xcoord = square[0]
            ycoord = square[1]
            print(f"{xcoord}{ycoord}", end =" ")
        print("")

def printbool():
    for row in board:
        for square in row:
            print(f"{square[2]}", end =" ")
        print("")

def fullboard():
    #Creates default values for each piece
    pawn = {
    "name": "p",
    "coordinates": (0, 0),
    "pieceName": "",
    "pieceColour": "",
    "moved": False,
    "isCaptured": False,
    "attacking": []
    }

    rook = {
    "name": "r",
    "coordinates": (0, 0),
    "pieceName": "",
    "pieceColour": "",
    "isCaptured": False,
    "attacking": []
    }

    bishop = {
    "name": "b",
    "coordinates": (0, 0),
    "pieceName": "",
    "pieceColour": "",
    "isCaptured": False,
    "attacking": []
    }

    knight = {
    "name": "n",
    "coordinates": (0, 0),
    "pieceName": "",
    "pieceColour": "",
    "isCaptured": False,
    "attacking": []
    }

    queen = {
    "name": "q",
    "coordinates": (0, 0),
    "pieceName": "",
    "pieceColour": "",
    "isCaptured": False,
    "attacking": []
    }

    king = {
    "name": "k",
    "coordinates": (0, 0),
    "pieceName": "",
    "pieceColour": "",
    "isCaptured": False,
    "attacking": [],
    "check": False
    }

    #Creates a board with a dictionary incase a piece occupies the square
    def createfullboard():
        for x in range(BOARDSIZE-1, -1, -1):
            fullrow = []
            for y in range(0, BOARDSIZE):        
                fullrow.append([x,y, {}])
            completeboard.append(fullrow)

    #Adds pawns to their proper locations
    def addpawns():
        for row in completeboard:
            for square in row:
                if square[0] == 1:
                    #Changes the details of the default pawn dictionary
                    addpawn = pawn
                    addpawn.update({"coordinates": (square[0], square[1])})
                    addpawn.update({"pieceName": f"p{square[1] + 1}"})
                    addpawn.update({"pieceColour": WHITE})
                    square[2].update(addpawn)
                if square[0] == 6:
                    addpawn = pawn
                    addpawn.update({"coordinates": (square[0], square[1])})
                    addpawn.update({"pieceName": f"p{square[1] + 1}"})
                    addpawn.update({"pieceColour": BLACK})
                    square[2].update(addpawn)
                    
    def addrooks():
        for row in completeboard:
            for square in row:
                if square[0] == 0 and square[1] == 0 or square[0] == 0 and square[1] == 7:
                    #Changes the details of the default rook dictionary
                    addrook = rook
                    addrook.update({"coordinates": (square[0], square[1])})
                    addrook.update({"pieceName": f"r{square[1] + 1}"})
                    addrook.update({"pieceColour": WHITE})
                    square[2].update(addrook)
                if square[0] == 7 and square[1] == 0 or square[0] == 7 and square[1] == 7:
                    addrook = rook
                    addrook.update({"coordinates": (square[0], square[1])})
                    addrook.update({"pieceName": f"r{square[1] + 1}"})
                    addrook.update({"pieceColour": BLACK})
                    square[2].update(addrook)

    def addknights():
        for row in completeboard:
            for square in row:
                if square[0] == 0 and square[1] == 1 or square[0] == 0 and square[1] == 6:
                    #Changes the details of the default rook dictionary
                    addknight = knight
                    addknight.update({"coordinates": (square[0], square[1])})
                    addknight.update({"pieceName": f"n{square[1] + 1}"})
                    addknight.update({"pieceColour": WHITE})
                    square[2].update(addknight)
                if square[0] == 7 and square[1] == 1 or square[0] == 7 and square[1] == 6:
                    addknight = knight
                    addknight.update({"coordinates": (square[0], square[1])})
                    addknight.update({"pieceName": f"n{square[1] + 1}"})
                    addknight.update({"pieceColour": BLACK})
                    square[2].update(addknight)

    def addbishops():
        for row in completeboard:
            for square in row:
                if square[0] == 0 and square[1] == 2 or square[0] == 0 and square[1] == 5:
                    #Changes the details of the default rook dictionary
                    addbishop = bishop
                    addbishop.update({"coordinates": (square[0], square[1])})
                    addbishop.update({"pieceName": f"b{square[1] + 1}"})
                    addbishop.update({"pieceColour": WHITE})
                    square[2].update(addbishop)
                if square[0] == 7 and square[1] == 2 or square[0] == 7 and square[1] == 5:
                    addbishop = bishop
                    addbishop.update({"coordinates": (square[0], square[1])})
                    addbishop.update({"pieceName": f"b{square[1] + 1}"})
                    addbishop.update({"pieceColour": BLACK})
                    square[2].update(addbishop)

    def addqueens():
        for row in completeboard:
            for square in row:
                if square[0] == 0 and square[1] == 3:
                    #Changes the details of the default rook dictionary
                    addqueen = queen
                    addqueen.update({"coordinates": (square[0], square[1])})
                    addqueen.update({"pieceName": f"q{square[1] + 1}"})
                    addqueen.update({"pieceColour": WHITE})
                    square[2].update(addqueen)
                if square[0] == 7 and square[1] == 3:
                    addqueen = queen
                    addqueen.update({"coordinates": (square[0], square[1])})
                    addqueen.update({"pieceName": f"q{square[1] + 1}"})
                    addqueen.update({"pieceColour": BLACK})
                    square[2].update(addqueen)

    def addkings():
        for row in completeboard:
            for square in row:
                if square[0] == 0 and square[1] == 4:
                    #Changes the details of the default rook dictionary
                    addking = king
                    addking.update({"coordinates": (square[0], square[1])})
                    addking.update({"pieceName": f"k{square[1] + 1}"})
                    addking.update({"pieceColour": WHITE})
                    square[2].update(addking)
                if square[0] == 7 and square[1] == 4:
                    addking = king
                    addking.update({"coordinates": (square[0], square[1])})
                    addking.update({"pieceName": f"k{square[1] + 1}"})
                    addking.update({"pieceColour": BLACK})
                    square[2].update(addking)

    def addpieces():
        createfullboard()
        addpawns()
        addrooks()
        addbishops()
        addknights()
        addqueens()
        addkings()

    addpieces()

#Creates a def
def createboard():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for x in range(BOARDSIZE-1, -1, -1):
        y_row = []
        for y in range(0, BOARDSIZE):
            letter = letters[x]
            #Checks for whether a piece is occupying each square
            if completeboard[x][y][2] == {}:
                notation = [letter, y + 1, False]
            else:
                notation = [letter, y + 1, True]
            y_row.append(notation)
        board.append(y_row)

#Prints board with only piece type
def printboard():
    for row in completeboard:
        for square in row:
            piecetype = square[2].get("name")
            piececolour = square[2].get("pieceColour")
            if piecetype == None:
                print(BLANK, end =" ")
            else:
                if piececolour == WHITE:
                    uppercase = f"{piecetype.upper()}"
                    print(uppercase, end =" ")
                else:
                    print(piecetype, end =" ")
        print("")

#Prints board with each piece ID
def printfullboard():
    for row in completeboard:
        for square in row:
            piecetype = square[2].get("pieceName")
            piececolour = square[2].get("pieceColour")
            if piecetype == None:
                print(ANNOBLANK, end =" ")
            else:
                if piececolour == WHITE:
                    uppercase = f"{piecetype.upper()}"
                    print(uppercase, end =" ")
                else:
                    print(piecetype, end =" ")
        print("")

def printannotatedboard():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    rownum = 1
    for row in completeboard:
        print(rownum, end =" ")
        for square in row:
            piecetype = square[2].get("pieceName")
            piececolour = square[2].get("pieceColour")
            if piecetype == None:
                print(ANNOBLANK, end =" ")
            else:
                if piececolour == WHITE:
                    uppercase = f"{piecetype.upper()}"
                    print(uppercase, end =" ")
                else:
                    print(piecetype, end =" ")
        rownum += 1
        print("")
    #Prints file letter
    print(" ", end =" ")
    for i in range(BOARDSIZE):            
        print(f"{letters[i]} ", end =" ")

#Creates board with all pieces
fullboard()
#Creates a notation board
createboard()

moves