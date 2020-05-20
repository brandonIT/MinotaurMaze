import random ###Importing the class Random

def initBoard(): ###Creating the initial game board
    row, col = (11, 11) ###Made the actual array 11x11 so that I could add walls to the board
    count = 0
    board = [[' ' for i in range(col)] for j in range(row)] ###Game board is getting initial values
    while(count < 11):
        board[0][count] = '\u0304'
        count += 1
        if(count == 11):
            count = 0
            while(count < 11):
                board[10][count] = '\u0304'
                count += 1
    count = 1
    while(count < 10):
        board[count][0] = '\u01C0'
        count += 1
        if(count == 10):
            count = 1
            while(count < 10):
                board[count][10] = '\u01C0'
                count += 1
    board[5][1] = 'A' ###Player 1
    board[5][9] = 'B' ###Player 2
    board[1][5] = 'M' ###The Minotaur
    count = 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == ' '):
                board[i][j] = count
                count += 1
    return board, count

def printDirections(): ###Directions for the game displayed to the user
    print("\nWelcome to the Minotaur Maze Version 2.0!")
    print("Each turn, you will be prompted to make a move.")
    print("You may move, place and object then move, place an object and not move, or remove an obstacle.")
    print("Your goal is to make it to the opposite wall (if you are player one, get to the right wall).")
    print("Watch out for the Minotaur! He can remove obstacles and if he lands on you, you will be eaten.\n")
    input("Press Enter to continue")

def printBoard(board): ###Printing the game board
    count = 1
    print("\n")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(isinstance(board[i][j],str)):
                print("",board[i][j],end=' ') ###Adjusting spacing for the walls and tracking count with non-integers
                count += 1
            elif((isinstance(board[i][j],int)) and (board[i][j] < 10)):
                print("",board[i][j],end=' ') ###Adjusting spacing for single digit numbers
                count += 1
            else:
                print("",board[i][j],end='')
                count += 1
        print('\n')
        count = 0
    print("\n")

def switchboard():
    uInput = 0 ###User input for prompts
    
    print("\nPress 1 to move")
    print("Press 2 to place an obstacle")
    print("Press 3 to remove an obstacle")
    print("Press 4 to stay")

    while True:
        uInput=input("\nPlease enter the corresponding number.\n")
        try:
            test = int(uInput) ###This is testing the input to see if it is a number (converts from string to int)
            if((test > 0) or (test < 5)):
                break;
            else:
                print("\nThe number must be between 1 and 4. Please try again.")
                printBoard(board)
                uInput = int(uInput)
        except ValueError:
            print("\nPlease enter a number!") ###This is telling the user that they entered an invalid value
            printBoard(board)
    uInput = int(uInput) ###This is type casting the confirmed number value to an int then storing it in a new variable
    return uInput

def move(board, playerTurn, gameOver):
    uInput = 0 ###User input
    valid = 0 ###Flag to check for valid move
    spriteLetter = 'Z' ###Player's letter equivalent to their number (i.e. A is Player 1's sprite)
    buffer = 0 

    ###Matching the player's letter to their number counter part (A is player 1 B is player 2)
    if(playerTurn == 1):
        spriteLetter = 'A'
        print(spriteLetter)
    else:
        spriteLetter = 'B'
        print(spriteLetter)

    ###This will keep running until a valid move is made
    while(valid == 0):
        print("\nPress 1 to move up 1 space")
        print("Press 2 to move right 1 space")
        print("Press 3 to move down 1 space")
        print("Press 4 to move left 1 space")

        ###Error checking input
        while True:
            uInput=input("\nPlease enter the corresponding number.\n")
            try:
                test = int(uInput) ###This is testing the input to see if it is a number (converts from string to int)
                if((test > 0) or (test < 5)):
                    break;
                else:
                    print("\nThe number must be between 1 and 4. Please try again.")
                    printBoard(board)
                    uInput = int(uInput)
            except ValueError:
                print("\nPlease enter a number!") ###This is telling the user that they entered an invalid value
                printBoard(board)
        uInput = int(uInput) ###This is type casting the confirmed number value to an int then storing it in a new variable

        if(uInput == 1):###Move up 1 space
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if((board[i][j] == spriteLetter) and (isinstance(board[i - 1][j],int))): ###Checks one spot above the player to make sure the player can move there
                        buffer = board[i - 1][j]
                        board[i - 1][j] = spriteLetter
                        board[i][j] = buffer
                        valid = 1
                        break
                    elif((board[i][j] == spriteLetter) and (isinstance(board[i - 1][j],str))): ###Checks one spot above the player to make sure the player can move there
                        if((board[i - 1][j] == 'x') or (board[i - 1][j] == 'B') or (board[i - 1][j] == '\u0304') or (board[i - 1][j] == 'A')):
                            print("\nYou can't move there. Please try again")
                            break
        elif(uInput == 2):###Move right
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if((board[i][j] == spriteLetter) and (isinstance(board[i][j + 1],int))): ###Checks one spot to the right of the player to make sure the player can move there
                        buffer = board[i][j + 1]
                        board[i][j + 1] = spriteLetter
                        board[i][j] = buffer
                        valid = 1
                        break
                    elif((board[i][j] == spriteLetter) and (isinstance(board[i][j + 1],str))): ###Checks the spot to the right of the player on the board to make sure the player can move there
                        if(board[i][j + 1] == '\u01C0'): ###Checks one spot to the right of the player for the vertical wall (the goal)
                            if(playerTurn == 1): ###Checks for win if it's player 1's turn
                                gameOver = playerTurn
                                board[i][j + 1] = spriteLetter
                                board[i][j] = 80
                                valid = 1
                                break
                            elif(playerTurn == 2): ###Restricts player 2 from moving to the wall on their own side
                                print("\nYou can't move there. Please try again") 
                                break
                        elif((board[i][j + 1] == 'x') or (board[i][j + 1] == 'B') or (board[i][j + 1] == '\u0304') or (board[i][j + 1] == 'A')): ###Checks for something already occupying the spot the player wants to move to
                            print("\nYou can't move there. Please try again")
                            break
        elif(uInput == 3):###Move down
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if(turnOver == 1):
                        break
                    elif((board[i][j] == spriteLetter) and (isinstance(board[i + 1][j],int))): ###Checks one spot below the player to make sure the player can move there
                        buffer = board[i + 1][j]
                        board[i + 1][j] = spriteLetter
                        board[i][j] = buffer
                        valid = 1
                        turnOver = 1
                    elif((board[i][j] == spriteLetter) and (isinstance(board[i + 1][j],str))):
                        if((board[i + 1][j] == 'x') or (board[i + 1][j] == 'B') or (board[i + 1][j] == '\u0304') or (board[i + 1][j] == 'A')): ###Checks for something already occupying the spot the player wants to move to
                            print("\nYou can't move there. Please try again")
                            break
        elif(uInput == 4):###Move left
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if((board[i][j] == spriteLetter) and (isinstance(board[i][j - 1],int))): ###Checks one spot to the left of the player to make sure the player can move there
                        buffer = board[i][j - 1]
                        board[i][j - 1] = spriteLetter
                        board[i][j] = buffer
                        valid = 1
                        break
                    elif((board[i][j] == spriteLetter) and (isinstance(board[i][j - 1],str))): ###Checks the spot to the left of the player on the board to make sure the player can move there
                        if(board[i][j - 1] == '\u01C0'):###Checks one spot to the left of the player for the vertical wall (the goal)
                            if(playerTurn == 2): ###Checks for win if it's player 2's turn
                                gameOver = playerTurn
                                board[i][j - 1] = spriteLetter
                                board[i][j] = 80
                                valid = 1
                                break
                            elif(playerTurn == 1): ###Restricts player 1 from moving to the wall on their own side
                                print("\nYou can't move there. Please try again")
                                break
                        elif((board[i][j - 1] == 'x') or (board[i][j - 1] == 'B') or (board[i][j - 1] == '\u0304') or (board[i][j - 1] == 'A')): ###Checks for something already occupying the spot the player wants to move to
                            print("\nYou can't move there. Please try again")
                            break
    return gameOver

def placeObstacle(board, count): ###Places an obstacle on the board
    valid = 0 ###Flag to check for valid move
    uInput = 0 ###User input
    
    while(valid == 0):
        ###Error checking input
        printBoard(board)
        while True:
            uInput=input("Please enter the corresponding number.\n")
            try:
                test = int(uInput) ###This is testing the input to see if it is a number (converts from string to int)
                if((test > 0) or (test < 80)):
                    break
                else:
                    print("\nThe number must be between 1 and 80. Please try again.")
                    printBoard(board)
                    uInput = int(uInput)
            except ValueError:
                print("\nPlease enter a number!") ###This is telling the user that they entered an invalid value
                printBoard(board)
        uInput = int(uInput) ###This is type casting the confirmed number value to an int then storing it in a new variable

        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == uInput): ###Placing obstacle (shown as an x) on the board
                    board[i][j] = 'x'
                    valid = 1
                    count -= 1
                    print(count)
                    return count

def removeObstacle(board, count):
    valid = 0  ###Flag to check for valid move
    uInput = 0 ###User input

    printBoard(board)
    while True:
        uInput=input("Please enter the number beside the obstacle you would like to remove.\n")
        try:
            test = int(uInput) ###This is testing the input to see if it is a number (converts from string to int)
            if((test > 0) or (test < 80)):
                break
            else:
                print("\nThe number must be between 1 and 80. Please try again.")
                printBoard(board)
                uInput = int(uInput)
        except ValueError:
            print("\nPlease enter a number!") ###This is telling the user that they entered an invalid value
            printBoard(board)
    uInput = int(uInput) ###This is type casting the confirmed number value to an int then storing it in a new variable

    for i in range(len(board)):
        for j in range(len(board[i])):
            if((board[i][j] == 'x') and (board[i][j + 1] == uInput)): ###Checks to the right of the number the user entered for an obstacle to remove
                count += 1
                board[i][j] = count
                valid = 1
                return count
            elif((board[i][j] == 'x') and (board[i][j - 1] == uInput)): ###Checks to the left of the number the user entered for an obstacle to remove
                count += 1
                board[i][j] = count
                valid = 1
                return count

def minotaurTurn(board, count, playerLoss):
    randomNumber = 0 ###Random number value
    xCoord = 0 ###X coordinate equivalent to the column that the Minotaur currently occupies
    yCoord = 0 ###Y coordinate equivalent to the row that the Minotaur currently occupies
    buffer = 0 ###Temporary holder of current board spot's value
    valid = 0 ###Flag to check for valid move
    nums = [1,2,3,4,5,6,7,8] ###Numbers for random number generation below

    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 'M'): ###Tracking the coordinates on the board of the Minotaur
                xCoord = i ###Setting the column of the Minotaur
                yCoord = j ###Setting the row of the Minotaur
    
    randomNumber = random.choice(nums) ###Choosing a random number from the list "nums" 
    
    while(valid == 0):
        if(randomNumber == 1): ###Minotaur moves up one spot
            if(isinstance(board[xCoord - 1][yCoord],int)): ###Checks spot above the Minotaur for an integer (checks for a valid move)
                buffer = board[xCoord - 1][yCoord] ###Sets current value in spot Minotaur is moving to
                board[xCoord - 1][yCoord] = 'M' ###Moves Minotaur to new spot (changes the value in the spot the Minotaur is moving to to "M")
                board[xCoord][yCoord] = buffer ###Sets spot the Minotaur moved from to the value of the spot the Minotaur moved to
                valid = 1 ###Sets valid flag to 1 indicating valid move was made
                break
            elif(board[xCoord - 1][yCoord] == 'x'): ###Checks to see if an obstacle is in the spot above the Minotaur
                board[xCoord - 1][yCoord] = 'M' ###Changes the value of the obstacle ('x') to the Minotaur's 'M'
                board[xCoord][yCoord] = count ###Replaces the spot with the next number in the board's sequence
                valid = 1 ###Sets valid flag to 1 indicating valid move was made
                break
            elif(board[xCoord - 1][yCoord] == 'A'): ###Checks to see if player 1 ('A') is in the spot above the Minotaur
                board[xCoord - 1][yCoord] = 'M' ###Changes the value of player 1 ('A') to the Minotaur's 'M'
                board[xCoord][yCoord] = count ###Replaces the spot with the next number in the board's sequence
                valid = 1 ###Sets valid flag to 1 indicating valid move was made
                playerLoss += 1 ###Tracks that at least player 1 has lost
                break
            elif(board[xCoord - 1][yCoord] == 'B'): ###Checks to see if player 2 ('B') is in the spot above the Minotaur
                board[xCoord - 1][yCoord] = 'M' ###Changes the value of player 1 ('A') to the Minotaur's 'M'
                board[xCoord][yCoord] = count ###Replaces the spot with the next number in the board's sequence
                valid = 1 ###Sets valid flag to 1 indicating valid move was made
                playerLoss += 2 ###Tracks that at least player 2 has lost
                break
            else:
                for i in range(len(nums) + 1):
                    if(randomNumber == i): ###Finds the current value of 'randomNumber' in the array 'nums'
                        nums.remove(i) ###Removes the numbered choice from the list 'nums' so that this isn't attempted again
                        randomNumber = random.choice(nums) ###Chooses a new random number from the adjusted 'nums' list
                        break
        elif(randomNumber == 2): ###Minotaur moves up one spot and right one spot
            if(isinstance(board[xCoord - 1][yCoord + 1],int)):
                buffer = board[xCoord - 1][yCoord + 1]
                board[xCoord - 1][yCoord + 1] = 'M'
                board[xCoord][yCoord] = buffer
                valid = 1
                break
            elif(board[xCoord - 1][yCoord + 1] == 'x'):
                board[xCoord - 1][yCoord + 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                break
            elif(board[xCoord - 1][yCoord + 1] == 'A'):
                board[xCoord - 1][yCoord + 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 1
                break
            elif(board[xCoord - 1][yCoord + 1] == 'B'):
                board[xCoord - 1][yCoord + 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 2
                break
            else:
               for i in range(len(nums) + 1):
                    if(randomNumber == i):
                        nums.remove(i)
                        randomNumber = random.choice(nums)
                        break
        elif(randomNumber == 3): ###Minotaur moves right one spot
            if(isinstance(board[xCoord][yCoord + 1],int)):
                buffer = board[xCoord][yCoord + 1]
                board[xCoord][yCoord + 1] = 'M'
                board[xCoord][yCoord] = buffer
                valid = 1
                break
            elif(board[xCoord][yCoord + 1] == 'x'):
                board[xCoord][yCoord + 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                break
            elif(board[xCoord][yCoord + 1] == 'A'):
                board[xCoord][yCoord + 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 1
                break
            elif(board[xCoord][yCoord + 1] == 'B'):
                board[xCoord][yCoord + 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 2
                break
            else:
               for i in range(len(nums) + 1):
                    if(randomNumber == i):
                        nums.remove(i)
                        randomNumber = random.choice(nums)
                        break
        elif(randomNumber == 4):  ###Minotaur moves right one spot and down one spot
            if(isinstance(board[xCoord + 1][yCoord + 1],int)):
                buffer = board[xCoord + 1][yCoord + 1]
                board[xCoord + 1][yCoord + 1] = 'M'
                board[xCoord][yCoord] = buffer
                valid = 1
                break
            elif(board[xCoord + 1][yCoord + 1] == 'x'):
                board[xCoord + 1][yCoord + 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                break
            elif(board[xCoord + 1][yCoord + 1] == 'A'):
                board[xCoord + 1][yCoord + 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 1
                break
            elif(board[xCoord + 1][yCoord + 1] == 'B'):
                board[xCoord + 1][yCoord + 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 2
                break
            else:
               for i in range(len(nums) + 1):
                    if(randomNumber == i):
                        nums.remove(i)
                        randomNumber = random.choice(nums)
                        break
        elif(randomNumber == 5): ###Minotaur moves down one spot
            if(isinstance(board[xCoord + 1][yCoord],int)):
                buffer = board[xCoord + 1][yCoord]
                board[xCoord + 1][yCoord] = 'M'
                board[xCoord][yCoord] = buffer
                valid = 1
                break
            elif(board[xCoord + 1][yCoord] == 'x'):
                board[xCoord + 1][yCoord] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                break
            elif(board[xCoord + 1][yCoord] == 'A'):
                board[xCoord + 1][yCoord] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 1
                break
            elif(board[xCoord + 1][yCoord] == 'B'):
                board[xCoord + 1][yCoord] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 2
                break
            else:
               for i in range(len(nums) + 1):
                    if(randomNumber == i):
                        nums.remove(i)
                        randomNumber = random.choice(nums)
                        break
        elif(randomNumber == 6): ###Minotaur moves down one spot and one spot left
            if(isinstance(board[xCoord + 1][yCoord - 1],int)):
                buffer = board[xCoord + 1][yCoord - 1]
                board[xCoord + 1][yCoord - 1] = 'M'
                board[xCoord][yCoord] = buffer
                valid = 1
                break
            elif(board[xCoord + 1][yCoord - 1] == 'x'):
                board[xCoord + 1][yCoord - 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                break
            elif(board[xCoord + 1][yCoord - 1] == 'A'):
                board[xCoord + 1][yCoord - 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 1
                break
            elif(board[xCoord + 1][yCoord - 1] == 'B'):
                board[xCoord + 1][yCoord - 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 2
                break
            else:
               for i in range(len(nums) + 1):
                    if(randomNumber == i):
                        nums.remove(i)
                        randomNumber = random.choice(nums)
                        break
        elif(randomNumber == 7): ###Minotaur moves left one spot
            if(isinstance(board[xCoord][yCoord - 1],int)):
                buffer = board[xCoord][yCoord - 1]
                board[xCoord][yCoord - 1] = 'M'
                board[xCoord][yCoord] = buffer
                valid = 1
                break
            elif(board[xCoord][yCoord - 1] == 'x'):
                board[xCoord][yCoord - 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                break
            elif(board[xCoord][yCoord - 1] == 'A'):
                board[xCoord][yCoord - 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 1
                break
            elif(board[xCoord][yCoord - 1] == 'B'):
                board[xCoord][yCoord - 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 2
                break
            else:
               for i in range(len(nums) + 1):
                    if(randomNumber == i):
                        nums.remove(i)
                        randomNumber = random.choice(nums)
                        break
        elif(randomNumber == 8): ###Minotaur moves left one spot and up one spot
            if(isinstance(board[xCoord - 1][yCoord - 1],int)):
                buffer = board[xCoord - 1][yCoord - 1]
                board[xCoord - 1][yCoord - 1] = 'M'
                board[xCoord][yCoord] = buffer
                valid = 1
                break
            elif(board[xCoord - 1][yCoord - 1] == 'x'):
                board[xCoord - 1][yCoord - 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                break
            elif(board[xCoord - 1][yCoord - 1] == 'A'):
                board[xCoord - 1][yCoord - 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 1
                break
            elif(board[xCoord - 1][yCoord - 1] == 'B'):
                board[xCoord - 1][yCoord - 1] = 'M'
                board[xCoord][yCoord] = count
                valid = 1
                playerLoss += 2
                break
            else:
               for i in range(len(nums) + 1):
                    if(randomNumber == i):
                        nums.remove(i)
                        randomNumber = random.choice(nums)
                        break
    return playerLoss, count
    
def playGame(): ###Game actually begins here
    gameOver = 0 ###Flag to track if the game is over or not
    playerTurn = 1 ###Tracks players turn
    playerLoss = 0 ###Tracks which player(s) have lost
    
    printDirections()
    board,count = initBoard()
    while(gameOver == 0): ###While the game is not over
        if((playerTurn == 1) and (playerLoss != 1)): ###If it's player 1's turn and they haven't lost
            printBoard(board)
            print("Player 1's turn!\n")
            userInput = switchboard() ###Player chooses what they'd like to do 
        elif((playerTurn == 2) and(playerLoss != 2)): ###If it's player 2's turn and they haven't lost
            printBoard(board)
            print("Player 2's turn!\n")
            userInput = switchboard()
        if(userInput == 1): ###Player decides to move
            gameOver = move(board,playerTurn,gameOver) ###Triggers 'move' function, player moves
        elif(userInput == 2): ###Player decides to place an obstacle
            count = placeObstacle(board, count) ###Triggers 'place obstacle' function, player places an obstacle
            userInput = input("\nTo move, enter 1. To end your turn, press enter.\n")
            if(userInput == str(1)): ###Checks to see if the player wants to move after placing the object
                gameOver = move(board,playerTurn,gameOver)
        elif(userInput == 3): ###Player decides to remove an obstacle
            count = removeObstacle(board, count) ###Triggers 'removeObstacle' function, player removes an obstacle
        if(playerTurn == 1): ###If it is player 1's turn
            playerTurn += 1 ###Changes to player 2's turn
        else:
            playerLoss,count = minotaurTurn(board, count, playerLoss) ###Triggers 'minotaurTurn' function, Minotaur moves
            playerTurn -= 1 ###Changes to player 1's turn
            userInput = 0 ###User input is reset
            if(playerLoss == 1): ###If the Minotaur moves to the spot player 1 is occupying
                print("\nPlayer 1 has been eaten")
            elif(playerLoss == 2): ###If the Minotaur moves to the spot player 2 is occupying
                print("\nPlayer 2 has been eaten")
            elif(playerLoss == 3): ###If player 1 and player 2 have lost
                 gameOver = 3 ###Minotaur win is set
            else:
                print("\nThat concludes your turn")
    if(gameOver == 1): ###Player 1 has made it to the right-most wall first
        print("\nPlayer 1 wins!")
    elif(gameOver == 2): ###Player 2 has made it to the left-most wall first
        print("\nPlayer 2 wins!")
    elif(gameOver == 3): ###Both players have lost, the Minotaur wins
        print("\nThe Minotaur has won")
    
def main(): ###Defines what the main code will do in the program
    playGame()

main() ###Runs the main code of the program
