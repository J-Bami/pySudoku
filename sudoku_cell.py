"""module to hold the class for a single sudoku cell"""
from sudoku_input import CHARACTER_SET

class SudokuCell:
    """Class that holds either a single number or a set of possible
    values that this cell can have"""
    
    def __init__(self):
        """initialises an instance of the sudoku cell"""
        self.row = None
        self.column = None
        self.box = None
        self.value = None
        self.possible_values = CHARACTER_SET.copy()
        return
    
    def set_value(self, value):
        """sets the sudoku cell value to value"""
        if value:
            if self.value:
                raise ValueError("cell already has value")
            assert value in CHARACTER_SET, "VALUE NOT IN CHARACTER SET"
            self.check_parents(value)
            self.value = value
            self.possible_values = set()
            self.update_parents()
        else:
            self.value = None
        return
    

    def set_row(self, row):
        """sets the row that this cell belongs to"""
        self.row = row
        return
    
    def set_column(self, column):
        """sets the column that this cell belongs to"""
        self.column = column
        return
    
    def set_box(self, box):
        """sets the box that this cell belongs to"""
        self.box = box
        return
    
    def check_parents(self, value):
        """checks the parent structures to see if the input value is valid"""
        self.row.check_cell_value(value)
        self.box.check_cell_value(value)
        self.column.check_cell_value(value)
        return
        
    def find_possible_values(self):
        """finds the possible values this SudokuCell can hold"""
        if not self.value:
            self.possible_values = (((self.row & self.column) & self.box) &
                                    CHARACTER_SET)
        return
    
    def update_parents(self):
        """removes the value of self from the parents' sets"""
        if self.value:
            self.row.remove_cell_value(self.value)
            self.box.remove_cell_value(self.value)
            self.column.remove_cell_value(self.value)
        return
    
    def __or__(self, other):
        return {self.value} | other
    
    def __and__(self, other):
        return {self.value} & other
        
    def __xor__(self, other):
        return {self.value} ^ other
    
    def __bool__(self):
        return bool(self.value)
    
    def __repr__(self):
        string = self.__class__.__name__
        if self.value:
            return str(self.value)
            string = ': '.join([string, str(self.value)])
        return '.'# string
