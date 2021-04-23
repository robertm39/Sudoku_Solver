# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:32:04 2021

@author: rober
"""

import sudoku_solver

# def copy_board(board_1, board_2):
#     """
#     Copy the data from board_1 onto board_2.
#     """
#     for coords, cell in board_1.items():
#         other_cell = board_2[coords]
        
#         to_remove = [n for n in other_cell.possible if not n in cell.possible]
#         for num in to_remove:
#             other_cell.remove_possibility(num)

def copy_board(solver_1, solver_2):
    """
    Copy the board data from solver_1 onto solver_2.
    """
    for coords, cell in solver_1.board.items():
        other_cell = solver_2.board[coords]
        
        to_remove = [n for n in other_cell.possible if not n in cell.possible]
        for num in to_remove:
            solver_2.remove_possibility(coords, num)
            # other_cell.remove_possibility(num)

class HypoNumber:
    """
    A strategy that fills in a square with a possible number and sees if it
    results in a contradiction. If it does, it removes that possibility.
    """
    def __init__(self, parent, max_depth):
        self.parent = parent
        self.max_depth = max_depth
        self.unsolved_cells = set()
        
        for _, cell in self.parent.board.items():
            self.unsolved_cells.add(cell)
    
    def notify_value(self, coords):
        self.unsolved_cells.remove(self.parent.board[coords])
    
    def notify_removal(self, coords, num):
        pass
    
    def do_removals(self):
        # print('Doing hypothetical')
        #Go through all the cells, try hypotheticals until one yields something
        for cell in self.unsolved_cells:
            for num in set(cell.possible):
                new_depth = self.max_depth - 1
                new_solver = sudoku_solver.SudokuSolver(self.parent.puzzle,
                                                        None,
                                                        max_depth=new_depth,
                                                        quiet=True)
                copy_board(self.parent, new_solver)
                
                #Now do the hypothetical
                for value in self.parent.puzzle.cell_values:
                    if value == num:
                        continue
                    new_solver.remove_possibility(cell.coords, value)
                
                # new_cell = new_solver.board[cell.coords]
                # new_cell.set_value(num)
                
                
                new_solver.solve()
                
                #If this led to a contradiction, then remove the possibility
                #And stop, because we want to minimize the amount of time
                #we spend doing expensive hypotheticals
                if new_solver.contradiction:
                    self.parent.remove_possibility(cell.coords, num)
                    # cell.remove_possibility(num)
                    return
                