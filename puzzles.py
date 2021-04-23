# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:16:00 2021

@author: rober
"""

import puzzle_utils

# The normal Sudoku puzzle.
# A 9x9 board with 9 rows, 9 columns and 9 3x3 squares.
NORMAL_SUDOKU_SIZE = 9
NORMAL_SUDOKU_SQUARE_SIZE = 3

#Initialize the layout
NORMAL_SUDOKU_LAYOUT = set()
for y in range(1, NORMAL_SUDOKU_SIZE+1):
    for x in range(1, NORMAL_SUDOKU_SIZE+1):
        coords = puzzle_utils.Coords(x, y)
        NORMAL_SUDOKU_LAYOUT.add(coords)

#Initialize the values
NORMAL_SUDOKU_VALUES = set('123456789') #use chars instead of ints

#Initialize the groups
NORMAL_SUDOKU_GROUPS = set()

#Add rows and columns
for c1 in range(1, NORMAL_SUDOKU_SIZE+1):
    row = set()
    col = set()
    for c2 in range(1, NORMAL_SUDOKU_SIZE+1):
        row_coords = puzzle_utils.Coords(c2, c1)
        col_coords = puzzle_utils.Coords(c1, c2)
       
        row.add(row_coords)
        col.add(col_coords)
    row_group = puzzle_utils.Group(row)
    col_group = puzzle_utils.Group(col)
    NORMAL_SUDOKU_GROUPS.add(row_group)
    NORMAL_SUDOKU_GROUPS.add(col_group)

#Initialize the squares
for uly in range(1, NORMAL_SUDOKU_SIZE+1, NORMAL_SUDOKU_SQUARE_SIZE):
    for ulx in range(1, NORMAL_SUDOKU_SIZE+1, NORMAL_SUDOKU_SQUARE_SIZE):
        square = set()
        for dy in range(0, NORMAL_SUDOKU_SQUARE_SIZE):
            for dx in range(0, NORMAL_SUDOKU_SQUARE_SIZE):
                x = ulx + dx
                y = uly + dy
                coords = puzzle_utils.Coords(x, y)
                square.add(coords)
        square_group = puzzle_utils.Group(square)
        NORMAL_SUDOKU_GROUPS.add(square_group)

def get_normal_sudoku_start(start_list):
    # print('Getting start')
    start = dict()
    for y, row in enumerate(start_list, 1):
        for x, val in enumerate(row, 1):
            if not val in range(1, NORMAL_SUDOKU_SIZE+1):
                continue
            # print('{}: {}'.format(coords, val))
            coords = puzzle_utils.Coords(x, y)
            start[coords] = str(val)
    return start

def print_normal_sudoku_board(board):
    print('+-----------+')
    for y in range(1, NORMAL_SUDOKU_SIZE+1):
        print('|', end='')
        for x in range(1, NORMAL_SUDOKU_SIZE+1):
            cell = board[puzzle_utils.Coords(x, y)]
            value = cell.value
            if value is None:
                print(' ', end='')
            else:
                print(value, end='')
            if x in (3, 6):
                print('|', end='')
        print('|')
        if y in(3, 6):
            print('|---+---+---|')
    print('+-----------+')

NORMAL_SUDOKU = puzzle_utils.Puzzle(NORMAL_SUDOKU_LAYOUT,
                                    NORMAL_SUDOKU_VALUES,
                                    NORMAL_SUDOKU_GROUPS,
                                    get_normal_sudoku_start,
                                    print_normal_sudoku_board)