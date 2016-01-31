import random

left = [7,4,1]
vert = [8,5,2]
right = [9,6,3]
top = [7,8,9]
mid = [4,5,6]
bottom = [1,2,3]
d1 = [7,5,3]
d2 = [9,5,1]

combos = [left, vert, right, top, mid, bottom, d1, d2]

def printBoard(board):
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("\n\n")

def playerTurn(board, playerChar, combos):
    playerMove = int( input("Enter move: ") )
    if board[playerMove] == ' ':
        board[playerMove] = playerChar
    printBoard(board)
    
    playerScore = getScore(playerChar, board, combos)
    if 3 in playerScore:
        return 1
    
    

def compMove (board, compChar, playerChar):
    compScore = getScore(compChar, board, combos)
    playerScore = getScore(playerChar, board, combos)

    #Check if player already won
    if 3 in playerScore:
        return [0,1]

    #Make winning move
    for i in range (len(compScore)):
        if compScore[i] == 2 and playerScore[i] == 0:
            index = findEmpty(board, combos, i)
            if index != 0:
                print('win')
                return [index,-1]

    #Block player winning move
    for i in range (len(compScore)):
        if playerScore[i] == 2:
            index = findEmpty(board, combos, i)
            if index != 0:
                print('block')
                return [index,0]

    #Take corners
    corners  = [1,3,9,7]
    openCorners = []
    for i in range( len(corners)):
        if board[ corners[i] ] == " ":
            openCorners.append( corners[i] )
    if len(openCorners) != 0:
        i = random.randrange( 0,len(openCorners) )
        print('corner')
        return [openCorners[i],0]

    #Take center
    if board[5] == " ":
        print('center')
        return [5,0]

    #Take sides
    sides  = [2,6,8,4]
    openSides = []
    for i in range( len(sides)):
        if board[ sides[i] ] == " ":
            openSides.append( sides[i] )
    if len(openSides) != 0:
        i = random.randrange( 0,len(openSides) )
        print('side')
        return [openSides[i],0]

    return [0,2]
    
def getScore(char, board, combos):
    score = [0] * 8
    for i in range(len(combos)):
        for j in range (0,3):
            if board[combos[i][j] ] == char:
                score[i] = score[i] + 1
    return score

def findEmpty(board, combos, comboIndex):
    for i in combos[comboIndex]:
        if board[i] == " ":
            return i    
    return 0

def compTurn(board, compChar, playerChar, combos):
    [move, status] = compMove(board, compChar, playerChar)
    if move != 0:
        board[move] = compChar
        printBoard(board)
    return status

#main
again = 'y'
playerChar = input("'x' or 'o'? ")
if playerChar == 'x':
    compChar = 'o'
else:
    compChar = 'x'

while again == 'y':
    status = 0
    board = [' '] * 10
    while status == 0:
        status = playerTurn(board, playerChar, combos)
        status = compTurn(board, compChar, playerChar, combos)

    if status == 1:
        print("Player wins")
    if status == -1:
        print("Computer wins")
    if status == 2:
        print("Draw")

    again = input("Play again? (y/n) ")
    
