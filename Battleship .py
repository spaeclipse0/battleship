import random
def mainmenu():
    loop=True
    print('''
´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´
''')
    while loop:
        try:
            print("Press a to start the game \nPress b to display the highscore \nPress c to delete the highscore \nPress d to exit the game\n")
            ans=input()
            if ans =="a":
                return diff()
            elif ans=="b":
                displayscore()
                loop=False
            elif ans=="c":
                deletescore()
                loop=False
            elif ans=="d":
                print("Thanks you and see you next time")
                loop=False
            else:
                print("Not valid choice try again")
        except ValueError:
            print("Please enter a,b,c or d")
        return mainmenu()

def diff():
    try:
        difficulty = int(input("What difficulty would you like to play? (1=Beginner/2=Intermediate/3=Advance) "))
        if difficulty == "1":
            beginner()
        else:
            if difficulty == "2":
                intermediate()
            else:
                advanced()
    except:
        print("Please enter 1,2 or 3")
        return diff()
            
def display():
    displayBoard = []
    for i in range(20):
        displayBoard.append(["#"]*60)
    booms = 1
    shipCounter = 0
    while booms <= 15:
        if shipCounter == 5:
            count = 1
            while count <= 6:
                if count == 6:
                    print ((" "*9), count, sep="")
                    count += 1
                else:
                    print ((" "*9), count, sep="", end="")
                    count += 1

            countPrint = 1
            count = 1
            while count <= 60:
                if count == 60:
                    countPrint = 0
                    print (countPrint,sep="")
                else:
                    if countPrint == 10:
                        countPrint = 0
                        print (countPrint,end="")
                    else:
                        print (countPrint,end="")
                countPrint += 1
                count += 1

            countRow = 1
            for row in displayBoard:
                print("".join(row), countRow)
                countRow += 1
            print ("You've sunk my battleship!")
            attempts = booms
            booms = 16
        else:
            count = 1
            while count <= 6:
                if count == 6:
                    print ((" "*9), count, sep="")
                    count += 1
                else:
                    print ((" "*9), count, sep="", end="")
                    count += 1

            countPrint = 1
            count = 1
            while count <= 60:
                if count == 60:
                    countPrint = 0
                    print (countPrint,sep="")
                else:
                    if countPrint == 10:
                        countPrint = 0
                        print (countPrint,end="")
                    else:
                        print (countPrint,end="")
                countPrint += 1
                count += 1

            countRow = 1
            for row in displayBoard:
                print("".join(row), countRow)
                countRow += 1
            try:
                userRow, userCol = map(int, input("Enter row and col: ").split())              
                if userRow < 1 or userRow > 20 or userCol < 1 or userCol > 60:
                    print ("Sorry, this ocean isn't that big.")
                    continue
            except ValueError:
                print("Sorry, I don't understand that.")
                continue
            else:
                booms += 1
                bombed = board[userRow-1][userCol-1]
                if bombed == 5:
                    print ("You've already bombed that ship.")
                else:
                    if bombed == 6:
                        print ("You've already know there isn't a ship there.")
                    else:
                        if bombed >= 1 and bombed <= 4:
                            shipCounter += 1
                            print ("You've sunk my battleship!")
                            shipIndex = []
                            for n, i in enumerate(board[userRow-1]):
                                if i == bombed:
                                    shipIndex.append(board[userRow-1].index(i))
                                    board[userRow-1][n] = 5
                                    for i in shipIndex:
                                        displayBoard[userRow-1][n] = "O"
                        else:
                            print ("You missed!")
                            board[userRow-1][userCol-1] = 6
                            displayBoard[userRow-1][userCol-1] = " "


def beginner():
    board = []
    row = 1
    probability = [0,1,0,2,0,3,0,4,0]
    ship = 80

    while row <= 20:
        rowBoard = []
        column = 1
        while column <= 60:
            surprise = random.choice(probability)
            if ship == 0:
                rowBoard.append(0)
                column += 1
            else:
                if surprise >= 1 and surprise <= 4 and surprise in rowBoard:
                    column = column
                else:
                    if surprise == 0:
                        rowBoard.append(surprise)
                        column += 1
                    else:
                        if surprise >= 1 and surprise <= 4:
                            for i in range(5):
                                rowBoard.append(surprise)
                        column += 5
                        ship -= 1

    board.append(rowBoard)
    row += 1

#intermediate mode

def intermediate():
    board = []
    row = 1
    probability = [0,0,0,0,1,0,0,0,0,2,0,0,0,0,0,3,0,0,0]
    ship = 50

    while row <= 20:
        rowBoard = []
        column = 1
        while column <= 60:
            surprise = random.choice(probability)
            if ship == 0:
                rowBoard.append(0)
                column += 1
            else:
                if surprise >= 1 and surprise <= 3 and surprise in rowBoard:
                    column = column
                else:
                    if surprise == 0:
                        rowBoard.append(surprise)
                        column += 1
                    else:
                        if surprise >= 1 and surprise <= 3:
                            for i in range(5):
                                rowBoard.append(surprise)
                        column += 5
                        ship -= 1

        board.append(rowBoard)
        row += 1

    ####################display time########################
    displayBoard = []

    for i in range(20):
            displayBoard.append(["#"]*60)

    booms = 0
    shipCounter = 0
    while booms <= 15:
        if shipCounter == 5:
            count = 1
            while count <= 6:
                if count == 6:
                    print ((" "*9), count, sep="")
                    count += 1
                else:
                    print ((" "*9), count, sep="", end="")
                    count += 1

            countPrint = 1
            count = 1
            while count <= 60:
                if count == 60:
                    countPrint = 0
                    print (countPrint,sep="")
                else:
                    if countPrint == 10:
                        countPrint = 0
                        print (countPrint,end="")
                    else:
                        print (countPrint,end="")
                countPrint += 1
                count += 1

            countRow = 1
            for row in displayBoard:
                print("".join(row), countRow)
                countRow += 1
                print ("You've sunk my battleship!")
                attempts = booms
                booms = 16
            else:
                count = 1
                while count <= 6:
                    if count == 6:
                        print ((" "*9), count, sep="")
                        count += 1
                    else:
                        print ((" "*9), count, sep="", end="")
                        count += 1

                countPrint = 1
                count = 1
                while count <= 60:
                    if count == 60:
                        countPrint = 0
                        print (countPrint,sep="")
                    else:
                        if countPrint == 10:
                            countPrint = 0
                            print (countPrint,end="")
                        else:
                            print (countPrint,end="")
                    countPrint += 1
                    count += 1

                countRow = 1
                for row in displayBoard:
                    print("".join(row), countRow)
                    countRow += 1
                try:
                    userRow, userCol = map(int, input("Enter row and col: ").split())              
                    if userRow < 1 or userRow > 20 or userCol < 1 or userCol > 60:
                        print ("Sorry, this ocean isn't that big.")
                        continue
                except ValueError:
                    print("Sorry, I don't understand that.")
                    continue
                else:
                    booms += 1
                    bombed = board[userRow-1][userCol-1]
                    if bombed == 4:
                        print ("You've already bombed that ship.")
                    else:
                        if bombed == 5:
                            print ("You've already know there isn't a ship there.")
                        else:
                            if bombed >= 1 and bombed <= 3:
                                shipCounter += 1
                                print ("You've sunk my battleship!")
                                shipIndex = []
                                for n, i in enumerate(board[userRow-1]):
                                    if i == bombed:
                                        shipIndex.append(board[userRow-1].index(i))
                                        board[userRow-1][n] = 4
                                        for i in shipIndex:
                                            displayBoard[userRow-1][n] = "O"
                            else:
                                print ("You missed!")
                                board[userRow-1][userCol-1] = 5
                                displayBoard[userRow-1][userCol-1] = " "


    #advanced mode

def advanced(): 
    board = [] 
    row = 1
    probability = [0,0,0,1,0,0,0,0,0,0,0,0]
    ship = 20
    shipCount = 0

    while row <= 20: 
        rowBoard = []
        column = 1
        while column <= 60:
            surprise = random.choice(probability)
            if ship == 0:
                rowBoard.append(0)
                column += 1
            else:
                if (surprise == 1) and (surprise in rowBoard):
                    column = column
                else:
                    if surprise == 0:
                        rowBoard.append(surprise)
                        column += 1
                    else:
                        if surprise == 1:
                            for i in range(5):
                                rowBoard.append(surprise)
                            column += 5
                            ship = ship - 1
                            shipCount += 1

        board.append(rowBoard)
        row += 1

    ###########################################display##############################################
    displayBoard = []

    for i in range(20): 
        displayBoard.append(["#"]*60)
        
    booms = 0
    shipCounter = 0
    while booms <= 15:
        if shipCounter == 5:
            attempts = booms #later display number of attempts made
            booms = 16 #to exit loop
        else:
            count = 1 
            while count <= 6:
                if count == 6:
                    print ((" "*9), count, sep="")
                    count += 1 #prints numbers for broad column
                else:
                    print ((" "*9), count,sep="",end="")
                    count += 1

            countPrint = 1
            count = 1
            while count <= 60:
                if count == 60:
                    countPrint = 0
                    print(countPrint,sep="")
                else:
                    if countPrint == 10:
                        countPrint = 0
                        print (countPrint,end="") #prints numbers for narrow column
                    else:
                        print (countPrint,end="")
                countPrint += 1
                count += 1

            countRow = 1
            for row in displayBoard:
                print ("".join(row), countRow)
                countRow += 1

            try:
                userRow, userCol = map(int, input("Enter row and column: ").split()) #users input
            except ValueError:
                print ("Sorry, I don't understand that.")
                continue
            else:
                if board[userRow-1][userCol-1] == 2: 
                    print ("You've already bombed that ship.")
                else:
                    if board[userRow-1][userCol-1] == 3:
                        print ("You already know there isn't a ship there.")
                    else:
                        if board[userRow-1][userCol-1] == 1: #if position chosen == 1 in board
                            print ("You've sunk my battleship")
                            shipIndex = [] #initialize index list to use for display board
                            for n, i in enumerate(board[userRow-1]): #for the row specificed by user in board list
                                if i == 1:
                                    shipIndex.append(board[userRow-1].index(i))
                                    board[userRow-1][n] = 2
                                    for i in shipIndex:
                                        displayBoard[userRow-1][n] = "O"
                        else:
                            print ("You missed")
                            board[userRow-1][userCol-1] = 3
                            displayBoard[userRow-1][userCol-1] = " "



            

def displayscore():
    readscore = open('score.txt','r')
    score = readscore.readlines()
    readscore.close

    print("HIGH SCORE")
    for line in score:
        shipCounter=(line.split("\n"))
        print(shipCounter[0])

def deletescore():
    clearscore=open('score.txt','w')
    clearscore.close


mainmenu()   
