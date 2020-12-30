#Sudoku_solver.py
#This program lets you play a game of Sudoku and can solve it for you
#It takes advantage of recursive backtracking in order to find a solution 
#to the Sudoku board

b1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

b2 = [
    [0, 8, 0, 0, 0, 0, 0, 3, 2],
    [4, 0, 0, 0, 0, 6, 5, 0, 0],
    [0, 0, 0, 0, 3, 0, 1, 0, 0],
    [0, 0, 3, 6, 0, 5, 4, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 4, 8, 0, 7, 9, 0, 0],
    [0, 0, 9, 0, 5, 0, 0, 0, 0],
    [0, 0, 8, 7, 0, 0, 0, 0, 9],
    [6, 2, 0, 0, 0, 0, 0, 8, 0]
]

b3 = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

b4 = [
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 3, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 1, 8],
    [0, 0, 0, 0, 8, 1, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 5, 0],
    [0, 4, 0, 0, 0, 0, 3, 0, 0]
]

def print_board(board):
    """
    Prints the sudoku board in its intial state
    """
    print("- - - - - - - - - - - - -")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print("| ",end="")

            if j == 8:
                print(board[i][j], end=" | \n")
            else:
                print(str(board[i][j]) + " ", end="")
    print("- - - - - - - - - - - - -")


def find_blank(board):
    """
    Figures out if the space is blank/ is "0"
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #row, col
        
    return False


def valid(board, num, pos):
    """
    Checks to see if the postion is a valid position
    """
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != 1:
            return False

    #check col
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != 1:
            return False

    #check box
    box_x = pos[1] // 3 
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True


def solve_board(board):
    """
    Solves the board by filling in all the "blanks" with their correct values
    """
    find = find_blank(board)
    if find:
        row, col = find
    else:
        return True
    
    #Recursively checks possible values for each blank space
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
        
            if solve_board(board):
                return True

        board[row][col] = 0

    return False


def play_game():
    """
    Starts a game of Sudoku and lets the user pick between a custom board or a premade board
    """
    print("Let's play a Game of Sudoku!")
    print("Do you want to create your own board or do you want to use one of the 3 pre-made boards")
    ans = input('If you want a pre-made board please type "premade" and if you want to play a custom board please type "custom"\n')
    ans = ans.lower()
    while ans != "premade" and ans != "custom":
        inpu = input("Sorry please type a valid choice\n")
        ans = inpu.lower()

    if ans == "premade":
        print("Expert takes a very long time to solve so I don't recommend it")
        choice = input("Which board would you like to play: Easy, Medium, Hard, or Expert\n")
        print(choice)
        board = create_empty_board()
        if choice.lower() == "easy":
            board = b1
        elif choice.lower() == "medium":
            board = b2
        elif choice.lower() == "hard":
            board = b3
        else:
            board = b4
    else:
        board = fill_board()

    print_board(board)
    
    print("The board has been registered now try to solve it!")
    print("If you have finished solving it or just want to see the answer")
    fin = input("Please type \"Solve\"\n")
    while fin.lower() != "solve":
        new = input("Whoops looks like you typed the wrong thing, please try again!")
        fin = new.lower()
    solve_board(board)
    print_board(board)


def create_empty_board():
    """
    Creates an empty 9 x 9 array or "board" that can be filled
    """
    row, col = (9, 9)
    newBoard = [[0 for i in range(col)] for j in range(row)]
    return newBoard


def fill_board():
    """
    Allows the user to input values into certain places in the board in order to create a custom game
    """
    print("WARNING: PROGRAM WILL BRAKE IN CURRENT STAGE IF BOARD HAS NO VALID SOLUTIONS OR AT LEAST IM LIKE 90% SURE IT WILL")
    print("IF INVALID BOARD JUST CANCEL THE RUN")
    board = create_empty_board()
    num = int(input("How many values are given in this board\n"))
    for i in range(1, num + 1):
        if i % 10 == 1:
            end = "st"
        elif i % 10 == 2:
            end = "nd"
        elif i % 10 == 3:
            end = "rd"
        else:
            end = "th"
        row = int(input("What row is the " + str(i) + end + " value in?\n"))
        if row > 9 or row < 1:
            row = int(input("Whoops looks like you typed the wrong thing, please type a number 1 - 9!\n"))
        col = int(input("What column is the " + str(i) + end + " value in?\n"))
        if col > 9 or row < 1:
            col = int(input("Whoops looks like you typed the wrong thing, please type a number 1 - 9!\n"))
        val = int(input("What number goes here\n"))
        if val > 9 or row < 1:
            val = int(input("Whoops looks like you typed the wrong thing, please type a number 1 - 9!\n"))
        board[row - 1][col - 1] = val
        print_board(board)
    return board


play_game()