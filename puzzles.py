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
    get_board_str = lambda board: get_rectangular_board_state_str(board,
                                                                  size,
                                                                  size,
                                                                  square_size)
    
    sudoku = puzzle_utils.Puzzle(layout,
                                 cell_values,
                                 groups,
                                 get_start,
                                 print_board,
                                 get_board_str)
    
    return sudoku

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

def get_rectangular_board_state_str(board, width, height, square_size):
    result = ''
    
    num_squares_per_row = width // square_size
    
    result += '┌'
    # print('┌', end='')
    
    result += ('─'*square_size + '┬')*(num_squares_per_row-1)
    # print(('─'*square_size + '┬')*(num_squares_per_row-1), end='')
    
    result += '─' *square_size + '┐\n'
    # print('─' *square_size + '┐')
    
    for y in range(1, height+1):
        result += '│'
        # print('│', end='')
        
        for x in range(1, width+1):
            cell = board[puzzle_utils.Coords(x, y)]
            value = cell.value
            if value is None:
                result += ' '
                # print(' ', end='')
            else:
                result += str(value)
                # print(value, end='')
            
            if x % square_size == 0 and x != width:
                result += '│'
                # print('│', end='')
        
        result += '│\n'
        # print('│')
        
        #┌───┬───┐
        #│   │   │
        #├───┼───┤
        #│   │   │
        #└───┴───┘
        if y % square_size == 0 and y != height:
            result += '├'
            # print('├', end='')
            
            result += ('─'*square_size + '┼')*(num_squares_per_row-1)
            # print(('─'*square_size + '┼')*(num_squares_per_row-1), end='')
            
            result += '─' *square_size + '┤\n'
            # print('─' *square_size + '┤')
    
    result += '└'
    # print('└', end='')
    
    result += ('─'*square_size + '┴')*(num_squares_per_row-1)
    # print(('─'*square_size + '┴')*(num_squares_per_row-1), end='')
    
    result += '─' *square_size + '┘\n'
    # print('─' *square_size + '┘')
    
    return result

def print_rectangular_board(board, width, height, square_size):
    num_squares_per_row = width // square_size
    
    # print('┌' + '─' * (width + num_squares_per_row - 1) + '┐')
    print('┌', end='')
    print(('─'*square_size + '┬')*(num_squares_per_row-1), end='')
    print('─' *square_size + '┐')
    
    for y in range(1, height+1):
        print('│', end='')
        for x in range(1, width+1):
            cell = board[puzzle_utils.Coords(x, y)]
            value = cell.value
            if value is None:
                print(' ', end='')
            else:
                print(value, end='')
            
            if x % square_size == 0 and x != width:
                print('│', end='')
        print('│')
        #┌───┬───┐
        #│   │   │
        #├───┼───┤
        #│   │   │
        #└───┴───┘
        if y % square_size == 0 and y != height:
            print('├', end='')
            print(('─'*square_size + '┼')*(num_squares_per_row-1), end='')
            print('─' *square_size + '┤')
    
    # print('└' + '─' * (width + num_squares_per_row - 1) + '┘')
    print('└', end='')
    print(('─'*square_size + '┴')*(num_squares_per_row-1), end='')
    print('─' *square_size + '┘')

NORMAL_SUDOKU = get_sudoku_variant(3)
HEXA_SUDOKU = get_sudoku_variant(4)
FIVE_SUDOKU = get_sudoku_variant(5, 'ABCDEFGHIJKLMNOPQRSTUVWXY')