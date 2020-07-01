"""module to house the sudoku grid class"""

from sudoku_input import (CELLS_PER_REGION_SIDE, REGIONS_PER_SIDE)
from sudoku_cell import SudokuCell
from sudoku_region import SudokuRow, SudokuBox, SudokuColumn

from numpy import array  # display purposes

class SudokuGrid:
    """Class that houses the sudoku grid"""
    
    def __init__(self, grid_input):
        """initialises the"""
        self.dimension = CELLS_PER_REGION_SIDE*REGIONS_PER_SIDE
        self.make_cells()
        self.make_regions()
        self.populate(grid_input)
        self.update_cells()
        return
    
    def make_cells(self):
        """Makes all the cells"""
        self.cells = []
        for j in range(self.dimension):
            row = []
            for i in range(self.dimension):
                row.append(SudokuCell())
            self.cells.append(row)
        return

    def make_regions(self):
        """makes all the regions associated with this grid"""
        self.make_rows_and_columns()
        self.make_boxes()
        return
    
    def make_rows_and_columns(self):
        """initialises the rows and columns of this grid"""
        self.rows = []
        self.columns = []
        for i in range(self.dimension):
            self.rows.append(SudokuRow(self, i))
            self.columns.append(SudokuColumn(self, i))
        return
        
    def make_boxes(self):
        """initialises the boxes of this grid. note boxes are stored as:
            [[0, 1, ..., CELLS_PER_REGION_SIDE -1]
             [CELLS_PER_REGION_SIDE, CELLS_PER_REGION_SIDE +1, ... ]
             you get it..."""
        self.boxes = []
        for j in range(REGIONS_PER_SIDE):
            for i in range(REGIONS_PER_SIDE):
                self.boxes.append(SudokuBox(self, i, j))
        return
    

    def populate(self, grid_input):
        """populates the grid with the input values. assumes the grid input
        is a dimension x dimension iterable"""
        for i in range(self.dimension):
            for j in range(self.dimension):
                try:
                    self.set_value(grid_input[i][j], i, j)
                except (TypeError, IndexError):
                    continue
        return                
        
    # we need a method to insert a value.
    def set_value(self, value, row_index, column_index):
        """sets the value for the element (row_index) rows down, (cloumn_index)
        rows across"""
        self.cells[row_index][column_index].set_value(value)
        self.update_cells()
        return
    
    
    def update_cells(self):
        """
        updates the possible values in every cell if the state of the
        SudokuGrid changes
        """
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.cells[i][j].find_possible_values()
        return
        
        
    def __getitem__(self, index):
        """indexes the sudoku Region"""
        return self.cells[index]
    
    def __iter__(self):
        """"""
        return self.cells.__iter__()
    
    def __repr__(self):
        """representation of self"""
        return "SudokuGrid:\n" + str(array(self.cells))
        