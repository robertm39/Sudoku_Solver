# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 16:30:16 2021

@author: rober
"""

import utils

import sudoku_solver

x = object()

#Easy
puzzle_1 = [[x, 9, 2, x, 3, x, x, 1, x],
            [x, 3, x, 6, 7, x, x, x, x],
            [x, 8, 7, x, x, 9, 3, x, x],
            [x, 6, x, 1, 4, x, x, x, 3],
            [4, x, 3, x, x, x, 1, x, 8],
            [8, x, x, x, 5, 7, x, 6, x],
            [x, x, 6, 7, x, x, 5, 8, x],
            [x, x, x, x, 8, 6, x, 3, x],
            [x, 7, x, x, 1, x, 6, 2, x]]

#Hard
puzzle_2 = [[x, x, x, 7, 9, x, x, 5, 6],
            [7, x, x, x, x, x, 8, x, 1],
            [x, 1, 9, x, x, x, x, x, x],
            [6, x, 1, x, x, x, x, 2, 8],
            [x, x, x, x, 1, x, x, x, x],
            [4, 2, x, x, x, x, 6, x, 3],
            [x, x, x, x, x, x, 2, 3, x],
            [1, x, 2, x, x, x, x, x, 5],
            [3, 9, x, x, 5, 4, x, x, x]]

#for testing
puzzle_3 = [[x, x, x, x, x, x, x, x, x],
            [x, x, x, 1, x, x, x, x, x],
            [x, x, x, x, x, x, 1, x, x],
            [x, x, x, x, x, x, x, x, x],
            [x, x, x, x, x, x, x, x, x],
            [x, x, 1, x, x, x, x, x, x],
            [x, x, x, x, x, x, x, x, x],
            [x, x, x, x, x, x, x, x, x],
            [x, 1, x, x, x, x, x, x, x]]

puzzle_4 = [[x, x, x, x, x, x, x, x, x],
            [x, x, x, 1, 2, x, x, x, x],
            [x, x, x, x, x, x, 1, 2, x],
            [x, x, x, x, x, x, x, x, x],
            [x, x, x, x, x, x, x, x, x],
            [x, x, x, x, x, x, x, x, x],
            [x, x, x, x, x, x, x, x, x],
            [x, x, 2, x, x, x, x, x, x],
            [x, x, 1, x, x, x, x, x, x]]

#Evil level
puzzle_5 = [[x, x, 6, x, x, x, x, x, x],
            [8, x, 9, x, x, 2, x, x, 5],
            [2, x, x, 6, x, 9, 1, x, x],
            [x, x, 5, x, 1, 7, x, x, x],
            [x, 7, x, x, x, x, x, 4, x],
            [x, x, x, 9, 2, x, 3, x, x],
            [x, x, 4, 1, x, 3, x, x, 6],
            [7, x, x, 5, x, x, 9, x, 3],
            [x, x, x, x, x, x, 8, x, x]]

#Puzzle 5, with a number taken out
puzzle_6 = [[x, x, 6, x, x, x, x, x, x],
            [8, x, 9, x, x, 2, x, x, x],
            [2, x, x, 6, x, 9, 1, x, x],
            [x, x, 5, x, 1, 7, x, x, x],
            [x, 7, x, x, x, x, x, 4, x],
            [x, x, x, 9, 2, x, 3, x, x],
            [x, x, 4, 1, x, 3, x, x, 6],
            [7, x, x, 5, x, x, 9, x, 3],
            [x, x, x, x, x, x, 8, x, x]]

puzzle_7 = [[x, x, x, x, 5, 4, x, 1, x],
            [x, 9, 1, x, x, 7, x, x, 3],
            [x, x, x, 8, x, x, x, 6, x],
            [x, x, 7, x, x, 8, x, x, x],
            [4, x, x, x, 7, x, x, x, 5],
            [x, x, x, 6, x, x, 1, x, x],
            [x, 4, x, x, x, 6, x, x, x],
            [7, x, x, 3, x, x, 2, 5, x],
            [x, 6, x, 7, 8, x, x, x, x]]

puzzle_8 = [[x, x, x, 4, x, x, x, x, 9],
            [x, 6, 4, x, x, 7, x, 2, 3],
            [5, x, 7, x, x, x, x, x, x],
            [x, x, x, 2, x, x, 6, x, x],
            [x, x, 8, 1, x, 6, 3, x, x],
            [x, x, 1, x, x, 4, x, x, x],
            [x, x, x, x, x, x, 7, x, 5],
            [2, 3, x, 7, x, x, 9, 1, x],
            [4, x, x, x, x, 1, x, x, x]]

puzzle_9 = [[x, x, x, x, x, x, 3, 1, x],
            [x, x, x, 3, 2, x, x, x, 7],
            [x, 9, x, 7, x, x, 8, x, 6],
            [x, x, x, x, x, 4, 2, 5, x],
            [x, x, x, x, 3, x, x, x, x],
            [x, 6, 4, 8, x, x, x, x, x],
            [7, x, 2, x, x, 3, x, 4, x],
            [9, x, x, x, 1, 7, x, x, x],
            [x, 8, 6, x, x, x, x, x, x]]

# puzzle_x = [[],
#             [],
#             [],
#             [],
#             [],
#             [],
#             [],
#             [],
#             []]

# puzzle_x = [[x, x, x, x, x, x, x, x, x],
#             [x, x, x, x, x, x, x, x, x],
#             [x, x, x, x, x, x, x, x, x],
#             [x, x, x, x, x, x, x, x, x],
#             [x, x, x, x, x, x, x, x, x],
#             [x, x, x, x, x, x, x, x, x],
#             [x, x, x, x, x, x, x, x, x],
#             [x, x, x, x, x, x, x, x, x],
#             [x, x, x, x, x, x, x, x, x]]

def solver_test():
    puzzle = puzzle_6
    solver = sudoku_solver.SudokuSolver(puzzle)
    solver.solve()

def adj_test():
    coords = (1, 1)
    adj = utils.adjacent(coords)
    for coords in adj:
        print(coords)

def groups_test():
    for group in utils.GROUPS:
        utils.print_group(group)

def main():
    solver_test()
    # adj_test()
    # groups_test()

if __name__ == '__main__':
    main()