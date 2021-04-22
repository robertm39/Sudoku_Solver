# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:43:09 2021

@author: rober
"""

from queue import SimpleQueue

SUDOKU_SIZE = 9
SQUARE_SIZE = 3

VALS = set(range(1, SUDOKU_SIZE+1))

#Data format: dict (int, int) -> Cell

def adjacent(cell_coords):
    """
    Return a generator that generates all adjacent cells.
    """
    x, y = cell_coords
    prev = set([cell_coords])
    
    #Yield cells in the same row or column
    for v in VALS:
        coords = (v, y)
        if coords in prev:
            continue
        prev.add(coords)
        yield coords
        
        coords = (x, v)
        if coords in prev:
            continue
        prev.add(coords)
        yield coords
    
    #Yield cells in same square
    ulx = ((x-1)//3) * 3 + 1
    uly = ((y-1)//3) * 3 + 1
    
    for dx in range(0, 3):
        for dy in range(0, 3):
            cx = ulx + dx
            cy = uly + dy
            coords = (cx, cy)
            if coords in prev:
                continue
            coords.add(prev)
            yield coords

class Cell:
    def __init__(self, parent, coords, num=None):
        self.parent = parent
        self.coords = coords
        self.num = num
        
        if self.num is None:
            self.possible = VALS.copy()
        else:
            self.possible = set([self.num])
    
    def remove_possibility(self, num):
        self.possible.remove(num)
        if len(self.possible) == 1:
            self.num = list(self.possible)[0]
            self.parent.alert_value(self)
        elif len(self.possible) == 0:
            self.num = None
            self.parent.alert_contradiction(self)

class SudokuSolver:
    def __init__(self, data=None):
        self.board = dict()
        self.known_value_cells = SimpleQueue()
        self.contradiction = False
        
        for y, row in enumerate(data, start=1):
            for x, num in enumerate(row, start=1):
                if not num in VALS:
                    num = None
                
                cell = Cell(self, (x, y), num)
                self.board[x, y] = cell
                if num in VALS:
                    self.known_value_cells.put(cell)
    
    def print_state(self):
        for y in VALS:
            for x in VALS:
                num = self.board[x, y].num
                if num is None:
                    print(' ', end='')
                else:
                    print(num, end='')
                if x in (3, 6):
                    print('|', end='')
            print('')
            if y in(3, 6):
                print('---+---+---')
    
    def alert_value(self, cell):
        self.known_value_cells.put(cell)
    
    def alert_contradiction(self, cell):
        self.contradiction = True
    
    def basic_elimination(self):
        """
        Eliminate possibilities from the known numbers.
        """
        while not self.known_value_cells.empty():
            cell = self.known_value_cells.get_nowait()
            if cell.num is None:
                continue
            num = cell.num
            for coords in adjacent(cell.coords):
                self.board[coords].possible.remove(num)
