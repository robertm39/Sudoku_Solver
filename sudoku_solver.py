# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:43:09 2021

@author: rober
"""

# from queue import SimpleQueue

# import utils
import puzzle_utils

from basic_elimination_strategy import BasicElimination
# from twins_strategy import InTwins
# from hypothetical_strategy import HypoNumber

class SudokuSolver:
    def __init__(self,
                 puzzle,
                 start=None,
                 max_depth=1,
                 quiet=False):
        
        self.puzzle = puzzle
        # self.start = start
        self.board = puzzle_utils.Board(puzzle)
        
        self.max_depth = max_depth
        self.quiet = quiet
        
        self.contradiction = False
        
        self.strategies = list()
        self.strategies.append(BasicElimination(self))
        
        # self.strategies.append(InTwins(self, [1, 2, 3, 4, 5, 6, 7, 8]))
        # if self.max_depth > 0:
        #     self.strategies.append(HypoNumber(self, self.max_depth))
        
        
        self.initialize(start)
        
        self.changed = False
    
    def initialize(self, start):
        if start is None:
            return
        
        for coords, val in start.items():
            other_vals = set(self.puzzle.cell_values)
            other_vals.discard(val)
            for o_val in other_vals:
                self.remove_possibility(coords, o_val)
    
    def print_state(self):
        # puzzle_utils.print_board(self.board)
        self.puzzle.print_board(self.board)
    
    def remove_possibility(self, coords, num):
        cell = self.board[coords]
        
        #If nothing happened, there's no need to notify anything
        if not cell.remove_possibility(num):
            return
        self.changed = True
        
        for strategy in self.strategies:
            strategy.notify_removal(coords, num)
            if cell.has_value():
                strategy.notify_value(coords)
        
        if cell.has_contradiction():
            self.set_contradiction()
            return
    
    def set_contradiction(self):
        self.contradiction = True
    
    # def alert_value(self, cell):
    #     self.known_value_cells.put(cell)
    #     self.changed = True
        
    #     for strat in self.strategies:
    #         strat.alert_value(cell)
    
    # def alert_removal(self, cell, num):
    #     self.changed = True
        
    #     for strat in self.strategies:
    #         strat.alert_removal(cell, num)
    
    # def alert_contradiction(self):
    #     self.contradiction = True
    
    # def basic_elimination(self):
    #     """
    #     Eliminate possibilities from the known numbers.
    #     """
    #     while not self.known_value_cells.empty():
    #         cell = self.known_value_cells.get_nowait()
    #         if cell.num is None:
    #             continue
    #         num = cell.num
    #         for coords in utils.get_adjacent(cell.coords):
    #             self.board[coords].remove_possibility(num)
    
    def solve(self):
        """
        Solve the sudoku.
        """
        if not self.quiet:
            self.print_state()
            print('')
        
        self.changed = True
        
        while self.changed and not self.contradiction:
            
            # self.basic_elimination()
            
            #We've done all the basic elimination we can
            #If we can't do anything else, we're done
            self.changed = False
            for strat in self.strategies:
                strat.do_removals()
                
                #If something changed, go back to basic elimination
                if self.changed:
                    continue
        
        if not self.quiet:
            if self.contradiction:
                print("Contradiction found")
            self.print_state()
