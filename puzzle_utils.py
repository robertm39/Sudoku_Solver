# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:30:47 2021

@author: rober
"""

class Coords:
    """
    A pair of coordinates.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._hash = None
    
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
    
    def __eq__(self, other):
        if not type(other) is Coords:
            return False
        
        return self.x == other.x and self.y == other.y
    
    def __neq__(self, other):
        return not (self == other)
    
    def __hash__(self):
        if self._hash is not None:
            return self._hash
        
        result = 17
        result = (result + self.x) * 31
        result = (result + self.y) * 31
        self._hash = result
        return self._hash

class Group:
    """
    A group of coordinates.
    """
    def __init__(self, coords):
        self._coords = set(coords)
        self._hash = None
    
    def __contains__(self, obj):
        return obj in self._coords
    
    def __iter__(self):
        return iter(self._coords)
    
    def __eq__(self, other):
        return self._coords == other._coords
    
    def __neq__(self, other):
        return not(self == other)
    
    def __hash__(self):
        if self._hash is not None:
            return self._hash
    
        sub_hashes = sorted([hash(c) for c in self._coords])
        
        result = 17
        for sub_hash in sub_hashes:
            result = (result + sub_hash) * 31
        
        self._hash = result
        return self._hash

class Puzzle:
    """
    A definition of a generalized sudoku puzzle.
    """
    def __init__(self, layout, cell_values, groups, get_start, print_board):
        self.layout = set(layout)
        self.cell_values = set(cell_values)
        self.groups = set(groups)
        self.get_start = get_start
        self.print_board = print_board
        
        self.groups_from_coord = dict()
        
        for group in self.groups:
            for coord in group:
                if not coord in self.groups_from_coord:
                    self.groups_from_coord[coord] = set()
                self.groups_from_coord[coord].add(group)

class Cell:
    """
    A cell in a generalized sudoku puzzle,
    with a set of possible values and maybe also a value.
    """
    def __init__(self, coords, puzzle, value=None):
        self.coords = coords
        self.puzzle = puzzle
        self.value = value
        
        if self.value is not None:
            self.possible = set([self.value])
        else:
            self.possible = set(self.puzzle.cell_values)
    
    def remove_possibility(self, p):
        """
        Remove the given possibility.
        Return True if a possibility was removed and False otherwise.
        
        Parameters:
            p: The possibility to remove.
            
        Returns:
            Whether a possibility was removed.
        """
        if not p in self.possible:
            return False
        
        self.possible.remove(p)
        
        if len(self.possible) == 1:
            self.value = list(self.possible)[0]
        
        return True
    
    def has_value(self):
        return self.value is not None
    
    def has_contradiction(self):
        return len(self.possible) == 0

class Board:
    """
    A board state for a generalized sudoku puzzle,
    tracking both values and possible values of cells.
    """
    def __init__(self, puzzle):
        """
        Make an empty board for the given puzzle.
        """
        self.puzzle = puzzle
        self.board = dict()
        
        for coords in self.puzzle.layout:
            cell = Cell(coords, self.puzzle)
            self.board[coords] = cell
    
    def __getitem__(self, coords):
        return self.board[coords]
    
    def items(self):
        return self.board.items()
