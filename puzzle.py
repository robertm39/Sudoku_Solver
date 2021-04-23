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
    def __init__(self, layout, numbering, groups):
        self.layout = set(layout)
        self.numbering = set(numbering)
        self.groups = {set(group) for group in groups}
        
        self.groups_from_coord = dict()
        
        for group in self.groups:
            for coord in group:
                if not coord in self.groups_from_coord:
                    self.groups_from_coord[coord] = set()
                self.groups_from_coord[coord].add(group)