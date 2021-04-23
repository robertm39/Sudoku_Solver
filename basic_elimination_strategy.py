# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:04:51 2021

@author: rober
"""

from queue import SimpleQueue

class BasicElimination:
    def __init__(self, solver):
        self.solver = solver
        self.puzzle = self.solver.puzzle
        
        self.known_value_coords = SimpleQueue()
    
    def notify_value(self, coords):
        self.known_value_coords.put(coords)
    
    def notify_removal(self, coords, num):
        pass
    
    def do_removals(self):
        removals = list()
        while not self.known_value_coords.empty():
            coords = self.known_value_coords.get_nowait()
            val = self.solver.board[coords].value
            
            for group in self.puzzle.groups_from_coord[coords]:
                for other_coords in group:
                    if other_coords == coords:
                        continue
                    removals.append((other_coords, val))
        
        for coords, val in removals:
            self.solver.remove_possibility(coords, val)