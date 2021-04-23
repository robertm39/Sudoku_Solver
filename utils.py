# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:59:00 2021

@author: rober
"""

SUDOKU_SIZE = 9
SQUARE_SIZE = 3

#All the possible values a cell can have
VALS = set(range(1, SUDOKU_SIZE+1))

#Data format: dict (int, int) -> Cell

def print_group(group):
    board = {cell.coords: Cell(cell.coords, 'x') for cell in group}
    print_board(board)

def print_board(board):
        print("+-----------+")
        for y in VALS:
            print('|', end='')
            for x in VALS:
                cell = board.get((x, y), None)
                num = cell.num if cell else None
                if num is None:
                    print(' ', end='')
                else:
                    print(num, end='')
                if x in (3, 6):
                    print('|', end='')
            print('|')
            if y in(3, 6):
                print('|---+---+---|')
        print("+-----------+")

def are_adjacent(coords_1, coords_2):
    x_1, y_1 = coords_1
    x_2, y_2 = coords_2
    
    
    if x_1 == x_2:
        if y_1 == y_2:
            return False
        return True
    
    if y_1 == y_2:
        return True
    
    if (x_1-1)//SQUARE_SIZE == (x_2-1)//SQUARE_SIZE\
       and (y_1-1)//SQUARE_SIZE == (y_2-1)//SQUARE_SIZE:
        return True
    
    return False

def get_adjacent(cell_coords):
    """
    Return a generator that generates all adjacent cells.
    """
    x, y = cell_coords
    prev = set([cell_coords])
    #Yield cells in the same row or column
    for v in VALS:
        coords = (v, y)
        if not coords in prev:
            prev.add(coords)
            yield coords
        
        coords = (x, v)
        if not coords in prev:
            prev.add(coords)
            yield coords
    
    #Yield cells in same square
    ulx = ((x-1)//SQUARE_SIZE) * SQUARE_SIZE + 1
    uly = ((y-1)//SQUARE_SIZE) * SQUARE_SIZE + 1
    
    for dx in range(0, SQUARE_SIZE):
        for dy in range(0, SQUARE_SIZE):
            cx = ulx + dx
            cy = uly + dy
            coords = (cx, cy)
            if coords in prev:
                continue
            prev.add(coords)
            yield coords

class Cell:
    def __init__(self, coords, num=None, parent=None):
        self.parent = parent
        self.coords = coords
        self.num = num
        
        self._hash = None
        
        if self.num is None:
            self.possible = VALS.copy()
        else:
            self.possible = set([self.num])
    
    def remove_possibility(self, num):
        if not num in self.possible:
            return
        
        self.possible.remove(num)
        self.parent.alert_removal(self, num)
        if len(self.possible) == 1:
            self.num = list(self.possible)[0]
            self.parent.alert_value(self)
        elif len(self.possible) == 0:
            self.num = None
            self.parent.alert_contradiction(self)
    
    def __str__(self):
        return '<{}: {}>'.format(self.coords, self.num)
    
    def __hash__(self):
        if self._hash:
            return self._hash

        x, y = self.coords
        result = 17
        result = (result + x) * 31
        result = (result + y) * 31
        self._hash = result
        return result
        

class Group:
    """
    A group of cells.
    """
    def __init__(self, cells):
        self._hash = None
        self.cells = set(cells)
        
        for cell in self.cells:
            coords = cell.coords
            if not coords in GROUPS_FROM_COORDS:
                GROUPS_FROM_COORDS[coords] = set()
            GROUPS_FROM_COORDS[coords].add(self)
    
    def __hash__(self):
        if self._hash:
            return self._hash
        
        #Groups with different orders of cells must have the same hash
        #So I can't multiply between additions, because that wouldn't
        #be commutative
        self._hash = sum([hash(cell) for cell in self.cells])
        return self._hash
    
    def __iter__(self):
        return iter(self.cells)

#Initialize the list of groups
GROUPS = set()
GROUPS_FROM_COORDS = dict()

#Add rows and columns to groups
for c1 in VALS:
    row = set()
    col = set()
    for c2 in VALS:
        row.add(Cell((c1, c2)))
        col.add(Cell((c2, c1)))
    GROUPS.add(Group(row))
    GROUPS.add(Group(col))

#Add squares to groups
for sx in range(1, 1 + SUDOKU_SIZE, SQUARE_SIZE):
    for sy in range(1, 1 + SUDOKU_SIZE, SQUARE_SIZE):
        square = set()
        for dx in range(SQUARE_SIZE):
            for dy in range(SQUARE_SIZE):
                coords = (sx + dx, sy + dy)
                square.add(Cell(coords))
        GROUPS.add(Group(square))