# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:11:55 2021

@author: rober
"""

import itertools

# import utils

class OneGroupInTwinsData:
    """
    Stores the data for the Twins algorithm for one group.
    """
    def __init__(self, group):
        self.group = group
        self.coords_from_number = dict()
        self.unsolved_numbers = set()

class InTwins:
    """
    A strategy that sees whether X cells in a group are the only cells left
    with X certain possible numbers, and makes those the only possibilities
    those cells have.
    """
    def __init__(self, parent, orders=None):
        """
        Initialize an InTwins strategy object.
        
        Parameters:
            parent: The parent SudokuSolver.
            orders: A tuple of the sizes of tuplets to consider.
        """
        if orders is None:
            self.orders = tuple([1])
        else:
            self.orders = tuple(orders)
        
        self.parent = parent
        self.puzzle = self.parent.puzzle
        self.data_from_groups = dict()
        
        self.initialize_data()
        
    def initialize_data(self):
        # for group in utils.GROUPS:
        for group in self.puzzle.groups:
            # unsolved_numbers = set(utils.VALS)
            unsolved_numbers = set(self.puzzle.cell_values)
            for coords in group:
                cell = self.parent.board[coords]
                if cell.value is not None:
                    unsolved_numbers.remove(cell.value)
            
            coords_from_number = {num:set() for num in unsolved_numbers}
            for coords in group:
                cell = self.parent.board[coords]
                for num in cell.possible:
                    if not num in coords_from_number:
                        continue
                    coords_from_number[num].add(coords)
                    
            data = OneGroupInTwinsData(group)
            data.coords_from_number = coords_from_number
            data.unsolved_numbers = unsolved_numbers
            
            self.data_from_groups[group] = data
            
    def notify_value(self, coords):
        """
        Eliminate this value from the unsolved values for all cells
        in the same group as this cell.
        
        Parameters:
            cell: The cell whose value was determined.
        """
        # for group in utils.GROUPS_FROM_COORDS[cell.coords]:
        for group in self.puzzle.groups_from_coord[coords]:
            if not group in self.data_from_groups:
                print('FAILED TO FIND GROUP')
                raise AssertionError
                continue
            data = self.data_from_groups[group]
            
            cell = self.parent.board[coords]
            
            data.unsolved_numbers.discard(cell.value)
    
    def notify_removal(self, coords, num):
        """
        Remove the given cell from the appropriate sets.
        
        Parameters:
            cell: The cell that had a possibility eliminated.
            num: The possibility that was eliminated.
        """
        # for group in utils.GROUPS_FROM_COORDS[cell.coords]:
        for group in self.puzzle.groups_from_coord[coords]:
            if not group in self.data_from_groups:
                print('FAILED TO FIND GROUP')
                raise AssertionError
                continue
            
            data = self.data_from_groups[group]
            
            if not num in data.coords_from_number:
                continue
            
            coords_from_number = data.coords_from_number[num]
            coords_from_number.discard(coords)
    
    def do_removals(self):
        for group, data in self.data_from_groups.items():
            for order in self.orders:
                nums_to_consider = set()
                #Only consider numbers with at most order cells
                #Otherwise, that number combined with others will always
                #have too many cells
                for num in data.unsolved_numbers:
                    num_cells = len(data.coords_from_number[num])
                    if num_cells <= order:
                        nums_to_consider.add(num)
                
                for comb in itertools.combinations(nums_to_consider, order):
                    comb = set(comb)
                    coords_with_nums = set()
                    for num in comb:
                        c_for_num = data.coords_from_number.get(num, set())
                        coords_with_nums.update(c_for_num)
                    num_of_cells = len(coords_with_nums)
                    
                    #If there are more cells than numbers,
                    #then we can't conclude anything
                    if num_of_cells > order:
                        continue
                    
                    #If there are fewer cells than numbers,
                    #this is a contradiction
                    if num_of_cells < order:
                        self.parent.set_contradiction()
                        return
                    
                    #If the number of cells equals the order,
                    #then we can get rid of all other possibilities
                    #from these cells
                    # for num in utils.VALS:
                    for num in self.puzzle.cell_values:
                        if num in comb:
                            continue
                        for coords in coords_with_nums:
                            self.parent.remove_possibility(coords, num)
                            # cell = self.parent.board[coords]
                            # cell.remove_possibility(num)
