"""
script to read in inputs for the sudoku solver.
should be able to try reading an input file as input.json
or as a straight up csv of the sudoku inputs.
"""

from utility import csv_reader
from json import load, dump
from os import getcwd

# Define some defaults:

DEFAULT_INPUT = "sudoku_inputs.json"


# will be extended in future for 6x6 sudokus with non-square boxes
INPUT_DICT = {
                "CELLS_PER_REGION_SIDE": 3, # needs a different name
                "REGIONS_PER_SIDE": 3,
                "CHARACTER_SET": None,
                "INPUT_FILE": None,
                "INPUT_TABLE": None,  # use a nested table;
              }


def read_inputs(filepath_json):
    """overwrites the INPUT_DICT with the inputs, assuming the input file is
    a .json file"""
    with open(filepath_json, 'r') as file:
        out = load(filepath_json, file)
    pass


def make_inputs(path=None):
    """makes an input template"""
    if not path:
        path = getcwd()
    file = path+'/'+DEFAULT_INPUT
    with open(file, 'w') as outfile:
        dump(INPUT_DICT, outfile, indent=4)
    pass


def set_characters(character_set=None):
    """defines the character set that the sudoku solver uses. Always
    a set of strings"""
    if not character_set:
        return set((str(i+1) for i in range(__UNIQUE_CHARACTERS)))
    else:
        assert len(set(character_set)) == __UNIQUE_CHARACTERS
        return set(map(str, character_set))
    

# now for the runtime parameters 

# if we have a json, we read and replace keys in input dict
        
# else, we assume a standard 3 by 3 grid with some sort of spacer, and try
# to read this

# raise an error if there are no arguments


for key in INPUT_DICT:
    value = INPUT_DICT[key]
    # print(key, value)
    try:
        exec(f"{key} = {value}")
    except ValueError:
        exec(f"{key} = '{value}'")

__UNIQUE_CHARACTERS = CELLS_PER_REGION_SIDE**2
assert REGIONS_PER_SIDE <= CELLS_PER_REGION_SIDE
CHARACTER_SET = set_characters()