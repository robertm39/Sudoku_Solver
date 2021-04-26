# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 16:30:16 2021

@author: rober
"""

import puzzles

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

#"Extremely Difficult" puzzle from http://www.sudoku9x9.com/expert.php
puzzle_10 = [[1, x, x, x, x, x, 2, 7, x],
             [x, 3, x, x, 2, x, x, 1, x],
             [7, x, 9, 6, x, x, x, x, x],
             [x, 4, 8, x, x, x, 6, x, x],
             [6, x, x, 8, x, x, 9, x, x],
             [x, x, x, 5, x, x, 3, x, x],
             [x, x, x, x, x, x, x, x, x],
             [x, x, x, 2, x, 6, x, x, x],
             [x, 7, x, 1, x, 3, 5, 4, x]]

#Puzzle 10, but modified
puzzle_11 = [[x, x, 1, x, x, x, 2, 7, x],
             [x, 3, x, x, 2, x, x, 1, x],
             [7, x, 9, 6, x, x, x, x, x],
             [x, 4, 8, x, 9, x, 6, x, x],
             [6, x, x, 8, 4, x, 9, x, x],
             [x, x, x, 5, x, x, 3, x, x],
             [3, x, x, x, x, x, 1, x, x],
             [x, x, x, 2, x, 6, x, x, x],
             [x, 7, x, 1, x, 3, 5, 4, x]]

#A 17-clue one
very_hard = ['....4....',
             '12.....73',
             '.3...8...',
             '..4...6..',
             '...2.3...',
             '..5......',
             '..6.9.5..',
             '.7.....2.',
             '.........']

very_hard_2 = ['.........',
               '.....1..2',
               '.34....5.',
               '........6',
               '..734....',
               '28......1',
               '....5..4.',
               '1........',
               '6....2...']

very_hard_3 = ['........1',
               '.......23',
               '..4..5...',
               '...1.....',
               '....3.6..',
               '..7...58.',
               '....67...',
               '.1...4...',
               '52.......']

very_hard_4 = ['...21....',
               '..73.....',
               '.58......',
               '43.......',
               '2.......8',
               '.......76',
               '......25.',
               '.....73..',
               '....98...']

very_hard_x = ['.........',
               '.........',
               '.........',
               '.........',
               '.........',
               '.........',
               '.........',
               '.........',
               '.........']

#Expert level hexadoku
#https://www.sudoku-puzzles-online.com/cgi-bin/hexadoku/print-1-grid-hexadoku.cgi
puzzle_12 = ['B......3...8.F7.',
             '.F..2.4..3.1....',
             '6.84A1.7.......2',
             '0......D.9E.8AC.',
             '9......AEB0..2.4',
             '.D.A...172...E0.',
             '7...5...8.C..B..',
             '.4...E.F5..3D.97',
             '4.E7D..2.C3.....',
             '.C.F.7..142..D..',
             '....B39..D...0..',
             '...B.F.4....7.39',
             '.1C..........8D.',
             '....7.69..D0..FB',
             'E9........F....5',
             '...2.0.8....3...']

#Beginner level hexadoku
puzzle_13 = ['FA.C..9.5.02.8.6',
             '........14...5..',
             '....A438..9....1',
             'D.B.......7A....',
             '..2...4....1.D.5',
             '..4E.6D......F..',
             '..3...12......4.',
             '95.7EC..0...A...',
             '...6B8..2..F039.',
             '...5....CE.98172',
             '.E..7.A..B......',
             '3.............B.',
             '4..B.5...7.3.0..',
             'E6.9C..BA0..3.57',
             '0C..17.F6.48..D.',
             '7.5..A..B.....C.']

#25x25 Sudoku
#http://sudoku4me.com/sudoku%2025x25.php
puzzle_14 = ['QS..W.G.O..PN..CE.L.K.R.M',
             '.YDVJ.FAXH...U..MG.NWI.E.',
             '.FH.T..WD.L..B..JS....VPX',
             'MG.C.KRI..D.O.YT...A.N.U.',
             'BKPE.Q...T..CWGV..F....JA',
             'GPUS.D.O..Q..AF.YL.C.RJ..',
             'HI.NO..XG.PM..KR...VDT..B',
             '..VJ..W.YN..UT..G.KBIC.XS',
             '.DR.ACVE...JHGLWNIMPOQ..K',
             '..EXQUML.P..BSRH.F....AY.',
             'PUXB.A.SKG.FI.QD.R.E.J..N',
             '.CSO..T..FMWDKPYQX..R.GB.',
             'LE.AFVO.Q.Y.G.TNH.....X.I',
             '.V.M.RE.BC...LX...PI.U.KO',
             'W.N...XU..VBS.A..O.JTYLH.',
             'S.QWU.YG.IC.....K..D.EBO.',
             'CT..IJ.PF..SK.NX.U.H..W..',
             'R.M.L..N.V..YHEQTBAGP...C',
             '.HA.DEK..RJTF.O..PIY.LSNQ',
             '..BK.XUQMAW.R.V.O.J..F.DH',
             '..WH.....OFI.D..VEYLM...T',
             'NOGICYQ.L.H..MJ.B.S.E.DV.',
             'J..LR.NH....EOBKUMG.XS.C.',
             'T.Y..S.CR...PNU.XA..FK.Q.',
             'XBK...JTIU.RQ.....DFLGH..']

puzzle_15 = ['QS..W.G.O..PN..CE.L.K.R.M',
             '.Y..J.F..H...U..MG.N.I.E.',
             '.FH.T..WD.L..B..JS....VPX',
             'MG.C.K.I..D.O.YT...A.N.U.',
             'B.PE.Q...T..CWGV..F....JA',
             'G.US.D.O..Q..AF.YL.C.RJ..',
             'HI.NO..XG.PM..KR...V.T..B',
             '..VJ..W.YN..UT..G.K..C.XS',
             '.DR.A..E...J..L.N.M.OQ..K',
             '..EX...L.P..B..H.F....AY.',
             'P..B.A.SKG.FI..D.R.E.J..N',
             '.C.O..T..F.W.K...X..R.GB.',
             'LE.A..O.Q.Y.G.T.H.....X.I',
             '.V.M.RE.BC...LX...PI.U.KO',
             'W.N...XU..VBS.A..O.J...H.',
             'S.Q.U.YG.IC.....K..D.E.O.',
             'CT..IJ.PF..SK.NX.U.H..W..',
             'R.M.L..N.V..Y.E.T...P...C',
             '.HA.D.K..R..F.O..PIY.L..Q',
             '..BK.X.Q.AW.R.V.O.J..F.DH',
             '..WH.....OFI.D..V...M...T',
             'N.....Q.L.H..MJ.B.S.E.DV.',
             'J..LR.NH....E.B.UMG.XS.C.',
             'T.Y..S.CR...P.U.XA..FK.Q.',
             'XBK...JTIU.RQ.....D.LGH..']

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

# puzzle_xy = [[x, x, x, x, x, x, x, x, x],
#              [x, x, x, x, x, x, x, x, x],
#              [x, x, x, x, x, x, x, x, x],
#              [x, x, x, x, x, x, x, x, x],
#              [x, x, x, x, x, x, x, x, x],
#              [x, x, x, x, x, x, x, x, x],
#              [x, x, x, x, x, x, x, x, x],
#              [x, x, x, x, x, x, x, x, x],
#              [x, x, x, x, x, x, x, x, x]]

def solver_test():
    puzzle = puzzles.NORMAL_SUDOKU
    start = puzzle.get_start(very_hard_4)
    solver = sudoku_solver.SudokuSolver(puzzle, start)
    solver.solve()

def main():
    solver_test()
    # adj_test()
    # groups_test()

if __name__ == '__main__':
    main()