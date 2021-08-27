# 1. find an empty space
# 2. try to put a number that works
# 3. move onto the next empty space (find)
# 4. once there arent any possibilities, you backtrack

# BACKTRACKING
# you erase the number that doesnt work and go to the previous square
# try other numbers that work
# keep going back if the number doesnt work in the current square

# FUNCTIONS NEEDED
# a function that finds an empty square
# a function that validates a number
    # check row, col and the square the number is in
# a function that backtracks

# ADDITIONAL FEATURES
# a function that prints the board



# sample board
sudo_board = [
                [0, 0, 6, 0, 0, 5, 0, 0, 0],
                [0, 0, 0, 9, 0, 2, 4, 5, 0],
                [0, 9, 0, 3, 0, 0, 7, 0, 8],
                [0, 0, 0, 7, 0, 0, 0, 8, 0],
                [6, 0, 3, 0, 0, 0, 2, 0, 5],
                [8, 5, 0, 0, 0, 3, 0, 0, 0],
                [0, 0, 2, 0, 4, 7, 0, 0, 0],
                [9, 6, 7, 0, 8, 1, 5, 3, 0],
                [5, 4, 0, 0, 3, 9, 1, 2, 7]
            ]

# a function that prints the board
def print_board(board):
    for row in range(len(board)): # looping through every row in the board
        for col in range(len(board[row])): # loop through the columns in every row
            print(board[row][col], end=' ')
        print()

# a function that finds an empty entity
# returns the position of the empty spot
# def is_empty(board):

# a function that validates the number
    # validating: checks to see if the number already exists in the grid or not
# if the number is valid in that position, return true; false otherwise
def is_valid(board, num, row, col):
    for i in range(9): # check if the row is valid
        if board[row][i] == num:
            return False
    for j in range(9): # checks if the col is valid
        if board[j][col] == num:
            return False

    # check if the number within the field is valid
    # box_i/j gives the value of either 0, 1, 2 which are the sudoku boxes
    box_i = (row // 3)*3 # multiply by 3 to get the actual indexes within the boxes
    box_j = (col // 3)*3 # this is the start of the boxes

    for i in range(box_i + 3): # you add three to the range to get the end of the boxes
        for j in range(box_j + 3):
            if board[i][j] == num:
                return False
    return True

            
    

print_board(sudo_board)