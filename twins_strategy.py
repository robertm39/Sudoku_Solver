# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:11:55 2021

@author: rober
"""

import itertools

import utils

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
        self.data_from_groups = dict()
        
        self.initialize_data()
        
    def initialize_data(self):
        for group in utils.GROUPS:
            unsolved_numbers = set(utils.VALS)
            for g_cell in group.cells:
                cell = self.parent.board[g_cell.coords]
                if cell.num is not None:
                    unsolved_numbers.remove(cell.num)
            
            coords_from_number = {num:set() for num in unsolved_numbers}
            for g_cell in group.cells:
                cell = self.parent.board[g_cell.coords]
                for num in cell.possible:
                    if not num in coords_from_number:
                        continue
                    coords_from_number[num].add(cell.coords)
                    
            data = OneGroupInTwinsData(group)
            data.coords_from_number = coords_from_number
            data.unsolved_numbers = unsolved_numbers
            
            self.data_from_groups[group] = data
            
    def alert_value(self, cell):
        """
        Eliminate this value from the unsolved values for all cells
        in the same group as this cell.
        
        Parameters:
            cell: The cell whose value was determined.
        """
        for group in utils.GROUPS_FROM_COORDS[cell.coords]:
            if not group in self.data_from_groups:
                print('FAILED TO FIND GROUP')
                raise AssertionError
                continue
            data = self.data_from_groups[group]
            data.unsolved_numbers.remove(cell.num)
            # del data.coords_from_number[cell.num]
    
    def alert_removal(self, cell, num):
        """
        Remove the given cell from the appropriate sets.
        
        Parameters:
            cell: The cell that had a possibility eliminated.
            num: The possibility that was eliminated.
        """
        # print("Alerting removal")
        # print("Removing {} in cell {}".format(num, cell))
        for group in utils.GROUPS_FROM_COORDS[cell.coords]:
            if not group in self.data_from_groups:
                print('FAILED TO FIND GROUP')
                raise AssertionError
                continue
            # utils.print_group(group)
            
            data = self.data_from_groups[group]
            
            # if 5 in data.coords_from_number:
                # print('Num of fives: {}'.format(len(data.coords_from_number[5])))
            
            if not num in data.coords_from_number:
                continue
            
            coords_from_number = data.coords_from_number[num]
            # print(coords_from_number)
            coords_from_number.discard(cell.coords)
            
            # if 5 in data.coords_from_number:
                # print('Num of fives: {}'.format(len(data.coords_from_number[5])))
            # print(coords_from_number)
        
        # print("Done alerting removal")
    
    def do_eliminations(self):
        # print('*******************************************')
        # print('Doing eliminations')
        for group, data in self.data_from_groups.items():
            # utils.print_group(group)
            for order in self.orders:
                nums_to_consider = set()
                #Only consider numbers with at most order cells
                #Otherwise, that number combined with others will always
                #have too many cells
                for num in data.unsolved_numbers:
                    num_cells = len(data.coords_from_number[num])
                    # print('Number {}: {} cells'.format(num, num_cells))
                    if num_cells <= order:
                        nums_to_consider.add(num)
                
                # print('Unsolved: {}'.format(data.unsolved_numbers))
                # print('Nums to consider: {}'.format(nums_to_consider))
                for comb in itertools.combinations(nums_to_consider, order):
                    # print('Testing {}'.format(comb))
                    comb = set(comb)
                    coords_with_nums = set()
                    for num in comb:
                        c_for_num = data.coords_from_number.get(num, set())
                        # print('Num {} has {}'.format(num, len(c_for_num)))
                        coords_with_nums.update(c_for_num)
                    num_of_cells = len(coords_with_nums)
                    # print('num_of_cells: {}'.format(num_of_cells))
                    
                    #If there are more cells than numbers,
                    #then we can't conclude anything
                    if num_of_cells > order:
                        continue
                    
                    #If there are fewer cells than numbers,
                    #this is a contradiction
                    if num_of_cells < order:
                        self.parent.alert_contradiction()
                        return
                    
                    # print('Eliminating')
                    #If the number of cells equals the order,
                    #then we can get rid of all other possibilities
                    #from these cells
                    for num in utils.VALS:
                        if num in comb:
                            continue
                        # print('Removing {}'.format(num))
                        for coords in coords_with_nums:
                            cell = self.parent.board[coords]
                            cell.remove_possibility(num)
            # print('\n')
        # print('*******************************************')
            