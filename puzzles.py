# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:16:00 2021

@author: rober
"""

import puzzle_utils

SUDOKU_VALUES = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_sudoku_variant(square_size, cell_values=None):
    layout = set()
    size = square_size ** 2
    
    #Initialize the layout
    for y in range(1, size+1):
        for x in range(1, size+1):
            coords = puzzle_utils.Coords(x, y)
            layout.add(coords)
    
    #Initialize the values
    if cell_values is None:
        cell_values = set(SUDOKU_VALUES[:size])
    else:
        cell_values = set(cell_values)
    
    #Initialize the groups
    groups = set()
    
    #Add rows and columns
    for c1 in range(1, size+1):
        row = set()
        col = set()
        for c2 in range(1, size+1):
            row_coords = puzzle_utils.Coords(c2, c1)
            col_coords = puzzle_utils.Coords(c1, c2)
           
            row.add(row_coords)
            col.add(col_coords)
        row_group = puzzle_utils.Group(row)
        col_group = puzzle_utils.Group(col)
        groups.add(row_group)
        groups.add(col_group)
    
    #Add squares
    for uly in range(1, size+1, square_size):
        for ulx in range(1, size+1, square_size):
            square = set()
            for dy in range(0, square_size):
                for dx in range(0, square_size):
                    x = ulx + dx
                    y = uly + dy
                    coords = puzzle_utils.Coords(x, y)
                    square.add(coords)
            square_group = puzzle_utils.Group(square)
            groups.add(square_group)
    
    #Get the layout and printing functions
    get_start = lambda ls: get_rectangular_start(ls, cell_values)
    print_board = lambda board: print_rectangular_board(board,
                                                        size,
                                                        size,
                                                        square_size)
    
    sudoku = puzzle_utils.Puzzle(layout,
                                 cell_values,
                                 groups,
                                 get_start,
                                 print_board)
    
    return sudoku

# # The normal Sudoku puzzle.
# # A 9x9 board with 9 rows, 9 columns and 9 3x3 squares.
# NORMAL_SUDOKU_SIZE = 9
# NORMAL_SUDOKU_SQUARE_SIZE = 3

# #Initialize the layout
# NORMAL_SUDOKU_LAYOUT = set()
# for y in range(1, NORMAL_SUDOKU_SIZE+1):
#     for x in range(1, NORMAL_SUDOKU_SIZE+1):
#         coords = puzzle_utils.Coords(x, y)
#         NORMAL_SUDOKU_LAYOUT.add(coords)

# #Initialize the values
# NORMAL_SUDOKU_VALUES = set('123456789') #use chars instead of ints

# #Initialize the groups
# NORMAL_SUDOKU_GROUPS = set()

# #Add rows and columns
# for c1 in range(1, NORMAL_SUDOKU_SIZE+1):
#     row = set()
#     col = set()
#     for c2 in range(1, NORMAL_SUDOKU_SIZE+1):
#         row_coords = puzzle_utils.Coords(c2, c1)
#         col_coords = puzzle_utils.Coords(c1, c2)
       
#         row.add(row_coords)
#         col.add(col_coords)
#     row_group = puzzle_utils.Group(row)
#     col_group = puzzle_utils.Group(col)
#     NORMAL_SUDOKU_GROUPS.add(row_group)
#     NORMAL_SUDOKU_GROUPS.add(col_group)

# #Add squares
# for uly in range(1, NORMAL_SUDOKU_SIZE+1, NORMAL_SUDOKU_SQUARE_SIZE):
#     for ulx in range(1, NORMAL_SUDOKU_SIZE+1, NORMAL_SUDOKU_SQUARE_SIZE):
#         square = set()
#         for dy in range(0, NORMAL_SUDOKU_SQUARE_SIZE):
#             for dx in range(0, NORMAL_SUDOKU_SQUARE_SIZE):
#                 x = ulx + dx
#                 y = uly + dy
#                 coords = puzzle_utils.Coords(x, y)
#                 square.add(coords)
#         square_group = puzzle_utils.Group(square)
#         NORMAL_SUDOKU_GROUPS.add(square_group)

def get_rectangular_start(start_list, cell_values):
    start = dict()
    for y, row in enumerate(start_list, 1):
        for x, val in enumerate(row, 1):
            val = str(val)
            if not val in cell_values:
                continue
            coords = puzzle_utils.Coords(x, y)
            start[coords] = str(val)
    return start

# get_normal_sudoku_start = lambda s: get_rectangular_start(s,
#                                                           NORMAL_SUDOKU_VALUES)

def print_rectangular_board(board, width, height, square_size):
    num_squares_per_row = width // square_size
    
    print('+' + '-' * (width + num_squares_per_row - 1) + '+')
    for y in range(1, height+1):
        print('|', end='')
        for x in range(1, width+1):
            cell = board[puzzle_utils.Coords(x, y)]
            value = cell.value
            if value is None:
                print(' ', end='')
            else:
                print(value, end='')
            
            if x % square_size == 0 and x != width:
                print('|', end='')
        print('|')
        
        if y % square_size == 0 and y != height:
            print('|', end='')
            print(('-'*square_size + '+')*(num_squares_per_row-1), end='')
            print('-' *square_size + '|')
    
    print('+' + '-' * (width + num_squares_per_row - 1) + '+')

# print_normal_sudoku_board = lambda board: print_rectangular_board(board,
#                                                                   NORMAL_SUDOKU_SIZE,
#                                                                   NORMAL_SUDOKU_SIZE,
#                                                                   NORMAL_SUDOKU_SQUARE_SIZE)
# def print_normal_sudoku_board(board):
#     print('+-----------+')
#     for y in range(1, NORMAL_SUDOKU_SIZE+1):
#         print('|', end='')
#         for x in range(1, NORMAL_SUDOKU_SIZE+1):
#             cell = board[puzzle_utils.Coords(x, y)]
#             value = cell.value
#             if value is None:
#                 print(' ', end='')
#             else:
#                 print(value, end='')
#             if x in (3, 6):
#                 print('|', end='')
#         print('|')
#         if y in(3, 6):
#             print('|---+---+---|')
#     print('+-----------+')

# NORMAL_SUDOKU = puzzle_utils.Puzzle(NORMAL_SUDOKU_LAYOUT,
#                                     NORMAL_SUDOKU_VALUES,
#                                     NORMAL_SUDOKU_GROUPS,
#                                     get_normal_sudoku_start,
#                                     print_normal_sudoku_board)
NORMAL_SUDOKU = get_sudoku_variant(3)
HEXA_SUDOKU = get_sudoku_variant(4)
FIVE_SUDOKU = get_sudoku_variant(5, 'ABCDEFGHIJKLMNOPQRSTUVWXY')