import unittest

from tictactoe.board import *


class BoardTest(unittest.TestCase):

    def test_columns(self):
        board = Board()
        board.rows = [['00', '01', '02'],
                      ['10', '11', '12'],
                      ['20', '21', '22']]
        expected_columns = [['00', '10', '20'],
                            ['01', '11', '21'],
                            ['02', '12', '22']]
        self.assertEqual(expected_columns, board.columns)

    def test_diagonals(self):
        board = Board()
        board.rows = [['00', '01', '02'],
                      ['10', '11', '12'],
                      ['20', '21', '22']]
        expected_diagonals = [['00', '11', '22'], ['02', '11', '20']]
        self.assertEqual(expected_diagonals, board.diagonals)

    def test_update(self):
        board = Board()
        board.update('X', (1, 1))
        expected_rows_columns = [[' ', ' ', ' '],
                                 [' ', 'X', ' '],
                                 [' ', ' ', ' ']]
        expected_diagonals = [[' ', 'X', ' '], [' ', 'X', ' ']]
        self.assertEqual(expected_rows_columns, board.columns)
        self.assertEqual(expected_rows_columns, board.rows)
        self.assertEqual(expected_diagonals, board.diagonals)

    def test_update_empty_coordinates(self):
        board = Board()
        board.update_empty_coordinates((1,1))
        expected_empty_coordinates = set([(0,0), (0,1), (0,2), (1,0), (1,2),
                                          (2,0), (2,1), (2,2)])
        self.assertEqual(expected_empty_coordinates, board.empty_coordinates)

    def test_id(self):
        board = Board()
        self.assertEqual(board.id, '         ')


if __name__ == '__main__':
    unittest.main()
