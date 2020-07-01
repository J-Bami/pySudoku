"""module to define a sudoku region"""

# what we can do is pass the required cells from Sudoku Grid to each region
# type in this module

from sudoku_input import (CELLS_PER_REGION_SIDE, CHARACTER_SET,
                          REGIONS_PER_SIDE)
from numpy import array

class SudokuRegion:
    """defines a Sudoku region """
    
    def __init__(self, grid):
        """
        represents itself as a sub region in a sudoku grid.
        INPUTS:
            grid:  a SudokuGrid class that this region points to
            index: defines the set of cells this class will represent
        """
        self.grid = grid   # pointer to the grid this is a part of
        self.characters = CHARACTER_SET.copy()  # character set
        self.cells = []  # 
        self.initialise()
        return
    
    def initialise(self):
        """empty function to override in initialisation routine"""
        return

    def check_cell_value(self, value):
        """checks the input value is valid"""
        if value not in self.characters:
            raise ValueError(f"{value} is not a valid option for {self}")
        return

    def remove_cell_value(self, value):
        """
        called when a cell can have value. removes it from self.characters
        """
        self.characters.remove(value)
        return
    
    def get_unsolved(self):
        """gets all the unsolves cells in this group"""
        out = []
        for cell in self.cells:
            if not cell:
                out.append(cell)
        return out

    def __or__(self, other):
        return self.characters | other
    
    def __and__(self, other):
        return self.characters & other
        
    def __xor__(self, other):
        return self.characters ^ other

    def __ror__(self, other):
        return other.__or__(self.characters)
    
    def __rand__(self, other):
        return other.__and__(self.characters)
        
    def __rxor__(self, other):
        return other.__xor__(self.characters)

    def __getitem__(self, index):
        """indexes the sudoku Region"""
        return self.cells[index]
    
    def __iter__(self):
        """"""
        return self.cells.__iter__()

    def __repr__(self):
        """representation of self"""
        return self.__class__.__name__ + ": " + str(array(self.cells))


class SudokuRow(SudokuRegion):
    """Defines a row in a sudoku grid"""
    def __init__(self, grid, index):
        self.index = index
        super().__init__(grid)
        return
    
    def initialise(self):
        self.cells = []
        for i in range(self.grid.dimension):
            cell = self.grid[self.index][i]
            cell.set_row(self)
            self.cells.append(cell)
        return

class SudokuColumn(SudokuRegion):
    """defines a column in a sudoku grid"""
    def __init__(self, grid, index):
        self.index = index
        super().__init__(grid)
        return

    def initialise(self):
        self.cells = []  # reset cells
        for i in range(self.grid.dimension):
            cell = self.grid[i][self.index]
            cell.set_column(self)
            self.cells.append(cell)
        return

class SudokuBox(SudokuRegion):
    """defines the sudoku box"""
    def __init__(self, grid, row_index, column_index):
        self.row_index = row_index
        self.column_index = column_index
        super().__init__(grid)
        return
    
    def initialise(self):
        """initilises the box type region"""
        for j in range(REGIONS_PER_SIDE):
            row_index = (self.row_index*CELLS_PER_REGION_SIDE) + j
            for i in range(CELLS_PER_REGION_SIDE):
                column_index = self.column_index*CELLS_PER_REGION_SIDE + i
                cell = self.grid[row_index][column_index]
                cell.set_box(self)
                self.cells.append(cell)
        return