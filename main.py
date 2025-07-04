class Board:
    def __init__(self, board): # Initializes the board with the 2D list board passed as an argument.
        self.board = board


    def __str__(self):
        board_str = '' # Converts the board into string for pretty printing
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row] #Replaces 0s(empty cells) with * to make it visually clear
            board_str += ' '.join(row_str) # Joins elements row by row
            board_str += '\n'
        return board_str



    def find_empty_cell(self):
        for row, contents in enumerate(self.board): #Scans the board for the first empty cell
            try:
                col = contents.index(0)
                return row, col
            except ValueError: # Returns a tuple(row,col) or None if the board is full
                pass
        return None


    # Validty Checkers
    def valid_in_row(self, row, num):
        return num not in self.board[row] # Returns True if num is not already in the specified row

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9)) # Checks that num doesn't exist in the specified column

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False                # Checks that num is not already present in the 3x3 square that the cell belongs to
        return True


    # Combines the three checks above
    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])



    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:  # If no empty cell is left return True
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess    # If valid, place the number and continue solving
                if self.solver():
                    return True
                self.board[row][col] = 0    # If solving fails, backtrack (rest cell to 0) and try next number
        return False


# Wraps the process
def solve_sudoku(board):
    gameboard = Board(board)     
    print(f'Puzzle to solve:\n{gameboard}')     #Prints original puzzle
    if gameboard.solver():  # Attempts to solve
        print(f'Solved puzzle:\n{gameboard}')
    else:       # Prints solution or failure message
        print('The provided puzzle is unsolvable.')
    return gameboard


puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)