import numpy as np

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print(np.matrix(grid))

def possible(grid, row, column, number):
    # return false if number already exists
     
    # checking if a number already exists row wise 
    for i in range(0,9):
        if grid[row][i] == number:
            return False
        
    # checking if a number already exists column wise 
    for j in range(0,9):
        if grid[j][column] == number:
            return False
        
    # checking if a number already exists square block wise
    # determine corner for a specific 3x3 square block  
     
    corner_row = row - row % 3
    corner_column = column - column % 3
    for i in range(3):
        for j in range(3):
            if (grid[corner_row + i][corner_column + j] == number):
                return False
    
    # number does not exist so can be placed on that cell 
    return True

def solve(grid):
    # we use backtracking and recursion so that it can correct its answers if wrong 

    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if (possible(grid, row, column, number)):
                        grid[row][column] = number
                        solve(grid)
                        grid[row][column] = 0
                return
    print("\nSolution:")        
    print(np.matrix(grid))

solve(grid)