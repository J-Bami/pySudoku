"""Module to house the solver object for a Sudoku"""

from utility import csv_reader
from sudoku_grid import SudokuGrid

from sys import argv
from time import time


def solved(grid):
    """determines if self is solved or not"""
    for i in range(grid.dimension):
        for j in range(grid.dimension):
            if not grid.cells[i][j]:
                return False
    return True

def check_possible_values(grid):
    """
    continuously checks the possible values each cell can have
    """
    check_flag = 1
    while check_flag:
        check_flag = 0
        for i in range(grid.dimension):
            for j in range(grid.dimension):
                cell = grid.cells[i][j]
                if len(cell.possible_values) == 1:
                    check_flag = 1
                    value = cell.possible_values.pop()
                    grid.set_value(value, i, j)
    return

def compare_related_cells(grid):
    """compares cells which are the in the same groups"""
    check_flag = 1
    while check_flag:
        check_possible_values(grid)
        check_flag = 0
        for group_type in (grid.rows, grid.columns,
                           grid.boxes):
            for group in group_type:
                unsolved = group.get_unsolved()
                for cell in unsolved:
                    result = cell.possible_values.copy()
                    for other in unsolved:
                        if other is cell:
                            continue
                        else:
                            result -= other.possible_values
                    if len(result) == 1:
                        check_flag = 1
                        cell.set_value(result.pop())
                    else:
                        continue
    return

def quasi_guess(grid):
    """when there remains multiple solutions to each remaining cell,
    we place any of the possible solutions for this cell in and continue...
    """
    # modify this to choose the cell with the smallest number of possibilities?
    for i in range(grid.dimension):
        for j in range(grid.dimension):
            cell = grid.cells[i][j]
            if not cell:
                value = cell.possible_values.pop()
                grid.set_value(value, i, j)
                grid.update_cells()
                compare_related_cells(grid)
    return

def solve(grid):
    """Uses a methodical approach in an attempt to find the solution to
    the grid:
    1) checks if len(possible_values) == 1 for each cell;
    2) checks over related cells
    3) yeets values in anyway
    """
    print(grid)
    check_possible_values(grid)
    compare_related_cells(grid)
    quasi_guess(grid)
    if not solved(grid):
        print("couldn't completely solve Sudoku")
    else:
        print("Solved")
    print(grid)
    return
        
    # use a decorator for this?
def sudoku_solver(grid, time_it=True):
    if time:
        start = time()
    solve()
    if time:
        dt = time() - start
    print("time taken = ", dt, "seconds")
    return 
                
if __name__ == "__main__":
    grid = csv_reader(argv[1])
    this_sudoku = SudokuGrid(grid)
    solve(this_sudoku)
