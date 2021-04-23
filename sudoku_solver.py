# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:43:09 2021

@author: rober
"""

from queue import SimpleQueue

import utils

import twins_strategy
import hypothetical_strategy

class SudokuSolver:
    def __init__(self, data=None, max_depth=1, quiet=False):
        self.board = dict()
        self.known_value_cells = SimpleQueue()
        
        if data is None:
            data = [[None for _ in range(utils.SUDOKU_SIZE)]\
                    for _ in range(utils.SUDOKU_SIZE)]
        
        for y, row in enumerate(data, start=1):
            for x, num in enumerate(row, start=1):
                if not num in utils.VALS:
                    num = None
                
                cell = utils.Cell((x, y), num, self)
                self.board[x, y] = cell
                if num in utils.VALS:
                    self.known_value_cells.put(cell)
        
        self.max_depth = max_depth
        self.quiet = quiet
        
        self.contradiction = False
        
        self.strategies = list()
        self.strategies.append(twins_strategy.InTwins(self, [1, 2, 3, 4, 5, 6, 7, 8]))
        if self.max_depth:
            strategy = hypothetical_strategy.HypoNumber(self, self.max_depth)
            self.strategies.append(strategy)
        
        self.changed = False
    
    def print_state(self):
        utils.print_board(self.board)
    
    def alert_value(self, cell):
        self.known_value_cells.put(cell)
        self.changed = True
        
        for strat in self.strategies:
            strat.alert_value(cell)
    
    def alert_removal(self, cell, num):
        self.changed = True
        
        for strat in self.strategies:
            strat.alert_removal(cell, num)
    
    def alert_contradiction(self):
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
            for coords in utils.get_adjacent(cell.coords):
                self.board[coords].remove_possibility(num)
    
    def solve(self):
        """
        Solve the sudoku.
        """
        if not self.quiet:
            self.print_state()
            print('')
        
        self.changed = True
        
        while self.changed and not self.contradiction:
            
            self.basic_elimination()
            
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
