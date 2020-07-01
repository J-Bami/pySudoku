"""utility."""

def csv_reader(filepath, delimiter=','):
    """reads in a .csv file as a sudoku input"""
    out = []
    with open(filepath, 'r') as csv:
        for line in csv:
            data = line.split(delimiter)
            out.append([i.strip() for i in data])
    return out


